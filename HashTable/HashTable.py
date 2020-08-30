'''
Created on Aug 20, 2020

@author: sidteegela
'''


class HashTable(object):
    '''
    Dictionary implementation in Python using list
    '''

    def __init__(self, length):
        '''
        Constructor
        '''
        # Initialize array with empty values
        self.array = [None] * length
        
    def hash(self, key):
        
        # Get index of array given key
        length = len(self.array)
        return hash(key) % length
    
    def add(self, key, value):
        
        if self.isFull():
            self.double()
            
        index = self.hash(key)
        
        if self.array[index] is not None:
            for k in self.array[index]:
                if k[0] == key:
                    k[1] = value
                    break
                else:
                    self.array[index].append([key, value])
        else:
            self.array[index] = []
            self.array[index].append([key, value])
            
    def get(self, key):
        index = self.hash(key)
        
        if self.array[index] is None:
            return KeyError()
        else:
            for k in self.array[index]:
                if k[0] == key:
                    return k[1]
    
    def isFull(self):
        items = 0
        # Count number of indexes full in hash table
        
        for item in self.array:
            if item is not None:
                items += 1
                
        # Check if number of items is more than half of array size
        
        return items > len(self.array) / 2
    
    def double(self):
        
        # Double the list length
        ht_new = HashTable(length=len(self.array) * 2)
        
        for i in range(len(self.array)):
            if self.array[i] is None:
                continue
            
            for k in self.array[i]:
                ht_new.add(k[0], k[1])
        
        self.array = ht_new.array
