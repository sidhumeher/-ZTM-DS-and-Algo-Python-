'''
Created on Sep 19, 2020

@author: sidteegela
'''

'''
Given head, the head of a linked list, determine if the linked list has a cycle in it.
Return true if there is a cycle in the linked list. Otherwise, return false.
'''

'''
Two Pointer technique:

1.If there is no cycle, the fast pointer will stop at the end of the linked list.
2.If there is a cycle, the fast pointer will eventually meet with the slow pointer.

'''


def checkForCycle(head):
    if head is None or head.next is None:
        return False
        
    currentPace = head
    fastPace = head
    '''
        while current:
            print(current.val)
            current = current.next
    '''
    while fastPace is not None:
        if currentPace.val != fastPace.val:
            currentPace = currentPace.next
            fastPace = fastPace.next.next
        else:
            return True
            
    return False


if __name__ == '__main__':
    pass
