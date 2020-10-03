'''
Created on Oct 2, 2020

@author: sidteegela
'''


class Node(object):
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree(object):
    
    def __init__(self):
        self.root = None
            
    def insert(self, data):
        
        if self.root == None:
            self.root = Node(data)
            return
        elif self.root.data == data:
            return
        
        # Recursive insert call
        if data < self.data:
            if self.left:
                return self.left.insert(data)
            else:
                self.left = Node(data)
                return
        else:
            if self.right:
                return self.right.insert(data)
            else:
                self.right = Node(data)
                return
    
    def find(self, data):
        '''
        if self.root == None:
            print('BST is empty')
            return
        elif self.root.data == data:
            return True
        '''
        if self.data == data:
            return True
        
        if data < self.data and self.left:
            return self.left.find(data)
        elif data > self.data and self.right:
            return self.right.find(data)
        else:
            return False
        
    # Pre order tree traversal (root,left,right)
    def preOrder(self, resultArray):
        
        resultArray.append(self.data)
        
        if self.left:
            return self.left.preOrder(resultArray)
        if self.right:
            return self.right.preOrder(resultArray)
        
        return resultArray

    # Post Order tree traversal (left, right, root)
    def postOrder(self, resultArray):
        if self.left:
            return self.left.postOrder(resultArray)
        if self.right:
            return self.right.postOrder(resultArray)
        resultArray.append(self.data)
        
        return resultArray
    
    # In order tree traversal (left, root, right)
    def inOrder(self, resultArray):
        if self.left:
            return self.left.inOrder(resultArray)
        resultArray.append(self.data)
        
        if self.right:
            return self.right.inOrder(resultArray)
        
        return resultArray

    def remove(self, data):
        # Empty tree
        if self.root == None:
            return False
        
        # Delete root node
        if self.root.data == data:
            # If root has no children
            if self.root.left == None and self.root.right == None:
                self.root = None
                return True
            # If root has left child
            if self.root.left:
                self.root = self.root.left
                return True
            # If root has right child
            if self.root.right:
                self.root = self.root.right
                return True
            # Root has 2 children. COMPLICATED PIECE
            # Traverse to the smallest leaf node on root.right and make it root
            else:
                moveNode = self.root.right
                moveNodeParent = None
                
                while moveNode.left:
                    moveNodeParent = moveNode
                    moveNode = moveNode.left
                self.root.data = moveNode.data
                
                # Ex: moveNode = 33 moveNodeParent = 34
                '''
                33
                  \
                   34
                     \
                      97
                '''
                
                if moveNode.data < moveNodeParent.data:
                    moveNodeParent.left = None
                else:
                    moveNodeParent.right = None
                return True
        
        # Find node to remove
        parent = None
        node = self.root
        
        while node and node.data != data:
            parent = node
            if data < node.data:
                node = node.left
            elif data > node.data:
                node = node.right
                
        # Node not found
        if node == None or node.data != data:
            return False
        
        # If node has no children
        elif node.left == None and node.right == None:
            if data < parent.data:
                parent.left = None
            elif data > parent.data:
                parent.right = None
            return True
        
        # If node has left child only
        elif node.left and node.right == None:
            if data < parent.data:
                parent.left = node.left
            else:
                parent.right = node.left
            return True
        
        # If node has right child only
        elif node.right and node.left == None:
            if data < parent.data:
                parent.left = node.right
            else:
                parent.right = node.right
        
        # If node has both left and right children. COMPLICATED PIECE
        else:
            moveNodeParent = node
            moveNode = None
            
            while moveNode.left:
                moveNodeParent = moveNode
                moveNode = moveNode.left
            node.data = moveNode.data
            
            if moveNode.right:
                if moveNode.data < moveNodeParent.data:
                    moveNodeParent.left = moveNode.right
                else:
                    moveNodeParent.right = moveNode.right
            else:
                if moveNode.data < moveNodeParent.data:
                    moveNodeParent.left = None
                else:
                    moveNodeParent.right = None
            return True
        

if __name__ == '__main__':
    pass
