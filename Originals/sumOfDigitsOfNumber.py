# The goal of this program is to count the sum of the digits within a number

def main():
    userDefinedNumber = input("Please enter a number to calculate the sum of its digits: ")
    digitSum = digitSummationer(userDefinedNumber)
    print("The sum of the digits in " + str(userDefinedNumber) + " is " + str(digitSum))

# Best name ever
def digitSummationer(providedNumber):
    digitSum = 0
    # Handle the number as a string so we can get each number individually
    for char in str(providedNumber):
        # Convert the chars back to ints for the summation
        digitSum += int(char)
    return digitSum

main()