'''
Created on Oct 16, 2020

@author: sidteegela
'''

'''
Insertion sort not the most efficient but in cases it can be extremely fast
When you list is almost or already sorted
Best case: O(n)
'''


def insertionSort(inputList):

    for i in range(1, len(inputList)):
        key = inputList[i]
        j = i - 1  # Shift items of list that are greater than the key one position to the right
        
        while j >= 0 and key < inputList[j]:
            inputList[j + 1] = inputList[j]
            j -= 1
        inputList[j + 1] = key
        print(inputList, '\n')
        
    print(inputList)
    
# Time complexity: O(n^2)


if __name__ == '__main__':
    inputList = [7, 5, 8, 3, 1, 9, 4, 2]
    insertionSort(inputList)
