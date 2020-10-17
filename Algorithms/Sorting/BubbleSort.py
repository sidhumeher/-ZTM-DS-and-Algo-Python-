'''
Created on Oct 16, 2020

@author: sidteegela
'''


def bubbleSort(inputList):
    
    if len(inputList) == 0:
        return []
    
    # i = 0; j = 1
    
    for i in range(0, len(inputList) - 1):
        for j in range(0, len(inputList) - i - 1):  # Last i elements will already be sorted
            
            if inputList[j] > inputList[j + 1]:
                inputList[j], inputList[j + 1] = inputList[j + 1], inputList[j]
        
    print(inputList)
    
# Time Complexity: O(n^2)-avg and worst case, Best case O(n)


if __name__ == '__main__':
    
    inputList = [7, 5, 8, 3, 1, 9, 4, 2]
    bubbleSort(inputList)
