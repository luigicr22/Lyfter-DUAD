class Node:
    def __init__(self, data, next=None, before=None):
        self.data = data
        self.next = next
        self.before = before
2

class LinkedList:
    def __init__(self, data):
        node = Node(data)
        self.head = node
        self.rear = node
    
    def print_all(self):
        current_node = self.head
        print_list = "-"
        while current_node is not None:
            print_list = print_list + str(current_node.data) + "-"
            current_node = current_node.next
        print(print_list.strip("-"))
    
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
    
    def bubble_sort(self):
        current_node = self.head
        last_node = self.rear
        while current_node != last_node:
            is_not_changed = True
            while current_node != last_node:
                next_node = current_node.next
                before_node = current_node.before
                if current_node.data > next_node.data:
                    next_node.before = current_node.before
                    current_node.before = next_node
                    current_node.next = next_node.next
                    next_node.next = current_node

                    if next_node == self.rear:
                        self.rear = current_node
                        last_node = self.rear
                    elif next_node == last_node:
                        last_node = current_node
                    
                    if current_node == self.head:
                        self.head = next_node
                    elif before_node is not None:
                        before_node.next = next_node
                    is_not_changed = False
                else:
                    current_node = current_node.next
            if is_not_changed:
                break
            current_node = self.head
            last_node = last_node.before

linked_list = LinkedList(1)
linked_list.insert_front(2)
linked_list.insert_front(3)
linked_list.insert_front(4)
linked_list.insert_front(5)
linked_list.insert_front(6)
linked_list.insert_front(7)
linked_list.insert_front(8)
linked_list.insert_front(9)

linked_list.print_all()
linked_list.bubble_sort()
linked_list.print_all()
