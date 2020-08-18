'''
Created on Aug 10, 2020

@author: sidteegela
'''

'''
Given an integer array nums, find the contiguous subarray 
(containing at least one number) which has the largest sum and return its sum.
'''


def maxSubarray(nums):
    
    if len(nums) == 1:
        return nums[0]
    '''
    i = 0
    j = 0
    while i < len(nums):
        for j in range(j, len(nums)):
            totalSum += nums[j]
        print('Sum:', totalSum)
        totalSum = 0
        i += 1
        j = i
    '''
    
    '''
    totalSum = nums[0]
    i = 0
    j = 1
    startIndex = 0
    endIndex = 0
    while i < len(nums) and j < len(nums):
        currentSum = nums[i]
        for item in range(i + 1, j + 1):
            currentSum += nums[item]
        if currentSum >= totalSum:
            # print(i, j)
            startIndex = i
            endIndex = j
            j += 1
            totalSum = currentSum
        else:
            i += 1
            j = i + 1
            # currentSum = 0
            
    '''
    currSum = totalSum = nums[0]
    
    for num in nums[1:]:
        currSum = max(num, currSum + num)
        totalSum = max(totalSum, currSum)
    
    return totalSum

        
if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result = maxSubarray(nums)
    print(result)

    nums = [-2, 1]
    result = maxSubarray(nums)
    print(result)
    
    nums = [-2, 1, 3]
    result = maxSubarray(nums)
    print(result)

