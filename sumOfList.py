# The goal of this program is to sum the values in a list

def main():
    baseList = [1,5,78,54,23,48,1,52,68,2,1,48,36,2,18,79]
    summationOfList = listSummationer(baseList)
    print("The sum of all items in the list is: " + str(summationOfList))

def listSummationer(inputList):
    runningTotal = 0
    for item in inputList:
        runningTotal += item
    return runningTotal

main()