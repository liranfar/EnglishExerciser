# coding=utf-8
import random
import sys
import traceback

from bidi.algorithm import get_display

from colors import green, cyan, yellow, red, magenta
from excel import Excel
from helpers import query_yes_no, progressBar
from phrase import Phrase
from styles import yellow_fill, red_fill, green_fill
from translator import Translations
from view import View
from voice import Voice


def main():
    View.print_('Opening workbook...')

    # opening the excel file
    vocbulary_wb = Excel('vocabulary.xlsx')

    # translation columns in the sheet ( export to config file? )
    phrase = Phrase(vocbulary_wb)
    # translate = Translate(vocbulary_wb)
    # known_words = phrase.get_high_marked()

    View.print_('Reading sheets...')
    # TODO: add switch case menu to choose the wished sheet or orders
    # iterate on reversed order sheets
    # for sheet_name in vocabulary_wb.get_sheet_names()[::-1]:
    # sheet_name = 'ProgrammingBooks'

    # if sheet_name:
    while True:

        sheet_name = random.choice(vocbulary_wb.get_sheet_names())

        sheets = [vocbulary_wb.get_sheet_by_name(sheet).max_row - 3 for sheet in vocbulary_wb.get_sheet_names()]

        total_phrases_num = sum(sheets)

        current_sheet = vocbulary_wb.get_sheet_by_name(sheet_name)

        # get number of rows
        rows = list(range(3, current_sheet.max_row + 1))

        # shuffle order
        random.shuffle(rows)

        # clear screen
        View.clear_screen()

        # choose a random row from the current sheet
        row = random.choice(rows)

        try:

            # display current sheet
            View.print_('Current sheet : {}'.format(sheet_name))
            # print progress-bar off known_words
            progressBar(phrase.seen, total_phrases_num, magenta, 80)
            # print seen words counter
            View.print_title('Seen: ' + str(phrase.seen) +
                             ' High: ' + str(phrase.get_high_marked(sheet_name)) +
                             ' Mid: ' + str(phrase.get_mid_marked(sheet_name)) +
                             ' Low: ' + str(phrase.get_low_marked(sheet_name)) +
                             ' Unknown: ' + str(phrase.get_not_yet_classified(sheet_name))
                             )
            # get phrase
            current_phrase = vocbulary_wb.get_value(current_sheet, 'A' + str(row))
            phrase.increase_seen_by_one()
            # get context
            current_context = vocbulary_wb.get_value(current_sheet, 'L' + str(row))
            # get translations ( verb, noun etc.. )
            current_translations = Translations.get_translations(current_sheet, row)
            # display the current word
            View.print_('Word is: {}.'.format(green(current_phrase)))

            # known prompt
            known = query_yes_no("Know it?")
            if not known:

                # display context
                View.print_('Context is: {}'.format(cyan(current_context)))
                Voice.say(current_context)
                if query_yes_no("And now?", ):
                    # sign known level as mid
                    vocbulary_wb.fill_color(current_sheet, 'A' + str(row), yellow_fill)

                else:
                    # sign known level as low
                    vocbulary_wb.fill_color(current_sheet, 'A' + str(row), red_fill)
            else:
                # sign known level as high
                vocbulary_wb.fill_color(current_sheet, 'A' + str(row), green_fill)

            # display translations
            query_yes_no(yellow(get_display(','.join(current_translations))).encode('utf-8'))

            # save to disk
            # vocbulary_wb.save_changes()

        except KeyboardInterrupt:

            # clear screen
            View.clear_screen()

            # save to disk
            vocbulary_wb.save_changes()

            # prompt continuing
            if query_yes_no("Are you sure you want to quit?"):
                sys.exit(0)

        except Exception as e:
            traceback.print_exc(file=sys.stdout)
            print(red("Error reading word... {}".format(e)))
            if not query_yes_no("Move to next word?"):
                # save to disk
                vocbulary_wb.save_changes()
                sys.exit(0)
        finally:
            # clear screen
            View.clear_screen()


if __name__ == '__main__':
    main()
