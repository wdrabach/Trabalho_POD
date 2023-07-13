import xlrd
import numpy as np

def read_xls_file():
    file_path = 'RELATORIO_DTB_BRASIL_MUNICIPIO.xls'
    workbook = xlrd.open_workbook(file_path)
    worksheet = workbook.sheet_by_index(0)

    data = []
    for row_index in range(worksheet.nrows):
        row = []
        for col_index in range(worksheet.ncols):
            cell_value = worksheet.cell_value(row_index, col_index )
            row.append(cell_value)
        data.append(row)
    
    return data


# result = read_xls_file(file_path)

# hash_table = {}
# for row in result:
#     for col in row:
#         hash_table[col] = row[0]
        
# print(hash_table['Brasília'])