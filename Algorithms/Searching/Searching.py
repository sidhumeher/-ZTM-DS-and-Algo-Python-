'''
Created on Nov 22, 2020

@author: sidteegela
'''
from queue import Queue


class Node:
    
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
         
         
def breadthFirstSearch(root):
    
    result = []
    current = root
    q = Queue()  # Keep track of parent nodes

    q.put(current)
    
    while q.empty() != True:
        current = q.get_nowait()
        result.append(current.value)
        if current.left:
            q.put(current.left)
        if current.right:
            q.put(current.right)
            
    return result


def depthFirstSearch(root, result):
    
    if root == None:
        return 
    
    # Pre order traversal
    result.append(root.value)
    if root.left:
        depthFirstSearch(root.left, result)
        
    if root.right:
        depthFirstSearch(root.right, result)


if __name__ == '__main__':
    
    root = Node(9)
    node1 = Node(4)
    node2 = Node(20)
    
    root.left = node1
    root.right = node2
    
    node3 = Node(1)
    node4 = Node(6)
    
    node1.left = node3
    node1.right = node4
    
    node5 = Node(15)
    node6 = Node(170)
    
    node2.left = node5
    node2.right = node6
    
    # BFS
    print('BFS:', breadthFirstSearch(root))
    
    # DFS
    result = []
    depthFirstSearch(root, result)
    print('DFS:', result)
