'''
Created on Nov 23, 2020

@author: sidteegela
'''


class Node:
    
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Technique: Keep a lower and upper limit for each node comparison
def isValidBST(root):
    
    def helper(node, lower=float('-inf'), upper=float('inf')):
        if node == None:
            return True
        
        val = node.val
        if val <= lower or val >= upper:
            return False
        if helper(node.left, lower, val) == False:
            return False
        if helper(node.right, val, upper) == False:
            return False
        
        return True
        
    return helper(root)

# Time complexity: O(n)
# Space: O(n)


if __name__ == '__main__':
    root = Node(2)
    node1 = Node(1)
    node2 = Node(3)
    
    root.left = node1
    root.right = node2
    
    print(isValidBST(root))
    
    ######
    
    root = Node(5)
    node1 = Node(1)
    node2 = Node(4)
    
    root.left = node1
    root.right = node2
    
    node3 = Node(3)
    node4 = Node(6)
    
    node2.left = node3
    node2.right = node4
    
    print(isValidBST(root))
