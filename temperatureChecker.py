# Description
# Given a list of daily temperatures, produce a list that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.
# For example, given the list temperatures = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].


# Example 1:
#     Input:  temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
#     Output:  [1, 1, 4, 2, 1, 1, 0, 0]
    
#     Explanation:
#     Just find the first day after it which has higher temperatures than it.

    
# Example 2:
#     Input: temperatures = [50, 40, 39, 30]
#     Output:  [0,0,0,0]

forcastTemperatures = [73, 74, 75, 71, 69, 72, 76, 73]
#forcastTemperatures = [50, 40, 39, 30]

def dailyTemperatures(temperatures):
    n = len(temperatures)
    result = [0] * n  # Initialize result list with 0s
    stack = []  # Stack to store indices of temperatures

    # Go through each index of the array
    for i in range(n):
        print("Stack info: " + str(stack))
        while stack and temperatures[i] > temperatures[stack[-1]]:
            j = stack.pop()
            result[j] = i - j
        stack.append(i)
        print("Temp info: i = " + str(temperatures[i]) + " end = " + str(temperatures[stack[-1]]))

    return result

# Test the program
result = dailyTemperatures(forcastTemperatures)
print(result)








'''
def calcDays(forcastTemperatures):
    daysUntilNextHigherTemp = []
    for i in range(len(forcastTemperatures)):
        print("-")
        numOfDaysToNextHighTemp = 0
        for j in range(i, len(forcastTemperatures)):
            if j <= i:
                continue
            
            print("Comparing i: " + str(forcastTemperatures[i]) + " j: " + str(forcastTemperatures[j]) + " num: " + str(numOfDaysToNextHighTemp))

            # If the day we are comparing to has a lesser temperature
            if forcastTemperatures[i] > forcastTemperatures[j]:
                print("A")
                numOfDaysToNextHighTemp += 1
            elif numOfDaysToNextHighTemp == 0 and j == len(forcastTemperatures):
                print("B")
                daysUntilNextHigherTemp.append(0)
                break
            elif forcastTemperatures[i] < forcastTemperatures[j]:
                print("C")
                numOfDaysToNextHighTemp += 1
                daysUntilNextHigherTemp.append(numOfDaysToNextHighTemp)
                break
        daysUntilNextHigherTemp.append(0)
    return(daysUntilNextHigherTemp)


             
print(calcDays(forcastTemperatures))
'''
#1)
# [1, 1, 4, 2, 1, 1, 0, 0]
# [1, 1, 4, 2, 1, 1]
    
#2)
#[50, 40, 39, 30]
#[0, 0]

    
    
'''
for i in range (len(forcastTemperatures)):
    numOfDaysUntilHigherTemp = 1
    
    for j in range(i+1, len(forcastTemperatures)):
        #print("Comparing: " + str(forcastTemperatures[i]) + " " + str(forcastTemperatures[j]) + " " + str(numOfDaysUntilHigherTemp))
    
        if forcastTemperatures[j] <= forcastTemperatures[i]:
            numOfDaysUntilHigherTemp += 1
            
        elif forcastTemperatures[j] > forcastTemperatures[i]:
            daysUntilNextHigherTemp.append(numOfDaysUntilHigherTemp)
            break
    
    if numOfDaysUntilHigherTemp == 1:
        daysUntilNextHigherTemp.append(0)
            
#daysUntilNextHigherTemp.append(0)
            
return daysUntilNextHigherTemp
        
print(calcDays(forcastTemperatures))


'''
