# The goal of this is to check is two strings are anagrams of each other

# An anagram is where two words are made of the same characters

def main():
    stringInput1 = input("What is the first word you want to check? ")
    stringInput2 = input("What is the second word you want to check? ")
    isAnagram = anagramChecker(stringInput1, stringInput2)
    print("Are the two strings anagrams? " + str(isAnagram))


def anagramChecker(stringInput1, stringInput2):
    if len(stringInput1) != len(stringInput2):
        return False
    sortedString1 = stringSorter(stringInput1)
    sortedString2 = stringSorter(stringInput2)
    for i in range(len(stringInput1)):
        if sortedString1[i] != sortedString2[i]:
            return False
    return True
    

def stringSorter(stringInput):
    stringInputList = []
    for char in stringInput:
        stringInputList.append(char)
    
    # Implement a selection sort
    for i in range(len(stringInputList)):
        minIndex = i
        for j in range(i+1, len(stringInputList)):
            if stringInputList[j] > stringInputList[minIndex]:
               minIndex = j
        stringInputList[minIndex], stringInputList[i] = stringInputList[i], stringInputList[minIndex]
    
    return stringInputList

main()