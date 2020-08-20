'''
Created on Aug 19, 2020

@author: sidteegela
'''
import re


def longestWord(input):
    regex = r"[a-zA-z]*"
    
    matches = re.findall(regex, input)
    longestWord = matches[0]
    maxlength = 0
    
    for word in matches:
        if len(word) > maxlength:
            maxlength = len(word)
            longestWord = word
    return longestWord


if __name__ == '__main__':
    input = "fun&!! time"
    result = longestWord(input)
    print(result)
    
    input = "I love dogs"
    result = longestWord(input)
    print(result)
