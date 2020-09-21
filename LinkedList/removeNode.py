'''
Created on Sep 20, 2020

@author: sidteegela
'''
'''
Given a linked list, remove the n-th node from the end of list and return its head
'''

# Time Complexity: O(n)
# Space Complexity O(1)


def removeNthNode(head, n):
    fastPointer = head
    slowPointer = head
        
    while fastPointer.next is not None:
        if n > 0:
            fastPointer = fastPointer.next
            n -= 1
        else:
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next
        
        # print(fastPointer.val)
        # print(slowPointer.val)
        
        slowPointer.next = slowPointer.next.next
        
        return head

    
if __name__ == '__main__':
    pass
