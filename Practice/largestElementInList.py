# Find and print the largest element in the list

def main():
    myList = [8,43,6,89,2,33,2,1,66,102,78]

    biggestNumInList = bigNumberFinder(myList)
    smallestNumInList = smallNumberFinder(myList)

    print(biggestNumInList)

    print(smallestNumInList)


def bigNumberFinder(inputList):
    biggestNumber = 0

    for i in range(len(inputList)):
        if inputList[i] > inputList[biggestNumber]:
            biggestNumber = i

    return inputList[biggestNumber]

def smallNumberFinder(inputList):
    smallestNumber = 0

    for i in range(len(inputList)):
        if inputList[i] < inputList[smallestNumber]:
            smallestNumber = i

    return inputList[smallestNumber]

main()