'''
Created on Aug 30, 2020

@author: sidteegela
'''


class Node(object):
    
    def __init__(self, data=None, prev_node=None, next_node=None):
        self.data = data
        self.prev = prev_node
        self.next = next_node

    def getData(self):
        return self.data
    
    def getPreviousNode(self):
        return self.prev
    
    def setPreviousNode(self, data):
        self.prev = data
    
    def getNextNode(self):
        return self.next
    
    def setNextNode(self, data):
        self.next = data


class DoublyLinkedList():

    def __init__(self, head=None):
        self.head = head
        
    def insert_atHead(self, data):
        newNode = Node(data)
        newNode.setNextNode(self.head)
        self.head.setPreviousNode(newNode)
        self.head = newNode
        
    # Insert at index
    def insert(self, index, data):                
        prev = self.head
        
        for _ in range(0, index - 1):
            prev = prev.getNextNode()
        
        after = Node(prev.getNextNode())
        newNode = Node(data)
        
        newNode.setNextNode(after.getData())
        after.setPreviousNode(newNode.getData())
        prev.setNextNode(newNode)
        newNode.setPreviousNode(prev.getData())
    
    def insert_atTail(self, data):
        newNode = Node(data)
        temp = self.head
        
        while temp.getNextNode() is not None:
            temp = temp.getNextNode()
        
        temp.setNextNode(newNode)
        newNode.setPreviousNode(temp)
        newNode.setNextNode(None)
        
    def size(self):
        current = self.head
        count = 0
        
        while current:
            current = current.getNextNode()
            count += 1
            
        return count
    
    def search(self, data):
        current = self.head
        found = False
        
        if current is None:
            print('List is empty')
        
        while current and found != True:
            if current.getData() == data:
                return current.getData()
            else:
                current = current.getNextNode()

    def delete(self, data):
        current = self.head
        previous = None
        found = False
        
        # If Node to be deleted is Head
        if current is None:
            print('List is empty')
            return
        elif current.getData() == data:
            self.head = self.head.getNextNode()
            self.head.setPreviousNode(None)
            return
        
        while current and found != True:
            if current.getData() == data:
                print('Found')
                found = True
            else:
                previous = current
                current = current.getNextNode()
                
        if current is None:
            print('Item not found')
        elif previous is None:
            self.head = current
        else:
            previous.setNextNode(current.getNextNode())
            
    def printList(self):
        array = []
        current = self.head
        
        while current is not None:        
            array.append(current.getData())
            current = current.getNextNode()
            
        print(array)
        
    def reverseDoublyLinkedList(self):
        
        if self.head is None:
            print('List is empty')
            return 
    
        '''
        if self.head.getNextNode() is None:
            return self.head
        '''
        prev = None
        curr = self.head
        curr_next = None
        
        while curr is not None:
            curr_next = curr.getNextNode()
            curr.setNextNode(prev)
            prev = curr
            curr = curr_next
        self.head = prev

        
if __name__ == '__main__':
    
    list1 = DoublyLinkedList()
    list1.head = Node(1)
    
    item2 = Node(2)
    item3 = Node(3)
    
    # list1.printList()
    
    list1.head.setNextNode(item2)
    item2.setPreviousNode(list1.head)
    item2.setNextNode(item3)
    item3.setPreviousNode(item2)
    
    # Insert Node at head
    list1.insert_atHead(4)
    # list1.printList()
    
    # Insert Node at Tail
    list1.insert_atTail(5)
    # list1.printList()
    
    # Insert Node at an index
    list1.insert(3, 9)
    # list1.printList()
    
    # Size
    print('Size:', list1.size())
    
    # Search
    print('Found:', list1.search(9))
    
    # Delete Head
    list1.delete(4)
    list1.printList()
    
    # Delete Tail
    list1.delete(5)
    list1.printList()
    
    list1.reverseDoublyLinkedList()
    list1.printList()
