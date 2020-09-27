'''
Created on Sep 26, 2020

@author: sidteegela
'''


class Stack():
    
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        
        if len(self.items) == 0:
            return True
        else:
            return False
    
    def push(self, data):
        self.items.append(data)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        
        if len(self.items) == 0:
            return None
        else:
            return self.items[-1]

    
if __name__ == '__main__':
    
    newStack = Stack()
    # Push
    newStack.push(1)
    newStack.push(2)
    newStack.push(3)
    newStack.push(4)
    newStack.push(5)
    
    print(newStack.items)
    
    # Pop
    print(newStack.pop())
    print(newStack.items)
    
    # Peek
    print(newStack.peek())
    
