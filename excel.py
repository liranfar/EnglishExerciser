import openpyxl

"""
Wrapper class for the excel reader engine - a kind of abstraction/separation layer for modularity
"""


class Excel:
    def __init__(self, path):
        self.path = path
        self.engine = openpyxl.load_workbook(path)

    def get_sheet_by_name(self, name):
        return self.engine.get_sheet_by_name(name)

    def get_sheet_names(self):
        return self.engine.get_sheet_names()

    def get_value(self, current_sheet, col_row):
        return current_sheet[col_row].value

    def fill_color(self, current_sheet, col_row, color):
        current_sheet[col_row].fill = color

    def save_changes(self):
        self.engine.save(self.path)
