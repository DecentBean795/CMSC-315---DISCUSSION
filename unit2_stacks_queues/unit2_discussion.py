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
        # Internal data structure: Python list to store stack values.
        # We use a list and append/pop from the end to achieve O(1) operations.
        self.items = []

    def push(self, value):
        # Add value to the top of the stack.
        # This operation supports LIFO behavior because we always add to the end
        # and remove from the end, ensuring the most recently added value
        # (last in) is the first one we remove (first out).
        self.items.append(value)

    def pop(self):
        # Remove and return the most recently added value.
        # If the stack is empty, we raise an IndexError to signal the error condition.
        # The caller can handle this exception appropriately.
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack")
        return self.items.pop()

    def peek(self):
        # Return the top value without removing it.
        # This allows us to inspect what will be popped next without
        # modifying the stack structure.
        if self.is_empty():
            raise IndexError("Cannot peek at an empty stack")
        return self.items[-1]

    def is_empty(self):
        # Return True if the stack has no values.
        return len(self.items) == 0


class Queue:
    def __init__(self):
        # Internal data structure: collections.deque for efficient queue operations.
        # deque allows O(1) append (enqueue) and popleft (dequeue) operations,
        # which is more efficient than using a list where popleft would be O(n).
        self.items = deque()

    def enqueue(self, value):
        # Add value to the back of the queue.
        # This operation supports FIFO behavior because we add to the back
        # and remove from the front, ensuring the first item added
        # (first in) is the first one we remove (first out).
        self.items.append(value)

    def dequeue(self):
        # Remove and return the value from the front of the queue.
        # If the queue is empty, we raise an IndexError to signal the error condition.
        # The caller can handle this exception appropriately.
        if self.is_empty():
            raise IndexError("Cannot dequeue from an empty queue")
        return self.items.popleft()

    def front(self):
        # Return the front value without removing it.
        # This allows us to see which item will be dequeued next
        # without modifying the queue structure.
        if self.is_empty():
            raise IndexError("Cannot access front of an empty queue")
        return self.items[0]

    def is_empty(self):
        # Return True if the queue has no values.
        return len(self.items) == 0


def main():
    print("=" * 60)
    print("UNIT 2: STACKS AND QUEUES")
    print("=" * 60)

    # ===============================
    # STACK DEMO
    # ===============================
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
    
    # Edge case: Test pop on empty stack
    print("\nTesting pop() on an empty stack:")
    try:
        stack.pop()
    except IndexError as e:
        print(f"Error caught: {e}")
    
    # Edge case: Test peek on empty stack
    print("\nTesting peek() on an empty stack:")
    try:
        stack.peek()
    except IndexError as e:
        print(f"Error caught: {e}")
    
    # Edge case: Single item stack
    print("\nTesting single-item stack:")
    stack.push("Single")
    print(f"Pushed 'Single' to stack")
    print(f"Stack is empty: {stack.is_empty()}")
    print(f"Peeked value: {stack.peek()}")
    popped = stack.pop()
    print(f"Popped '{popped}' from stack")
    print(f"Stack is now empty: {stack.is_empty()}")

    # ===============================
    # QUEUE DEMO
    # ===============================
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
    
    # Edge case: Test dequeue on empty queue
    print("\nTesting dequeue() on an empty queue:")
    try:
        queue.dequeue()
    except IndexError as e:
        print(f"Error caught: {e}")
    
    # Edge case: Test front on empty queue
    print("\nTesting front() on an empty queue:")
    try:
        queue.front()
    except IndexError as e:
        print(f"Error caught: {e}")
    
    # Edge case: Single item queue
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
