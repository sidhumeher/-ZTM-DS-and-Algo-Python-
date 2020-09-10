'''
Created on Aug 24, 2020

@author: sidteegela
'''


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


class LinkedList():
    
    def __init__(self, head=None):
        self.head = head
        
    def insert_atHead(self, data):
        newNode = Node(data)
        newNode.set_next(self.head)
        self.head = newNode

    # Append
    def insert_atEnd(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = data
            return
        lastNode = self.head
        while lastNode.get_next() is not None:
            lastNode = lastNode.next_node
        lastNode.next_node = newNode
        
    def insert_between(self, middleNode, data):
        # Insert after middleNode
        if middleNode is None:
            print('Node does not exist')
            return 
        
        newNode = Node(data)
        newNode.next_node = middleNode.next_node
        middleNode.next_node = newNode
        
    def size(self):
        count = 0
        current = self.head
        
        while current:
            current = current.next_node
            count += 1
            
        return count
    
    def search(self, data):
        current = self.head
        found = False
        
        while current and found != True:
            if current.get_data() == data:
                found = True
                return current
            else:
                current = current.next_node
        if current is None:
            print('Item not found')
        else:
            return current

    def delete(self, data):
        current = self.head
        previous = None
        found = False
        
        while current and found != True:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next() 
                
        if current is None:
            print('Item not found')
        elif previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
            
    def printList(self):
        array = []
        current = self.head
        while current is not None:
            array.append(current.data)
            current = current.get_next()
        print(array)

    
if __name__ == '__main__':
    list1 = LinkedList()
    list1.head = Node(1)
    
    item2 = Node(2)
    item3 = Node(3)
    
    list1.head.next_node = item2
    item2.next_node = item3
    
    list1.printList()
    
    list1.insert_atEnd(4)
    # list1.printList()
    
    list1.insert_between(item3, 5)
    # list1.printList()
    
    list1.insert_atHead(9)
    # list1.printList()
    
    list1.delete(5)
    list1.printList()
    
    size = list1.size()
    print('List size:', size)
    
    found = list1.search(3)
    print('Found item:', found.get_data())
    
