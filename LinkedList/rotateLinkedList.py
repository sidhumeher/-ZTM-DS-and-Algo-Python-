'''
Created on Sep 22, 2020

@author: sidteegela
'''

'''
Rotate linked list to the right by k
Let p go till the node K and q till the last node of linked list.
Point q.next to head
Change head to p.next node
Make p as tail (p.next = None)
'''


def rotateRight(head, k):
        
    count = 0
    p = head
    q = head
        
    while p and count < k:
        p = p.next
        q = q.next
        count += 1
        # print(p.val)
        
    while q.next is not None:
        q = q.next
        # print(q.val)
        
    q.next = head
    head = p.next
    p.next = None
        
    return head


if __name__ == '__main__':
    pass
