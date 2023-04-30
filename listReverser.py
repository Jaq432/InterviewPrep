# The goal of this program is to reverse the order of a list

def main():
    ascendingList = [1, 1, 1, 2, 2, 5, 18, 23, 36, 48, 48, 52, 54, 68, 78, 79]
    descendingList = listReverser(ascendingList)
    print("This is the list ascending: " + str(ascendingList))
    print("This is the list descending: " + str(descendingList))

def listReverser(inputList):
    reversedList = []
    for i in range(len(inputList)-1,-1,-1):
        reversedList.append(inputList[i])
    return reversedList

main()