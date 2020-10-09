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
        for edge in self.generateEdges(graph):
            edges += str(edge) + ' '
        print(edges)

    def findPath(self, startNode, endNode, path=None):
        if path is None:
            path = []
            
        graph = self.graph_dict
        path += [startNode]
        
        if startNode == endNode:
            return path
        if startNode not in graph:
            return None
        
        for node in graph[startNode]:
            if node not in path:
                extendPath = self.findPath(node, endNode, path)
                
                if extendPath:
                    return extendPath
            
        return None
    
    def findAllPaths(self, startNode, endNode, path):
        
        if path is None:
            path = []
        graph = self.graph_dict
        path += [startNode]
        
        if startNode == endNode:
            return path

        if startNode == None:
            return None
        
        paths = []
        for node in graph[startNode]:
            if node not in path:
                extend_path = self.findAllPaths(node, endNode, path)
                
                for path in extend_path:
                    paths.append(path)
        return paths


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
    
    # Find path from a to b
    path = g.findPath('a', 'b', [])
    print(path)
    
    # Print graph
    g.print()
    
    # Find all paths
    # paths = g.findAllPaths('a', 'b', [])
    # print(paths)
    
