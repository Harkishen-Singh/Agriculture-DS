import sys, subprocess

from openpyxl import load_workbook, Workbook
from reason import Reason

class Block_Division(Reason):

    def opening(self):
        self.globalWorkBookName = self.globalWorkbookAvailable
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


        print('Extracting files')
        i = 1
        a = 1
        b = 1
        n = 1
        g = 1

        for blocks in self.blockNames :

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
                    print('Blocks : '+blocks + '\tWorkbook block : '+self.sheet_bad.cell(row=i, column= 2).value)
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

            i = 1
            a = 1

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
            nb.close()
            nn.close()
            ng.close()
            ngeneral.close()

        self.building_Good()

    def building_Good(self):
        print('\nBuilding "Good" Sectors ...')
        for i in range(0, len(self.blockName)) :

            if i != 0:
                if self.blockName[i] == self.blockName[i-1] :
                    continue

        #for blocks in self.blockName :
            print(self.blockName[i] + ' is now going on')

            #filename = self.sortedFileName_Good
            filename = 'Blocks/'+self.blockName[i]+'/sorts/sortedFile_Good_'+self.globalWorkBookName+'_.xlsx'
            wb3 = load_workbook(filename)
            ws3 = wb3['Sorted']
            row = 2

            while True :
                if ws3.cell(row=row, column=2).value != None:
                    row = row + 1
                else:
                    break

            file = Workbook()
            sheet = file.active
            sheet.cell(row=1, column=1, value='greenWtProduced_ratio')
            sheet.cell(row=1, column=2, value='DryWtProduced_ratio')
            sheet.cell(row=1, column=3, value='normalYldKilo_ratio')
            sheet.cell(row=1, column=4, value='Variety_Name')

            sg = 0;
            sd = 0;
            sn = 0;
            counter = 2
            ag = 0;
            ad = 0;
            an = 0
            checker = True;
            rowCounter = 1
            for i in range(2, row):

                if ws3.cell(row=i, column=19).value == 'Good':

                    rowCounter = rowCounter + 1
                    no = i
                    if checker == True:
                        if type(ws3.cell(row=no, column=10).value) == int:

                            seedExtractor = ws3.cell(row=no, column=5).value
                            # l2 = len(seedExtractor)
                            if type(seedExtractor) == str:
                                number = ''
                                for uu in seedExtractor:
                                    if uu.isdigit() or uu == '.':
                                        number = number + uu
                                p1 = float(number)
                                number = ''

                            seedExtractor2 = ws3.cell(row=no, column=10).value
                            if type(seedExtractor2) != int:

                                for uu2 in seedExtractor2:
                                    if uu2.isdigit() or uu2 == '.': number = number + uu2
                                p2 = float(number)
                                number = ''
                                # print('p1 is ' + str(p1) + ' p2 is ' + str(p2))
                            if type(seedExtractor2) == int:
                                p2 = seedExtractor2
                                # print('p1 is '+str(p1) + ' p2(int wala) is '+str(p2))

                            self.totalseeds = p1 * p2
                        else:
                            if type(ws3.cell(row=no, column=10).value) == int:

                                seedExtractor = ws3.cell(row=no, column=5).value
                                l2 = len(seedExtractor)
                                number = ''
                                for uu in seedExtractor:
                                    if uu.isdigit() or uu == '.':
                                        number = number + uu
                                p1 = float(number)
                                number = ''

                                seedExtractor2 = ws3.cell(row=no, column=10).value
                                if type(seedExtractor2) != int and type(seedExtractor2) != float:

                                    for uu2 in seedExtractor2:
                                        if uu2.isdigit() or uu2 == '.': number = number + uu2
                                    p2 = float(number)
                                    number = ''
                                    # print('p1 is ' + str(p1) + ' p2 is ' + str(p2))
                                if type(seedExtractor2) == int:
                                    p2 = seedExtractor2
                                    # print('p1 is ' + str(p1) + ' p2(int wala) is ' + str(p2))

                                self.totalseeds = p1 * p2
                        # print(str(ws3.cell(row=no, column=15).value) + ' ' + str(self.totalseeds))
                        # print(str(ws3.cell(row=no, column=15).value) + ' here is it' + str(i))
                        self.greenWtProduced_ratio = ws3.cell(row=no, column=15).value / self.totalseeds
                        self.DryWtProduced_ratio = ws3.cell(row=no, column=16).value / self.totalseeds
                        self.normalYldKilo_ratio = ws3.cell(row=no, column=18).value / self.totalseeds
                        sg = sg + self.greenWtProduced_ratio
                        ag = ag + 1
                        sd = sd + self.DryWtProduced_ratio
                        ad = ad + 1
                        sn = sn + self.normalYldKilo_ratio
                        an = an + 1
                        checker = False

                    elif ws3.cell(row=no, column=8).value == ws3.cell(row=no - 1, column=8).value:
                        if type(ws3.cell(row=no, column=10).value) == int:

                            seedExtractor = ws3.cell(row=no, column=5).value
                            if type(seedExtractor) == str:
                                l2 = len(seedExtractor)
                                number = ''
                                for uu in seedExtractor:
                                    if uu.isdigit() or uu == '.':
                                        number = number + uu
                                p1 = float(number)
                                number = ''

                            seedExtractor2 = ws3.cell(row=no, column=10).value
                            if type(seedExtractor2) != int and type(seedExtractor2) != float:

                                for uu2 in seedExtractor2:
                                    if uu2.isdigit() or uu2 == '.': number = number + uu2
                                p2 = float(number)
                                number = ''
                                # print('p1 is ' + str(p1) + ' p2 is ' + str(p2))
                            if type(seedExtractor2) == int:
                                p2 = seedExtractor2
                                # print('p1 is '+str(p1) + ' p2(int wala) is '+str(p2))

                            self.totalseeds = p1 * p2
                        else:
                            if type(ws3.cell(row=no, column=10).value) == int:

                                seedExtractor = ws3.cell(row=no, column=5).value
                                if type(seedExtractor) == str:
                                    l2 = len(seedExtractor)
                                    number = ''
                                    for uu in seedExtractor:
                                        if uu.isdigit() or uu == '.':
                                            number = number + uu

                                    p1 = float(number)
                                    number = ''

                                seedExtractor2 = ws3.cell(row=no, column=10).value
                                if type(seedExtractor2) != int and type(seedExtractor2) != float:

                                    for uu2 in seedExtractor2:
                                        if uu2.isdigit() or uu2 == '.': number = number + uu2
                                    p2 = float(number)
                                    number = ''
                                    # print('p1 is ' + str(p1) + ' p2 is ' + str(p2))
                                if type(seedExtractor2) == int:
                                    p2 = seedExtractor2
                                    # print('p1 is ' + str(p1) + ' p2(int wala) is ' + str(p2))

                                self.totalseeds = p1 * p2
                        # print(str(ws3.cell(row=no, column=15).value) + ' ' + str(self.totalseeds))

                        self.greenWtProduced_ratio = ws3.cell(row=no, column=15).value / self.totalseeds
                        self.DryWtProduced_ratio = ws3.cell(row=no, column=16).value / self.totalseeds
                        self.normalYldKilo_ratio = ws3.cell(row=no, column=18).value / self.totalseeds
                        sg = sg + self.greenWtProduced_ratio;
                        ag = ag + 1
                        sd = sd + self.DryWtProduced_ratio;
                        ad = ad + 1
                        sn = sn + self.normalYldKilo_ratio;
                        an = an + 1

                    if ws3.cell(row=no, column=8).value != ws3.cell(row=no - 1, column=8).value:
                        sheet.cell(row=counter, column=1, value=sg / ag);
                        ag = 0;
                        sg = 0
                        sheet.cell(row=counter, column=2, value=sd / ad);
                        ad = 0;
                        sd = 0
                        sheet.cell(row=counter, column=3, value=sn / an);
                        an = 0;
                        sn = 0
                        sheet.cell(row=counter, column=4, value=ws3.cell(row=no, column=8).value)
                        checker = True
                        counter = counter + 1

            file.save('Blocks/'+self.blockName[i]+'/ratios/ratio_good_' + self.globalWorkBookName + '.xlsx')
        self.building_Normal()

    def building_Normal(self):

        print('\nBuilding "Normal" Sectors ...')

        for i in range(0, len(self.blockName)) :

            if i != 0:
                if self.blockName[i] == self.blockName[i-1] :
                    continue

        #for blocks in self.blockName :
            print(self.blockName[i] + ' is currently going on')
            #filename = self.sortedFileName_Good
            filename = 'Blocks/'+self.blockName[i]+'/sorts/sortedFile_Normal_'+self.globalWorkBookName+'_.xlsx'
            wb3 = load_workbook(filename)
            ws3 = wb3['Sorted']
            row = 2

            while (row):
                if ws3.cell(row=row, column=2).value != None:
                    row = row + 1
                else:
                    break

            file = Workbook()
            sheet = file.active
            sheet.cell(row=1, column=1, value='greenWtProduced_ratio')
            sheet.cell(row=1, column=2, value='DryWtProduced_ratio')
            sheet.cell(row=1, column=3, value='normalYldKilo_ratio')
            sheet.cell(row=1, column=4, value='Variety_Name')

            sg = 0;
            sd = 0;
            sn = 0;
            counter = 2
            ag = 0;
            ad = 0;
            an = 0
            checker = True;
            rowCounter = 1
            for i in range(2, row):

                if ws3.cell(row=i, column=19).value == 'Good':

                    rowCounter = rowCounter + 1
                    no = i
                    if checker == True:
                        if type(ws3.cell(row=no, column=10).value) == int:

                            seedExtractor = ws3.cell(row=no, column=5).value
                            # l2 = len(seedExtractor)
                            if type(seedExtractor) == str:
                                number = ''
                                for uu in seedExtractor:
                                    if uu.isdigit() or uu == '.':
                                        number = number + uu
                                p1 = float(number)
                                number = ''

                            seedExtractor2 = ws3.cell(row=no, column=10).value
                            if type(seedExtractor2) != int:

                                for uu2 in seedExtractor2:
                                    if uu2.isdigit() or uu2 == '.': number = number + uu2
                                p2 = float(number)
                                number = ''
                                # print('p1 is ' + str(p1) + ' p2 is ' + str(p2))
                            if type(seedExtractor2) == int:
                                p2 = seedExtractor2
                                # print('p1 is '+str(p1) + ' p2(int wala) is '+str(p2))

                            self.totalseeds = p1 * p2
                        else:
                            if type(ws3.cell(row=no, column=10).value) == int:

                                seedExtractor = ws3.cell(row=no, column=5).value
                                l2 = len(seedExtractor)
                                number = ''
                                for uu in seedExtractor:
                                    if uu.isdigit() or uu == '.':
                                        number = number + uu
                                p1 = float(number)
                                number = ''

                                seedExtractor2 = ws3.cell(row=no, column=10).value
                                if type(seedExtractor2) != int and type(seedExtractor2) != float:

                                    for uu2 in seedExtractor2:
                                        if uu2.isdigit() or uu2 == '.': number = number + uu2
                                    p2 = float(number)
                                    number = ''
                                    # print('p1 is ' + str(p1) + ' p2 is ' + str(p2))
                                if type(seedExtractor2) == int:
                                    p2 = seedExtractor2
                                    # print('p1 is ' + str(p1) + ' p2(int wala) is ' + str(p2))

                                self.totalseeds = p1 * p2
                        # print(str(ws3.cell(row=no, column=15).value) + ' ' + str(self.totalseeds))
                        # print(str(ws3.cell(row=no, column=15).value) + ' here is it' + str(i))
                        self.greenWtProduced_ratio = ws3.cell(row=no, column=15).value / self.totalseeds
                        self.DryWtProduced_ratio = ws3.cell(row=no, column=16).value / self.totalseeds
                        self.normalYldKilo_ratio = ws3.cell(row=no, column=18).value / self.totalseeds
                        sg = sg + self.greenWtProduced_ratio
                        ag = ag + 1
                        sd = sd + self.DryWtProduced_ratio
                        ad = ad + 1
                        sn = sn + self.normalYldKilo_ratio
                        an = an + 1
                        checker = False

                    elif ws3.cell(row=no, column=8).value == ws3.cell(row=no - 1, column=8).value:
                        if type(ws3.cell(row=no, column=10).value) == int:

                            seedExtractor = ws3.cell(row=no, column=5).value
                            if type(seedExtractor) == str:
                                l2 = len(seedExtractor)
                                number = ''
                                for uu in seedExtractor:
                                    if uu.isdigit() or uu == '.':
                                        number = number + uu
                                p1 = float(number)
                                number = ''

                            seedExtractor2 = ws3.cell(row=no, column=10).value
                            if type(seedExtractor2) != int and type(seedExtractor2) != float:

                                for uu2 in seedExtractor2:
                                    if uu2.isdigit() or uu2 == '.': number = number + uu2
                                p2 = float(number)
                                number = ''
                                # print('p1 is ' + str(p1) + ' p2 is ' + str(p2))
                            if type(seedExtractor2) == int:
                                p2 = seedExtractor2
                                # print('p1 is '+str(p1) + ' p2(int wala) is '+str(p2))

                            self.totalseeds = p1 * p2
                        else:
                            if type(ws3.cell(row=no, column=10).value) == int:

                                seedExtractor = ws3.cell(row=no, column=5).value
                                if type(seedExtractor) == str:
                                    l2 = len(seedExtractor)
                                    number = ''
                                    for uu in seedExtractor:
                                        if uu.isdigit() or uu == '.':
                                            number = number + uu

                                    p1 = float(number)
                                    number = ''

                                seedExtractor2 = ws3.cell(row=no, column=10).value
                                if type(seedExtractor2) != int and type(seedExtractor2) != float:

                                    for uu2 in seedExtractor2:
                                        if uu2.isdigit() or uu2 == '.': number = number + uu2
                                    p2 = float(number)
                                    number = ''
                                    # print('p1 is ' + str(p1) + ' p2 is ' + str(p2))
                                if type(seedExtractor2) == int:
                                    p2 = seedExtractor2
                                    # print('p1 is ' + str(p1) + ' p2(int wala) is ' + str(p2))

                                self.totalseeds = p1 * p2
                        # print(str(ws3.cell(row=no, column=15).value) + ' ' + str(self.totalseeds))

                        self.greenWtProduced_ratio = ws3.cell(row=no, column=15).value / self.totalseeds
                        self.DryWtProduced_ratio = ws3.cell(row=no, column=16).value / self.totalseeds
                        self.normalYldKilo_ratio = ws3.cell(row=no, column=18).value / self.totalseeds
                        sg = sg + self.greenWtProduced_ratio;
                        ag = ag + 1
                        sd = sd + self.DryWtProduced_ratio;
                        ad = ad + 1
                        sn = sn + self.normalYldKilo_ratio;
                        an = an + 1

                    if ws3.cell(row=no, column=8).value != ws3.cell(row=no - 1, column=8).value:
                        sheet.cell(row=counter, column=1, value=sg / ag);
                        ag = 0;
                        sg = 0
                        sheet.cell(row=counter, column=2, value=sd / ad);
                        ad = 0;
                        sd = 0
                        sheet.cell(row=counter, column=3, value=sn / an);
                        an = 0;
                        sn = 0
                        sheet.cell(row=counter, column=4, value=ws3.cell(row=no, column=8).value)
                        checker = True
                        counter = counter + 1

            file.save('Blocks/'+self.blockName[i]+'/ratios/ratio_normal_' + self.globalWorkBookName + '.xlsx')
        self.building_Bad()

    def building_Bad(self):

        print('\nBuilding "Bad" Sectors ...\n')
        for i in range(0, len(self.blockName)) :

            if i != 0:
                if self.blockName[i] == self.blockName[i-1] :
                    continue

        #for blocks in self.blockName :
            print(self.blockName[i] + ' is currently going on')

            #filename = self.sortedFileName_Good
            filename = 'Blocks/'+self.blockName[i]+'/sorts/sortedFile_Bad_'+self.globalWorkBookName+'_.xlsx'
            wb3 = load_workbook(filename)
            ws3 = wb3['Sorted']
            row = 2

            while (row):
                if ws3.cell(row=row, column=2).value != None:
                    row = row + 1
                else:
                    break

            file = Workbook()
            sheet = file.active
            sheet.cell(row=1, column=1, value='greenWtProduced_ratio')
            sheet.cell(row=1, column=2, value='DryWtProduced_ratio')
            sheet.cell(row=1, column=3, value='normalYldKilo_ratio')
            sheet.cell(row=1, column=4, value='Variety_Name')

            sg = 0;
            sd = 0;
            sn = 0;
            counter = 2
            ag = 0;
            ad = 0;
            an = 0
            checker = True;
            rowCounter = 1
            for i in range(2, row):

                if ws3.cell(row=i, column=19).value == 'Good':

                    rowCounter = rowCounter + 1
                    no = i
                    if checker == True:
                        if type(ws3.cell(row=no, column=10).value) == int:

                            seedExtractor = ws3.cell(row=no, column=5).value
                            # l2 = len(seedExtractor)
                            if type(seedExtractor) == str:
                                number = ''
                                for uu in seedExtractor:
                                    if uu.isdigit() or uu == '.':
                                        number = number + uu
                                p1 = float(number)
                                number = ''

                            seedExtractor2 = ws3.cell(row=no, column=10).value
                            if type(seedExtractor2) != int:

                                for uu2 in seedExtractor2:
                                    if uu2.isdigit() or uu2 == '.': number = number + uu2
                                p2 = float(number)
                                number = ''
                                # print('p1 is ' + str(p1) + ' p2 is ' + str(p2))
                            if type(seedExtractor2) == int:
                                p2 = seedExtractor2
                                # print('p1 is '+str(p1) + ' p2(int wala) is '+str(p2))

                            self.totalseeds = p1 * p2
                        else:
                            if type(ws3.cell(row=no, column=10).value) == int:

                                seedExtractor = ws3.cell(row=no, column=5).value
                                l2 = len(seedExtractor)
                                number = ''
                                for uu in seedExtractor:
                                    if uu.isdigit() or uu == '.':
                                        number = number + uu
                                p1 = float(number)
                                number = ''

                                seedExtractor2 = ws3.cell(row=no, column=10).value
                                if type(seedExtractor2) != int and type(seedExtractor2) != float:

                                    for uu2 in seedExtractor2:
                                        if uu2.isdigit() or uu2 == '.': number = number + uu2
                                    p2 = float(number)
                                    number = ''
                                    # print('p1 is ' + str(p1) + ' p2 is ' + str(p2))
                                if type(seedExtractor2) == int:
                                    p2 = seedExtractor2
                                    # print('p1 is ' + str(p1) + ' p2(int wala) is ' + str(p2))

                                self.totalseeds = p1 * p2
                        # print(str(ws3.cell(row=no, column=15).value) + ' ' + str(self.totalseeds))
                        # print(str(ws3.cell(row=no, column=15).value) + ' here is it' + str(i))
                        self.greenWtProduced_ratio = ws3.cell(row=no, column=15).value / self.totalseeds
                        self.DryWtProduced_ratio = ws3.cell(row=no, column=16).value / self.totalseeds
                        self.normalYldKilo_ratio = ws3.cell(row=no, column=18).value / self.totalseeds
                        sg = sg + self.greenWtProduced_ratio
                        ag = ag + 1
                        sd = sd + self.DryWtProduced_ratio
                        ad = ad + 1
                        sn = sn + self.normalYldKilo_ratio
                        an = an + 1
                        checker = False

                    elif ws3.cell(row=no, column=8).value == ws3.cell(row=no - 1, column=8).value:
                        if type(ws3.cell(row=no, column=10).value) == int:

                            seedExtractor = ws3.cell(row=no, column=5).value
                            if type(seedExtractor) == str:
                                l2 = len(seedExtractor)
                                number = ''
                                for uu in seedExtractor:
                                    if uu.isdigit() or uu == '.':
                                        number = number + uu
                                p1 = float(number)
                                number = ''

                            seedExtractor2 = ws3.cell(row=no, column=10).value
                            if type(seedExtractor2) != int and type(seedExtractor2) != float:

                                for uu2 in seedExtractor2:
                                    if uu2.isdigit() or uu2 == '.': number = number + uu2
                                p2 = float(number)
                                number = ''
                                # print('p1 is ' + str(p1) + ' p2 is ' + str(p2))
                            if type(seedExtractor2) == int:
                                p2 = seedExtractor2
                                # print('p1 is '+str(p1) + ' p2(int wala) is '+str(p2))

                            self.totalseeds = p1 * p2
                        else:
                            if type(ws3.cell(row=no, column=10).value) == int:

                                seedExtractor = ws3.cell(row=no, column=5).value
                                if type(seedExtractor) == str:
                                    l2 = len(seedExtractor)
                                    number = ''
                                    for uu in seedExtractor:
                                        if uu.isdigit() or uu == '.':
                                            number = number + uu

                                    p1 = float(number)
                                    number = ''

                                seedExtractor2 = ws3.cell(row=no, column=10).value
                                if type(seedExtractor2) != int and type(seedExtractor2) != float:

                                    for uu2 in seedExtractor2:
                                        if uu2.isdigit() or uu2 == '.': number = number + uu2
                                    p2 = float(number)
                                    number = ''
                                    # print('p1 is ' + str(p1) + ' p2 is ' + str(p2))
                                if type(seedExtractor2) == int:
                                    p2 = seedExtractor2
                                    # print('p1 is ' + str(p1) + ' p2(int wala) is ' + str(p2))

                                self.totalseeds = p1 * p2
                        # print(str(ws3.cell(row=no, column=15).value) + ' ' + str(self.totalseeds))

                        self.greenWtProduced_ratio = ws3.cell(row=no, column=15).value / self.totalseeds
                        self.DryWtProduced_ratio = ws3.cell(row=no, column=16).value / self.totalseeds
                        self.normalYldKilo_ratio = ws3.cell(row=no, column=18).value / self.totalseeds
                        sg = sg + self.greenWtProduced_ratio;
                        ag = ag + 1
                        sd = sd + self.DryWtProduced_ratio;
                        ad = ad + 1
                        sn = sn + self.normalYldKilo_ratio;
                        an = an + 1

                    if ws3.cell(row=no, column=8).value != ws3.cell(row=no - 1, column=8).value:
                        sheet.cell(row=counter, column=1, value=sg / ag);
                        ag = 0;
                        sg = 0
                        sheet.cell(row=counter, column=2, value=sd / ad);
                        ad = 0;
                        sd = 0
                        sheet.cell(row=counter, column=3, value=sn / an);
                        an = 0;
                        sn = 0
                        sheet.cell(row=counter, column=4, value=ws3.cell(row=no, column=8).value)
                        checker = True
                        counter = counter + 1

            file.save('Blocks/'+self.blockName[i]+'/ratios/ratio_bad_' + self.globalWorkBookName + '.xlsx')
        print(self.blockName)


if __name__  ==  '__main__' :
    obj = Block_Division()
    obj.individualAllotment()
    obj.process_General()
    obj.xx()
    obj.avg_Good()
    obj.bad()
    obj.opening()




