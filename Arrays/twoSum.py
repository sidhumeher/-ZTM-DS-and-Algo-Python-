'''
Created on Jul 30, 2020

@author: sidteegela
'''


def twoSum(nums, target):
    dic = {}
    for i, num in enumerate(nums):
        if target - num in dic:
            return (dic[target - num], i)
        dic[num] = i


if __name__ == '__main__':
    inputList = [-1, -2, -3, -4, -5]
    target = -8
    result = twoSum(inputList, target)
    print(result)
    
    inputList = [3, 2, 95, 4, -3]
    target = 92
    result = twoSum(inputList, target)
    print(result)
    
    inputList = [4, 2, 5, 1, 9]
    target = 9
    result = twoSum(inputList, target)
    print(result)
