'''
Created on Nov 1, 2020

@author: sidteegela
'''
from queue import Queue

# Given a tree, find a level with maximum no of nodes


class Node(object):
    
    def __init__(self, data, left=None, right=None):
        
        self.data = data
        self.left = left
        self.right = right


def MaxNodeLevel(root):
    
    if root == None:
        return 
    
    q = Queue()
    
    # Append root
    q.put(root)
    
    current_level = 0; maxNodes = float('-inf'); result_level = 0
    
    while True:
        # No of nodes in current level
        nodeCount = q.qsize()
        
        if nodeCount == 0:
            break
        
        # check max nodes
        if nodeCount > maxNodes:
            maxNodes = nodeCount
            result_level = current_level
            
        # Pop current level nodes
        while nodeCount > 0:
            node = q.queue[0]
            q.get()
            if node.left != None:
                q.put(node.left)
            if node.right != None:
                q.put(node.right)
                
            nodeCount -= 1
        # Increase current level
        current_level += 1
        
    return result_level

# Time Complexity: O(n)
# Space Complexity: O(n)


if __name__ == '__main__':
    root = Node(1)
    node1 = Node(2)
    node2 = Node(3)
    
    root.left = node1
    root.right = node2
    
    node3 = Node(4)
    node4 = Node(5)
    
    node1.left = node3
    node1.right = node4
    
    node5 = Node(6)
    node2.right = node5
    
    print(MaxNodeLevel(root))
    
