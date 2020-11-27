'''
Created on Nov 25, 2020

@author: sidteegela
'''


# Without dynamic programming
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

# Dynamic programming
'''
If n = 1, maxamount = a1, n=2 maxamount = max(a1,a2)
If n = 3, we have 2 options
1. Rob third house and add 1st house amount
2. Stick with maxamont of first and second house
f(k) = max(a3+f(k-2),f(k-1))

We can solve this with 2 variables keeping track of previous 2 max amounts
'''


def proRobber1(nums):
    
    if len(nums) == 0:
        return 0
    
    prev_prev = 0; prev = 0; curr = 0
    
    for amount in nums:
        prev = curr
        curr = max(amount + prev_prev, prev)
        prev_prev = prev
        
    return curr

# Time complexity: O(n)
# Space: O(1)


if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    print(proRobber(nums))
    
    nums = [2, 7, 9, 3, 1]
    print(proRobber(nums))
    
    # Using Dynamic programming
    nums = [1, 2, 3, 1]
    print(proRobber1(nums))
    
    nums = [2, 7, 9, 3, 1]
    print(proRobber1(nums))
