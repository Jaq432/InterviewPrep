# The goal of this is to take an input list and reverse the order of it

def main():
    myList = [0,1,2,3,4,5,6,7,8,9]

    reversedList = listReverser(myList)

    print(reversedList)


def listReverser(inputList):
    reversedList = []

    for i in range(len(inputList)):
        reversedList.append(inputList[len(inputList)-1-i])

    return reversedList

main()