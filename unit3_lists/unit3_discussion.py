"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
    # Use Python's built-in insert method to add the value at the specified index.
    # This operation shifts all elements at and after the insertion point one position to the right.
    lst.insert(index, value)
    
    # Performance note: Insertion at the beginning (index 0) requires shifting all existing
    # elements, resulting in O(n) time complexity. Insertion at the end (index len(lst))
    # requires no shifting and is O(1). Middle insertions are O(n) on average.


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """
    # Index validation is critical because accessing an invalid index would raise an IndexError.
    # In production code, we want to handle this gracefully rather than crashing.
    # Check if the index is within the valid range (0 to len(lst) - 1).
    if index < 0 or index >= len(lst):
        return None
    
    # Use Python's pop method to remove and return the value at the specified index.
    # This operation shifts all elements after the deletion point one position to the left.
    removed_value = lst.pop(index)
    return removed_value


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    # This is a linear search, which means we scan through the list sequentially from start to end.
    # We check each element one by one until we find a match or reach the end of the list.
    # Linear search is O(n) because in the worst case, we must examine every element.
    for i in range(len(lst)):
        if lst[i] == value:
            # Return the index immediately when the value is found.
            return i
    
    # If we exit the loop without finding the value, return -1 to indicate the value is not in the list.
    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===")
    
    # Create a list with initial values.
    numbers = [10, 20, 30, 40]
    print(f"Original list: {numbers}")
    
    # Insert at the beginning (index 0).
    # This requires shifting all existing elements one position to the right.
    insert_at(numbers, 0, 5)
    print(f"After inserting 5 at the beginning: {numbers}")
    
    # Insert in the middle (index 2).
    # Elements after index 2 are shifted to the right.
    insert_at(numbers, 2, 15)
    print(f"After inserting 15 at the middle: {numbers}")
    
    # Insert at the end (index len(numbers)).
    # No shifting is required because we are adding past the last element.
    insert_at(numbers, len(numbers), 50)
    print(f"After inserting 50 at the end: {numbers}")

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")
    
    # Start with a fresh list for deletion tests.
    numbers = [10, 20, 30, 40, 50]
    print(f"Original list for deletion: {numbers}")
    
    # Delete from the beginning (index 0).
    # The element at index 0 is removed, and all other elements shift left.
    removed = delete_at(numbers, 0)
    print(f"Removed from beginning: {removed}, List is now: {numbers}")
    
    # Delete from the middle (index 1, which now contains 30 after the first deletion).
    # Elements after the deletion point shift left.
    removed = delete_at(numbers, 1)
    print(f"Removed from middle: {removed}, List is now: {numbers}")
    
    # Delete from the end (index len(numbers) - 1).
    # No shifting is required because we are removing the last element.
    removed = delete_at(numbers, len(numbers) - 1)
    print(f"Removed from end: {removed}, List is now: {numbers}")

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")
    
    # Create a list for searching.
    numbers = [10, 20, 30, 40, 50]
    print(f"List for searching: {numbers}")
    
    # Search for a value that exists in the list.
    # The linear search scans from index 0 until it finds the matching value.
    index = search_value(numbers, 30)
    if index != -1:
        print(f"Found 30 at index {index}")
    
    # Search for a value that does not exist in the list.
    # The linear search scans all elements and returns -1 when no match is found.
    index = search_value(numbers, 99)
    if index == -1:
        print(f"Value 99 not found in the list (returned -1)")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")
    
    # Edge case 1: Delete using an invalid index.
    # When we try to delete at an index that does not exist, the function returns None
    # instead of crashing. This graceful handling prevents program failure.
    numbers = [10, 20, 30]
    print(f"Test list: {numbers}")
    result = delete_at(numbers, 10)
    print(f"Attempt to delete at index 10 (invalid): returned {result}, list remains: {numbers}")
    
    # Edge case 2: Insert into an empty list.
    # Even an empty list can accept insertions at index 0.
    empty_list = []
    print(f"Empty list: {empty_list}")
    insert_at(empty_list, 0, 100)
    print(f"After inserting 100 into empty list: {empty_list}")
    
    # Edge case 3: Delete from an empty list.
    # Attempting to delete from an empty list returns None because there are no valid indices.
    empty_list = []
    result = delete_at(empty_list, 0)
    print(f"Attempt to delete from empty list: returned {result}")
    
    # Edge case 4: Search for the first element.
    # A linear search finds the value immediately when it appears at index 0.
    numbers = [100, 20, 30, 40]
    index = search_value(numbers, 100)
    print(f"Search for first element (100): found at index {index}")



if __name__ == "__main__":
    main()
