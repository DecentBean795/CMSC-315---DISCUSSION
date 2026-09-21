"""
===========================================================
UNIT 7 DISCUSSION: SORTING ALGORITHMS (BUBBLE SORT VS MERGE SORT)
===========================================================

STUDENT INSTRUCTIONS:

This project explores two fundamental sorting algorithms:
- Bubble Sort (iterative, comparison-based)
- Merge Sort (recursive, divide-and-conquer)

Your goal is to demonstrate both your coding ability and your
understanding of algorithm efficiency and behavior.
"""


def bubble_sort(lst):
    """
    TODO (Student):
    Implement Bubble Sort.

    Requirements:
    - Create a copy of the original list.
    - Compare adjacent elements.
    - Swap elements when they are out of order.
    - Continue until the list is sorted.
    - Return the sorted list.
    - Add meaningful comments.

    """
    # Work on a copy so the caller's original list is never mutated.
    result = lst.copy()
    n = len(result)

    # Repeat passes over the list, shrinking the unsorted portion each time.
    for i in range(n):
        swapped = False
        # The largest values "bubble" to the end after each pass, so the
        # inner loop can ignore the already-sorted tail (n - i - 1).
        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                # Elements are out of order, so swap them.
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        # If no swaps happened, the list is already sorted -- stop early.
        if not swapped:
            break

    return result


def merge_sort(lst):
    """
    TODO (Student):
    Implement Merge Sort.

    Requirements:
    - Use recursion.
    - Divide the list into smaller halves.
    - Sort each half recursively.
    - Merge the sorted halves together.
    - Return the sorted list.
    - Add meaningful comments.

    """
    # Base case: a list of 0 or 1 elements is already sorted.
    if len(lst) <= 1:
        return lst.copy()

    # Divide the list into two halves.
    mid = len(lst) // 2
    left_half = lst[:mid]
    right_half = lst[mid:]

    # Recursively sort each half.
    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    # Merge the two sorted halves back together.
    return merge(sorted_left, sorted_right)


def merge(left, right):
    """
    TODO (Student):
    Implement the merge step used by Merge Sort.

    Requirements:
    - Compare values from the left and right lists.
    - Build a new sorted result list.
    - Append any remaining values.
    - Return the merged sorted list.
    - Add meaningful comments.
    """
    result = []
    i = j = 0

    # Compare values from the left and right lists, taking the smaller
    # one each time so the result stays in sorted order.
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # One of the two lists may still have leftover values once the other
    # is exhausted -- append whatever remains (already sorted).
    result.extend(left[i:])
    result.extend(right[j:])

    return result


def main():
    print("=== UNIT 7: SORTING ALGORITHMS ===")

    # ===============================
    # TODO (Student): DATASET #1
    # ===============================
    #
    # Requirements:
    # 1. Create an unsorted list containing at least 7 values.
    # 2. Display the original list.
    # 3. Sort the list using Bubble Sort.
    # 4. Sort the same list using Merge Sort.
    # 5. Clearly label and display all results.

    print("\n=== DATASET #1 ===")
    dataset1 = [64, 25, 12, 22, 11, 90, 5]
    print(f"Original list:   {dataset1}")
    print(f"Bubble Sort:     {bubble_sort(dataset1)}")
    print(f"Merge Sort:      {merge_sort(dataset1)}")

    # ===============================
    # TODO (Student): DATASET #2
    # ===============================
    #
    # Requirements:
    # 1. Create a second dataset.
    # 2. Use different values than Dataset #1.
    # 3. Sort using both algorithms.
    # 4. Compare the results.

    print("\n=== DATASET #2 ===")
    dataset2 = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2]
    bubble_result2 = bubble_sort(dataset2)
    merge_result2 = merge_sort(dataset2)
    print(f"Original list:   {dataset2}")
    print(f"Bubble Sort:     {bubble_result2}")
    print(f"Merge Sort:      {merge_result2}")
    # Both algorithms are correctness-equivalent -- they should always
    # produce the same sorted output, even though they get there differently.
    print(f"Results match:   {bubble_result2 == merge_result2}")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Already sorted list
    # - Reverse-sorted list
    # - List with duplicate values
    # - Single-element list
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")

    # Edge case 1: Empty list.
    # Both algorithms should handle this gracefully and simply return an
    # empty list, since there is nothing to compare or swap.
    empty_list = []
    print(f"\nEmpty list:            {empty_list}")
    print(f"  Bubble Sort result:  {bubble_sort(empty_list)}")
    print(f"  Merge Sort result:   {merge_sort(empty_list)}")

    # Edge case 2: Already sorted list.
    # Bubble Sort can finish in a single pass here thanks to the
    # "swapped" early-exit check, making it very fast (best case O(n)).
    # Merge Sort still does the full divide-and-merge process regardless
    # of the input order, so its runtime stays O(n log n).
    already_sorted = [1, 2, 3, 4, 5, 6, 7]
    print(f"\nAlready sorted list:   {already_sorted}")
    print(f"  Bubble Sort result:  {bubble_sort(already_sorted)}")
    print(f"  Merge Sort result:   {merge_sort(already_sorted)}")

    # Edge case 3: Reverse-sorted list.
    # This is the worst case for Bubble Sort -- every adjacent pair is out
    # of order, so it performs the maximum number of swaps (O(n^2)).
    # Merge Sort's performance is unaffected by the input order.
    reverse_sorted = [9, 7, 5, 3, 1]
    print(f"\nReverse-sorted list:   {reverse_sorted}")
    print(f"  Bubble Sort result:  {bubble_sort(reverse_sorted)}")
    print(f"  Merge Sort result:   {merge_sort(reverse_sorted)}")

    # Edge case 4: List with duplicate values.
    # Duplicates should stay in the sorted list (not be removed), and the
    # <= comparison in merge() keeps the sort stable for equal values.
    duplicates = [4, 2, 7, 2, 9, 4, 1, 7]
    print(f"\nList with duplicates:  {duplicates}")
    print(f"  Bubble Sort result:  {bubble_sort(duplicates)}")
    print(f"  Merge Sort result:   {merge_sort(duplicates)}")

    # Edge case 5: Single-element list.
    # There is nothing to compare, so the list is trivially already sorted.
    single_element = [42]
    print(f"\nSingle-element list:   {single_element}")
    print(f"  Bubble Sort result:  {bubble_sort(single_element)}")
    print(f"  Merge Sort result:   {merge_sort(single_element)}")




if __name__ == "__main__":
    main()