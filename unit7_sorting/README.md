# Unit 7 Discussion: Sorting Algorithms

## Overview

This assignment compares Bubble Sort and Merge Sort.

## Learning Objectives

- Implement Bubble Sort
- Implement Merge Sort
- Understand divide-and-conquer
- Compare algorithm efficiency

## Requirements

1. Test Bubble Sort and Merge Sort.
2. Use multiple datasets.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world sorting example.

## Implementation Documentation

Bubble Sort begins by copying the input list so the caller's original list is never mutated, then repeatedly passes over the copy comparing each pair of adjacent elements. Whenever a pair is found out of order, the two elements are swapped; after each full pass, the largest remaining unsorted value has "bubbled" to its correct position at the end of the list, so the following pass can safely ignore that already-sorted tail. A `swapped` flag tracks whether any swap occurred during a pass, and if a full pass completes with no swaps the list is already sorted, so the function breaks out early instead of continuing to loop unnecessarily. Once no more swaps are needed, the sorted copy is returned.

Merge Sort Recursive Structure

Merge Sort takes a divide-and-conquer approach instead of the iterative approach used by Bubble Sort. The base case handles any list of length 0 or 1, which is trivially already sorted and returned as-is. For longer lists, the function finds the midpoint and splits the list into a left half and a right half, then calls `merge_sort` on each half recursively. This recursion keeps dividing each half in two until every sublist has shrunk down to the base case, at which point the results are combined back together by calling `merge()` on the two sorted halves.

Merge Step

The `merge()` function is what actually reassembles two sorted lists into one sorted result. It walks both the `left` and `right` lists at the same time with two index pointers, comparing the current elements from each side and appending whichever one is smaller to the `result` list, advancing only the pointer for the list that value came from. Using `<=` rather than `<` in that comparison keeps the sort stable, meaning equal values keep their original relative order. Once one of the two lists runs out of elements, the loop ends, and any values still remaining in the other list are appended in bulk with `extend()`, since they are already sorted and all guaranteed to be larger than everything already placed in `result`.

Main Function

The main function tests both algorithms against two separate unsorted datasets, printing the original list alongside the Bubble Sort and Merge Sort results for each so the outputs can be compared side by side. For Dataset #2, the two results are additionally compared directly with `==` and the boolean match is printed, showing concretely that both algorithms always agree on the correct sorted order even though they arrive at it through very different processes. The edge case section then runs both algorithms against five scenarios: an empty list, an already-sorted list, a reverse-sorted list, a list containing duplicate values, and a single-element list. Comments above each edge case explain not just what the code does but why the case matters algorithmically — for example, an already-sorted list is Bubble Sort's best case (it can exit after a single pass thanks to the `swapped` flag) while a reverse-sorted list is its worst case (every adjacent pair is out of order, forcing the maximum number of swaps), whereas Merge Sort's divide-and-merge process runs the same way regardless of input order, so its performance does not change between these cases.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare and constrast each sorting algorithm based on efficiency differences, tradeoffs made, and when to each.