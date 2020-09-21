'''
Created on Sep 20, 2020

@author: sidteegela
'''

'''
Input: l1 = 2->4->3 l2 = 5->6->4
Output: 7->0->8
Explanation: 342+465 = 807 
'''


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
        
        head = temp = ListNode()
        carry = 0
        
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            temp.next = ListNode(carry % 10)
            temp = temp.next
            carry //= 10
            
        return head.next


if __name__ == '__main__':
    pass
