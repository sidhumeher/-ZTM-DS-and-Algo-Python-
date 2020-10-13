'''
Created on Oct 12, 2020

@author: sidteegela
'''

# String reverse with recursion


def reverseWithRecursion(inputString):
    
    # Base case
    if len(inputString) == 0:
        return inputString
    
    return reverseWithRecursion(inputString[1:]) + inputString[0]
# Splice input into first character and rest of the input and pass it back to recursive method


if __name__ == '__main__':
    
    inputString = 'string'
    print(reverseWithRecursion(inputString))
    
    inputString = 'geeksforgeeks'
    print(reverseWithRecursion(inputString))
