from styles import green_fill, red_fill, yellow_fill, blank_fill


class Level:
    HIGH = 'green'
    MID = 'yellow'
    LOW = 'red'
    UNKNOWN = 'white'

    to_style = {
        HIGH: green_fill,
        MID: yellow_fill,
        LOW: red_fill,
        UNKNOWN: blank_fill
    }
    
    @staticmethod
    def get_phrase_level(current_sheet, position):
        if current_sheet[position].fill.fgColor.rgb == 'FFD33D3D':
            return Level.LOW

        elif current_sheet[position].fill.fgColor.rgb == 'FFD0D637':
            return Level.MID

        elif current_sheet[position].fill.fgColor.rgb == 'FF55996F':
            return Level.HIGH
        else:
            return Level.UNKNOWN

translation_cols = ['C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']