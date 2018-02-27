from styles import yellow_fill, green_fill


class Phrase:
    def __init__(self, work_book):
        self.work_book = work_book
        self._sheetname_to_knowledge_status = self._init_status()

        self._seen = 0

    # TODO extract statuses values to common file
    def get_mid_marked(self, sheet_name=None):
        total_phrases = self.get_number_of_words_by_status(sheet_name=sheet_name, status='mid')
        return total_phrases

    def get_low_marked(self, sheet_name=None):
        total_phrases = self.get_number_of_words_by_status(sheet_name=sheet_name, status='low')
        return total_phrases

    def get_high_marked(self, sheet_name=None):
        total_phrases = self.get_number_of_words_by_status(sheet_name=sheet_name, status='high')
        return total_phrases

    def get_not_yet_classified(self, sheet_name=None):
        total_phrases = self.get_number_of_words_by_status(sheet_name=sheet_name, status='undiscovered')
        return total_phrases

    def get_number_of_words_by_status(self, status, sheet_name=None):
        total_phrases = 0
        if sheet_name is None:
            for sheet_name in self.work_book.get_sheet_names():
                total_phrases += self._sheetname_to_knowledge_status[sheet_name][status]
        else:
            try:
                total_phrases = self._sheetname_to_knowledge_status[sheet_name][status]
            except KeyError:
                pass

        return total_phrases

    def increase_seen_by_one(self):
        self._seen += 1

    @property
    def seen(self):
        """I'm the 'seen' property """
        return self._seen

    def get_phrase(self, sheet, col_row):
        pass

    def _init_status(self):
        sheet_to_status = {}
        for sheet_name in self.work_book.get_sheet_names():
            sheet_to_status[sheet_name] = {}
            current_sheet = self.work_book.get_sheet_by_name(sheet_name)
            rows = list(range(3, self.work_book.get_sheet_by_name(sheet_name).max_row + 1))
            for row in rows:
                # the background color implies the phrase's status
                # TODO: create a map from fill to status, scraping these code

                if current_sheet['A' + str(row)].fill.fgColor.rgb == 'FFD33D3D':
                    self._update_status_counter(sheet_name, sheet_to_status, 'low')

                elif current_sheet['A' + str(row)].fill.fgColor.rgb == 'FFD0D637':
                    self._update_status_counter(sheet_name, sheet_to_status, 'mid')

                elif current_sheet['A' + str(row)].fill.fgColor.rgb == 'FF55996F':
                    self._update_status_counter(sheet_name, sheet_to_status, 'high')

                else:
                    self._update_status_counter(sheet_name, sheet_to_status, 'undiscovered')

        return sheet_to_status

    def _update_status_counter(self, sheet_name, sheet_to_status, status):
        try:
            sheet_to_status[sheet_name][status] += 1
           # print('sheet: {}, status: {}, counter: {}'.format(sheet_name,status, str(sheet_to_status[sheet_name][status])))
        except KeyError:
           # print('Initialized status: {} of sheet: {} with 1'.format(status,sheet_name))
            sheet_to_status[sheet_name][status] = 1
