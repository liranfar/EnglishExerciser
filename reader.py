import openpyxl
import sys
import os
import random
from helpers import query_yes_no, progressBar
from styles import yellow_fill, red_fill, green_fill

sys.stdout.write('\rOpening workbook...')
sys.stdout.flush()
vocbulary_wb = openpyxl.load_workbook('vocabulary.xlsx')

sys.stdout.write('\rReading sheets...')


for sheet_name in vocbulary_wb.get_sheet_names():
    sys.stdout.write('\rCurrent sheet : {}\n'.format(sheet_name))
    current_sheet = vocbulary_wb.get_sheet_by_name(sheet_name)
    sys.stdout.write('Reading rows...')

    # shuffled_rows = shuffle_content(3, current_sheet.max_row + 1)
    rows = list(range(3, current_sheet.max_row + 1))
    random.shuffle(rows)
    os.system('clear')
    for row in rows:
        word = current_sheet['A' + str(row)].value
        context = current_sheet['L' + str(row)].value
        sys.stdout.write('\rWord is: {}.'.format(word))
        show_context = query_yes_no(" Display context (no if you know the word)?")
        if show_context:
            sys.stdout.write('\rContext is: {}'.format(context))
            if query_yes_no("...", ):
                current_sheet['A' + str(row)].fill = yellow_fill
            else:
                current_sheet['A' + str(row)].fill = red_fill
        else:
            current_sheet['A' + str(row)].fill = green_fill

        vocbulary_wb.save('vocabulary.xlsx')
        os.system('clear')
