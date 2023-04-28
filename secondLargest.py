# This is to find the second largest item in an array

# The goal of this program is to re-engineer the sorting algorithm and sort items of a list in ascending order

def main():
    baseList = [1,5,78,54,23,48,1,52,68,2,1,48,36,2,18,79]
    sortedList = selectionSort(baseList)
    print("The second largest object in the array: " + str(sortedList[len(sortedList)-2]))

def selectionSort(inputList):
    n = len(inputList)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if inputList[j] < inputList[min_idx]:
                min_idx = j
        inputList[i], inputList[min_idx] = inputList[min_idx], inputList[i]

    return inputList

main()