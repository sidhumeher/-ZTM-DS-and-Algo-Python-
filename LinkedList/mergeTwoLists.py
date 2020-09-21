'''
Created on Sep 20, 2020

@author: sidteegela
'''

'''
Merge two sorted linked lists and return it as a new sorted list. 
The new list should be made by splicing together the nodes of the first two lists.
'''


class ListNode:
    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(l1, l2):
        
        head = temp = ListNode()
        
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                temp.next = l1
                l1 = l1.next
            else :
                temp.next = l2
                l2 = l2.next
            temp = temp.next
            
        temp.next = l1 or l2
        
        return head.next
    
    
if __name__ == '__main__':
    pass
