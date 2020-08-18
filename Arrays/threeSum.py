'''
Created on Aug 3, 2020

@author: sidteegela
'''


def threeSum(nums, target):
    
    # My 1st attempt
    if len(nums) == 0:
        return [] 
    result = []
    
    i = 0
    j = 1
    k = 2
    while i < len(nums) - 2 :
        while j < len(nums) - 1 and k < len(nums):
            if nums[i] + nums[j] + nums[k] == target:
                # print(nums[i], nums[j], nums[k])
                result.append([nums[i], nums[j], nums[k]])
            j += 1
            k += 1
        i += 1 
    return result
            

if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    target = 0
    
    result = threeSum(nums, target)
    print(result)
