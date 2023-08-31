# The goal of this program is to determine if numbers are prime or not

def main():
    userInput = int(input("What number would you like to check if it is prime? "))
    isPrime = primeNumberChecker(userInput)
    print("Is the number prime? " + str(isPrime))

def primeNumberChecker(userInput):
    if userInput < 2:
        return False
    # ** does an exponent operation so a value of 0.5 is a square root
    for x in range(2, int(userInput**0.5) +1):
        if userInput % x == 0:
            return False
    return True

main()