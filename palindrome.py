# The goal of this program is to determine if a string is a palindrome or not
# Palindromes are words spelled forward and backward the same.

def main():
    userInput = input("What string would you like to check? ")
    isPalindrome = palindromeChecker(userInput)
    print("Is it a palindrome? " + str(isPalindrome))
    isEasierPalindrome = easierPalindromeChecker(userInput)
    print("Is it an easier palindrome? " + str(isEasierPalindrome))

# I'd suggest using this one as it displays programming concepts
def palindromeChecker(userInput):
    for index in range(int(len(userInput)/2)):
        if userInput[index] == userInput[len(userInput)-index-1]:
            continue
        else:
            return False
    return True

# This is how you'd really do it if you were programming as it's a simple one-liner
def easierPalindromeChecker(userInput):
    return userInput == userInput[::-1]

main()