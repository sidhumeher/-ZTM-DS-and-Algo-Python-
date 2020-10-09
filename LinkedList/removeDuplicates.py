'''
Created on Oct 7, 2020

@author: sidteegela
'''


def removeDuplicates(head):
    
    if head == None:
        return None

    slow = head
    
    while slow:
        fast = slow.next
        
        while fast and fast.data == slow.data:
            fast = fast.next
        slow.next = fast
        slow = fast
        
    return head

# Time complexity: O(n)


if __name__ == '__main__':
    pass
