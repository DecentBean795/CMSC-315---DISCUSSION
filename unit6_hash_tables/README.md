# Unit 6 Discussion: Dictionaries as Hash Tables

## Overview

This assignment uses Python dictionaries to demonstrate hash table behavior.

## Learning Objectives

- Insert key-value pairs
- Retrieve values efficiently
- Update existing values
- Remove entries
- Understand hashing concepts

## Requirements

1. Create and populate a dictionary.
2. Demonstrate lookup operations.
3. Demonstrate update operations.
4. Demonstrate delete operations.
5. Test edge cases.
6. Create a real-world scenario.

## Implementation Documentation

The program starts by creating an empty dictionary named hash_table and then inserting five key-value pairs one at a time, pairing five fruit names with their prices. This section is where the connection to hash tables is explained directly in the comments: a Python dictionary is a hash table under the hood, since every key is run through a hash function to compute an index into an internal array of buckets. That hashed placement is what lets Python jump straight to a key's storage location instead of scanning the whole structure, which is why insert, lookup, update, and delete all run in average O(1) time rather than the O(n) time a list search would need. After the five pairs are added, the full dictionary is printed so the contents are visible before any further operations run.

Lookup Operations

Two existing keys, "apple" and "cherry", are retrieved directly with dictionary indexing and printed. The comment above this block ties the behavior back to hashing: looking up a key hashes it and jumps straight to the bucket holding its value, which is the same constant-time mechanism that made insertion fast. Both lookups succeed because both keys were added in the insert step, and printing each result alongside its key label makes it clear which value came from which lookup.

Update Operations

This section reassigns the value stored under the "banana" key from its original price to a new one, printing the dictionary's value for that key both before and after the change. The comment explains that assigning to an existing key hashes to the exact same bucket used during insertion and simply overwrites the value already sitting there, rather than creating a second entry. That is the practical difference between updating and inserting: the key count in the dictionary does not grow, only the stored value changes.

Delete Operations

The "date" key is removed with the del statement, and the dictionary is printed both before and after the deletion so the missing entry is visible in the output. The accompanying comment explains that deleting a key hashes it to locate its bucket and then clears that bucket's entry entirely, which frees the slot for a future key rather than leaving a placeholder behind.

Edge Case Testing

Three edge cases are demonstrated. The first looks up "date" again immediately after it was deleted, using dictionary.get() with a default string instead of direct indexing; this avoids the KeyError that direct indexing would raise on a missing key and instead returns a clear "not found" message. The second edge case attempts to delete "date" a second time, but first checks membership with the in operator before calling del, which shows the safe pattern for deleting a key that may or may not exist without crashing the program. The third edge case creates a brand-new empty dictionary and calls .get() on it, showing that an empty hash table is still valid and simply returns the default value on any lookup since it has no keys hashed into it yet.

Main Function

The main function runs all four core operations in order (insert, lookup, update, delete) followed by the edge case demonstrations, printing a labeled header before each section so the output reads top to bottom in the same order the requirements list them. Explanatory comments sit directly above each block of code so the reasoning behind hashing, collisions being avoided by Python's implementation, and each operation's behavior is visible in the source file and not only inferred from the printed results.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain how hash tables behave, what collisions are, and how hash tables can improve efficiency.