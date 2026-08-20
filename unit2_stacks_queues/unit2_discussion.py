"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        # Implementation: Python list to store stack values.
        # We use a list and append/pop from the end to achieve O(1) operations.
        self.items = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        # Implementation: Add value to the top of the stack.
        # This operation supports LIFO behavior because we always add to the end
        # and remove from the end, ensuring the most recently added value
        # (last in) is the first one we remove (first out).
        self.items.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?
        # Implementation: Remove and return the most recently added value.
        # If the stack is empty, we raise an IndexError to signal the error condition.
        # The caller can handle this exception appropriately.
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack")
        return self.items.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        # Implementation: Return the top value without removing it.
        # This allows us to inspect what will be popped next without
        # modifying the stack structure.
        if self.is_empty():
            raise IndexError("Cannot peek at an empty stack")
        return self.items[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        # Implementation:
        return len(self.items) == 0


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        # Implementation: collections.deque for efficient queue operations.
        # deque allows O(1) append (enqueue) and popleft (dequeue) operations,
        # which is more efficient than using a list where popleft would be O(n).
        self.items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        # Implementation: Add value to the back of the queue.
        # This operation supports FIFO behavior because we add to the back
        # and remove from the front, ensuring the first item added
        # (first in) is the first one we remove (first out).
        self.items.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        # Implementation: Remove and return the value from the front of the queue.
        # If the queue is empty, we raise an IndexError to signal the error condition.
        # The caller can handle this exception appropriately.
        if self.is_empty():
            raise IndexError("Cannot dequeue from an empty queue")
        return self.items.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        # Implementation: Return the front value without removing it.
        # This allows us to see which item will be dequeued next
        # without modifying the queue structure.
        if self.is_empty():
            raise IndexError("Cannot access front of an empty queue")
        return self.items[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        # Implementation:
        return len(self.items) == 0


def main():
    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.
    
    print("=" * 60)
    print("UNIT 2: STACKS AND QUEUES")
    print("=" * 60)

    print("\n=== STACK DEMO ===")
    print("Creating a stack and adding 4 values: A, B, C, D")
    stack = Stack()
    values = ['A', 'B', 'C', 'D']
    
    for value in values:
        stack.push(value)
        print(f"Pushed '{value}' to stack")
    
    print("\nDemonstrating LIFO (Last In, First Out) behavior:")
    print("The values were added in order: A, B, C, D")
    print("They will be removed in reverse order: D, C, B, A")
    
    while not stack.is_empty():
        top_value = stack.pop()
        print(f"Popped '{top_value}' from stack")
    
    print("\nStack is now empty.")
    
    print("\nTesting pop() on an empty stack:")
    try:
        stack.pop()
    except IndexError as e:
        print(f"Error caught: {e}")
    
    print("\nTesting peek() on an empty stack:")
    try:
        stack.peek()
    except IndexError as e:
        print(f"Error caught: {e}")
    
    print("\nTesting single-item stack:")
    stack.push("Single")
    print(f"Pushed 'Single' to stack")
    print(f"Stack is empty: {stack.is_empty()}")
    print(f"Peeked value: {stack.peek()}")
    popped = stack.pop()
    print(f"Popped '{popped}' from stack")
    print(f"Stack is now empty: {stack.is_empty()}")

    # ===============================
    # TODO (Student): QUEUE DEMO
    # ===============================
    # Requirements:
    # 1. Create a Queue object.
    # 2. Add at least 4 values to the queue.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate FIFO behavior.
    # 5. Show what happens when dequeue() is used on an empty queue.
    #
    # Edge Cases:
    # 6. Show what happens when front() is used on an empty queue.
    # 7. Create a queue with only one item, remove it,
    #    and verify the queue is empty afterward.

    print("\n" + "=" * 60)
    print("=== QUEUE DEMO ===")
    print("Creating a queue and adding 4 values: 1, 2, 3, 4")
    queue = Queue()
    values = [1, 2, 3, 4]
    
    for value in values:
        queue.enqueue(value)
        print(f"Enqueued {value} to queue")
    
    print("\nDemonstrating FIFO (First In, First Out) behavior:")
    print("The values were added in order: 1, 2, 3, 4")
    print("They will be removed in the same order: 1, 2, 3, 4")
    
    while not queue.is_empty():
        front_value = queue.dequeue()
        print(f"Dequeued {front_value} from queue")
    
    print("\nQueue is now empty.")
    
    print("\nTesting dequeue() on an empty queue:")
    try:
        queue.dequeue()
    except IndexError as e:
        print(f"Error caught: {e}")
    
    print("\nTesting front() on an empty queue:")
    try:
        queue.front()
    except IndexError as e:
        print(f"Error caught: {e}")
    
    print("\nTesting single-item queue:")
    queue.enqueue("First")
    print(f"Enqueued 'First' to queue")
    print(f"Queue is empty: {queue.is_empty()}")
    print(f"Front value: {queue.front()}")
    dequeued = queue.dequeue()
    print(f"Dequeued '{dequeued}' from queue")
    print(f"Queue is now empty: {queue.is_empty()}")


if __name__ == "__main__":
    main()
