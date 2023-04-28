# The goal of this program is to calculate the factorial of a given number

def main():
    userInputValue = int(input("What number do you want the factorial of? "))
    factorialValue = factorialCalculator(userInputValue)
    print("The factorial of that number is: " + str(factorialValue))

def factorialCalculator(inputValue):
    if inputValue > 0:
        return inputValue * factorialCalculator(inputValue - 1)
    if inputValue < 0:
        return inputValue * factorialCalculator(inputValue + 1)
    else:
        return 1

main()