from colors import magenta
from common import Level
from helpers import progressBar
from view import View


class StatisticService:
    def __init__(self, vocabulary_dict):
        self.vocabulary_dict = vocabulary_dict
        self.seen = 0
        self.all_count = 0
        # TODO make a tuple of the levels instead of this verbosity
        self._counters = {n: 0 for n in [Level.UNKNOWN, Level.HIGH, Level.MID, Level.LOW]}


    # TODO
    def show(self):

        self._update_phrases_counts()
        # print progress-bar off known_words
        progressBar(self._counters[Level.HIGH], self.all_count, magenta, 80)

        # count high
        View.print_title('Seen: ' + str(self.seen) +
                         ' High: ' + str(self._counters[Level.HIGH]) +
                         ' Mid: ' + str(self._counters[Level.MID]) +
                         ' Low: ' + str(self._counters[Level.LOW]) +
                         ' Unknown: ' + str(self._counters[Level.UNKNOWN])
                         )

    def _update_phrases_counts(self):

        self.seen += 1
        self.all_count = 0
        self._counters = dict.fromkeys(self._counters.iterkeys(), 0 )
        for sheet_name, sheet_val in self.vocabulary_dict.iteritems():
            for level, level_val in self.vocabulary_dict[sheet_name].iteritems():
                for phrase_val, phrase_obj in self.vocabulary_dict[sheet_name][level].iteritems():
                    self.all_count += 1
                    self._counters[phrase_obj.get_level()] += 1
