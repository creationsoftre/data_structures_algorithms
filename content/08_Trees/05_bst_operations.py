# ============================================================
# BST Operations - Search and Insert
# ============================================================
#
# A Binary Search Tree uses this rule:
#
#   smaller values go left
#   larger values go right
#
# Because of this rule, we do not always need to check every node.
#
# ------------------------------------------------------------
# SIMPLE BST EXAMPLE
# ------------------------------------------------------------
#
#              10
#            /    \
#           5      15
#          / \    /  \
#         2   7  12   20
#
# Search for 12:
#
#   Start at 10.
#   12 > 10, so go right.
#
#   Now at 15.
#   12 < 15, so go left.
#
#   Now at 12.
#   Found it.
#
# We skipped:
#
#   5, 2, 7, 20
#
# ------------------------------------------------------------
# BIG O / SPEED
# ------------------------------------------------------------
#
# Search in a balanced BST:
#
#   O(log n)
#
# Speed:
#   Fast.
#
# Why?
#   Each comparison removes about half of the remaining tree.
#
# Insert in a balanced BST:
#
#   O(log n)
#
# Speed:
#   Fast.
#
# Why?
#   Insert follows the same left/right path as search.
#
# ------------------------------------------------------------
# WORST CASE
# ------------------------------------------------------------
#
# Search in an unbalanced BST:
#
#   O(n)
#
# Insert in an unbalanced BST:
#
#   O(n)
#
# Speed:
#   Slow.
#
# Why?
#   The tree can become a chain.
#
# Example:
#
#   1
#    \
#     2
#      \
#       3
#        \
#         4
#
# Searching for 4 checks:
#
#   1 -> 2 -> 3 -> 4
#
# ------------------------------------------------------------
# SPACE COMPLEXITY
# ------------------------------------------------------------
#
# Storing the BST:
#
#   O(n)
#
# Why?
#   We store n nodes.
#
# Iterative search:
#
#   O(1)
#
# Why?
#   We only use a few variables.
#
# Recursive search:
#
#   O(h)
#
# Why?
#   Recursive calls use the call stack.
#
# h = height of the tree
#
# Balanced tree:
#
#   h = log n
#
# Unbalanced tree:
#
#   h = n
#
# ------------------------------------------------------------
# IMPORTANT NOTE
# ------------------------------------------------------------
#
# BST speed depends on tree height.
#
# Short tree:
#   Faster search.
#
# Tall chain-like tree:
#   Slower search.
# ============================================================


class Node:
    def __init__(self, value):
        # Store the value inside the node.
        self.value = value

        # Smaller values go on the left.
        self.left = None

        # Larger values go on the right.
        self.right = None


class BinarySearchTree:
    def __init__(self):
        # The root is the first node in the tree.
        #
        # If root is None, the tree is empty.
        self.root = None

    # --------------------------------------------------------
    # Insert
    # --------------------------------------------------------
    #
    # Insert adds a new value into the BST.
    #
    # Rule:
    #
    #   If new value is smaller, go left.
    #   If new value is larger, go right.
    #
    # Time Complexity:
    #
    #   Balanced tree:   O(log n)
    #   Unbalanced tree: O(n)
    # --------------------------------------------------------

    def insert(self, value):
        new_node = Node(value)

        # If the tree is empty, the new node becomes the root.
        if self.root is None:
            self.root = new_node
            return

        # Start at the root.
        current = self.root

        while True:
            # If the new value is smaller, go left.
            if value < current.value:

                # If there is no left child, insert here.
                if current.left is None:
                    current.left = new_node
                    return

                # Otherwise, keep moving left.
                current = current.left

            # If the new value is larger, go right.
            elif value > current.value:

                # If there is no right child, insert here.
                if current.right is None:
                    current.right = new_node
                    return

                # Otherwise, keep moving right.
                current = current.right

            else:
                # If the value already exists, do nothing.
                #
                # This simple BST does not allow duplicates.
                return

    # --------------------------------------------------------
    # Search
    # --------------------------------------------------------
    #
    # Search checks if a value exists in the BST.
    #
    # Rule:
    #
    #   If target equals current value, found it.
    #   If target is smaller, go left.
    #   If target is larger, go right.
    #
    # Time Complexity:
    #
    #   Balanced tree:   O(log n)
    #   Unbalanced tree: O(n)
    # --------------------------------------------------------

    def search(self, target):
        # Start at the root.
        current = self.root

        # Keep searching until we run out of nodes.
        while current is not None:

            # If the current node is the target, we found it.
            if target == current.value:
                return True

            # If target is smaller, search left.
            elif target < current.value:
                current = current.left

            # If target is larger, search right.
            else:
                current = current.right

        # If we reach None, the target is not in the tree.
        return False

    # --------------------------------------------------------
    # Search with explanation
    # --------------------------------------------------------
    #
    # This version prints the decisions.
    #
    # It helps show why BST search is faster than normal
    # binary tree search.
    # --------------------------------------------------------

    def search_with_steps(self, target):
        print(f"Search for {target}")
        print("-" * 60)

        current = self.root

        while current is not None:
            print(f"Current node: {current.value}")

            if target == current.value:
                print(f"{target} == {current.value}")
                print("Found it.")
                return True

            elif target < current.value:
                print(f"{target} < {current.value}")
                print("Go left.")
                print()
                current = current.left

            else:
                print(f"{target} > {current.value}")
                print("Go right.")
                print()
                current = current.right

        print("Reached None.")
        print(f"{target} is not in the tree.")
        return False

    # --------------------------------------------------------
    # Insert with explanation
    # --------------------------------------------------------
    #
    # This version prints the path used to insert the value.
    # --------------------------------------------------------

    def insert_with_steps(self, value):
        print(f"Insert {value}")
        print("-" * 60)

        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            print("Tree is empty.")
            print(f"{value} becomes the root.")
            return

        current = self.root

        while True:
            print(f"Current node: {current.value}")

            if value < current.value:
                print(f"{value} < {current.value}")
                print("Go left.")

                if current.left is None:
                    current.left = new_node
                    print(f"Left child is empty.")
                    print(f"Insert {value} as left child of {current.value}.")
                    return

                print()
                current = current.left

            elif value > current.value:
                print(f"{value} > {current.value}")
                print("Go right.")

                if current.right is None:
                    current.right = new_node
                    print(f"Right child is empty.")
                    print(f"Insert {value} as right child of {current.value}.")
                    return

                print()
                current = current.right

            else:
                print(f"{value} already exists.")
                print("This BST does not allow duplicates.")
                return


# ------------------------------------------------------------
# Build a BST
# ------------------------------------------------------------
#
# Insert values in this order:
#
#   10, 5, 15, 2, 7, 12, 20
#
# This creates:
#
#              10
#            /    \
#           5      15
#          / \    /  \
#         2   7  12   20
# ------------------------------------------------------------

bst = BinarySearchTree()

print("BST Operations - Search and Insert")
print("=" * 60)
print()

print("Build BST")
print("-" * 60)

# Insert 10.
# Tree is empty, so 10 becomes the root.
bst.insert_with_steps(10)
print()

# Insert 5.
# Start at 10.
# 5 < 10, so go left.
# Left child is empty, so insert 5 there.
bst.insert_with_steps(5)
print()

# Insert 15.
# Start at 10.
# 15 > 10, so go right.
# Right child is empty, so insert 15 there.
bst.insert_with_steps(15)
print()

# Insert 2.
# Start at 10.
# 2 < 10, so go left to 5.
# 2 < 5, so go left.
# Left child is empty, so insert 2 there.
bst.insert_with_steps(2)
print()

# Insert 7.
# Start at 10.
# 7 < 10, so go left to 5.
# 7 > 5, so go right.
# Right child is empty, so insert 7 there.
bst.insert_with_steps(7)
print()

# Insert 12.
# Start at 10.
# 12 > 10, so go right to 15.
# 12 < 15, so go left.
# Left child is empty, so insert 12 there.
bst.insert_with_steps(12)
print()

# Insert 20.
# Start at 10.
# 20 > 10, so go right to 15.
# 20 > 15, so go right.
# Right child is empty, so insert 20 there.
bst.insert_with_steps(20)
print()


# ------------------------------------------------------------
# Search examples
# ------------------------------------------------------------

print()
print("BST Search Examples")
print("=" * 60)
print()

bst.search_with_steps(12)

print()
bst.search_with_steps(7)

print()
bst.search_with_steps(99)


# ------------------------------------------------------------
# Balanced vs unbalanced reminder
# ------------------------------------------------------------

print()
print("Speed Reminder")
print("=" * 60)

print("Balanced BST:")
print("Search and insert are usually O(log n).")
print()

print("Unbalanced BST:")
print("Search and insert can become O(n).")
print()

print("Why?")
print("BST performance depends on height.")
print("A shorter tree is faster.")
print("A tall chain-like tree is slower.")