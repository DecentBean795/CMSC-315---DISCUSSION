"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.


    print("\n=== INSERT OPERATIONS ===")
    print("TODO: Create a dictionary and add multiple key-value pairs.")

    # A Python dictionary behaves like a hash table: each key is run through
    # a hash function to compute an index into an internal array (the "buckets").
    # That means insert, lookup, update, and delete all run in average O(1) time
    # instead of having to scan every entry like a list would.
    hash_table = {}

    # Adding key-value pairs is like inserting into a hash table: Python hashes
    # each key to decide where the value is stored internally.
    hash_table["apple"] = 1.25
    hash_table["banana"] = 0.60
    hash_table["cherry"] = 3.75
    hash_table["date"] = 4.50
    hash_table["egg"] = 2.10

    print("Dictionary after inserting 5 key-value pairs:")
    print(hash_table)

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    print("\n=== LOOKUP OPERATIONS ===")
    print("TODO: Demonstrate successful key lookups.")

    # Looking up a key hashes it to jump straight to the bucket where the
    # value lives, instead of scanning every item like a list search would.
    apple_price = hash_table["apple"]
    cherry_price = hash_table["cherry"]

    print(f"Lookup 'apple' -> {apple_price}")
    print(f"Lookup 'cherry' -> {cherry_price}")

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    print("\n=== UPDATE OPERATIONS ===")
    print("TODO: Demonstrate updating an existing key.")

    print(f"Before update: 'banana' -> {hash_table['banana']}")

    # Assigning a new value to an existing key hashes to the same bucket and
    # simply overwrites the value stored there; the key is not duplicated.
    hash_table["banana"] = 0.75

    print(f"After update: 'banana' -> {hash_table['banana']}")

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    print("\n=== DELETE OPERATIONS ===")
    print("TODO: Demonstrate deleting a key-value pair.")

    print(f"Before deletion: {hash_table}")

    # Deleting a key hashes it to find its bucket, then removes the entry
    # from that bucket entirely, freeing up the slot for future keys.
    del hash_table["date"]

    print(f"After deleting 'date': {hash_table}")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain edge cases.")

    # Edge case 1: looking up a key that was never inserted (and was just
    # deleted above) raises a KeyError if accessed directly, so we use
    # .get() to look it up safely and return a default value instead.
    missing_lookup = hash_table.get("date", "KEY NOT FOUND")
    print(f"Lookup missing key 'date' with .get() -> {missing_lookup}")

    # Edge case 2: deleting a key that doesn't exist raises a KeyError with
    # `del`, so we check membership first (or use dict.pop with a default)
    # to delete safely without crashing the program.
    if "date" in hash_table:
        del hash_table["date"]
        print("Deleted 'date'.")
    else:
        print("Attempted to delete 'date' safely, but it does not exist.")

    # Edge case 3 (bonus): an empty dictionary is still a valid hash table -
    # it simply has zero buckets in use, so lookups on it always miss safely.
    empty_table = {}
    print(f"Lookup on an empty dictionary -> {empty_table.get('anything', 'EMPTY TABLE')}")



if __name__ == "__main__":
    main()