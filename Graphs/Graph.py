'''
Created on Oct 8, 2020

@author: sidteegela
'''

# Graph implementation with Dictionary


class Graph():
    
    def __init__(self, graph=None):
        if graph == None:
            self.graph_dict = {}
        self.graph_dict = graph

    def generateEdges(self, graph):
        
        edges = []
        
        for node in graph:
            for neighbor in graph[node]:
                edges.append((node, neighbor))
        
        return edges

    def isolatedNodes(self, graph):
        
        isolatedNodes = []
        
        for node in graph:
            if len(graph[node]) == 0:
                isolatedNodes.append(node)

        return isolatedNodes
    
    def nodes(self):
        return list(self.graph_dict.keys())
    
    def addNode(self, node):
        if node not in self.graph_dict:
            self.graph_dict[node] = []
        return
    
    def addEdge(self, node):
        # Edge can be a list, since a node can connect to many nodes
        
        nodes = list(node)
        if nodes[0] in self.graph_dict:
            self.graph_dict[nodes[0]].append(nodes[1])
        else:
            self.graph_dict[nodes[0]] = [nodes[1]]
    
    def print(self):
        nodes = 'Nodes: '
        for node in self.graph_dict:
            nodes += str(node) + ' '
        print(nodes)
        
        edges = 'Edges:'
        edges += self.generateEdges(graph)
        print(edges)


if __name__ == '__main__':

    graph = { "a" : ["c"],
          "b" : ["c", "e"],
          "c" : ["a", "b", "d", "e"],
          "d" : ["c"],
          "e" : ["c", "b"],
          "f" : []
        }
    g = Graph(graph)
    
    # Graph edges
    edges = g.generateEdges(graph)
    print(edges)
    
    # Isolated nodes
    print(g.isolatedNodes(graph))
    
    # Adding node
    g.addNode('g')
    
    # Add edge
    g.addEdge('g' 'd')
    
    edges = g.generateEdges(graph)
    print(edges)
    
