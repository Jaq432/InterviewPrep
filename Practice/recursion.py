# Going over the main topics for it and what to look for

# Think about the base case first (most easy option to create the return bounds)

def main():
    #print(sumAllNonNeg(5))
    #print(gridPathLength(3,3))
    print (partitioning(9,7))


def sumAllNonNeg(inputInteger):
    if inputInteger == 0:
        return 0
    else:
        return inputInteger + sumAllNonNeg(inputInteger - 1)


# Write a function that takes two inputs and outputs the number
# of unique paths from the top left corner to bottom right
# Can only move down or right 1 unit at a time
def gridPathLength(n, m):

    if n == 1 or m == 1:
        return 1
    else:
        return gridPathLength(n, m-1) + gridPathLength(n-1, m)
    

# Write a function that counts the number of ways you can partition n objects
# using parts up to m (assuming m >= 0)
def partitioning(n, m):
    if n == 0:
        return 1
    elif m == 0 or n < 0:
        return 0
    else:
        return partitioning(n - m, m) + partitioning(n, m - 1)
    

main()