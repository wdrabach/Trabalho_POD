import xlrd

def read_xls_file(RELATORIO_DTB_BRASIL_MUNICIPIO):
    workbook = xlrd.open_workbook(RELATORIO_DTB_BRASIL_MUNICIPIO)
    worksheet = workbook.sheet_by_index(0)

    data = []
    for row_index in range(worksheet.nrows):
        row = []
        for col_index in range(worksheet.ncols):
            cell_value = worksheet.cell_value(row_index, col_index)
            row.append(cell_value)
        data.append(row)
    #print(data)
    
    return data

file_path = 'RELATORIO_DTB_BRASIL_MUNICIPIO.xls'
result = read_xls_file(file_path)
print(result)