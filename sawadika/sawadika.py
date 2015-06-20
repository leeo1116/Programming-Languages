__author__ = 'liangl2'
# https://openpyxl.readthedocs.org/en/latest/tutorial.html#loading-from-a-file
from openpyxl import Workbook
from openpyxl import load_workbook
from hxg import diversity_inclusion_search

wb = load_workbook(filename="websites  audit.xlsx")
ws = wb.active
url_list = []
row_num = 1
for cell in ws.columns[1]:  # get column B value cell by cell, ws.column[1][:].value
    print("Processing "+ws.cell(row=row_num, column=1).value+"...")
    if cell.value is not None and type(cell.value) is not bool and \
                    len(cell.value) > 3 and "http" in cell.value:

        url = cell.value
        result = diversity_inclusion_search(url)


        has_DI_index = 'C'+str(row_num)
        has_search_index = 'E'+str(row_num)
        if result['has_DI']:
            ws[has_DI_index] = result['has_DI']*1
        if result['has_search']:
            ws[has_search_index] = result['has_search']*1

        url_list.append(cell.value)
        # url_list = ws["B2":"B1190"].value
    row_num += 1
wb.save("websites  audit.xlsx")

#print('\n'.join(url_list[:100]))





"""
print(ws.cell(row=1, column=1).value)
print(wb.get_sheet_names())

import datetime

wb = Workbook()
ws = wb.active
ws["A1"] = 16
ws.append([11, 2, 3])
ws["A3"] = datetime.datetime.now()
print(ws.cell(row=2, column=2).value)
wb.save("excel_example.xlsx")
"""