

class VocabularyService:
    def __init__(self, vocabulary_dict):
        self._vocabulary_dict = vocabulary_dict

    def get_next_phrase_generator(self, desired_level):
        # TODO change to all sheets
        for phrase_key, phrase_value in self._vocabulary_dict['SiliconValley'][desired_level].iteritems():
            yield phrase_value

    def get_vocabulary(self):
        return self._vocabulary_dict