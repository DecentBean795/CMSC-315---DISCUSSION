"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""


def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """
    pass

    # Walk through every position from the front of the list to the back.
    # There is no assumption that the list is sorted, so the only way to be
    # sure a value is missing is to look at all of it.
    for index in range(len(lst)):

        # One comparison per element. If it matches, stop immediately and
        # hand back the position where it was found.
        if lst[index] == target:
            return index

    # Reaching this line means every element was checked and none matched.
    return -1

    # WHY THIS IS O(n):
    # The amount of work grows in a straight line with the size of the list.
    # In the best case the target sits at index 0 and only one comparison
    # happens. In the worst case the target is at the very last index, or it
    # is not in the list at all, and all n elements get compared. Big-O
    # describes that worst case, so doubling the list size doubles the number
    # of comparisons. A list of 1,000 items takes up to 1,000 comparisons and
    # a list of 2,000 items takes up to 2,000.


def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """
    pass

    # low and high mark the boundaries of the section still worth searching.
    # At the start that section is the whole list.
    low = 0
    high = len(lst) - 1

    # Keep going while there is at least one element left between the
    # boundaries. Once low passes high, the search space is empty.
    while low <= high:

        # Look at the middle of the current section. Integer division keeps
        # the index a whole number.
        mid = (low + high) // 2

        if lst[mid] == target:
            # Found it on this guess.
            return mid

        elif lst[mid] < target:
            # The middle value is too small. Because the list is sorted,
            # everything from mid and below is also too small, so that entire
            # half is thrown away in one step. Move low past mid.
            low = mid + 1

        else:
            # The middle value is too large, so mid and everything above it
            # cannot be the target. Throw away that half by moving high
            # below mid.
            high = mid - 1

    # low passed high, so the search space shrank to nothing without a match.
    return -1

    # HOW EACH ITERATION REDUCES THE SEARCH SPACE:
    # Every pass through the loop makes one comparison and then discards
    # roughly half of what is left. A list of 100 items drops to about 50,
    # then 25, then 12, then 6, then 3, then 1. That halving pattern is why
    # the time complexity is O(log n). Doubling the list size only adds one
    # extra comparison instead of doubling the work like linear search does.


# ADDED HELPER FUNCTIONS (not required, used only for the performance
# analysis below). These mirror the two searches above but also count how
# many comparisons each one made, so the output can show the actual work
# done instead of just claiming one is faster.

def linear_search_steps(lst, target):
    """Same logic as linear_search, but returns (index, comparison_count)."""
    steps = 0
    for index in range(len(lst)):
        steps += 1
        if lst[index] == target:
            return index, steps
    return -1, steps


def binary_search_steps(lst, target):
    """Same logic as binary_search, but returns (index, comparison_count)."""
    steps = 0
    low = 0
    high = len(lst) - 1
    while low <= high:
        steps += 1
        mid = (low + high) // 2
        if lst[mid] == target:
            return mid, steps
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1, steps


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")
    print("TODO: Create a small dataset and test both searches.")

    # A small sorted list of ten even numbers. Binary search requires sorted
    # input, so the same list can be handed to both algorithms fairly.
    small_data = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    print("Dataset:", small_data)

    # CASE 1: a value that exists. 14 sits at index 6.
    target = 14
    linear_result, linear_steps = linear_search_steps(small_data, target)
    binary_result, binary_steps = binary_search_steps(small_data, target)
    print("\nSearching for", target, "(exists)")
    print("  linear_search returned index", linear_search(small_data, target),
          "after", linear_steps, "comparisons")
    print("  binary_search returned index", binary_search(small_data, target),
          "after", binary_steps, "comparisons")

    # Both return index 6, so both are correct. Linear search needed seven
    # comparisons because it checked positions 0 through 6 one at a time.
    # Binary search needed only four because it started in the middle and
    # cut the remaining range in half each time. On a list this small the
    # difference is tiny and either one feels instant.

    # CASE 2: a value that does not exist. 15 is odd, so it is not in the list.
    target = 15
    linear_result, linear_steps = linear_search_steps(small_data, target)
    binary_result, binary_steps = binary_search_steps(small_data, target)
    print("\nSearching for", target, "(does not exist)")
    print("  linear_search returned", linear_search(small_data, target),
          "after", linear_steps, "comparisons")
    print("  binary_search returned", binary_search(small_data, target),
          "after", binary_steps, "comparisons")

    # Both correctly return -1. This is the worst case for linear search
    # because a missing value forces it to check all ten elements before it
    # can rule the list out. Binary search still finishes in a handful of
    # steps since each failed guess still eliminates half the range.

    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")
    print("TODO: Create a larger dataset and compare results.")

    # 100,000 even numbers, still sorted. Built with range() so no data has
    # to be typed by hand.
    large_data = list(range(0, 200000, 2))
    print("Dataset size:", len(large_data), "elements")

    # A value near the end of the list. This is close to the worst case for
    # linear search and shows the gap clearly.
    target = 199998
    linear_result, linear_steps = linear_search_steps(large_data, target)
    binary_result, binary_steps = binary_search_steps(large_data, target)
    print("\nSearching for", target, "(near the end of the list)")
    print("  linear_search returned index", linear_result,
          "after", linear_steps, "comparisons")
    print("  binary_search returned index", binary_result,
          "after", binary_steps, "comparisons")

    # A value that is not present, which is the true worst case for both.
    target = 199999
    linear_result, linear_steps = linear_search_steps(large_data, target)
    binary_result, binary_steps = binary_search_steps(large_data, target)
    print("\nSearching for", target, "(does not exist)")
    print("  linear_search returned", linear_result,
          "after", linear_steps, "comparisons")
    print("  binary_search returned", binary_result,
          "after", binary_steps, "comparisons")

    # WHY BINARY SEARCH PULLS AHEAD AS THE DATA GROWS:
    # Linear search does one comparison per element, so its worst case on
    # 100,000 items is 100,000 comparisons. Binary search halves the range
    # every pass, so its worst case is log base 2 of 100,000, which is about
    # 17 comparisons. Going from the small list to the large list multiplied
    # the list size by 10,000 but only added about 14 comparisons for binary
    # search. That is the practical meaning of O(log n) versus O(n): the
    # linear cost scales with the data while the logarithmic cost barely
    # moves. If the dataset doubled again to 200,000, linear search would
    # need up to 200,000 comparisons and binary search would need 18.

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    print("TODO: Demonstrate and explain edge cases.")

    # EDGE CASE 1: empty list.
    empty = []
    print("\n1. Empty list", empty, "searching for 5")
    print("   linear_search:", linear_search(empty, 5))
    print("   binary_search:", binary_search(empty, 5))
    # Both return -1 without crashing. linear_search never enters its loop
    # because range(0) produces nothing. binary_search sets high to -1, so
    # the condition low <= high is false right away and the loop is skipped.

    # EDGE CASE 2: single-element list where the value matches.
    single = [42]
    print("\n2. Single-element list", single, "searching for 42")
    print("   linear_search:", linear_search(single, 42))
    print("   binary_search:", binary_search(single, 42))
    # Both return index 0. For binary search low and high both equal 0, so
    # mid is 0 and the single element is checked on the first pass.

    # EDGE CASE 3: single-element list where the value does not match.
    print("\n3. Single-element list", single, "searching for 7")
    print("   linear_search:", linear_search(single, 7))
    print("   binary_search:", binary_search(single, 7))
    # Both return -1. Binary search compares 42 to 7, sees 42 is larger,
    # moves high to -1, and the loop ends with an empty search space.

    # EDGE CASE 4: value at the very first position.
    print("\n4. First position of", small_data, "searching for 2")
    print("   linear_search:", linear_search(small_data, 2),
          "in", linear_search_steps(small_data, 2)[1], "comparisons")
    print("   binary_search:", binary_search(small_data, 2),
          "in", binary_search_steps(small_data, 2)[1], "comparisons")
    # This is the best case for linear search and one of the slower cases for
    # binary search, since binary has to work its way down from the middle to
    # the left edge. It is a good reminder that binary search is not faster on
    # every single lookup, only on the average and the worst case.

    # EDGE CASE 5: value at the very last position.
    print("\n5. Last position of", small_data, "searching for 20")
    print("   linear_search:", linear_search(small_data, 20),
          "in", linear_search_steps(small_data, 20)[1], "comparisons")
    print("   binary_search:", binary_search(small_data, 20),
          "in", binary_search_steps(small_data, 20)[1], "comparisons")
    # This flips the previous case. Linear search has to touch all ten
    # elements while binary search still finishes in about four.

    # ===============================
    # ADDED (Student): REAL-WORLD SCENARIO
    # ===============================
    #
    # Requirement 5 in the README asks for a real-world search scenario.
    # This section looks up student ID numbers in a university roster.

    print("\n=== REAL-WORLD SCENARIO: STUDENT ID LOOKUP ===")

    # A registrar system stores student IDs in sorted order. Sorted storage is
    # a one-time cost at insertion, and every lookup afterward gets to use
    # binary search.
    student_ids = [
        100234, 100891, 101445, 102003, 102876,
        103120, 103998, 104562, 105001, 105774
    ]
    names = [
        "Alvarez", "Bhatt", "Chen", "Diallo", "Ellis",
        "Fontaine", "Grewal", "Huang", "Ibrahim", "Jensen"
    ]
    print("Roster size:", len(student_ids), "students")

    # A student swipes in at the library door with ID 103998.
    scanned_id = 103998
    position = binary_search(student_ids, scanned_id)
    if position != -1:
        print("ID", scanned_id, "found at index", position,
              "-> student:", names[position])
    else:
        print("ID", scanned_id, "not found. Access denied.")

    # An ID that is not enrolled.
    scanned_id = 109999
    position = binary_search(student_ids, scanned_id)
    if position != -1:
        print("ID", scanned_id, "found at index", position,
              "-> student:", names[position])
    else:
        print("ID", scanned_id, "not found. Access denied.")

    # WHY BINARY SEARCH FITS THIS SCENARIO:
    # Student IDs are numeric, stable, and easy to keep sorted, and the same
    # roster gets searched thousands of times a day at doors, labs, and
    # checkout desks. Paying once to keep the list sorted buys a fast lookup
    # every time after that.
    #
    # WHEN LINEAR SEARCH WOULD STILL BE THE RIGHT CALL:
    # If the registrar instead searched an unsorted list of same-day drop
    # requests, or searched by something messy like a partial last name,
    # binary search would not work at all. Sorting a list just to run one
    # search costs more than the single linear pass it was meant to replace.

    print("\n=== END OF PROGRAM ===")


if __name__ == "__main__":
    main()
