# The goal of this program is to find the largest element in a list and return it

def main():
    baseList = [1,5,78,54,23,48,1,52,68,2,1,48,36,2,18,79]

    largestElementInList = largestElementFinder(baseList)

    print("The largest element is: " + str(largestElementInList))

def largestElementFinder(inputList):
    largestElement = inputList[0]
    for item in inputList:
        if item > largestElement:
            largestElement = item
    return largestElement

main()