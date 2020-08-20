'''
Created on Aug 17, 2020

@author: sidteegela
'''


def dupliactes2(nums, k):
    if len(nums) == 2 and nums[0] == nums[1] and abs(1 - 0) <= k:
            return True
    i = 0
    j = 1
        
    while i < len(nums):
        while j < len(nums):
            print('i:', i)
            print('j:', j)
            if nums[i] == nums[j] and abs(i - j) <= k:
                return True
            else:
                j += 1
                    
        i += 1
        j = i + 1
        
    return False

# NOTE: Time limit exceeded on Leetcode


if __name__ == '__main__':
    nums = [1, 0, 1, 1]
    k = 1
    
    result = dupliactes2(nums, k)
    print(result)
