'''
Created on Aug 13, 2020

@author: sidteegela
'''

'''
Given an array nums, write a function to move all 0's to 
the end of it while maintaining the relative order of the non-zero elements.
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
'''


def moveZeroes(nums):
    
    # Using pop() and append() in List NOTE: DID NOT WORK FOR ALL INPUTS. Ex: [0,0,1]
    '''
    for index, item in enumerate(nums):
        if item == 0:
            poppedItem = nums.pop(index)
            nums.append(poppedItem)
    '''        
    
    # Using extra array
    '''
    resultArray = []
    zeroCount = 0
    index = 0
    
    while index < len(nums):
        if nums[index] == 0:
            zeroCount += 1
        else:
            resultArray.append(nums[index])
        index += 1
        
    resultArray = resultArray + zeroCount * [0]
    '''
        
    # Using in-place swapping
    
    zeroPosition = 0
    
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[zeroPosition] = nums[zeroPosition], nums[i]
            zeroPosition += 1
    
    return nums


if __name__ == '__main__':
    
    nums = [0, 1, 0, 3, 12]
    result = moveZeroes(nums)
    print(result)
    
    nums = [0, 0, 1]
    result = moveZeroes(nums)
    print(result)
