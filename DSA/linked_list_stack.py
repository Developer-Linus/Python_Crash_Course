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
    # Update the Node of a linked list

    def updateNode(self, val, index):
        current_node = self.head
        position = 0

        if position == index:
            current_node.data = val
        else:
            while (current_node != None and position+1 != index):
                current_node = current_node.next
                if current_node != None:
                    current_node.data = val
                else:
                    print('Index not found.')

    # Remove first node from linked list
    def remove_first_node(self):
        if self.head is None:
            return
        self.head = self.head.next
    # Remove last node from linked list

    def remove_last_node(self):
        if self.head is None:
            return
        current_node = self.head
        while (current_node != None and current_node.next.next != None):
            current_node = current_node.next
        current_node.next = None

    # Remove an item from a specific position in a linked list
    def remove_at_index(self, index):
        if self.head is None:
            return
        current_node = self.head
        position = 0

        if index == 0:
            self.remove_first_node()
        else:
            while current_node is not None and position < index-1:
                position += 1
                current_node = current_node.next

                if current_node is None or current_node.next is None:
                    print('Index not found.')
                else:
                    current_node.next = current_node.next.next
    # Delete a linked list node of given data

    def remove_node(self, data):
        current_node = self.head

        if current_node == data:
            self.remove_first_node()
            return
        while current_node is not None and current_node.next.data != data:
            current_node = current_node.next
            if current_node is None:
                return
            else:
                current_node.next = current_node.next.next
    # Linked list traversal

    def printLL(self):
        current_node = self.head
        while (current_node):
            print(current_node.data)
            current_node = current_node.next
    # Get length of linked list

    def sizeOfLL(self):
        size = 0
        if (self.head):
            current_node = self.head
            while (current_node):
                size += 1
                current_node = current_node.next
            return size
        else:
            return 0


def main():
    llist = LinkedList()
    # add nodes to the linked list
    llist.insertAtEnd('a')
    llist.insertAtEnd('b')
    llist.insertAtBegin('c')
    llist.insertAtEnd('d')
    llist.insertAtIndex('g', 2)

    # print the linked list
    print("Node Data:")
    llist.printLL()

    # remove nodes from the linked list
    print("\nRemove First Node:")
    llist.remove_first_node()
    llist.printLL()

    print("\nRemove Last Node:")
    llist.remove_last_node()
    llist.printLL()

    print("\nRemove Node at Index 1:")
    llist.remove_at_index(1)
    llist.printLL()

    # print the linked list after all removals
    print("\nLinked list after removing a node:")
    llist.printLL()

    print("\nUpdate node Value at Index 0:")
    llist.updateNode('z', 0)
    llist.printLL()

    print("\nSize of linked list:", llist.sizeOfLL())


if __name__ == "__main__":
    main()
