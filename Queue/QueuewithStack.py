'''
Created on Sep 27, 2020

@author: sidteegela
'''

'''
Using one stack and using recursion
Enqueue: Push to stack
Dequeue: If stack is empty, return error. If stack has only 1 element, return it
Recursively pop everything from stack,store popped item, push it back to stack and return
'''


class QueuewithStack:
    
    def __init__(self):
        self.stack = []
        
    def enqueue(self, data):
        
        self.stack.append(data)
        
    def dequeue(self):
        
        if len(self.stack) == 0:
            print('Queue is empty')
            return None
        
        x = self.stack[len(self.stack) - 1]
        self.stack.pop()
        
        if len(self.stack) == 0:
            return x
        # Recursive call
        item = self.dequeue()
        
        self.stack.append(x)
        
        return item
    
    def peek(self):
        if len(self.stack) == 0:
            print('Queue is empty')
            return None
        else:
            return self.stack[0]
    
    def printQueue(self):
        print(self.stack)


if __name__ == '__main__':
    
    newQueue = QueuewithStack()
    
    newQueue.enqueue(1)
    newQueue.enqueue(2)
    newQueue.enqueue(3)
    newQueue.enqueue(4)
    newQueue.enqueue(5)
    
    newQueue.printQueue()

    # Dequeue
    newQueue.dequeue()
    newQueue.printQueue()
    
    # Peek
    print(newQueue.peek())
