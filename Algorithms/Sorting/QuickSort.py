'''
Created on Oct 17, 2020

@author: sidteegela
'''
'''
Technique: Divide and conquer
Time complexity: average is O(n log n) but based on how we pick the pivot item the worst case can be
O(n^2) when the pivot is the small item or the largest item
Space: O(n log n)

Pick a pivot and compare it other items in sub array
Pivot can be first item, last item, middle item or random
'''


def partiiton(array, low, high):
    pivot = array[high]  # Pivot element
    i = low - 1  # Index of smaller item
    
    for j in range(low, high):
        if array[j] <= pivot:  # If current item is less than pivot
            i += 1
            array[i], array[j] = array[j], array[i]
            
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1
            

def quickSort(inputList, low, high):
    
    if len(inputList) == 1:
        return inputList
    
    if low < high:
        partition = partiiton(inputList, low, high)
        
        quickSort(inputList, low, partition - 1)
        quickSort(inputList, partition + 1, high)


if __name__ == '__main__':

    inputList = [7, 5, 8, 3, 1, 9, 4, 2, 10]
    quickSort(inputList, 0 , len(inputList) - 1)
    
    print(inputList)
