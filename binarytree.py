from node import Node
import random

class BinaryTree:
    def __init__(self, data = None, node=None):
        if node:
            self.root = node
        elif data:
            node = Node(data)
            self.root = node
        else:
            self.root = None

    def inorder_traversal(self, node = None):
        if node is None:
            node = self.root
        if node.left:
            self.inorder_traversal(node.left)
        print(node, end=" ")
        if node.right:
            self.inorder_traversal(node.right)

    def postorder_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.postorder_traversal(node.left)
        if node.right :
            self.postorder_traversal(node.right)
        print(node, end="")

    def height(self, node=None):
        if node is None:
            node = self.root
        hleft = 0
        hright = 0
        if node.left:
            hleft = self.height(node.left)
        if node.right :
            hright = self.height(node.right)
        if hright > hleft:
            return hright + 1
        return hleft + 1

def inorder_example_tree():
    tree = BinaryTree()
    n1 = Node('a')
    n2 = Node('+')
    n3 = Node('*')
    n4 = Node('b')
    n5 = Node('-')
    n6 = Node('/')
    n7 = Node('c')
    n8 = Node('d')
    n9 = Node('e')

    n6.left = n7
    n6.right = n8
    n5.left = n6
    n5.right = n9
    n3.left = n4
    n3.right = n5
    n2.left = n1
    n2.right = n3
    
    tree.root = n2
    return tree

def postorder_example_tree():
    tree = BinaryTree()
    n1 = Node("I")
    n2 = Node("N")
    n3 = Node("S")
    n4 = Node("C")
    n5 = Node("R")
    n6 = Node("E")
    n7 = Node("V")
    n8 = Node("A")
    n9 = Node("5")
    n0 = Node("3")

    n2.left = n1
    n4.right = n3
    n5.right = n4
    n6.left = n2
    n6.right = n5
    n9.left = n7
    n9.right = n8
    n0.left = n6
    n0.right = n9

    tree.root = n5
    return tree

def binarysearch_example_tree():
    tree = BinaryTree()
    
    n0 = Node(61)
    n1 = Node(89)
    n2 = Node(66)
    n3 = Node(43)
    n4 = Node(51)
    n5 = Node(16)
    n6 = Node(55)
    n7 = Node(11)
    n8 = Node(79)
    n9 = Node(77)
    n11 = Node(82)
    n12 = Node(32)

    n0.right = n1
    n0.left = n3
    n1.left = n2
    n2.right = n8
    n3.right = n4
    n3.left = n5
    n4.right = n6
    n5.left = n7
    n8.left = n9
    n8.right = n11
    n5.right = n12

    node = Node(51)
    
    tree.root = n0
    tree.binary_search(node)
    return tree

class BinarySearchTree(BinaryTree):
    def insert(self, value):
        parent = None
        x = self.root
        while(x):
            parent = x
            if value < x.data:
                x = x.left
            else:
                x = x.right
        if parent is None:
            self.root= Node(value)
        elif value < parent.data:
            parent.left = Node(value)
        else:
            parent.right = Node(value)

    def search(self, value, node=0):
        if node == 0:
            node = self.root
        if node is None:
            return node
        if node.data == value:
            return BinarySearchTree(node)
        if value < node.data:
            return self.search(value, node.left)
        return self.search(value, node.right)
            
if __name__ == "__main__":
    random.seed(77)
    values = random.sample(range(1, 1000), 42)
    
    bst = BinarySearchTree()

    for v in values:
        bst.insert(v)

    bst.inorder_traversal()

    items = [1, 3, 981, 510, 1000]
    for item in items:
        r = bst.search(item)
        if r is None:
            print(item, "não encontrado")
        else:
            print(r.root.data, "encontrado")
    
