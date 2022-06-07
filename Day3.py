
# Code for the projects of Day 3 of Advent of Code

rawData = open("C:\\Users\laten\Desktop\Projects\Advent of Code - 2021\Day3Data.txt", "r")
dataset = rawData.readlines()
rawData.close()

masterList = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve"]

indicesList = list(range(0, 12))
Index = indicesList[0]
def makingList():
    gammaList = list(range(0, 12))
    epsilonList = list(range(0, 12))
    for Index in indicesList:
        zeros = 0
        ones = 0
        binary = []
        for element in dataset:
            binary.append(str(element[Index]))
            masterList[Index] = binary
        for element in masterList[Index]:
            if element == "1":
                ones += 1
            elif element == "0":
                zeros += 1
        if ones > zeros:
            gammaList[Index] = 1
            epsilonList[Index] = 0
        elif zeros > ones:
            gammaList[Index] = 0
            epsilonList[Index] = 1
    gammaBinary = "".join([str(item) for item in gammaList])
    epsilonBinary = "".join([str(item) for item in epsilonList])
    gammaDecimal = int(gammaBinary, 2)
    epsilonDecimal = int(epsilonBinary, 2)
    """
    print(f"Gamma Binary: {gammaBinary}")
    print(f"Epsilon Binary: {epsilonBinary}")
    print(f"Gamma Decimal: {gammaDecimal}")
    print(f"Epsilon Decimal: {epsilonDecimal}")
    print(f"Final Answer: {gammaDecimal * epsilonDecimal}")
    """
    return masterList

masterList = makingList()
# Final answer for part one was 749376 for my specific data

# Start code for Part 2
commonsList = []
oxygenGeneratorList = []
CO2scrubberList = []
indicesList = list(range(0, 12))
Index = indicesList[0]
for Index in indicesList:
    ones = 0
    zeros = 0
    if len(oxygenGeneratorList) == 1:
        break
    if len(CO2scrubberList) == 1:
        break
    currentList = masterList[Index]
    for element in currentList:
        if element == "0":
            zeros += 1
        elif element == "1":
            ones += 1
    if Index == 0:
        if zeros > ones:
            commonsList.append("0")
            for element in dataset:
                if str(element[Index]) == "0":
                    oxygenGeneratorList.append(str(element))
                elif str(element[Index]) == "1":
                    CO2scrubberList.append(str(element))
        if ones >= zeros:
            commonsList.append("1")
            for element in dataset:
                if str(element[Index]) == "1":
                    oxygenGeneratorList.append(str(element))
                elif str(element[Index]) == "0":
                    CO2scrubberList.append(str(element))
    if Index >= 1:
        # Debugging
        if zeros > ones:
            commonsList.append("0")
            firstvaluesList = range(0, len(oxygenGeneratorList))
            firstvalue = firstvaluesList[0]
            secondvalueslist = range(0, len(CO2scrubberList))
            secondvalue = secondvalueslist[0]
            for firstvalue in firstvaluesList:
                if firstvalue >= len(oxygenGeneratorList):
                    break
                else:
                    while str(oxygenGeneratorList[firstvalue]) == "1":
                        oxygenGeneratorList.remove(oxygenGeneratorList[firstvalue])
                        firstvaluesList = range(0, len(oxygenGeneratorList))
                        if firstvalue >= len(oxygenGeneratorList):
                            break
            for secondvalue in secondvalueslist:
                if secondvalue >= len(CO2scrubberList):
                    break
                else:
                    while str(CO2scrubberList[secondvalue][Index]) == "0":
                        CO2scrubberList.remove(CO2scrubberList[secondvalue])
                        secondvalueslist = range(0, len(CO2scrubberList))
                        if secondvalue >= len(CO2scrubberList):
                            break
        if ones >= zeros:
            commonsList.append("1")
            firstvaluesList = range(0, len(oxygenGeneratorList))
            firstvalue = firstvaluesList[0]
            secondvalueslist = range(0, len(CO2scrubberList))
            secondvalue = secondvalueslist[0]
            for firstvalue in firstvaluesList:
                if firstvalue >= len(oxygenGeneratorList):
                    break
                else:
                    while str(oxygenGeneratorList[firstvalue][Index]) == "0":
                        oxygenGeneratorList.remove(oxygenGeneratorList[firstvalue])
                        firstvaluesList = range(0, len(oxygenGeneratorList))
                        if firstvalue >= len(oxygenGeneratorList):
                            break
            for secondvalue in secondvalueslist:
                if secondvalue >= len(CO2scrubberList):
                    break
                else:
                    while str(CO2scrubberList[secondvalue][Index]) == "1":
                        CO2scrubberList.remove(CO2scrubberList[secondvalue])
                        secondvalueslist = range(0, len(CO2scrubberList))
                        if secondvalue >= len(CO2scrubberList):
                            break
            None
print(oxygenGeneratorList)
print(CO2scrubberList)