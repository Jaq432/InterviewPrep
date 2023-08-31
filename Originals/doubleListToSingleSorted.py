# The goal of this program is to have two lists and merge them into a single sorted list

def main():
    firstList = [2,5,1,3,2,7,8]
    secondList = [1,6,2,3,2,9,4]
    mergedAndSortedList = mergeSortList(firstList, secondList)
    print("The merged and sorted list is: " + str(mergedAndSortedList))

def mergeSortList(list1, list2):
    mergedList = list1
    mergedList += list2

    lengthOfList = len(mergedList)

    # Implement a selection sort
    for i in range(lengthOfList):
        smallestKnownIndex = i
        for j in range(i+1,lengthOfList):
            if mergedList[j] < mergedList[smallestKnownIndex]:
                smallestKnownIndex = j
        mergedList[i], mergedList[smallestKnownIndex] = mergedList[smallestKnownIndex], mergedList[i]

    return mergedList

main()