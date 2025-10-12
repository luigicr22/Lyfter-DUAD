class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, data):
        node = Node(data)
        self.root = node
    
    def push (self,data):
        print(f"\nIngreso {data}")
        self.push_number (self.root, data)
    
    def push_number (self, node, data):
        if data < node.data:
            if node.left is not None:
                self.push_number(node.left, data)
            else:
                node.left = Node(data)
        if data >= node.data:
            if node.right is not None:
                self.push_number(node.right, data)
            else:
                node.right = Node(data)
    
    def print_binary_tree (self):
        print("\nBinary Tree Structure:")
        self.print_binary_node (self.root)
    
    def print_binary_node (self, node, log="Root"):
        log = log + f" --> {node.data}"
        print (log)
        if node.left is not None:
            self.print_binary_node (node.left, log)
        if node.right is not None:
            self.print_binary_node (node.right, log)


#PRUEBAS
#Ver imagen adjunta Binary Tree.pdf
binary_tree = BinaryTree(30)
binary_tree.push(15)
binary_tree.push(7)
binary_tree.push(25)
binary_tree.push(5)
binary_tree.push(8)
binary_tree.push(18)
binary_tree.push(26)
binary_tree.push(20)
binary_tree.push(45)
binary_tree.push(35)
binary_tree.push(30)
binary_tree.push(50)
binary_tree.push(47)
binary_tree.push(53)

binary_tree.print_binary_tree()









