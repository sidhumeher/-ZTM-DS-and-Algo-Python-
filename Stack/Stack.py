'''
Created on Sep 26, 2020

@author: sidteegela
'''

# Stack implementation with Linked List


class Node(object):
    
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node
    
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next_node
    
    def set_next(self, data):
        self.next_node = data


class Stack():
    
    def __init__(self):
        self.head = None
        
    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False
        
    def push(self, data):
        newNode = Node(data)
        
        if self.head == None:
            self.head = newNode
        else:
            newNode.set_next(self.head)
            self.head = newNode

    def peek(self):
        
        if self.head == None:
            return None
        else:
            return self.head.data
        
    def pop(self):
        
        if self.isEmpty():
            return None
        else:
            poppedNode = self.head
            self.head = self.head.get_next()
            poppedNode.set_next(None)
            return poppedNode.data
    
    def printStack(self):
        array = []
        current = self.head
        while current is not None:
            array.append(current.data)
            current = current.get_next()
        print(array)
        

if __name__ == '__main__':
    newStack = Stack()
    # Push
    newStack.push(1)
    newStack.push(2)
    newStack.push(3)
    newStack.push(4)
    newStack.push(5)
    '''
    Stack printed as array. Element in first index is top of stack
    and also the head of linked list
    '''
    newStack.printStack()
    # Pop
    print(newStack.pop())
    newStack.printStack()
    
    # Peek
    print(newStack.peek())
    
