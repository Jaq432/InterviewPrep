# The goal is to perform a factorial operator on a given number

def main():
    try:
        inputNumber = int(input("What number do you want to factorial? "))
    
    except:
        main()

    factorialNumber = giveMeFactorialPlz(inputNumber)

    print(factorialNumber)

# RECURSION
def giveMeFactorialPlz(userInputNumber):

    if userInputNumber > 0:
        return userInputNumber * giveMeFactorialPlz(userInputNumber-1)
    if userInputNumber < 0:
        return userInputNumber * giveMeFactorialPlz(userInputNumber+1)
    else:
        return 1
    
    
main()