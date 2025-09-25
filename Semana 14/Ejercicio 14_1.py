#Stack

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self, data):
        node = Node(data)
        self.head = node
    
    def print_structure(self):
        current_node = self.head
        while current_node is not None:
            print (current_node.data)
            current_node = current_node.next
    
    def push (self, data):
        node = Node(data)
        if self.head is not None:
            node.next = self.head
            self.head = node
        else:
            self.head = node
    
    def pop (self):
        if self.head is not None:
            pop_node = self.head
            self.head = self.head.next
            pop_node.next = None

#PRUEBAS

my_stack= Stack('A')
my_stack.push('B')
print("\nPrimera Pila")
my_stack.print_structure()

my_stack.pop()
print("\nPila Modificada")
my_stack.print_structure()

my_stack.pop()
my_stack.pop()
print("\nPila Vacia")
my_stack.print_structure()

my_stack.push('A')
my_stack.push('B')
my_stack.push('C')
my_stack.push('D')
print("\nPila Modificada 2")
my_stack.print_structure()