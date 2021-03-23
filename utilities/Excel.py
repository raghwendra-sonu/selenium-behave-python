import unittest
import xlrd

class Test(unittest.TestCase):
    def get_specific_column_data(self, filepath, SheetName):
        workbook = xlrd.open_workbook(filepath)
        worksheet = workbook.sheet_by_name(SheetName)
        first_row = []  # The row where we stock the name of the column
        for col in range(worksheet.ncols):
            first_row.append(worksheet.cell_value(0, col))
        # transform the workbook to a list of dictionaries
        data = []
        for row in range(1, worksheet.nrows):
            elm = {}
            for col in range(worksheet.ncols):
                elm[first_row[col]] = worksheet.cell_value(row, col)
            data.append(elm)
        print(data)
        return data
