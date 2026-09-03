# Unit 4 Discussion: Binary Search Trees

## Overview

This assignment introduces Binary Search Trees (BSTs) and recursive tree operations.

## Learning Objectives

- Build a BST
- Insert values recursively
- Search recursively
- Perform in-order traversal
- Understand BST organization

## Requirements

1. Build a BST.
2. Insert multiple values.
3. Demonstrate in-order traversal.
4. Test searching.
5. Demonstrate edge cases.
6. Create a real-world BST example.

## Implementation Documentation
Node Class

The Node class was implemented as the basic building block of the tree. The constructor stores the value passed in and initializes two references, left and right, to None.

init(value): Stores the node's value and creates two empty child references. Both references start as None because a new node is always added as a leaf, meaning it has no children when it is first created. Those references get filled in later as more values are inserted below it.

The left reference points to the subtree holding smaller values and the right reference points to the subtree holding larger values. That split is the rule the entire structure depends on.

BST Class

The BST class holds a single attribute, root, which is the entry point to the whole structure. Everything else in the tree is reachable by following left and right links down from the root, so a root of None means the tree is empty. The class includes the following methods:

init(): Initializes an empty tree by setting root to None.

insert(value): The public insertion method. It calls the recursive helper and reassigns self.root to whatever the helper returns, which handles the case where the tree was empty and the new value becomes the root. Insertion depends on comparison because smaller values have to go left and larger values have to go right. If that rule were ever broken, in-order traversal would stop producing sorted output and search would lose the ability to skip half the tree.

_insert_recursive(node, value): The recursive worker. Its base case is reaching a None position, which means an empty spot was found and a new Node is created and returned there. Otherwise it compares the value to the current node and recurses left for smaller values or right for larger values, reassigning the child link with whatever comes back. Duplicate values are handled by returning the existing node unchanged, so the tree keeps one copy of each value. Every path returns the current node so the parent's link stays correct.

search(value): The public search method. It delegates to the recursive helper and returns True or False. BST search is more efficient than linear search because a list has to check every item one at a time, which is about n comparisons in the worst case, while a BST makes one comparison at each node and then discards an entire subtree. A balanced tree cuts the remaining search space roughly in half at every step, which is O(log n) instead of O(n). With 1,000 values that difference is about 10 comparisons instead of 1,000.

_search_recursive(node, value): The recursive worker. It returns False when it runs off the bottom of the tree, True on a match, and otherwise recurses into only the one subtree that could possibly hold the value.

search_path(value): An extra helper that was added beyond the required methods. It returns the list of node values that were actually compared during a search, which makes the reduction in search space visible in the program output instead of only describing it in a comment.

inorder(): Creates an empty list, passes it to the recursive helper, and returns the filled list.

_inorder_recursive(node, values): Visits the left subtree, then appends the current node's value, then visits the right subtree. This produces sorted output because of how the tree was built. Everything in a node's left subtree is smaller than that node and everything in its right subtree is larger, so visiting left first guarantees all smaller values are recorded before the current value and visiting right last guarantees all larger values come after it. That property holds at every node, so the whole list comes out in ascending order without any sorting step.

Tree Construction

The construction section creates a BST and inserts seven values in the order 50, 30, 70, 20, 40, 60, 80. Because 50 is inserted first it becomes the root, and the remaining values split evenly so that 20, 30, and 40 land in the left subtree and 60, 70, and 80 land in the right subtree. The output displays the insertion order, the root value, the contents of each subtree, and a simple text drawing of the resulting shape.

A comment explains why this arrangement is efficient. One comparison at the root already rules out half the values, and the same halving happens again at every level going down, so each step reduces the remaining search space instead of checking values one at a time like a list would.

In-Order Traversal Demonstration

The traversal section prints the insertion order and the in-order output side by side so the difference is obvious. The values went in as 50, 30, 70, 20, 40, 60, 80 and come out as 20, 30, 40, 50, 60, 70, 80. The program also compares the traversal result against Python's built-in sorted() and prints True to confirm the match. Nothing in the traversal sorts anything. The ordering comes from the structure of the tree itself.

Search Tests

The search section tests four values. 40 and 80 are both in the tree and return True, while 45 and 100 are not and return False. Each line also prints the comparison path taken from search_path, which shows that every one of the four searches finished in 3 comparisons out of 7 values. Searching for 100 only touched 50, 70, and 80 before running off the bottom of the tree, so even a failed search answered the question without scanning the whole structure.

Edge Case Testing

The implementation tests four edge cases:

Empty tree: A new BST is created and both traversal and search are called on it. The traversal helper hits its base case immediately and returns an empty list, and search returns False. Neither one raises an error, which is the point of testing it.

Duplicate values: 30 is inserted into a tree that already contains it. The recursion walks down to the existing node, finds the value is neither smaller nor larger, and returns that node unchanged. The output prints the traversal and value count before and after to show the tree did not grow.

Single node tree: A tree containing only 42 is built to confirm that a one node tree is still valid. Traversal returns a single item list, a search for 42 returns True, a search for 41 returns False after exactly one comparison, and both child references print as None.

Sorted insertion order: Values are inserted as 10, 20, 30, 40, 50. Since every value is larger than the one before it, every value goes right and the tree collapses into a straight line. The traversal is still correct, but finding 50 now takes 5 comparisons instead of the 3 the balanced tree needed, which demonstrates the O(n) worst case and explains why self balancing structures like AVL and red-black trees exist.

Main Function

The main() function runs all six sections in order with clear headers so the output reads top to bottom as a walkthrough. It builds the balanced tree, demonstrates traversal, loops through the search tests with formatted output showing each comparison path, works through the four edge cases with separate BST objects so the original tree stays intact, and finishes with the library catalog example. Every print statement is written so that a reader can tell what operation is happening and why it produced that result.


## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain BST behavior and compare to how ordering works to create efficiency as compared to other data structures.
