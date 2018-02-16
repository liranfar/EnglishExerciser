translation_cols = ['C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']


class Translations:

    @classmethod
    def get_translations(cls, sheet, row):
        return [sheet[col + str(row)].value for col in translation_cols if sheet[col + str(row)].value is not None]

