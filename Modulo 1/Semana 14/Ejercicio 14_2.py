#Double Ended Queue

class Node:
    def __init__(self, data, next=None, previous=None):
        self.data = data
        self.next = next
        self.previous = previous

class DoubleEndedQueue:
    def __init__(self, data):
        node = Node(data)
        self.head = node
        self.rear = node
    
    def print_structure_left_right(self):
        current_node = self.head
        while current_node is not None:
            print (current_node.data)
            current_node = current_node.next
    
    def print_structure_right_left(self):
        current_node = self.rear
        while current_node is not None:
            print (current_node.data)
            current_node = current_node.previous
    
    def push_left (self,data):
        node = Node(data)
        if self.head is not None:
            self.head.previous = node
            node.next = self.head
            self.head = node
        else:
            self.head = node
            self.rear = node
    
    def push_right (self,data):
        node = Node(data)
        if self.rear is not None:
            node.previous = self.rear
            self.rear.next = node
            self.rear = node
        else:
            self.head = node
            self.rear = node
    
    def pop_left(self):
        if self.head is not None:
            if self.head is not self.rear:
                pop_node = self.head
                self.head = self.head.next
                self.head.previous = None
                pop_node.next = None
            else:
                self.head = None
                self.rear = None
    
    def pop_right(self):
        if self.rear is not None:
            if self.rear is not self.head:
                pop_node = self.rear
                self.rear = self.rear.previous
                self.rear.next = None
                pop_node.previous = None

            else:
                self.head = None
                self.rear = None


#PRUEBAS

print("Full Push left")
my_double_ended_queue= DoubleEndedQueue('A')
my_double_ended_queue.push_left('B')
my_double_ended_queue.push_left('C')
my_double_ended_queue.push_left('D')
print("Left to right")
my_double_ended_queue.print_structure_left_right()
print("Right to left")
my_double_ended_queue.print_structure_right_left()
my_double_ended_queue.pop_left()
my_double_ended_queue.pop_left()
my_double_ended_queue.pop_left()
my_double_ended_queue.pop_left()
print("\nDouble ended queue vacia")
print("Left to right")
my_double_ended_queue.print_structure_left_right()
print("Right to left")
my_double_ended_queue.print_structure_right_left()

print("\n\nFull Push Right")
my_double_ended_queue.push_right('A')
my_double_ended_queue.push_right('B')
my_double_ended_queue.push_right('C')
my_double_ended_queue.push_right('D')
print("Left to right")
my_double_ended_queue.print_structure_left_right()
print("Right to left")
my_double_ended_queue.print_structure_right_left()
my_double_ended_queue.pop_right()
my_double_ended_queue.pop_right()
my_double_ended_queue.pop_right()
my_double_ended_queue.pop_right()
print("\nDouble ended queue vacia")
print("Left to right")
my_double_ended_queue.print_structure_left_right()
print("Right to left")
my_double_ended_queue.print_structure_right_left()


print("\n\nFull Push Mix")
my_double_ended_queue.push_right('A')
my_double_ended_queue.push_left('B')
my_double_ended_queue.push_right('C')
my_double_ended_queue.push_left('D')
print("Left to right")
my_double_ended_queue.print_structure_left_right()
print("Right to left")
my_double_ended_queue.print_structure_right_left()
my_double_ended_queue.pop_right()
my_double_ended_queue.pop_left()
my_double_ended_queue.pop_right()
my_double_ended_queue.pop_right()
my_double_ended_queue.pop_left()
print("\nDouble ended queue vacia")
print("Left to right")
my_double_ended_queue.print_structure_left_right()
print("Right to left")
my_double_ended_queue.print_structure_right_left()