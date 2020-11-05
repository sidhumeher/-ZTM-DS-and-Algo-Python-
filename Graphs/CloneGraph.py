'''
Created on Nov 2, 2020

@author: sidteegela
'''

# For simplicity sake, each node's value is the same as the node's index (1-indexed).


class Node(object):
    
    def __init__(self, val=0, neighbors=None):
        
        self.val = val
        if neighbors == None:
            self.neighbors = []


def cloneGraph(inputList):
    
    # Empty graph
    if len(inputList) == 0:
        return []
    elif len(inputList[0]) == 0:  # Graph contains only 1 node
        return [[]]
             
    graph_dict = {}
    
    for index, neighborList in enumerate(inputList):
        if index + 1 in graph_dict:
            for neighbor in neighborList:
                if neighbor not in graph_dict:
                    graph_dict[neighbor] = []
        else:
            graph_dict[index + 1] = neighborList
    print(graph_dict.values())
    
    
def cloneGraph_recursive(node):

    if node == None:
        return node
    
    if node in visited[node]:
        return visited[node]
    
    # Create clone if not
    clone = Node(node.val, [])
    visited[node] = clone  # given node is key and its clone is value
    
    if node.neighbors:
        clone.neighbors = [cloneGraph(node) for node in node.neighbors]
        
    return clone

# Time complexity: O(n+m), where n=No of nodes, m=No of edges
# Space: O(n), size of dictionary, O(m)= size of recursive stack


if __name__ == '__main__':
    inputList = [[2, 4], [1, 3], [2, 4], [1, 3]]
    
    # cloneGraph(inputList)
    
    visited = {}
    cloneGraph_recursive(Node(1))
