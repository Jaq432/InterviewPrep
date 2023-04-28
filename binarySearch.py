# The goal of this is to locate the position of a value of an item in an array given that it is already sorted

def main():
    sortedArray = []
    # Make an array which is 0->100 in order
    for x in range(1,101):
        sortedArray.append(x)
    userInput = input("What value (1-100) do you want to search for? ")
    positionOfBinSearch = binarySearch(sortedArray,int(userInput))
    print("Position of found value: " + str(positionOfBinSearch))

def binarySearch(sortedArray, searchingValue):
 
    left = 0 
    right = len(sortedArray) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if sortedArray[mid] == searchingValue:
            return mid
        elif sortedArray[mid] < searchingValue:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1

main()