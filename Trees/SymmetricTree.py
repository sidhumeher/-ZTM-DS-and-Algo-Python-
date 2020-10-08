'''
Created on Oct 3, 2020

@author: sidteegela
'''


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def isSymmetric(self, root):
        
        if root is None:
            return True
        
        return self.helper(root.left, root.right)
        
    def helper(self, node1, node2):
        
        '''
        Two pointers
        node1 searches using DFS, Left-Root-Right manner.
        node2 searches using DFS, Right-Root-Left manner.
        '''
        
        if node1 == None and node2 == None:
            return True
        else:
            # If both nodes are not NONE
            if node1.data != node2.data:
                return False
            if node1.data == node2.data:
                x = self.helper(node1.left, node2.right)
                y = self.helper(node1.right, node2.left)
                return x and y  # If node1 left is not same as node right then False else True
        
        return False
        

if __name__ == '__main__':
    pass
