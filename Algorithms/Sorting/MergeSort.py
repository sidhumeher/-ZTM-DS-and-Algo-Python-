'''
Created on Oct 17, 2020

@author: sidteegela
'''
'''
 Time: O(nlogn)
 Merge sort: divide and conquer approach
 Space: O(n) since we  need store all divided sub arrays
 Splitting takes 'log n' time and merging takes 'n' time
'''


def mergeSort(alist):
    
    print("Splitting ", alist)
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1
    print("Merging ", alist)

    
if __name__ == '__main__':
    
    inputList = [7, 5, 8, 3, 1, 9, 4, 2, 10]
    mergeSort(inputList)
