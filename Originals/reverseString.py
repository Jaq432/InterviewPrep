# The goal of this program is to reverse the input string

def main():
    userInput = input("What string do you want reversed? ")
    reversedUserInput = stringReverser(userInput)
    print("Your reversed string is: " + str(reversedUserInput))
    easierReversedUserInput = easierStringReverser(userInput)
    print("Your easier reversed string is: " + str(easierReversedUserInput))


def stringReverser(inputString):
    reversedString = ""
    for char in inputString:
        reversedString = char + reversedString
    return reversedString

def easierStringReverser(inputString):
    return inputString[::-1]

main()