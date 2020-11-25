'''
Created on Nov 25, 2020

@author: sidteegela
'''
# Fibonacci sequence  f(n) = f(n-1) + f(n-2)


# Using recursion
def fibonacci(num):
    if num < 0:
        return
    if num == 0:
        return 0
    if num == 1:
        return 1
    
    return fibonacci(num - 2) + fibonacci(num - 1)

# Time complexity: O(2^n)
# Space: O(1), o(n) if call stack size is considered


# Using Dynamic programming
def fibonacci1(num):
    
    cache = [0, 1]
    
    for i in range(2, num + 1):
        cache.append(cache[i - 1] + cache[i - 2])
    return cache[num]

# Time complexity: O(n)


# Using Dynamic programming
cache = {}


def fibonacci2(num):
    
    if num in cache:
        return cache[num]
    elif num < 2:
        return num
    else:
        cache[num] = fibonacci2(num - 2) + fibonacci2(num - 1)
        
    return cache[num]


if __name__ == '__main__':
    num = 9
    print(fibonacci(num))
    
    num = 9
    print(fibonacci1(num))
    
    num = 9
    print(fibonacci2(num))
    print(cache)
