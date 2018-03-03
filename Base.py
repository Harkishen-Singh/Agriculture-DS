from train_ML import Training_ML
from openpyxl import Workbook, load_workbook


class Base(Training_ML):
    #def __init__(self):



    def individualAllotment(self):
        self.workSheet = self.nameSheet
        # finding no of blockName, i.e., no of diff villages
        check2 = self.blockName[0]
        countBlocks = 1
        self.blockNameOnly = []
        self.blockNameOnly.append(self.blockName[0])
        self.rowNoEndingBlock = []
        for i in range(0, len(self.blockName)-1):
            if self.blockName[i] != self.blockName[i+1]:
                countBlocks = countBlocks + 1
                self.blockNameOnly.append(self.blockName[i+1])
                self.rowNoEndingBlock.append(i)
        print(self.blockNameOnly)
        print(self.rowNoEndingBlock)

        self.villageNameOnly = []
        self.villageNameOnly.append(self.villageName[0])
        finalChecker= True
        for i in range(0, len(self.villageName)):
            finalChecker = True
            length = len(self.villageNameOnly)
            compare = self.villageName[i]
            for j in self.villageNameOnly:
                if compare != j:
                    finalChecker = False
                else:
                    finalChecker = True
                    break
            if finalChecker == False:
                self.villageNameOnly.append(compare)

        print(self.villageNameOnly)
        # village name allotment ends here

        # variety name allotment
        self.varietyNameOnly = []
        self.varietyNameOnly.append(self.varietyName[0])

        for i in range(0, len(self.varietyName)):
            finalChecker = True
            compare = self.varietyName[i]
            for j in self.varietyNameOnly:

                    if compare != j:
                        finalChecker = False
                    else:
                        finalChecker = True
                        break
            if finalChecker == False:
                self.varietyNameOnly.append(compare)
                finalChecker = True

        print(self.varietyNameOnly)
        # sources of seeds
        self.sourceSeedOnly = []
        self.sourceSeedOnly.append(self.sourceSeed[0])
        for i in range(0, len(self.sourceSeed)):
            finalChecker = True
            compare = self.sourceSeed[i]
            for j in self.sourceSeedOnly:

                    if compare != j:
                        finalChecker = False
                    else:
                        finalChecker = True
                        break
            if finalChecker == False:
                self.sourceSeedOnly.append(compare)
                finalChecker = True

        print(self.sourceSeedOnly)
        # ends here

        # Yielding Quality of the seeds

        self.yieldingQualityOnly = []
        self.yieldingQualityOnly.append(self.cropVariety[0])
        for i in range(0, len(self.cropVariety)):
            finalChecker = True
            compare = self.cropVariety[i]
            for j in self.yieldingQualityOnly:

                if compare != j:
                    finalChecker = False
                else:
                    finalChecker = True
                    break
            if finalChecker == False:
                self.yieldingQualityOnly.append(compare)
                finalChecker = True

        print(self.yieldingQualityOnly)


        # ends here
        #self.sortingBasedOnQualityRemarks()


    '''def algorithmProcess(self):

        for i in range(2, self.numberOfRows):
            arr = self.workSheet.cell(row=i, column=)
        for variety in self.varietyNameOnly:

            for seedsSource in self.sourceSeedOnly:
    '''


