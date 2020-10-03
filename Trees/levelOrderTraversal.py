'''
Created on Oct 3, 2020

@author: sidteegela
'''


class Node(object):
    
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Tree(object):
    
    def __init(self, data):
        self.root = data
    
    def levelOrderTraveral(self, root):
        resultArray = []
        
        if root == None:
            return []
        
        levelTracker = [root]
        
        while root and levelTracker:
            currentLevelNodes = []
            nextLevelNodes = []
            
            for node in levelTracker:
                currentLevelNodes.append(node.data)
                if node.left:
                    nextLevelNodes.append(node)
                if node.right:
                    nextLevelNodes.append(node)
                resultArray.append(currentLevelNodes)
                levelTracker = nextLevelNodes
        
        return resultArray


if __name__ == '__main__':
    pass
