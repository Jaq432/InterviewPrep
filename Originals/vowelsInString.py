# The goal of this program is to count the number of vowels in a string

def main():
    userInput = input("Please enter a word or series of words: ")
    numberOfVowels = vowelCounter(userInput)
    print("The number of vowels is: " + str(numberOfVowels))

def vowelCounter(inputString):
    listOfVowels = ["a", "e", "i", "o", "u"]
    vowelCount = 0
    for char in inputString:
        # if _ in _ -> this is a way to see if an item exists in an array
        if char in listOfVowels:
            vowelCount += 1

    return vowelCount

main()