# The goal of this program is to check if two strings are anagrams of each other

def main():
    firstPhrase = input("Please enter your first phrase: ")
    secondPhrase = input("Please enter your second phrase: ")
    isAnagram = anagramChecker(firstPhrase, secondPhrase)
    print("The two strings are anagrams of each other: {isAnagram}".format(isAnagram = str(isAnagram)))

def anagramChecker(firstPhrase, secondPhrase):
    sortedFirstPhrase = selectionSort(firstPhrase)
    sortedSecondPhrase = selectionSort(secondPhrase)
    return sortedFirstPhrase == sortedSecondPhrase

def selectionSort(inputList):
    cloneInputList = []
    
    for letter in inputList:
        cloneInputList.append(str(letter))
    
    for i in range(len(cloneInputList)):
        minIndex = i
        for j in range(i+1, len(cloneInputList)):
            if cloneInputList[j] < cloneInputList[minIndex]:
                minIndex = j
        cloneInputList[i], cloneInputList[minIndex] = cloneInputList[minIndex], cloneInputList[i]
    return cloneInputList

main()



'''
def anagramChecker(firstString, secondString):
    
    firstString = sorted(firstString)
    secondString = sorted(secondString)
    
    # In here is a way to convert into a char array.
    # Python also handles strings as char arrays anyways to it wasn't required.
    firstStringCharArray = []
    secondStringCharArray = []
    for char in firstString:
        firstStringCharArray.append(char)
    for char in secondString:
        secondStringCharArray.append(char)
    firstStringCharArray = sorted(firstStringCharArray)
    secondStringCharArray = sorted(secondStringCharArray)
    return firstStringCharArray == secondStringCharArray
    
    return firstString == secondString

'''