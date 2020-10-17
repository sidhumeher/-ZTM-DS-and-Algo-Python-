'''
Created on Oct 16, 2020

@author: sidteegela
'''

# Select a min value and compare it with other items and swap if larger and change min value


def selectionSort(inputList):

    minValue = 0;j = 0
    for i in range(0, len(inputList)):
        minValue = i  # Reset min index to i'th index
        for j in range(i + 1, len(inputList)):  # Find min element in the list and swap
            if inputList[minValue] > inputList[j]:
                minValue = j
        inputList[i], inputList[minValue] = inputList[minValue], inputList[i]
        
    print(inputList)
    
# Time Complexity: O(n^2)
    

if __name__ == '__main__':
    
    inputList = [7, 5, 8, 3, 1, 9, 4, 2]
    selectionSort(inputList)
