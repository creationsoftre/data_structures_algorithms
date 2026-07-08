# ============================================================
# BST Recursion
# ============================================================
#
# Recursion means a function calls itself.
#
# Trees work well with recursion because each part of a tree is
# also a smaller tree.
#
# Example:
#
#              10
#            /    \
#           5      15
#          / \    /  \
#         2   7  12   20
#
# The whole tree starts at 10.
#
# But the left side is also a tree:
#
#           5
#          / \
#         2   7
#
# And the right side is also a tree:
#
#           15
#          /  \
#         12   20
#
# This is why recursion fits trees.
#
# ------------------------------------------------------------
# RECURSION IDEA
# ------------------------------------------------------------
#
# A recursive tree function usually has:
#
#   1. Base case
#   2. Work on current node
#   3. Recursive call on left child
#   4. Recursive call on right child
#
# ------------------------------------------------------------
# BASE CASE
# ------------------------------------------------------------
#
# The base case tells recursion when to stop.
#
# For trees, the base case is usually:
#
#   if node is None:
#       stop
#
# Why?
#   None means we went past a leaf node.
#
# ------------------------------------------------------------
# BIG O / SPEED
# ------------------------------------------------------------
#
# Recursive traversal:
#
#   O(n)
#
# Speed:
#   Linear.
#
# Why?
#   We visit every node one time.
#
# Recursive search in a balanced BST:
#
#   O(log n)
#
# Speed:
#   Fast.
#
# Why?
#   Each step goes left or right, not both.
#
# Recursive search in an unbalanced BST:
#
#   O(n)
#
# Speed:
#   Slow.
#
# Why?
#   The tree can become a chain.
#
# ------------------------------------------------------------
# SPACE COMPLEXITY
# ------------------------------------------------------------
#
# Recursive functions use the call stack.
#
# Space complexity:
#
#   O(h)
#
# h = height of the tree
#
# Balanced tree:
#
#   O(log n)
#
# Unbalanced tree:
#
#   O(n)
#
# ------------------------------------------------------------
# IMPORTANT NOTE
# ------------------------------------------------------------
#
# Recursion does not always mean O(n).
#
# The time depends on how many nodes the function visits.
#
# Traversal visits every node:
#
#   O(n)
#
# BST search follows one path:
#
#   O(log n) average
#   O(n) worst case
# ============================================================
#
# Iterative search and recursive search do the same thing.
#
# Both follow the BST rule:
#
#   smaller -> left
#   larger  -> right
#
# The difference is how they move:
#
#   Iterative search uses a while loop.
#   Recursive search uses function calls.
#
# Iterative search uses O(1) extra space.
# Recursive search uses O(h) extra space because of the call stack.


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # --------------------------------------------------------
    # Insert
    # --------------------------------------------------------
    #
    # We use normal iterative insert to build the tree.
    # --------------------------------------------------------

    def insert(self, value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            return

        current = self.root

        while True:
            if value < current.value:
                if current.left is None:
                    current.left = new_node
                    return

                current = current.left

            elif value > current.value:
                if current.right is None:
                    current.right = new_node
                    return

                current = current.right

            else:
                return

    # --------------------------------------------------------
    # Recursive search
    # --------------------------------------------------------
    #
    # Search rule:
    #
    #   if target == current node, found it
    #   if target < current node, search left
    #   if target > current node, search right
    #
    # Time Complexity:
    #
    #   Balanced tree:   O(log n)
    #   Unbalanced tree: O(n)
    #
    # Space Complexity:
    #
    #   O(h)
    #
    # Why?
    #   Recursion uses the call stack.
    # --------------------------------------------------------

    def search_recursive(self, target):
        return self._search_recursive(self.root, target)

    def _search_recursive(self, node, target):
        # Base case 1:
        # If node is None, we reached an empty spot.
        # The target is not in the tree.
        if node is None:
            return False

        # Base case 2:
        # If the current node is the target, we found it.
        if target == node.value:
            return True

        # Recursive case 1:
        # If target is smaller, search the left subtree.
        if target < node.value:
            return self._search_recursive(node.left, target)

        # Recursive case 2:
        # If target is larger, search the right subtree.
        return self._search_recursive(node.right, target)

    # --------------------------------------------------------
    # Recursive search with explanation
    # --------------------------------------------------------

    def search_recursive_with_steps(self, target):
        print(f"Recursive Search for {target}")
        print("=" * 60)
        return self._search_recursive_with_steps(self.root, target, 0)

    def _search_recursive_with_steps(self, node, target, depth):
        indent = "  " * depth

        # Base case:
        # We reached None, so the target was not found.
        if node is None:
            print(f"{indent}Node is None.")
            print(f"{indent}{target} was not found.")
            return False

        print(f"{indent}Current node: {node.value}")

        if target == node.value:
            print(f"{indent}{target} == {node.value}")
            print(f"{indent}Found it.")
            return True

        if target < node.value:
            print(f"{indent}{target} < {node.value}")
            print(f"{indent}Recursive call on LEFT child.")
            return self._search_recursive_with_steps(node.left, target, depth + 1)

        print(f"{indent}{target} > {node.value}")
        print(f"{indent}Recursive call on RIGHT child.")
        return self._search_recursive_with_steps(node.right, target, depth + 1)

    # --------------------------------------------------------
    # Recursive count nodes
    # --------------------------------------------------------
    #
    # This function counts every node in the tree.
    #
    # Time Complexity:
    #
    #   O(n)
    #
    # Why?
    #   It visits every node.
    # --------------------------------------------------------

    def count_nodes(self):
        return self._count_nodes_recursive(self.root)

    def _count_nodes_recursive(self, node):
        # Base case:
        # Empty subtree has 0 nodes.
        if node is None:
            return 0

        # Count current node.
        current_node = 1

        # Count left subtree.
        left_count = self._count_nodes_recursive(node.left)

        # Count right subtree.
        right_count = self._count_nodes_recursive(node.right)

        # Total nodes = current + left + right.
        return current_node + left_count + right_count

    # --------------------------------------------------------
    # Count nodes with explanation
    # --------------------------------------------------------

    def count_nodes_with_steps(self):
        print("Count Nodes Recursively")
        print("=" * 60)
        total = self._count_nodes_with_steps(self.root, 0)
        print()
        print(f"Total nodes: {total}")
        return total

    def _count_nodes_with_steps(self, node, depth):
        indent = "  " * depth

        if node is None:
            print(f"{indent}None -> count 0")
            return 0

        print(f"{indent}Visit node {node.value}")

        left_count = self._count_nodes_with_steps(node.left, depth + 1)
        right_count = self._count_nodes_with_steps(node.right, depth + 1)

        total = 1 + left_count + right_count

        print(f"{indent}Node {node.value} total:")
        print(f"{indent}1 + left_count({left_count}) + right_count({right_count}) = {total}")

        return total

    # --------------------------------------------------------
    # Recursive height
    # --------------------------------------------------------
    #
    # Height counts edges from the root to the deepest leaf.
    #
    # A single node has height 0.
    #
    # Empty tree returns -1 because:
    #
    #   height of leaf = 1 + max(-1, -1)
    #   height of leaf = 0
    # --------------------------------------------------------

    def height(self):
        return self._height_recursive(self.root)

    def _height_recursive(self, node):
        if node is None:
            return -1

        left_height = self._height_recursive(node.left)
        right_height = self._height_recursive(node.right)

        return 1 + max(left_height, right_height)

    # --------------------------------------------------------
    # Height with explanation
    # --------------------------------------------------------

    def height_with_steps(self):
        print("Find Height Recursively")
        print("=" * 60)
        height = self._height_with_steps(self.root, 0)
        print()
        print("Height counts edges, not levels.")
        print(f"Tree height: {height}")
        return height

    def _height_with_steps(self, node, depth):
        indent = "  " * depth

        if node is None:
            print(f"{indent}None -> height -1")
            return -1

        print(f"{indent}Find height of node {node.value}")

        left_height = self._height_with_steps(node.left, depth + 1)
        right_height = self._height_with_steps(node.right, depth + 1)

        height = 1 + max(left_height, right_height)

        print(f"{indent}Node {node.value} height:")
        print(f"{indent}1 + max({left_height}, {right_height}) = {height}")

        return height

    # --------------------------------------------------------
    # Print tree visually
    # --------------------------------------------------------

    def print_tree_visual(self):
        if self.root is None:
            print("Tree is empty.")
            return

        lines = self._build_tree_lines(self.root)

        for line in lines:
            print(line)

    def _build_tree_lines(self, node):
        if node is None:
            return []

        node_text = str(node.value)

        if node.left is None and node.right is None:
            return [node_text]

        left_lines = self._build_tree_lines(node.left)
        right_lines = self._build_tree_lines(node.right)

        left_width = max(len(line) for line in left_lines) if left_lines else 0
        right_width = max(len(line) for line in right_lines) if right_lines else 0

        left_lines = [line.ljust(left_width) for line in left_lines]
        right_lines = [line.ljust(right_width) for line in right_lines]

        root_line = " " * left_width + node_text + " " * right_width

        branch_line = ""

        if node.left is not None:
            branch_line += " " * (left_width - 1) + "/"
        else:
            branch_line += " " * left_width

        branch_line += " " * len(node_text)

        if node.right is not None:
            branch_line += "\\"
        else:
            branch_line += " "

        branch_line += " " * (right_width - 1)

        child_lines = []
        max_child_lines = max(len(left_lines), len(right_lines))

        for i in range(max_child_lines):
            if i < len(left_lines):
                left_part = left_lines[i]
            else:
                left_part = " " * left_width

            if i < len(right_lines):
                right_part = right_lines[i]
            else:
                right_part = " " * right_width

            child_lines.append(left_part + " " * len(node_text) + right_part)

        return [root_line, branch_line] + child_lines


# ------------------------------------------------------------
# Build the BST
# ------------------------------------------------------------

# ------------------------------------------------------------
# Build the BST
# ------------------------------------------------------------

bst = BinarySearchTree()

values = [10, 5, 15, 2, 7, 12, 20]

for value in values:
    bst.insert(value)


print("BST Recursion")
print("=" * 60)
print()

print("Starting Tree")
print("-" * 60)
bst.print_tree_visual()
print()


# ------------------------------------------------------------
# Why recursion matters
# ------------------------------------------------------------

print("Why Recursion Works With Trees")
print("=" * 60)
print("A tree is made of smaller trees.")
print()
print("The full tree starts at 10:")
print()
bst.print_tree_visual()
print()

print("The left side is also a smaller tree:")
print()
print("   5")
print("  / \\")
print(" 2   7")
print()

print("The right side is also a smaller tree:")
print()
print("   15")
print("  /  \\")
print(" 12   20")
print()

print("That is why recursion fits trees well.")
print("A recursive function can solve the current node,")
print("then call itself on the left or right child.")
print()


# ------------------------------------------------------------
# Iterative vs recursive search
# ------------------------------------------------------------

print("Iterative Search vs Recursive Search")
print("=" * 60)
print("Both searches do the same job.")
print("Both follow the same BST rule:")
print()
print("  smaller -> left")
print("  larger  -> right")
print()

print("Difference:")
print("  Iterative search uses a while loop.")
print("  Recursive search uses function calls.")
print()


# ------------------------------------------------------------
# Recursive search example
# ------------------------------------------------------------

print("Recursive Search Example")
print("=" * 60)
print("Search for 12")
print()

print("Path:")
print("10 -> 15 -> 12")
print()

print("Step 1:")
print("Current node: 10")
print("12 > 10")
print("Recursive call on RIGHT child.")
print()

print("Step 2:")
print("Current node: 15")
print("12 < 15")
print("Recursive call on LEFT child.")
print()

print("Step 3:")
print("Current node: 12")
print("12 == 12")
print("Found it.")
print()

found = bst.search_recursive(12)
print(f"Search result: {found}")
print()


# ------------------------------------------------------------
# Recursive search missing value example
# ------------------------------------------------------------

print("Recursive Search Missing Value")
print("=" * 60)
print("Search for 99")
print()

print("Path:")
print("10 -> 15 -> 20 -> None")
print()

print("Step 1:")
print("Current node: 10")
print("99 > 10")
print("Recursive call on RIGHT child.")
print()

print("Step 2:")
print("Current node: 15")
print("99 > 15")
print("Recursive call on RIGHT child.")
print()

print("Step 3:")
print("Current node: 20")
print("99 > 20")
print("Recursive call on RIGHT child.")
print()

print("Step 4:")
print("Current node: None")
print("Reached an empty spot.")
print("99 is not in the tree.")
print()

found = bst.search_recursive(99)
print(f"Search result: {found}")
print()


# ------------------------------------------------------------
# Count nodes example
# ------------------------------------------------------------

print("Count Nodes Recursively")
print("=" * 60)
print("Counting nodes visits every node one time.")
print()

print("Tree values:")
print("10, 5, 15, 2, 7, 12, 20")
print()

print("There are 7 total nodes.")
print()

total_nodes = bst.count_nodes()
print(f"Count result: {total_nodes}")
print()

print("Time Complexity:")
print("O(n)")
print()
print("Why?")
print("Counting nodes must visit every node.")
print()


# ------------------------------------------------------------
# Height example
# ------------------------------------------------------------

print("Find Height Recursively")
print("=" * 60)
print("Height counts edges, not levels.")
print()

print("Tree:")
bst.print_tree_visual()
print()

print("Levels:")
print("Level 1: 10")
print("Level 2: 5, 15")
print("Level 3: 2, 7, 12, 20")
print()

print("There are 3 levels.")
print("But height starts at 0 and counts edges.")
print()

print("Longest path example:")
print("10 -> 15 -> 20")
print()

print("Edge count:")
print("10 to 15 = 1 edge")
print("15 to 20 = 1 edge")
print("Total edges = 2")
print()

tree_height = bst.height()
print(f"Height result: {tree_height}")
print()


# ------------------------------------------------------------
# Complexity summary
# ------------------------------------------------------------

print("Complexity Summary")
print("=" * 60)

print("Recursive BST Search:")
print("Balanced tree:   O(log n)")
print("Unbalanced tree: O(n)")
print("Extra space:     O(h)")
print()

print("Recursive Count Nodes:")
print("Time:        O(n)")
print("Extra space: O(h)")
print()

print("Recursive Height:")
print("Time:        O(n)")
print("Extra space: O(h)")
print()

print("h = height of the tree")
print()


# ------------------------------------------------------------
# Main takeaway
# ------------------------------------------------------------

print("Main Takeaway")
print("=" * 60)

print("Iterative and recursive search use the same BST logic.")
print()
print("Iterative search:")
print("  Uses a while loop.")
print("  Extra space is O(1).")
print()

print("Recursive search:")
print("  Uses function calls.")
print("  Extra space is O(h) because of the call stack.")
print()

print("The search path is the same.")
print("Only the method of moving through the tree is different.")