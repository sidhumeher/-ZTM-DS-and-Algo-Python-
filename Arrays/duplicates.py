'''
Created on Aug 17, 2020

@author: sidteegela
'''

'''
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, 
and it should return false if every element is distinct.
'''


def containsDuplicate(nums):
    
    uniq = {}
    for item in nums:
        if item not in uniq:
            uniq[item] = 1
        else:
            return True
    
    return False
    
    
if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    result = containsDuplicate(nums)
    print(result)
    
    nums = [1, 2, 3, 4]
    result = containsDuplicate(nums)
    print(result)
    
    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    result = containsDuplicate(nums)
    print(result)
