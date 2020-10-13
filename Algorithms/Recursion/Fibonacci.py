'''
Created on Oct 12, 2020

@author: sidteegela
'''
'''
Given a number N return the index value of the Fibonacci sequence, where the sequence is:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144 ...
the pattern of the sequence is that each value is the sum of the 2 previous values,
that means that for N=5 → 2+3

For example: fibonacciRecursive(6) should return 8
'''


def fibonacciWithRecursion(num):
    
    if num == 0:
        return 0
    if num == 1 or num == 2:
        return 1
    
    return fibonacciWithRecursion(num - 1) + fibonacciWithRecursion(num - 2)
    
# Time Complexity: Exponential time O(2^n). Pretty bad


def fibonacciWithIteration(num):
    if num == 0:
        return 0
    if num == 1 or num == 2:
        return 1
    
    sum1 = 1
    sum2 = 1
    totalSum = 0
    for _ in range(3, num + 1):
        totalSum = sum1 + sum2
        sum1 = sum2
        sum2 = totalSum

    return totalSum
# Time Complexity: O(n)


if __name__ == '__main__':
    print(fibonacciWithRecursion(6))
    print(fibonacciWithRecursion(5))
    print(fibonacciWithRecursion(4))

    print('\n')
    print(fibonacciWithIteration(6))
    print(fibonacciWithIteration(5))
    print(fibonacciWithIteration(4))
