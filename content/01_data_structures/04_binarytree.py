## TIME COMPLEXITY:
# Big O describes how the work grows as the amount of data grows.
#
# From fastest to slower:
# O(1)     -> Constant time
#             The operation takes about the same amount of work no matter how much data exists.
#
# O(log n) -> Logarithmic time
#             The operation gets faster than O(n) because the data is split into smaller parts.
#
# O(n)     -> Linear time
#             The operation gets slower as the amount of data grows because you may need to check each item.
#
# Simple rule:
# O(1) is usually better/faster than O(log n), and O(log n) is usually better/faster than O(n).
#
# BINARY SEARCH TREE TIME COMPLEXITY:
#
# - Search: O(log n) average, O(n) worst case
#   A balanced tree lets you eliminate about half the remaining nodes each step.
#   A badly unbalanced tree can act like a linked list.
#
# - Insert: O(log n) average, O(n) worst case
#   You move left or right until you find the correct empty spot.
#
# - Delete: O(log n) average, O(n) worst case
#   You must first search for the node, then reconnect the tree.
#
# - Traverse all nodes: O(n)
#   You must visit every node once.
#
# - Find minimum/maximum: O(log n) average, O(n) worst case
#   You keep moving left for minimum or right for maximum.


# BINARY SEARCH TREE VISUAL:
#
# A binary search tree is a tree where each node can have up to two children.
#
# Each node can have:
# - one left child
# - one right child
#
# In this project, we are building a Binary Search Tree using wheel prices.
#
# Rule:
# - Cheaper wheels go to the left.
# - More expensive wheels go to the right.
#
# Example:
#
#               $3500
#              /     \
#          $3000     $4500
#                       \
#                       $5500
#
# Same tree with wheel names:
#
#                 TE37
#                $3500
#               /     \
#         Enkei RPF1   Work VSKF
#            $3000       $4500
#                          \
#                         Work Emitz
#                           $5500
#
# Mental model:
#
# At each node, ask:
# "Is the new value smaller or larger?"
#
# Smaller = go left
# Larger  = go right
#
# Binary Search Tree = sorted decision tree

from dataclasses import dataclass


# =========================================
# RECORD
# =========================================

# RECORD:
# Represents one wheel.
#
# This is the same idea from your record lesson.
# We are using a Wheel record as the data stored inside each tree node.
#
# Important:
# The tree node itself does not care that this is a wheel.
# It just stores "data".
#
# In our case, the data happens to be a Wheel object.

@dataclass
class Wheel:
    name: str           # The name of the wheel
    diameter: int       # The diameter of the wheel in inches
    width: float        # The width of the wheel in inches
    bolt_pattern: str   # The bolt pattern of the wheel, e.g., "5x114.3"
    color: str          # The color of the wheel
    price: float        # The price of the wheel in dollars


# =========================================
# TREE NODE
# =========================================

# NODE:
# A tree node stores three things:
#
# 1. data
#    The actual value we care about.
#    In this project, that is a Wheel record.
#
# 2. left
#    A reference to another TreeNode.
#    This points to a wheel with a smaller price.
#
# 3. right
#    A reference to another TreeNode.
#    This points to a wheel with a larger price.
#
# This is different from a linked list node.
#
# Linked List Node:
#   data -> next
#
# Tree Node:
#        data
#       /    \
#    left    right

class TreeNode:
    def __init__(self, data):
        self.data = data

        # Left starts as None because this node does not have a left child yet.
        self.left = None

        # Right starts as None because this node does not have a right child yet.
        self.right = None


# =========================================
# BINARY SEARCH TREE
# =========================================

# BINARY SEARCH TREE:
# The tree keeps track of the first node.
#
# The first node is called the root.
#
# Similar comparison:
# - Linked list starts at the head.
# - Binary tree starts at the root.
#
# The root is the entry point into the entire tree.

class BinarySearchTree:
    def __init__(self):
        # The tree starts empty.
        # Since there are no nodes yet, the root is None.
        self.root = None


    # =========================================
    # INSERT
    # =========================================

    # INSERT:
    # Add a new wheel into the tree based on price.
    #
    # The price decides where the wheel goes.
    #
    # If the new wheel price is lower than the current node's price:
    #   go left
    #
    # If the new wheel price is higher than or equal to the current node's price:
    #   go right
    #
    # We keep doing this until we find an empty spot.

    def insert(self, data):
        # Wrap the Wheel record inside a TreeNode.
        #
        # The Wheel is the data.
        # The TreeNode gives it left and right pointers.
        new_node = TreeNode(data)

        # Case 1:
        # If the tree is empty, this new node becomes the root.
        #
        # Example:
        # Before:
        #   root = None
        #
        # After:
        #   root = new_node
        #
        # The first wheel inserted becomes the starting point of the tree.
        if self.root is None:
            self.root = new_node
            return

        # Case 2:
        # If the tree is not empty, start comparing from the root.
        current_node = self.root

        # We use while True because we do not know how many steps it will take.
        # The loop will keep running until we insert the node and return.
        while True:

            # If the new wheel is cheaper than the current wheel,
            # it belongs somewhere on the left side.
            if data.price < current_node.data.price:

                # If there is no left child, we found the empty spot.
                # Put the new node here.
                if current_node.left is None:
                    current_node.left = new_node
                    return

                # If a left child already exists, move down to that child
                # and keep searching.
                current_node = current_node.left

            # If the new wheel is more expensive or the same price,
            # it belongs somewhere on the right side.
            else:

                # If there is no right child, we found the empty spot.
                # Put the new node here.
                if current_node.right is None:
                    current_node.right = new_node
                    return

                # If a right child already exists, move down to that child
                # and keep searching.
                current_node = current_node.right


    # =========================================
    # DISPLAY IN ORDER
    # =========================================

    # DISPLAY IN ORDER:
    # This prints the wheels from cheapest to most expensive.
    #
    # Why?
    # Because in a binary search tree:
    # - cheaper values are on the left
    # - larger values are on the right
    #
    # In-order traversal means:
    # 1. Visit the left side
    # 2. Visit the current node
    # 3. Visit the right side
    #
    # In simple terms:
    # left -> current -> right

    def display_in_order(self):
        # Start the recursive display at the root of the tree.
        self._display_in_order_recursive(self.root)


    # The underscore means this is a helper method.
    #
    # It is not meant to be called directly from the main program.
    #
    # The public method is:
    #   display_in_order()
    #
    # The helper method is:
    #   _display_in_order_recursive()
    #
    # Recursion means the function calls itself.
    #
    # A tree is naturally recursive because each child can also have children.

    def _display_in_order_recursive(self, current_node):

        # Base case:
        # If current_node is None, there is nothing to display.
        #
        # This stops the recursion.
        #
        # Without this, the function would keep calling itself forever.
        if current_node is None:
            return

        # Step 1:
        # Visit the left side first.
        #
        # Since cheaper wheels go left, this finds cheaper wheels first.
        self._display_in_order_recursive(current_node.left)

        # Step 2:
        # Print the current node's wheel.
        wheel = current_node.data

        print(f"Model: {wheel.name}")
        print(f"Price: ${wheel.price:.2f}")
        print(f"Diameter: {wheel.diameter} inches")
        print(f"Width: {wheel.width} inches")
        print(f"Bolt Pattern: {wheel.bolt_pattern}")
        print(f"Color: {wheel.color}")
        print()

        # Step 3:
        # Visit the right side last.
        #
        # Since more expensive wheels go right,
        # this prints higher-priced wheels after cheaper ones.
        self._display_in_order_recursive(current_node.right)


    # =========================================
    # SEARCH BY PRICE
    # =========================================

    # SEARCH BY PRICE:
    # Search for a wheel using its price.
    #
    # Important:
    # This tree is organized by price.
    #
    # That means searching by price can be fast.
    #
    # If we searched by name instead, the tree would not help as much,
    # because names are not what we used to organize the tree.
    #
    # Search rule:
    # - If the search price is lower than the current node's price, go left.
    # - If the search price is higher than the current node's price, go right.
    # - If the prices match, return the wheel.

    def search_by_price(self, search_price):
        # Start searching at the root.
        current_node = self.root

        # Keep searching while we still have a node to check.
        while current_node is not None:
            wheel = current_node.data

            # Case 1:
            # The current node is the wheel we are looking for.
            if search_price == wheel.price:
                return wheel

            # Case 2:
            # The search price is smaller, so move left.
            elif search_price < wheel.price:
                current_node = current_node.left

            # Case 3:
            # The search price is larger, so move right.
            else:
                current_node = current_node.right

        # If we reach None, that means we ran out of tree to search.
        # The wheel was not found.
        return None


    # =========================================
    # FIND CHEAPEST
    # =========================================

    # FIND MINIMUM:
    # Since this tree is sorted by price,
    # the cheapest wheel is always the farthest left node.
    #
    # Why?
    # Because every time we go left, we are going to a smaller price.

    def find_cheapest(self):
        # If there is no root, the tree is empty.
        if self.root is None:
            return None

        # Start at the root.
        current_node = self.root

        # Keep moving left until there is no more left child.
        while current_node.left is not None:
            current_node = current_node.left

        # The farthest left node contains the cheapest wheel.
        return current_node.data


    # =========================================
    # FIND MOST EXPENSIVE
    # =========================================

    # FIND MAXIMUM:
    # Since this tree is sorted by price,
    # the most expensive wheel is always the farthest right node.
    #
    # Why?
    # Because every time we go right, we are going to a larger price.

    def find_most_expensive(self):
        # If there is no root, the tree is empty.
        if self.root is None:
            return None

        # Start at the root.
        current_node = self.root

        # Keep moving right until there is no more right child.
        while current_node.right is not None:
            current_node = current_node.right

        # The farthest right node contains the most expensive wheel.
        return current_node.data


# =========================================
# HELPER FUNCTIONS
# =========================================

# This function keeps the output clean.
# Each section gets a title and divider lines.
def show_section_title(title):
    print("\n" + "=" * len(title))
    print(title)
    print("=" * len(title) + "\n")


# This function creates the starting tree.
#
# Notice:
# We do not create a normal array/list here.
#
# Instead, we:
# 1. Create an empty BinarySearchTree
# 2. Insert wheels one by one
# 3. Let the tree decide where each wheel belongs
#
# The insertion order matters because it affects the shape of the tree.
#
# A balanced-looking tree performs better.
# A badly ordered tree can become tall and slow, almost like a linked list.

def create_inventory_tree():
    inventory = BinarySearchTree()

    inventory.insert(Wheel("Volk Racing TE37", 18, 9.5, "5x114.3", "Matte Bronze", 3500.00))
    inventory.insert(Wheel("Work VSKF", 18, 10.0, "5x114.3", "Silver", 4500.00))
    inventory.insert(Wheel("Work Emitz", 18, 11.5, "5x114.3", "Gold", 5500.00))
    inventory.insert(Wheel("BBS LM", 18, 10.5, "5x114.3", "Polished Silver", 7500.00))
    inventory.insert(Wheel("Enkei RPF1", 18, 9.0, "5x114.3", "Hyper Silver", 3000.00))

    return inventory


# =========================================
# MAIN PROGRAM
# =========================================

# Create the starting tree.
inventory = create_inventory_tree()


# SECTION 1:
# Display all wheels.
#
# Because we are using in-order traversal,
# the output should print from cheapest to most expensive.
show_section_title("1. Display Binary Search Tree Inventory")

print("Wheels are displayed from cheapest to most expensive:\n")
inventory.display_in_order()


# SECTION 2:
# Insert a new wheel.
#
# The tree will compare this wheel's price against the root,
# then move left or right until it finds the correct empty spot.
show_section_title("2. Insert Into Binary Search Tree")

new_wheel = Wheel("SSR Professor SP1", 18, 10.5, "5x114.3", "Silver", 6000.00)
inventory.insert(new_wheel)

print(f"Added new wheel to inventory: {new_wheel.name}")
print(f"Price: ${new_wheel.price:.2f}")


# SECTION 3:
# Search by price.
#
# This works efficiently because the tree is organized by price.
show_section_title("3. Search Binary Search Tree By Price")

search_price = 4500.00
result = inventory.search_by_price(search_price)

print(f"Search Result for price ${search_price:.2f}:")

if result:
    print(f"Wheel found: {result.name}")
    print(f"Color: {result.color}")
    print(f"Price: ${result.price:.2f}")
else:
    print("Wheel not found.")


# SECTION 4:
# Find the cheapest wheel.
#
# This works by moving left until we cannot move left anymore.
show_section_title("4. Find Cheapest Wheel")

cheapest_wheel = inventory.find_cheapest()

if cheapest_wheel:
    print(f"Cheapest wheel: {cheapest_wheel.name}")
    print(f"Price: ${cheapest_wheel.price:.2f}")
else:
    print("Inventory is empty.")


# SECTION 5:
# Find the most expensive wheel.
#
# This works by moving right until we cannot move right anymore.
show_section_title("5. Find Most Expensive Wheel")

most_expensive_wheel = inventory.find_most_expensive()

if most_expensive_wheel:
    print(f"Most expensive wheel: {most_expensive_wheel.name}")
    print(f"Price: ${most_expensive_wheel.price:.2f}")
else:
    print("Inventory is empty.")


# SECTION 6:
# Display the final tree after insertion.
#
# The new SSR Professor SP1 wheel should now appear in the correct price order.
show_section_title("6. Final Binary Search Tree Inventory")

print("Final inventory from cheapest to most expensive:\n")
inventory.display_in_order()