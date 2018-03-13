
class Phrase:
    def __init__(self, value, context, translation, position, level):
        self._value = value
        self._context = context
        self._translation = translation
        self._position = position
        self._level = level
        self._seen = 0

    # TODO extract statuses values to a common statistic file

    def increase_seen_by_one(self):
        self._seen += 1

    @property
    def seen(self):
        """I'm the 'seen' property """
        return self._seen

    def get_phrase(self, sheet, col_row):
        pass

    def get_translation(self):
        return self._translation

    def get_value(self):
        return self._value

    def get_context(self):
        return self._context

    def get_position(self):
        return self._position

    def set_level(self, level):
        self._level = level

    def get_level(self):
        return self._level

    def to_dict(self):
        return {
            'value': self._value,
            'context': self._context,
            'translation': self._translation,
            'position': self._position,
            'level': self._level
        }
