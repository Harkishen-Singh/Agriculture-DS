import sys, subprocess

from openpyxl import load_workbook, Workbook

class Block_Division():

    def opening(self):
        self.globalWorkBookName = input('WorkBook name : ')
        sortGeneralAdd = 'sorts/sortedFile_General_'+self.globalWorkBookName+'.xlsx'
        wb = load_workbook(sortGeneralAdd)
        self.sheet_general = wb['Sorted']
        self.allBlocks = []
        i = 1
        while True:
            i += 1
            if self.sheet_general.cell(row = i, column = 2).value == None:
                break
            else:
                self.allBlocks.append(self.sheet_general.cell(row = i, column = 2).value)
        sortGeneralAdd = 'sorts/sortedFile_Bad_'+self.globalWorkBookName+'.xlsx'
        wb = load_workbook(sortGeneralAdd)
        self.sheet_bad = wb['Sorted']

        sortGeneralAdd = 'sorts/sortedFile_Normal_' + self.globalWorkBookName + '.xlsx'
        wb = load_workbook(sortGeneralAdd)
        self.sheet_normal = wb['Sorted']

        sortGeneralAdd = 'sorts/sortedFile_Good_' + self.globalWorkBookName + '.xlsx'
        wb = load_workbook(sortGeneralAdd)
        self.sheet_good = wb['Sorted']

        self.blockNames = []

        self.scanner()

    def scanner(self):
        self.blockNames.append(self.allBlocks[0])

        for block in self.allBlocks :
            presence = False

            for loop in self.blockNames :
                if loop == block :
                    presence = True
                    break
            if presence == False :
                self.blockNames.append(block)
            else:
                presence = False
        print(self.blockNames)
        self.creating_required_directories()


    def creating_required_directories(self):
        defaultConsoleAdd = 'Blocks'

        # creating new directories
        print("Number of directories to be created : "+ str(len(self.blockNames)))

        for blocks in self.blockNames :

            c = subprocess.call(['mkdir', defaultConsoleAdd+'/'+blocks])
            e = subprocess.call(['mkdir', defaultConsoleAdd + '/' + blocks + '/' + 'ratios'])
            d = subprocess.call(['mkdir', defaultConsoleAdd+'/'+blocks+'/'+'sorts'])

        print('Created directories successfully ! ')

        self.extracting_required_files()

    def extracting_required_files(self):
        # creating new files
        nb = Workbook()
        nn = Workbook()
        ng = Workbook()
        ngeneral = Workbook()

        nsBad = nb.active
        nsBad.title = 'Sorted'

        nsNormal = nn.active
        nsNormal.title = 'Sorted'

        nsGood = ng.active
        nsGood.title = 'Sorted'

        nsGeneral = ngeneral.active
        nsGeneral.title = 'Sorted'

        print('Extracting files')
        i = 1
        a = 1
        b = 1
        n = 1
        g = 1

        for blocks in self.blockNames :

            i = 1
            a = 1
            b = 1
            n = 1
            g = 1

            while True:
                i += 1
                if self.sheet_general.cell(row=i, column= 2).value == None:
                    break

                if blocks == self.sheet_general.cell(row=i, column= 2).value :
                    a +=1
                    nsGeneral.cell(row=a, column=2, value=self.sheet_general.cell(row=i, column=2).value)
                    nsGeneral.cell(row=a, column=3, value=self.sheet_general.cell(row=i, column=3).value)
                    nsGeneral.cell(row=a, column=4, value=self.sheet_general.cell(row=i, column=4).value)
                    nsGeneral.cell(row=a, column=5, value=self.sheet_general.cell(row=i, column=5).value)
                    nsGeneral.cell(row=a, column=6, value=self.sheet_general.cell(row=i, column=6).value)
                    nsGeneral.cell(row=a, column=7, value=self.sheet_general.cell(row=i, column=7).value)
                    nsGeneral.cell(row=a, column=8, value=self.sheet_general.cell(row=i, column=8).value)
                    nsGeneral.cell(row=a, column=9, value=self.sheet_general.cell(row=i, column=9).value)
                    nsGeneral.cell(row=a, column=10, value=self.sheet_general.cell(row=i, column=10).value)
                    nsGeneral.cell(row=a, column=11, value=self.sheet_general.cell(row=i, column=11).value)
                    nsGeneral.cell(row=a, column=12, value=self.sheet_general.cell(row=i, column=12).value)
                    nsGeneral.cell(row=a, column=13, value=self.sheet_general.cell(row=i, column=13).value)
                    nsGeneral.cell(row=a, column=14, value=self.sheet_general.cell(row=i, column=14).value)
                    nsGeneral.cell(row=a, column=15, value=self.sheet_general.cell(row=i, column=15).value)
                    nsGeneral.cell(row=a, column=16, value=self.sheet_general.cell(row=i, column=16).value)
                    nsGeneral.cell(row=a, column=17, value=self.sheet_general.cell(row=i, column=17).value)
                    nsGeneral.cell(row=a, column=18, value=self.sheet_general.cell(row=i, column=18).value)
                    nsGeneral.cell(row=a, column=19, value=self.sheet_general.cell(row=i, column=19).value)
                    nsGeneral.cell(row=a, column=20, value=self.sheet_general.cell(row=i, column=20).value)
                    nsGeneral.cell(row=a, column=21, value=self.sheet_general.cell(row=i, column=21).value)
                    nsGeneral.cell(row=a, column=22, value=self.sheet_general.cell(row=i, column=22).value)
                    nsGeneral.cell(row=a, column=23, value=self.sheet_general.cell(row=i, column=23).value)
                    nsGeneral.cell(row=a, column=24, value=self.sheet_general.cell(row=i, column=24).value)
                    nsGeneral.cell(row=a, column=25, value=self.sheet_general.cell(row=i, column=25).value)
                    nsGeneral.cell(row=a, column=26, value=self.sheet_general.cell(row=i, column=26).value)

            i = 1
            a = 1

            while True:
                i += 1
                if self.sheet_bad.cell(row=i, column= 2).value == None:
                    break

                if blocks == self.sheet_bad.cell(row=i, column= 2).value :
                    a +=1
                    nsBad.cell(row=a, column=2, value=self.sheet_bad.cell(row=i, column=2).value)
                    nsBad.cell(row=a, column=3, value=self.sheet_bad.cell(row=i, column=3).value)
                    nsBad.cell(row=a, column=4, value=self.sheet_bad.cell(row=i, column=4).value)
                    nsBad.cell(row=a, column=5, value=self.sheet_bad.cell(row=i, column=5).value)
                    nsBad.cell(row=a, column=6, value=self.sheet_bad.cell(row=i, column=6).value)
                    nsBad.cell(row=a, column=7, value=self.sheet_bad.cell(row=i, column=7).value)
                    nsBad.cell(row=a, column=8, value=self.sheet_bad.cell(row=i, column=8).value)
                    nsBad.cell(row=a, column=9, value=self.sheet_bad.cell(row=i, column=9).value)
                    nsBad.cell(row=a, column=10, value=self.sheet_bad.cell(row=i, column=10).value)
                    nsBad.cell(row=a, column=11, value=self.sheet_bad.cell(row=i, column=11).value)
                    nsBad.cell(row=a, column=12, value=self.sheet_bad.cell(row=i, column=12).value)
                    nsBad.cell(row=a, column=13, value=self.sheet_bad.cell(row=i, column=13).value)
                    nsBad.cell(row=a, column=14, value=self.sheet_bad.cell(row=i, column=14).value)
                    nsBad.cell(row=a, column=15, value=self.sheet_bad.cell(row=i, column=15).value)
                    nsBad.cell(row=a, column=16, value=self.sheet_bad.cell(row=i, column=16).value)
                    nsBad.cell(row=a, column=17, value=self.sheet_bad.cell(row=i, column=17).value)
                    nsBad.cell(row=a, column=18, value=self.sheet_bad.cell(row=i, column=18).value)
                    nsBad.cell(row=a, column=19, value=self.sheet_bad.cell(row=i, column=19).value)
                    nsBad.cell(row=a, column=20, value=self.sheet_bad.cell(row=i, column=20).value)
                    nsBad.cell(row=a, column=21, value=self.sheet_bad.cell(row=i, column=21).value)
                    nsBad.cell(row=a, column=22, value=self.sheet_bad.cell(row=i, column=22).value)
                    nsBad.cell(row=a, column=23, value=self.sheet_bad.cell(row=i, column=23).value)
                    nsBad.cell(row=a, column=24, value=self.sheet_bad.cell(row=i, column=24).value)
                    nsBad.cell(row=a, column=25, value=self.sheet_bad.cell(row=i, column=25).value)
                    nsBad.cell(row=a, column=26, value=self.sheet_bad.cell(row=i, column=26).value)

            while True:
                i += 1
                if self.sheet_normal.cell(row=i, column= 2).value == None:
                    break

                if blocks == self.sheet_normal.cell(row=i, column= 2).value :
                    a +=1
                    nsNormal.cell(row=a, column=2, value=self.sheet_normal.cell(row=i, column=2).value)
                    nsNormal.cell(row=a, column=3, value=self.sheet_normal.cell(row=i, column=3).value)
                    nsNormal.cell(row=a, column=4, value=self.sheet_normal.cell(row=i, column=4).value)
                    nsNormal.cell(row=a, column=5, value=self.sheet_normal.cell(row=i, column=5).value)
                    nsNormal.cell(row=a, column=6, value=self.sheet_normal.cell(row=i, column=6).value)
                    nsNormal.cell(row=a, column=7, value=self.sheet_normal.cell(row=i, column=7).value)
                    nsNormal.cell(row=a, column=8, value=self.sheet_normal.cell(row=i, column=8).value)
                    nsNormal.cell(row=a, column=9, value=self.sheet_normal.cell(row=i, column=9).value)
                    nsNormal.cell(row=a, column=10, value=self.sheet_normal.cell(row=i, column=10).value)
                    nsNormal.cell(row=a, column=11, value=self.sheet_normal.cell(row=i, column=11).value)
                    nsNormal.cell(row=a, column=12, value=self.sheet_normal.cell(row=i, column=12).value)
                    nsNormal.cell(row=a, column=13, value=self.sheet_normal.cell(row=i, column=13).value)
                    nsNormal.cell(row=a, column=14, value=self.sheet_normal.cell(row=i, column=14).value)
                    nsNormal.cell(row=a, column=15, value=self.sheet_normal.cell(row=i, column=15).value)
                    nsNormal.cell(row=a, column=16, value=self.sheet_normal.cell(row=i, column=16).value)
                    nsNormal.cell(row=a, column=17, value=self.sheet_normal.cell(row=i, column=17).value)
                    nsNormal.cell(row=a, column=18, value=self.sheet_normal.cell(row=i, column=18).value)
                    nsNormal.cell(row=a, column=19, value=self.sheet_normal.cell(row=i, column=19).value)
                    nsNormal.cell(row=a, column=20, value=self.sheet_normal.cell(row=i, column=20).value)
                    nsNormal.cell(row=a, column=21, value=self.sheet_normal.cell(row=i, column=21).value)
                    nsNormal.cell(row=a, column=22, value=self.sheet_normal.cell(row=i, column=22).value)
                    nsNormal.cell(row=a, column=23, value=self.sheet_normal.cell(row=i, column=23).value)
                    nsNormal.cell(row=a, column=24, value=self.sheet_normal.cell(row=i, column=24).value)
                    nsNormal.cell(row=a, column=25, value=self.sheet_normal.cell(row=i, column=25).value)
                    nsNormal.cell(row=a, column=26, value=self.sheet_normal.cell(row=i, column=26).value)

            i = 1
            a = 1

            while True:
                i += 1
                if self.sheet_good.cell(row=i, column= 2).value == None:
                    break

                if blocks == self.sheet_good.cell(row=i, column= 2).value :
                    a +=1
                    nsGood.cell(row=a, column=2, value=self.sheet_good.cell(row=i, column=2).value)
                    nsGood.cell(row=a, column=3, value=self.sheet_good.cell(row=i, column=3).value)
                    nsGood.cell(row=a, column=4, value=self.sheet_good.cell(row=i, column=4).value)
                    nsGood.cell(row=a, column=5, value=self.sheet_good.cell(row=i, column=5).value)
                    nsGood.cell(row=a, column=6, value=self.sheet_good.cell(row=i, column=6).value)
                    nsGood.cell(row=a, column=7, value=self.sheet_good.cell(row=i, column=7).value)
                    nsGood.cell(row=a, column=8, value=self.sheet_good.cell(row=i, column=8).value)
                    nsGood.cell(row=a, column=9, value=self.sheet_good.cell(row=i, column=9).value)
                    nsGood.cell(row=a, column=10, value=self.sheet_good.cell(row=i, column=10).value)
                    nsGood.cell(row=a, column=11, value=self.sheet_good.cell(row=i, column=11).value)
                    nsGood.cell(row=a, column=12, value=self.sheet_good.cell(row=i, column=12).value)
                    nsGood.cell(row=a, column=13, value=self.sheet_good.cell(row=i, column=13).value)
                    nsGood.cell(row=a, column=14, value=self.sheet_good.cell(row=i, column=14).value)
                    nsGood.cell(row=a, column=15, value=self.sheet_good.cell(row=i, column=15).value)
                    nsGood.cell(row=a, column=16, value=self.sheet_good.cell(row=i, column=16).value)
                    nsGood.cell(row=a, column=17, value=self.sheet_good.cell(row=i, column=17).value)
                    nsGood.cell(row=a, column=18, value=self.sheet_good.cell(row=i, column=18).value)
                    nsGood.cell(row=a, column=19, value=self.sheet_good.cell(row=i, column=19).value)
                    nsGood.cell(row=a, column=20, value=self.sheet_good.cell(row=i, column=20).value)
                    nsGood.cell(row=a, column=21, value=self.sheet_good.cell(row=i, column=21).value)
                    nsGood.cell(row=a, column=22, value=self.sheet_good.cell(row=i, column=22).value)
                    nsGood.cell(row=a, column=23, value=self.sheet_good.cell(row=i, column=23).value)
                    nsGood.cell(row=a, column=24, value=self.sheet_good.cell(row=i, column=24).value)
                    nsGood.cell(row=a, column=25, value=self.sheet_good.cell(row=i, column=25).value)
                    nsGood.cell(row=a, column=26, value=self.sheet_good.cell(row=i, column=26).value)

            print('Creating the required Files')

            # saving the files

            nb.save('Blocks/'+blocks+'/sorts/'+'sortedFile_Bad_' + self.globalWorkBookName+ '_.xlsx')
            nn.save('Blocks/'+blocks+'/sorts/'+'sortedFile_Normal_' + self.globalWorkBookName+ '_.xlsx')
            ng.save('Blocks/'+blocks+'/sorts/'+'sortedFile_Good_' + self.globalWorkBookName+ '_.xlsx')
            ngeneral.save('Blocks/'+blocks+'/sorts/'+'sortedFile_General_' + self.globalWorkBookName+ '_.xlsx')

    




if __name__  ==  '__main__' :
    oj = Block_Division()
    oj.opening()




