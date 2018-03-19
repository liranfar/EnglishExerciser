# coding=utf-8
import sys
import traceback

from bidi.algorithm import get_display

from colors import green, cyan, yellow, red
from common import Level
from excel import Excel
from helpers import query_yes_no
from statistic import StatisticService
from view import View
from vocabulary import VocabularyService
from voice import Voice


def main():
    View.print_('Opening workbook...')

    # opening the excel file
    vocbulary_wb = Excel('vocabulary.xlsx')

    vocabulary_dict = vocbulary_wb.get_wb_as_dict()

    # TODO change to singleton
    vocabulary_service = VocabularyService(vocabulary_dict, vocbulary_wb.get_sheet_names())
    statistic_service = StatisticService(vocabulary_dict)

    try:
        # TODO parse the desired level as a Level data
        desired_level = sys.argv[1]

    except IndexError:
        desired_level = Level.UNKNOWN

    phrase_gen = vocabulary_service.get_next_phrase_generator()

    View.clear_screen()

    while True:

        try:
            statistic_service.show()

            phrase = next(phrase_gen)

            View.print_('Word is: {}.'.format(green(phrase.get_value())))

            known = query_yes_no("Know it?")

            if not known:

                # display context
                View.print_('Context is: {}'.format(cyan(phrase.get_context())))

                Voice.say(phrase.get_context())

                if query_yes_no("And now?"):
                    # sign known level as mid
                    phrase.set_level(Level.MID)

                else:
                    # sign known level as low
                    phrase.set_level(Level.LOW)

            else:
                phrase.set_level(Level.HIGH)
                # print("phrase {} level has been set to {}". format(phrase.get_value, phrase._level))

            # display translations
            query_yes_no(yellow(get_display(','.join(phrase.get_translation()))).encode('utf-8'))

        except KeyboardInterrupt:

            # clear screen
            View.clear_screen()

            # save to disk
            vocbulary_wb.save_changes(vocabulary_service.get_vocabulary())

            # prompt continuing
            if query_yes_no("Are you sure you want to quit?"):
                sys.exit(0)

        except StopIteration:
            # clear screen
            View.clear_screen()
            vocbulary_wb.save_changes(vocabulary_service.get_vocabulary())
            View.print_(
                "Well Done! you passed all the terms for level : {} , see you next time! ".format(desired_level))
            sys.exit(0)

        except Exception as e:
            traceback.print_exc(file=sys.stdout)
            print(red("Error reading word... {}".format(e)))
            if not query_yes_no("Move to next word?"):
                # save to disk
                vocbulary_wb.save_changes(vocabulary_service.get_vocabulary())
                break
        finally:
            # clear screen
            View.clear_screen()


if __name__ == '__main__':
    main()
