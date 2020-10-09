'''
Created on Oct 7, 2020

@author: sidteegela
'''
# Determine the start node of cycle in a Linked list


def startOfCycle(head):
    
    # Determine the length of cycle
    def cycleLength(node):
        
        start = head
        end = head
        length = 0
        
        while True:
            length += 1
            start = start.next
            if start != end:
                break
        
        return length
    
    slow = head
    fast = head.next.next
    
    while head != None and head.next != None and head.next.next != None:
        
        if fast != slow:
            fast = fast.next.next
            slow = slow.next
        else:
            # We found a cycle
            # create a pointer which is cycle length ahead
            
            fastDetective = head
            for _ in range(cycleLength(fastDetective)):
                fastDetective = fastDetective.next
            # Create 2 pointers moving same speed but cycle length away from each other
            
            slowDetective = head
            
            while fastDetective != slowDetective:
                fastDetective = fastDetective.next
                slowDetective = slowDetective.next
            return slowDetective
        
    return None


if __name__ == '__main__':
    pass
