"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.
        pass
        # A node is the basic building block of the tree. It holds one
        # value and two links. Both links start as None because a brand
        # new node is always added as a leaf, meaning it has no children
        # yet. The links get filled in later as more values are inserted.
        self.value = value
        self.left = None   # points to the subtree holding smaller values
        self.right = None  # points to the subtree holding larger values


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.
        pass
        # The tree only needs to remember where it starts. Everything else
        # is reachable by following left and right links from the root.
        # A root of None means the tree is empty.
        self.root = None

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """
        pass
        # Every insertion starts at the root and walks down the tree.
        # At each node we compare the new value to the node's value.
        # Smaller values have to go left and larger values have to go
        # right, because that is the rule that defines a BST. If we ever
        # broke that rule, in-order traversal would stop coming out
        # sorted and search would no longer be able to skip half the tree.
        # The helper returns the (possibly new) subtree root, so we
        # reassign self.root to capture the case where the tree was empty.
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
        pass
        # Base case: an empty spot is exactly where the value belongs,
        # so build the node here and hand it back to the caller.
        if node is None:
            return Node(value)

        # Smaller values belong in the left subtree.
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        # Larger values belong in the right subtree.
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)
        else:
            # Duplicate value. This implementation keeps a single copy of
            # each value, so nothing changes and the existing node is
            # returned unchanged.
            return node

        # Return the current node so the parent's link stays correct.
        return node

    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
        pass
        # A linear search through a list has to check every item one at a
        # time, so it does about n comparisons in the worst case. A BST
        # compares once at each node and then throws away an entire
        # subtree, so a balanced tree cuts the remaining search space
        # roughly in half at every step. That is O(log n) instead of O(n).
        # With 1,000 values that is about 10 comparisons instead of 1,000.
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """
        pass
        # Base case: ran off the bottom of the tree without a match.
        if node is None:
            return False

        # Found it.
        if value == node.value:
            return True

        # Not a match, so only one direction can possibly hold the value.
        # The other half of this subtree is skipped entirely.
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

    def search_path(self, value):
        """
        Extra helper (not required, added to make the search process
        visible in the output).

        Returns the list of node values that were compared while looking
        for the target. The length of this list is how many comparisons
        the search actually needed.
        """
        path = []
        node = self.root
        while node is not None:
            path.append(node.value)
            if value == node.value:
                break
            elif value < node.value:
                node = node.left
            else:
                node = node.right
        return path

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """
        pass
        # The list is built up by the recursive helper and then handed back.
        values = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """
        pass
        # Base case: nothing to visit in an empty subtree.
        if node is None:
            return

        # Left, then current, then right. This produces sorted output
        # because of how the tree was built. Everything in the left
        # subtree is smaller than the current node and everything in the
        # right subtree is larger, so visiting left first guarantees all
        # the smaller values get recorded before the current value, and
        # visiting right last guarantees all the larger values come after.
        # That holds at every single node, so the whole list comes out
        # in ascending order.
        self._inorder_recursive(node.left, values)
        values.append(node.value)
        self._inorder_recursive(node.right, values)


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== TREE CONSTRUCTION ===")
    print("TODO: Create a BST and insert multiple values.")

    # 50 is inserted first, so it becomes the root. Everything smaller
    # than 50 ends up in the left subtree and everything larger ends up
    # in the right subtree. That split is what makes the tree efficient:
    # one comparison at the root already rules out half the values, and
    # the same thing happens again at every level going down. Each step
    # cuts the remaining search space roughly in half instead of checking
    # values one at a time like a list would.
    tree = BST()
    values_to_insert = [50, 30, 70, 20, 40, 60, 80]

    for value in values_to_insert:
        tree.insert(value)

    print("Values inserted in this order:", values_to_insert)
    print("Root of the tree:", tree.root.value)
    print("Left subtree (values smaller than 50):", [v for v in tree.inorder() if v < 50])
    print("Right subtree (values larger than 50):", [v for v in tree.inorder() if v > 50])
    print("\nShape of the tree:")
    print("            50")
    print("          /    \\")
    print("        30      70")
    print("       /  \\    /  \\")
    print("     20    40 60   80")

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")
    print("TODO: Display and explain traversal results.")

    # The values went in as 50, 30, 70, 20, 40, 60, 80 but they come out
    # in ascending order. Nothing sorts them along the way. The order
    # comes from the structure itself, since in-order traversal always
    # visits the entire left subtree (all the smaller values) before the
    # current node, and the entire right subtree (all the larger values)
    # after it.
    traversal = tree.inorder()
    print("Insertion order: ", values_to_insert)
    print("In-order output: ", traversal)
    print("Is the output sorted?", traversal == sorted(traversal))

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate BST searching.")

    # 40 and 80 are both in the tree, so both searches return True.
    # 45 and 100 are not, so both return False. The interesting part is
    # the path. Searching for 100 only touches 50, 70, and 80 before it
    # runs off the bottom of the tree, so it answers the question in 3
    # comparisons instead of scanning all 7 values.
    for target in [40, 80, 45, 100]:
        found = tree.search(target)
        path = tree.search_path(target)
        status = "FOUND" if found else "NOT FOUND"
        print(f"Search for {target:>3}: {found}  ({status}, compared against {path}, "
              f"{len(path)} comparisons out of {len(traversal)} values)")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain an edge case.")

    # Edge case 1: empty tree.
    # The root is None, so the traversal helper hits its base case
    # immediately and returns an empty list. Search does the same thing
    # and returns False. Neither one crashes, which is the point.
    empty_tree = BST()
    print("\nEdge case 1: empty tree")
    print("  Root is:", empty_tree.root)
    print("  In-order traversal:", empty_tree.inorder(), "(empty list, no crash)")
    print("  Search for 10:", empty_tree.search(10), "(nothing to find)")

    # Edge case 2: duplicate values.
    # 30 is already in the tree. The recursion walks down to that node,
    # finds that the value is neither smaller nor larger, and returns the
    # existing node without adding anything. The tree stays the same size.
    print("\nEdge case 2: inserting a duplicate value")
    print("  Before inserting 30 again:", tree.inorder(), f"({len(tree.inorder())} values)")
    tree.insert(30)
    print("  After inserting 30 again: ", tree.inorder(), f"({len(tree.inorder())} values)")
    print("  The duplicate was ignored, so the tree did not grow.")

    # Edge case 3: single node tree.
    # A tree with one value is still a valid BST. The root has no
    # children, so traversal returns a one item list and any search other
    # than the root value fails after exactly one comparison.
    print("\nEdge case 3: tree with only one node")
    single = BST()
    single.insert(42)
    print("  In-order traversal:", single.inorder())
    print("  Search for 42:", single.search(42))
    print("  Search for 41:", single.search(41))
    print("  Left child:", single.root.left, " Right child:", single.root.right)

    # Edge case 4: values inserted in sorted order.
    # This is the worst case for a BST. Every value is larger than the
    # one before it, so every value goes right and the tree turns into a
    # straight line. Search degrades from O(log n) to O(n) because there
    # is no longer a left subtree to skip. This is why balanced trees
    # like AVL and red-black trees exist.
    print("\nEdge case 4: inserting values already in sorted order")
    unbalanced = BST()
    for value in [10, 20, 30, 40, 50]:
        unbalanced.insert(value)
    print("  In-order traversal:", unbalanced.inorder(), "(still correct)")
    print("  Path to find 50:", unbalanced.search_path(50),
          f"({len(unbalanced.search_path(50))} comparisons, the tree is a straight line)")
    print("  Compare that to the balanced tree, where finding 80 took",
          len(tree.search_path(80)), "comparisons.")

    # ===============================
    # REAL-WORLD BST EXAMPLE (Requirement 6)
    # ===============================
    #
    # A BST is not just a numbers exercise. Any data that can be ordered
    # can go in one, including text.
    #
    # Scenario: a small library catalog. Books get added to the catalog in
    # whatever order they show up at the front desk, but the librarian
    # needs two things constantly. First, a fast way to check whether the
    # library owns a title. Second, an alphabetical shelf list for the
    # printed catalog. A BST gives both at once. Insertion keeps the
    # ordering rule automatically, search skips half the catalog at every
    # comparison, and in-order traversal prints the alphabetical list
    # without ever running a sort.

    print("\n=== REAL-WORLD EXAMPLE: LIBRARY CATALOG ===")

    catalog = BST()
    books = [
        "The Hobbit",
        "Dune",
        "Sapiens",
        "Beloved",
        "Educated",
        "Neuromancer",
        "Wuthering Heights",
    ]

    # Titles arrive in the order they were donated, not alphabetically.
    for book in books:
        catalog.insert(book)

    print("Order the books were added to the catalog:")
    for book in books:
        print("  -", book)

    print("\nAlphabetical shelf list (in-order traversal, never sorted):")
    for book in catalog.inorder():
        print("  -", book)

    print("\nChecking the catalog:")
    for title in ["Dune", "Educated", "Moby Dick"]:
        owned = catalog.search(title)
        answer = "in the catalog" if owned else "not in the catalog"
        print(f"  '{title}' is {answer} "
              f"(checked {len(catalog.search_path(title))} of {len(books)} titles)")

    print("\nStrings work the same way numbers do here because Python compares")
    print("them alphabetically, so the same left and right rule still applies.")


if __name__ == "__main__":
    main()
