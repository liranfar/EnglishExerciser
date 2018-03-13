from common import Level


class VocabularyService:
    def __init__(self, vocabulary_dict, sheet_names):
        self._vocabulary_dict = vocabulary_dict
        self._sheet_names = sheet_names

    def get_next_phrase_generator(self):
        for level in [Level.UNKNOWN, Level.LOW, Level.MID, Level.HIGH]:
            for sheet_name in self._sheet_names:
            # TODO: extract the list to a constant one in Level class
                for phrase_key, phrase_value in self._vocabulary_dict[sheet_name][level].iteritems():
                    yield phrase_value

    def get_vocabulary(self):
        return self._vocabulary_dict
