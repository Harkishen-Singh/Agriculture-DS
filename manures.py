from Process import Process
from openpyxl import load_workbook

class Manures(Process):
    def avg_Good(self):
        rows = 1
        file = load_workbook(self.sortedFileName_Good)
        sheet = file['Sorted']
        while(rows):
            if sheet.cell(row=rows, column=2).value != None:
                rows = rows + 1
            else: break
        total_chemfer = 0; c_chemfer = 0
        total_manure = 0 ; c_manure = 0
        file2 = load_workbook('./ratios/ratio_good.xlsx')
        sheet2 = file['Sheet']
        sheet2.cell(row= 1,column=5, value='ChemFer_Ratio')
        sheet2.cell(row=1, column=6, value='Manure_Ratio')

        for i in range(2, rows+1):

            if sheet.cell(row=i, column=12).value == None:
                continue

            elif type(sheet.cell(row=i, column=12).value) == str:
                number = ''
                for j in sheet.cell(row=i, column=12).value:
                    if j.isdigit():
                        number = number + j
                total_chemfer = total_chemfer + float(number)
                c_chemfer = c_chemfer + 1
            else:
                total_chemfer = total_chemfer + float(number)
                c_chemfer = c_chemfer + 1

            if sheet.cell(row=i, column=11).value == None:
                continue

            elif type(sheet.cell(row=i, column=11).value) == str:
                number = ''
                for j in sheet.cell(row=i, column=11).value:
                    if j.isdigit():
                        number = number + j
                total_manure = total_manure + float(number)
                c_manure = c_manure + 1
            else:
                total_manure = total_manure + float(number)
                c_manure = c_manure + 1


        sheet2.cell(row= i, column = 5, value=total_chemfer/c_chemfer)
        sheet2.cell(row=i, column=6, value=total_manure / c_manure)
        file2.save('./ratios/ratio_good.xlsx')