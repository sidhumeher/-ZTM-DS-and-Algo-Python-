'''
Created on Aug 18, 2020

@author: sidteegela
'''
'''
Given an array, rotate the array to the right by k steps, where k is non-negative.
'''


def rotateArray(nums, k):
    
    if k == 0 or len(nums) == 1:
        return nums

    while k > 0:
        poppedItem = nums.pop(-1)
        # print(nums)
        nums.insert(0, poppedItem)
        k -= 1
    return nums


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    result = rotateArray(nums, k)
    print(result)
    
    nums = [-1, -100, 3, 99]
    k = 2
    result = rotateArray(nums, k)
    print(result)
    
