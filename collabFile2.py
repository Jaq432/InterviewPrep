# This is paired with collabFile1.py
# These two files work together to show how you can use a method from one file in another

# This file imports the other file and we call it using <filename>.<methodName>() syntax

import collabFile1

def file2Method():
    collabFile1.file1Method()

def main():
    file2Method()

main()