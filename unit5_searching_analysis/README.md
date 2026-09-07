# Unit 5 Discussion: Search Algorithms

## Overview

This assignment compares linear search and binary search.

## Learning Objectives

- Implement linear search
- Implement binary search
- Compare performance
- Analyze algorithm efficiency

## Requirements

1. Test both algorithms on a small dataset.
2. Test both algorithms on a large dataset.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world search scenario.

## Implementation Documentation

The linear_search function was implemented using a single for loop that walks the list from index 0 to the last index. Each pass compares one element to the target, and the function returns that index immediately if the values match. If the loop finishes without a match, the function returns -1 so the caller can tell the difference between a valid index and a failed search. Linear search makes no assumption about the order of the list, which is why it has to be willing to check every element. That is the reason the time complexity is O(n): the best case is one comparison when the target sits at the front, but the worst case is n comparisons when the target is at the back or missing entirely, so doubling the list size doubles the work.

binary_search Function

The binary_search function was implemented with two boundary variables, low and high, that mark the section of the list still worth searching. A while loop runs as long as low is less than or equal to high, meaning at least one element remains. Each pass computes a midpoint using integer division and compares the value at that midpoint to the target. If they match, the index is returned. If the midpoint value is too small, low is moved past the midpoint, which discards the entire lower half in one step because the list is sorted. If the midpoint value is too large, high is moved below the midpoint and the upper half is discarded the same way. When low finally passes high, the search space has shrunk to nothing and the function returns -1.

The halving behavior is what produces O(log n) time complexity. A list of 100 elements narrows to roughly 50, then 25, then 12, then 6, then 3, then 1, so only a handful of comparisons are ever needed. Binary search does require the list to be sorted, which is the tradeoff for that speed.

Added Step-Counting Helpers

Two extra functions, linear_search_steps and binary_search_steps, were added to support the performance analysis. They use the exact same logic as the required functions but also return the number of comparisons made. These exist only so the program can print real measured numbers instead of asserting that one algorithm is faster than the other. The required linear_search and binary_search functions were left with their original signatures so they still return a plain index or -1.

Small Dataset Test

The small dataset test uses a sorted list of ten even numbers from 2 to 20. Both algorithms search for 14, a value that exists at index 6, and both return 6. Linear search needs seven comparisons to reach that index while binary search needs four. Both algorithms then search for 15, an odd number that is not in the list, and both correctly return -1. The missing value is the worst case for linear search because it has to check all ten elements before ruling the list out, while binary search still finishes in four comparisons. On a list this small the difference is not noticeable in practice, which is worth stating honestly.

Large Dataset Test

The large dataset test builds a sorted list of 100,000 even numbers using range, then searches for 199998, which sits at the very last index. Linear search takes 100,000 comparisons to find it and binary search takes 17. Searching for 199999, a value that does not exist, produces the same counts with a return value of -1 for both.

These numbers show the gap clearly. The list grew by a factor of 10,000 compared to the small dataset, and linear search grew right along with it, but binary search only went from four comparisons to 17. That is the practical meaning of O(log n) against O(n). If the dataset doubled again to 200,000 elements, linear search would need up to 200,000 comparisons while binary search would need 18.

Edge Case Testing

Five edge cases were tested. The empty list returns -1 from both functions without raising an error, since linear search never enters its loop and binary search sets high to -1 so its loop condition fails immediately. A single-element list containing 42 returns index 0 from both functions when searching for 42, and returns -1 from both when searching for 7. The first-position case searches for 2 in the small dataset, where linear search wins with a single comparison while binary search needs three because it has to work down from the middle to the left edge. The last-position case searches for 20 and flips that result, with linear search needing all ten comparisons and binary search needing four.

The first-position case is included on purpose. Binary search is not faster on every individual lookup, only on the average and the worst case, and testing only the convenient values would hide that.

Real-World Search Scenario

The real-world scenario models a university registrar looking up student ID numbers. A sorted list of ten student IDs is paired with a matching list of last names, and binary search is used to find the index of a scanned ID so the corresponding name can be displayed. One lookup uses an enrolled ID and succeeds, and a second uses an ID that is not on the roster and correctly reports that access is denied.

Binary search fits this situation because student IDs are numeric and stable, the roster is easy to keep sorted, and the same list gets searched thousands of times a day at doors, labs, and checkout desks. Paying the sorting cost once buys a fast lookup on every search after that. Linear search would still be the better call for something like an unsorted list of same-day drop requests, or a search by partial last name, where the data cannot be kept in sorted order or the ordering does not help. Sorting a list just to run one search costs more than the single linear pass it was supposed to replace.

Main Function

The main function runs all four demonstrations in order and prints formatted headers so the output is readable from top to bottom. It creates the datasets, calls both search functions on each test case, prints the returned index alongside the comparison count from the helper functions, and finishes with the real-world scenario. Explanatory comments sit directly above or below each block so the reasoning behind every result is visible in the source file and not only in the printed output.


## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain when to use linear versus binary search, including tradeoffs in real-world scenarios.
