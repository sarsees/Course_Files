from openpyxl import load_workbook
import scipy.optimize
import numpy as np
#Read me: describe the problem and anything you need to run the code
#Conclusion of nested loop
def excel_col(col):
    """col is a column number returns letter. 1=A """
    quot, rem = divmod(col-1,26)
    return excel_col(quot) + chr(rem+ord('A')) if col!=0 else ''


data_range_start = []
data_range_end = []
usable_data = []
for column in range(2,40):
    data_range_start.append(str(excel_col(column))+'17')
    data_range_end.append(str(excel_col(column))+'24')

wb_template = load_workbook('Data_for_Sarah.xlsx', data_only=True)
data = wb_template[ "Signal" ]
for i, start_pos in enumerate(data_range_start):
    end_pos = data_range_end[i]
    cell_range = data[start_pos:end_pos]
    col_results = [x[0].value for x in cell_range]
    usable_data.append(col_results)
    




    