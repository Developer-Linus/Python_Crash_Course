# Defining a class to encapsulate stack data structure
class Stack:
    # Initialize stack with an empty list
    def __init__(self):
        self.items = []
    # Adding an item to the top of the stack (LIFO principle)

    def push(self, item):
        self.items.append(item)

    # Removing and returning the top item from the stack
    # Return None if the stack is empty
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None
    # Viewing the top item without removing it
    # Return None if the Stack is empty

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    # Checking if the stack is empty
    def is_empty(self):
        return len(self.items) == 0

    # Returning the current size of the stack
    def size(self):
        return len(self.items)


def main():
    # Creating a new stack instance
    stack = Stack()

    # Pushing items on the stack
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(f'Stack after pushing 1, 2, 3: {stack.items}')

    # Peeking at the top item
    peek_item = stack.peek()
    print(f'Top item (peek): {peek_item}')

    # Popping items off the stack
    popped_item = stack.pop()
    print(f'Popped item: {popped_item}')
    print(f'Stack after popping item: {stack.items}')

    # Checking if the stack is empty
    print(f'Is the stack empty? : {stack.is_empty()}')

    # Checking the size of the stack
    print(f'Stack size: {stack.size}')


if __name__ == "__main__":
    main()
