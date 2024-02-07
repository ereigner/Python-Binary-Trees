# LAB 5
# REMINDER: The work in this assignment must be your own original work and must be completed alone.

from xml.dom.expatbuilder import parseFragmentString


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def __str__(self):
        return ("Node({})".format(self.value)) 

    __repr__ = __str__


class BinarySearchTree:
    '''
        >>> x=BinarySearchTree()
        >>> x.isEmpty()
        True
        >>> x.insert(9)
        >>> x.insert(4)
        >>> x._numLeaves()
        1
        >>> x.insert(11)
        >>> x.insert(2)
        >>> len(x)
        4
        >>> x.insert(5)
        >>> x.insert(10)
        >>> x._numLeaves()
        3
        >>> x.insert(9.5)
        >>> x.insert(7)
        >>> len(x)
        8
        >>> x.getMin
        Node(2)
        >>> x.getMax
        Node(11)
        >>> 67 in x
        False
        >>> 9.5 in x
        True
        >>> x.isEmpty()
        False
        >>> x.getHeight(x.root)   # Height of the tree
        3
        >>> x.getHeight(x.root.left.right)
        1
        >>> x.getHeight(x.root.right)
        2
        >>> x.getHeight(x.root.right.left)
        1
        >>> x.printInorder
        2 : 4 : 5 : 7 : 9 : 9.5 : 10 : 11 : 
    '''
    def __init__(self):
        self.root = None


    def insert(self, value):
        if self.root is None:
            self.root=Node(value)
        else:
            self._insert(self.root, value)


    def _insert(self, node, value):
        if(value<node.value):
            if(node.left==None):
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        else:   
            if(node.right==None):
                node.right = Node(value)
            else:
                self._insert(node.right, value)
    
    @property
    def printInorder(self):
        if self.isEmpty(): 
            return None
        else:
            self._inorderHelper(self.root)
        
    def _inorderHelper(self, node):
        if node is not None:
            self._inorderHelper(node.left) 
            print(node.value, end=' : ') 
            self._inorderHelper(node.right)  


    def isEmpty(self):
        if self.root == None:
            return True
        else:
            return False
       
   
    def __len__(self):
        return self._lenHelper(self.root)

    def _lenHelper(self,node):
        if node == None:
            return 0
        if node.left == None and node.right == None:                            # If there are no children then it's a leaf node and just return 1
            return 1
        else:
            return 1 + self._lenHelper(node.left) + self._lenHelper(node.right)         # Adds up all the nodes on the left and right side plus the root node
        


    def _numLeaves(self):
        return self._numLeavesHelper(self.root)


    def _numLeavesHelper(self,node):
        if node == None:
            return 0
        if node.left == None and node.right == None:                            # If there are no children then it's a leaf node and just return 1
            return 1
        else:
            return self._numLeavesHelper(node.left) + self._numLeavesHelper(node.right)         # Goes through the left side of the tree and right side and gathers all the leaf nodes from either side

        



    @property
    def getMin(self): 
        if self.isEmpty() == True:
            return 0
        return self.minHelper(self.root)

    def minHelper(self,node):
        if self.root and node.left == None:                         # If the root and the node on the left are none return the node
            return node
        else:
            return self.minHelper(node.left)                        # Returns the mimimum node of the left side of the tree



    @property
    def getMax(self): 
        if self.isEmpty() == True:
            return 0
        return self.maxHelper(self.root)


    def maxHelper(self,node):
        if self.root and node.right == None:                        # If the root and the nodes on the right side are none return the node  
            return node
        else:
            return self.maxHelper(node.right)                       # Return the max node of the right side of the tree
        



    def __contains__(self,value):
        if self.isEmpty() == True:
            return 0
        return self.containsHelper(self.root,value)

    def containsHelper(self,node,value):
        if node == None:
            return False
        if node.value == value:                                 # compares the value of the node with the value passed in and if it is true return True
            return True
        else:
            return self.containsHelper(node.left,value) or self.containsHelper(node.right,value)                # recursion of the left side of the tree or the right side of the tree and checks all the nodes



    def getHeight(self, node):
        if node == None:
            return 0
        if node.left == None and node.right == None:                # If the node has no children it is a leaf and you return 0 for height
            return 0
        else:
            left_child = self.getHeight(node.left)                  # Gets the height of all the left nodes
            right_child = self.getHeight(node.right)                # Gets the height of all the right nodes
            if left_child > right_child:                            # If there is a greater height on the left side return the height from the left plus root node
                return left_child + 1   
            else:
                return right_child + 1


if __name__ == '__main__':
    import doctest
    doctest.run_docstring_examples(BinarySearchTree, globals(), name='LAB5',verbose=True)

