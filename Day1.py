
# Code for the projects of Day 1 of Advent of Code

rawData = open("C:\\Users\laten\Desktop\Projects\Advent of Code - 2021\Day1Data.txt", "r")
dataset = rawData.readlines()
rawData.close()

newDataSet = []
firstAnswer = 0
Index = 0
while Index <= len(dataset) - 1:
    newDataSet.append(int(dataset[Index].strip("\n")))
    Index += 1
    if Index >= 2:
        if newDataSet[Index - 1] > newDataSet[Index - 2]:
            firstAnswer += 1

print(f"First answer: {firstAnswer}")
# The answer for part 1 is 1233 for my specific data

# Start code for part 2

slidingWindowsList = []
temporarySum = []
Index = 0
while Index <= len(newDataSet) - 1:
    temporarySum.append(newDataSet[Index])
    Index += 1
    if (len(temporarySum) % 3 == 0):
        slidingWindowsList.append(sum(temporarySum))
        del temporarySum[0]

Index = 0
secondAnswer = 0
while Index <= len(slidingWindowsList) - 1:
    Index += 1
    if Index > len(slidingWindowsList) - 1:
        break
    if slidingWindowsList[Index] > slidingWindowsList[Index - 1]:
        secondAnswer += 1

print(f"Second Answer: {secondAnswer}")
# The answer for part 2 is 1275 for my specific data
