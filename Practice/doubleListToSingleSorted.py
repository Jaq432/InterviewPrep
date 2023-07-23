# The goal of this is to take two random lists, sort them, and combine them into a single list

import random

def main():
    randomList1 = []
    randomList2 = []
    for i in range(10):
        randomNum1 = random.randint(0,9)
        randomNum2 = random.randint(0,9)
        randomList1.append(randomNum1)
        randomList2.append(randomNum2)

    combinedList = randomList1 + randomList2

    sortedCombinedList = listSorter(combinedList)

    print(sortedCombinedList)
    


# Selection Sort
def listSorter(inputList):
    for i in range(len(inputList)):
        #print("The list we are looking at: " + str(inputList))
        minIndex = i
        
        for j in range(i+1, len(inputList)):
            if inputList[j] < inputList[minIndex]:
                minIndex = j
        inputList[minIndex], inputList[i] = inputList[i], inputList[minIndex]

    return inputList


main()