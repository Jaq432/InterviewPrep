# The goal of this program is to do a center join on two arrays

# The knowledge check is sets vs lists and the use of '&'
# Sets don't allow duplicates where lists do

def main():
    arr1 = [1,2,3,4,5]
    arr2 = [3,4,5,6,7]

    joinedArrays = centerJoinArrays(arr1,arr2)

    print("This is the center joined array: " + str(joinedArrays))

def centerJoinArrays(firstArray, secondArray):
    firstSet = set(firstArray)
    secondSet = set(secondArray)

    joinedArray = list(firstSet & secondSet)

    return joinedArray

main()