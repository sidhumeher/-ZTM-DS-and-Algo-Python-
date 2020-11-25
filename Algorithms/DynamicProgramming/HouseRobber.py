'''
Created on Nov 25, 2020

@author: sidteegela
'''


def proRobber(nums):
    
    if nums == 0:
        return 0
    
    p = 0; q = 1
    p_num = 0; q_num = 0
    
    while p < len(nums):
        p_num += nums[p]
        p += 2
    while q < len(nums):
        q_num += nums[q]
        q += 2
        
    maxMoney = max(p_num, q_num)
    return maxMoney


if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    print(proRobber(nums))
    
    nums = [2, 7, 9, 3, 1]
    print(proRobber(nums))
