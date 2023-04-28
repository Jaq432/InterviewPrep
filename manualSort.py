# The goal of this program is to re-engineer the sorting algorithm and sort items of a list in ascending order
# The sorting algorithm used here is a selection sort

def main():
    baseList = [1,5,78,54,23,48,1,52,68,2,1,48,36,2,18,79]
    sortedList = selectionSort(baseList)
    print("The order of the list should be ascending: " + str(sortedList))

def selectionSort(inputList):
    # Make a var that is the length of the list
    n = len(inputList)
    # Loop for the quantity of the size of the list
    for i in range(n):
        # Capture the index of the current known smallest number
        min_idx = i
        # Loop for the part of the array we haven't looked at yet
        for j in range(i+1, n):
            # Compare each value to that of the one in the current minimum's index
            if inputList[j] < inputList[min_idx]:
                # If the position is lower in value, save the index
                min_idx = j
        # replace the position of the lowest found value with that of the position we were checking against
        inputList[i], inputList[min_idx] = inputList[min_idx], inputList[i]

    return inputList

main()

# Here's the steps/comments from above to use as a study guide

# Make a var that is the length of the list
# Loop for the quantity of the size of the list
# Capture the index of the current known smallest number
# Loop for the part of the array we haven't looked at yet
# Compare each value to that of the one in the current minimum's index
# If the position is lower in value, save the index
# replace the position of the lowest found value with that of the position we were checking against