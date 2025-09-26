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
    
    def print_forward(self):
        current_node = self.head
        print("Print forward")
        while current_node is not None:
            print (current_node.data)
            current_node = current_node.next
    
    def print_bacward(self):
        current_node = self.rear
        print("Print bacward")
        while current_node is not None:
            print (current_node.data)
            current_node = current_node.previous
    
    def prepend (self,data):
        node = Node(data)
        if self.head is not None:
            self.head.previous = node
            node.next = self.head
            self.head = node
        else:
            self.head = node
            self.rear = node
    
    def append (self,data):
        node = Node(data)
        if self.rear is not None:
            node.previous = self.rear
            self.rear.next = node
            self.rear = node
        else:
            self.head = node
            self.rear = node
    
    def delete(self,data):
        current_node = self.head
        while current_node is not None:
            if data == current_node.data:
                if current_node == self.head and current_node == self.rear:
                    self.head = None
                    self.rear = None
                elif current_node == self.head:
                    current_node.next.previous = None
                    self.head = current_node.next
                    current_node.next = None
                elif current_node == self.rear:
                    current_node.previous.next = None
                    self.rear = current_node.previous
                    current_node.previous = None
                else:
                    current_node.previous.next = current_node.next
                    current_node.next.previous = current_node.previous
                    current_node.previous = None
                    current_node.next = None
                break
            else:
                current_node = current_node.next

#PRUEBAS
print("APPEND")
double_ended_queue = DoubleEndedQueue('A')
double_ended_queue.append('B')
double_ended_queue.append('C')
double_ended_queue.print_forward()
double_ended_queue.print_bacward()

print("\nPREPEND")
double_ended_queue.prepend('X')
double_ended_queue.print_forward()
double_ended_queue.print_bacward()

print("\nDELETE")
double_ended_queue.delete('B')
double_ended_queue.print_forward()
double_ended_queue.print_bacward()