'''
Created on Sep 26, 2020

@author: sidteegela
'''
# Queue implementation with Linked list


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


class Queue():
    
    '''
    Lookup: O(n)
    Enqueue: O(1)
    Dequeue: O(1)
    Peek: O(1)
    '''
    
    def __init__(self):
        self.head = None
        self.last = None
        
    def enqueue(self, data):
        
        if self.last is None:
            newNode = Node(data)
            self.head = newNode
            self.last = self.head
        else:
            newNode = Node(data)
            self.last.set_next(newNode)
            self.last = newNode
            
    def dequeue(self):
        
        if self.head is None:
            return None
        else:
            returnNode = self.head.data
            self.head = self.head.get_next()
            return returnNode
                
    def peek(self):
        
        if self.head is None:
            return None
        else:
            return self.head.data
        
    def printQueue(self):
        array = []
        current = self.head
        while current is not None:
            array.append(current.get_data())
            current = current.get_next()
        print(array)

        
if __name__ == '__main__':
    
    newQueue = Queue()
    
    # Enqueue
    newQueue.enqueue(1)
    newQueue.enqueue(2)
    newQueue.enqueue(3)
    newQueue.enqueue(4)
    newQueue.enqueue(5)
    
    newQueue.printQueue()
    
    # Dequeue
    print(newQueue.dequeue())
    newQueue.printQueue()
    
    # Peek
    print(newQueue.peek())
    
