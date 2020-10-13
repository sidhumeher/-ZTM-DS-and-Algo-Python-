'''
Created on Oct 12, 2020

@author: sidteegela
'''

# 5! = 5 * 4 * 3 * 2 * 1
# or 5! = 5 * 4!
# 4! = 4 * 3!


def factorialWithRecursion(num):
    
    if num == 1:
        return 1
    if num == 0:
        return 1
    if num == 2:
        return 2
    
    return num * factorialWithRecursion(num - 1)

# Time Complexity: O(n)


def factorialWithIteration(num):
    
    if num == 1 or num == 0:
        return 1
    result = 1
    for i in range(2, num + 1):  # We dont need to start at 1 since 1! is 1. One less loop
        result *= i
        
    return result

# Time Complexity: O(n)


if __name__ == '__main__':
    
    print(factorialWithRecursion(5))
    print(factorialWithRecursion(4))
    print(factorialWithRecursion(3))
    print(factorialWithRecursion(2))
    print(factorialWithRecursion(1))
    
    print('\n')
    print(factorialWithIteration(5))
    print(factorialWithRecursion(4))
    print(factorialWithRecursion(3))
