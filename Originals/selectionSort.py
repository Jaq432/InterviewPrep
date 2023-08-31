orderedList = [2,7,1,34,87,42,1,6,78,4,3,45,23,12]

print("Before: " + str(orderedList))

for i in range(len(orderedList)):
    minIndex = i
    for j in range(i+1, len(orderedList)):
        if orderedList[j] < orderedList[minIndex]:
            minIndex = j
    orderedList[minIndex], orderedList[i] = orderedList[i], orderedList[minIndex]

print("After: " + str(orderedList))