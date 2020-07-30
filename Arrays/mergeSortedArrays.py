'''
Created on Jul 27, 2020

@author: sidteegela
'''

def mergeSortedArrays(list1, list2):
    
    #check if lists are empty
    if len(list1) == 0 and len(list2) == 0:
        return []
    elif len(list1) == 0:
        return list2
    elif len(list2) == 0:
        return list1
    
    list1_pointer = 0
    list2_pointer = 0
    resultList = []
    while(list1_pointer < len(list1) and list2_pointer < len(list2)):
        if list1[list1_pointer] < list2[list2_pointer]:
            resultList.append(list1[list1_pointer])
            list1_pointer += 1
        elif list1[list1_pointer] > list2[list2_pointer]:
            resultList.append(list2[list2_pointer])
            list2_pointer += 1
        elif list1[list1_pointer] == list2[list2_pointer]:
            resultList.append(list1[list1_pointer])
            resultList.append(list2[list2_pointer])
            list1_pointer += 1
            list2_pointer += 1
    
    while list1_pointer < len(list1):
        resultList.append(list1[list1_pointer])
        list1_pointer += 1
    while list2_pointer < len(list2):
        resultList.append(list2[list2_pointer])
        list2_pointer += 1
    
    return resultList
        
            

if __name__ == '__main__':
    list1 = [0,3,4,31]
    list2 = [3,4,6,30]
    result = mergeSortedArrays(list1, list2)
    print(result)
    
    list1 = [1,2,4,6,8]
    list2 = [2,4,5,7]
    result = mergeSortedArrays(list1, list2)
    print(result)
    
    list1 = [1,2,4,6,8]
    list2 = []
    result = mergeSortedArrays(list1, list2)
    print(result)
    
    #Time complexity: O(len of list1 + len of list2)
    #Space complexity: O(No of items in list1 + No of items in list2)