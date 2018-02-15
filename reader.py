# coding=utf-8
import openpyxl
import os
import random

import sys
from bidi.algorithm import get_display
from colors import green, cyan, yellow, red
from helpers import query_yes_no, progressBar
from styles import yellow_fill, red_fill, green_fill

sys.stdout.write('\rOpening workbook...')
sys.stdout.flush()
vocbulary_wb = openpyxl.load_workbook('vocabulary.xlsx')

translation_cols = ['C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

sys.stdout.write('\rReading sheets...')

for sheet_name in vocbulary_wb.get_sheet_names():
    sys.stdout.write('\rCurrent sheet : {}\n'.format(sheet_name))
    current_sheet = vocbulary_wb.get_sheet_by_name(sheet_name)
    sys.stdout.write('Reading rows...')

    rows = list(range(3, current_sheet.max_row + 1))
    random.shuffle(rows)
    os.system('clear')
    for row in rows:

        try:
            word = current_sheet['A' + str(row)].value
            context = current_sheet['L' + str(row)].value
            translations = [current_sheet[c + str(row)].value for c in translation_cols if current_sheet[c + str(row)].value is not None]
            sys.stdout.write('\rWord is: {}.'.format(green(word)))
            known = query_yes_no(" Know it?")
            if not known:
                sys.stdout.write('\rContext is: {}'.format(cyan(context)))
                if query_yes_no("...", ):
                    current_sheet['A' + str(row)].fill = yellow_fill
                else:
                    current_sheet['A' + str(row)].fill = red_fill
            else:
                current_sheet['A' + str(row)].fill = green_fill

            query_yes_no(yellow(get_display(','.join(translations))).encode('utf-8'))
        except Exception:
            print(red("Error reading word..."))
            if not query_yes_no("Move to next word?"):
                sys.exit(1)

        finally:
            vocbulary_wb.save('vocabulary.xlsx')
            os.system('clear')
