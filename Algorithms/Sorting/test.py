'''
Created on Oct 14, 2020

@author: sidteegela
'''

if __name__ == '__main__':

    alpha = ['z', 'x', 'a', 'e', 'g', 'n']
    numbers = [1, 5, 7, 10, 99, 27, 82, 3]
    
    # sorted()- creates a new list
    print(sorted(alpha))  # Output: ['a', 'e', 'g', 'n', 'x', 'z']
    print(sorted(numbers))  # Output: [1, 3, 5, 7, 10, 27, 82, 99]

    # sort()-sorts in place
    alpha.sort()
    numbers.sort()
    print(alpha)
    print(numbers)
