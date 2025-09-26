class Node:
    def __init__(self, data, next=None, before=None):
        self.data = data
        self.next = next
        self.before = before


class LinkedList:
    def __init__(self, data):
        node = Node(data)
        self.head = node
        self.rear = node
    
    def print_all(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next
    
    def insert_front (self, data):
         node = Node(data)
         if self.head is not None:
            self.head.before = node
            node.next = self.head        
            self.head = node
         else:
            self.head = node
            self.rear = node
    
    def insert_back (self, data):
        node = Node(data)
        if self.rear is not None:
            node.before = self.rear
            self.rear.next = node        
            self.rear = node
        else:
            self.head = node
            self.rear = node
    
    def delete_data(self, data):
        current_node = self.head
        while current_node is not None:
            if data == current_node.data:
                if current_node == self.head and current_node == self.rear:
                    self.head = None
                    self.rear = None
                elif current_node == self.head:
                    current_node.next.before = None
                    self.head = current_node.next
                    current_node.next = None

                elif current_node == self.rear:
                    current_node.before.next = None
                    self.rear = current_node.before
                    current_node.before = None

                else:
                    current_node.before.next = current_node.next
                    current_node.next.before = current_node.before
                    current_node.before = None
                    current_node.next = None

                break
            else:
                current_node = current_node.next


#PRUEBAS
print ("\nInsert Front")
linked_list = LinkedList(10)
linked_list.insert_front(20)
linked_list.print_all()

print ("\nInsert Back")
linked_list.insert_back(30)
linked_list.print_all()

print ("\nDelete data")
linked_list.insert_front(30)
linked_list.insert_front(10)
print("List before delete")
linked_list.print_all()
linked_list.delete_data(30)
print("\nList after delete")
linked_list.print_all()