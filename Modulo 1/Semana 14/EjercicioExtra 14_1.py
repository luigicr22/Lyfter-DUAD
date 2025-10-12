#Queue

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Queue:
    def __init__(self, data):
        node = Node(data)
        self.head = node
    
    def print_all(self):
        current_node = self.head
        while current_node is not None:
            print (current_node.data)
            current_node = current_node.next
    
    def dequeue(self):
        if self.head is not None:
            dequeue_node = self.head
            self.head = self.head.next
            dequeue_node.next = None
            return dequeue_node
    
    def enqueue(self, data):
        node = Node(data)
        if self.head is not None:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = node
        else:
            self.head = node


#PRUEBAS
my_queue = Queue('A')
my_queue.enqueue('B')
my_queue.enqueue('C')
print("\nQueue Actual")
my_queue.print_all()

print (f"\nNodo eliminado: {my_queue.dequeue().data}")
print("Queue Actual")
my_queue.print_all()