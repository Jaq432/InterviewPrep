# This script is to check if a string is a palindrome

# Palindromes are words spelled the same forward and backward

def main():
    userInput = input("What word would you like to check? ")
    isPalindrome = palindromeChecker(userInput)

    print("Is the word a palindrome? " + str(isPalindrome))


def palindromeChecker(inputString):
    
    # Convert the string into a list
    inputStringList = []
    for char in inputString:
        inputStringList.append(char)
    
    for index in range(int(len(inputStringList)/2)+1):
        if inputStringList[index] != inputStringList[len(inputStringList)-1-index]:
            return False
        
    return True

main()