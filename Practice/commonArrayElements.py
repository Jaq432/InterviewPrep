# The goal of this is to get a list of the common elements in two lists

def main():
    list1 = [1,2,3,4,5,6]
    list2 = [3,4,5,6,7,8,9]

    innerJoinList = getCommonElements(list1,list2)

    print(innerJoinList)


def getCommonElements(inputList1, inputList2):
    setList1 = set(inputList1)
    setList2 = set(inputList2)
    combinedList = setList1 & setList2
    return list(combinedList)

main()