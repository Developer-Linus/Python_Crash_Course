class PriorityQueue:
    # Starting with an empty list to hold toys and their priority number
    def __init__(self):
        self.items = []
    # Adding an item with a priority number (enqueue)

    def enqueue(self, item, priority):
        self.items.append([priority, item])
        # sorting out items so that item with smaller number is of highest importance
        self.items.sort()
    # Showing all the items in queue

    def display(self):
        print(self.items)
    # Taking out the most important item (dequeue)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)[1]  # returns item and not priority
        return None

    # Looking at the most important toy without taking it (peek)
    def peek(self):
        if not self.is_empty():
            return self.items[0][1]  # Toy only and not priority
        return None
    # Checking if the toy box is empty

    def is_empty(self):
        return len(self.items) == 0
    # Counting how many items are in a queue

    def size(self):
        return len(self.items)


def main():
    priority_queue = PriorityQueue()
    # Adding toys with priority numbers
    priority_queue.enqueue('Doll', 3)
    priority_queue.enqueue('Car', 1)
    priority_queue.enqueue('Ball', 2)

    # Displaying items in queue
    priority_queue.display()

    # Looking at the most important toy
    print(f'The most important toy: {priority_queue.peek()}')

    # Taking toys out one by one
    toy2 = priority_queue.dequeue()
    print(f'Took out toy: {toy2}')  # should be car with the highest priority
    print(f'Queue after removing toy2:')
    priority_queue.display()

    toy3 = priority_queue.dequeue()
    print(f'Took out toy: {toy3}')  # should be ball
    print(f'Queue after removing toy3:')
    priority_queue.display()

    # Check if the queue is empty
    print(f'Is the queue empty?: {priority_queue.is_empty()}')

    # Check the queue size
    print(f'The size of the queue is: {priority_queue.size()}')


if __name__ == "__main__":
    main()
