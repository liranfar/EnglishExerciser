import openpyxl

my_red = openpyxl.styles.colors.Color(rgb='00D33D3D')
red_fill = openpyxl.styles.fills.PatternFill(patternType='solid', fgColor=my_red)
my_green = openpyxl.styles.colors.Color(rgb='0055996F')
green_fill = openpyxl.styles.fills.PatternFill(patternType='solid', fgColor=my_green)
my_yellow = openpyxl.styles.colors.Color(rgb='00D0D637')
yellow_fill = openpyxl.styles.fills.PatternFill(patternType='solid', fgColor=my_yellow)