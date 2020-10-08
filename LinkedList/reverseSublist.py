'''
Created on Oct 7, 2020

@author: sidteegela
'''

# Reverse specified portion of a Singly linked list
'''
Input: 1->2->3->4->5->6->7
Output: 1->5->4->3->2->6->7
'''
import LinkedList


def reverseSublist(head, start, finish):
    
    prev = None
    current = head
    
    # Skipping nodes still start point
    for _ in range(start):
        prev = current
        current = current.next

    # current points to node at start point
    # prev points to start-1 node
    
    startNode = current
    endNode = None
    index = start
    
    while current != None and index <= finish:
        next = current.next
        current.next = endNode
        endNode = current
        current = next
        
        index += 1
    
    # Now startNode points to node at start index
    # endNode points to node at finish index and current points to finish+1 node
    
    startNode.next = current
    if prev == None:
        head = endNode
    else:
        prev.next = endNode
        
    return head

# Time complexity depends on search for finish node. O(finish)


if __name__ == '__main__':
    pass
