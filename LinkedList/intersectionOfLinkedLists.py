'''
Created on Sep 20, 2020

@author: sidteegela
'''
'''
Write a program to find the node at which the intersection of two singly linked lists begins.
'''


def getIntersectionNode(headA, headB):
    
    # Approach 1: Using Dictionary
    # Time Complexity: O(m + n)
    # Space Complexity: O(m) + O(n)
    '''
    Traverse list A and store the address / reference to each node in a hash set. 
    Then check every node bi in list B: if bi appears in the hash set, then bi is 
    the intersection node.
    ''' 
    
    dirA = {}
        
    if headA is None or headB is None:
        return None
        
    current = headA
        
    while current.next is not None:
        if current.val not in dirA:
            dirA[current.val] = current.next.val
            
        dirA[current.val] = current.next.val
        current = current.next
        
        current = headB
        while current.val is not None:
            if current.val in dirA and dirA[current.val] == current.next.val:
                return current.next
            else:
                current = current.next
        
        return None
    
    # Approach 2: Using 2 pointer technique
    # Time Complexity: O(m + n)
    # Space Complexity: O(1)
    
    '''
    Maintain two pointers pA and pB initialized at the head of A and B, respectively. 
    Then let them both traverse through the lists, one node at a time.
    When pA reaches the end of a list, then redirect it to the head of B; 
    similarly when pB reaches the end of a list, redirect it the head of A.
    If at any point pA meets pB, then pA/pB is the intersection node.
    
    If two lists have intersection, then their last nodes must be the same one. 
    So when pA/pB reaches the end of a list, record the last element of A/B respectively.
    If the two last elements are not the same one, then the two lists have no intersections.
    '''
    
    pointerA = headA
    pointerB = headB
        
    while pointerA is not pointerB:
        if pointerA is not None:
            pointerA = pointerA.next
        else:
            pointerA = headB
            
        if pointerB is not None:
            pointerB = pointerB.next
        else:
            pointerB = headA
            
    return pointerA


if __name__ == '__main__':
    pass
