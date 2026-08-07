# Unit 2 Discussion: Stacks and Queues

## Overview

This assignment explores two fundamental linear data structures:

- Stack (LIFO)
- Queue (FIFO)

## Learning Objectives

- Implement stack operations
- Implement queue operations
- Understand LIFO and FIFO behavior
- Create edge cases

## Requirements

Complete all TODO sections:

1. Implement stack operations.
2. Implement queue operations.
3. Demonstrate LIFO behavior.
4. Demonstrate FIFO behavior.
5. Create and test edge cases.
6. Create a real-world scenario.

## Implementation Documentation
The Stack class was implemented using a Python list as the internal data structure. The class includes the following methods:

__init__(): Initializes an empty list to store stack values.
push(value): Adds a value to the top of the stack by appending to the list. This operation supports LIFO behavior because both addition and removal occur at the end of the list.
pop(): Removes and returns the most recently added value. An IndexError is raised if the stack is empty, forcing the caller to handle empty conditions explicitly.
peek(): Returns the value at the top of the stack without removing it, allowing inspection of the next value to be popped.
is_empty(): Returns True if the stack contains no values.

The Stack class demonstrates LIFO ordering where values added last are removed first, similar to a stack of plates where you take from the top.

2. Queue Class

The Queue class was implemented using collections.deque as the internal data structure. This choice was made because deque provides O(1) time complexity for both append and popleft operations, which is more efficient than using a regular list.

The class includes the following methods:

__init__(): Initializes an empty deque to store queue values.
enqueue(value): Adds a value to the back of the queue. This operation supports FIFO behavior because values are added to one end and removed from the other.
dequeue(): Removes and returns the value from the front of the queue. An IndexError is raised if the queue is empty.
front(): Returns the value at the front of the queue without removing it, allowing inspection of the next value to be dequeued.
is_empty(): Returns True if the queue contains no values.

The Queue class demonstrates FIFO ordering where values added first are removed first, similar to a line at a store where people are served in the order they arrived.

3. LIFO Behavior Demonstration

The stack demonstration creates a stack and adds four string values: A, B, C, and D. After adding all values, the stack is emptied by repeatedly calling pop(). The output clearly shows that values are removed in reverse order (D, C, B, A), confirming LIFO behavior.

The demonstration includes a comment explaining the expected order before removal occurs, making the LIFO principle explicit to anyone reading the code.

4. FIFO Behavior Demonstration

The queue demonstration creates a queue and adds four integer values: 1, 2, 3, and 4. After adding all values, the queue is emptied by repeatedly calling dequeue(). The output clearly shows that values are removed in the same order they were added (1, 2, 3, 4), confirming FIFO behavior.

Like the stack demonstration, the queue includes explanatory comments about the expected order before removal occurs.

5. Edge Case Testing

The implementation tests several important edge cases:

Pop from empty stack: Attempts to pop from an empty stack and catches the IndexError to show proper error handling.
Peek at empty stack: Attempts to peek at an empty stack and handles the resulting exception.
Dequeue from empty queue: Attempts to dequeue from an empty queue and handles the exception.
Front of empty queue: Attempts to view the front of an empty queue and handles the exception.
Single-item structures: Tests that a stack or queue with one item behaves correctly, including checking is_empty before and after removal, using peek/front, and verifying that removal empties the structure.

These edge cases are critical because they test boundary conditions that commonly cause bugs in production code.

6. Main Function

The main() function orchestrates all demonstrations. It creates both a Stack and Queue object, adds values, displays the LIFO and FIFO behavior through loop-based output, tests edge cases with try-except blocks, and tests single-item scenarios. The function uses formatted output with clear headers and descriptive print statements so that anyone reading the output understands what operation is occurring and why.


## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain the differences between stacks and queues as this relates to real-world applications.
