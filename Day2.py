
# Code for the projects of Day 2 of Advent of Code

rawData = open("C:\\Users\laten\Desktop\Projects\Advent of Code - 2021\Day2Data.txt", "r")
dataset = rawData.readlines()
rawData.close()

totalForward = 0
totalUp = 0
totalDown = 0
totalVertical = 0
aim = 0
for element in dataset:
    if element[0 : 7] == "forward":
        addAmount = int(element[8])
        totalForward = (totalForward + addAmount)
        totalVertical = totalVertical + (addAmount * aim)
    elif element[0 : 2] == "up":
        addAmount = int(element[3])
        aim -= addAmount
    elif element[0 : 4] == "down":
        addAmount = int(element[5])
        aim += addAmount

grandTotal = totalVertical * totalForward
print(f"Grand total: {grandTotal}")
