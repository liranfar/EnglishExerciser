

class Phrase:
    def __init__(self, work_book):
        self.work_book = work_book

        self._seen = 0

    def get_mid_marked(self):

        # move on each row of each sheet

        # count the yellow marked
        pass

    def get_low_marked(self):

        # move on each row of each sheet

        # count the red marked
        pass

    def get_high_marked(self):
        # move on each row of each sheet

        # count the green background
        pass

    def get_not_yet_classified(self):

        # TODO: remove this stub
        return 500
        # move on each row of each sheet

        # count the transparent background
        pass

    def increase_seen_by_one(self):
        self._seen += 1

    @property
    def seen(self):
        """I'm the 'seen' property """
        return self._seen

    def get_phrase(self, sheet, col_row):
        return wo



