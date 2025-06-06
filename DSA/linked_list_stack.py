# Class to represent each element in a linked list (Data and reference to the next node)
class Node:
    def __init__(self, data):
        self.data = data  # Value ( a string or number, etc)
        self.next = None  # Link to the next node
# Creat a  class  for managing nodes of Linked List


class LinkedList:
    def __init__(self):
        self.head = None

    # Method for inserting a new node at head
    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node
    # Insert a node at a specific position in a Linked List
    # Index starts from zero

    def insertAtIndex(self, data, index):
        if (index == 0):
            self.insertAtBegin(data)
            return
        position = 0
        current_node = self.head
        while (current_node != None and position+1 != index):
            position = position+1
            current_node = current_node.next
        if current_node != None:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next
            current_node.next = new_node
        else:
            print("Index not found.")
    # Insertion in a Linked List at End

    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while (current_node.next):
            current_node = current_node.next
        current_node.next = new_node
