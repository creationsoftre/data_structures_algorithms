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

# A binary search tree is a data structure where each node can have up to two children
# Values smaller than current node go to the left
# Values larger than the current node go to the right.

from dataclasses import dataclass

# RECORD: 

# A record for one wheel.
@dataclass
class Wheel:
    # Each variable below is a field in the record.
    # A field stores one piece of information about the wheel.

    name: str           # The name of the wheel
    diameter: int       # The diameter of the wheel in inches
    width: float        # The width of the wheel in inches
    bolt_pattern: str   # The bolt pattern of the wheel, e.g., "5x114.3"
    color: str          # The color of the wheel
    price: float        # The price of the wheel in dollars

# NODE:
# A Tree node stores three things: 
# 1 data -> the wheel record
# 2 left -> smaller child node
# 3 right -> larger child node

class TreeNode:
    def __init__(self, wheel: Wheel):
        self.data = wheel # stores the wheel record 
        self.left = None # stores the smaller child node
        self.right = None # stores the larger child node

# BINARY SEARCH TREE:
# The three keeps track of the first node in the tree, called the root node.
class BinarySearchTree:
    def __init__(self):
        self.root = None # The root node of the tree, initially empty
    
    #INSERT:
    # Add a new wheel to the tree
    def insert(self,data):
        new_node = TreeNode(data) # Create a new node with the wheel data

        if self.root is None: # If the tree is empty, set the new node as the root
            self.root = new_node
            return
        
        # Start at the root and look for the correct position to insert the new node
        current_node = self.root

        while True:
            if data.price < current_node.data.price: # If the new wheel's price is less than the current node's price, go left
                if current_node.left is None: # If there is no left child, insert the new node here
                    current_node.left = new_node
                    return
                current_node = current_node.left # Move to the left child and continue searching
            else: # If the new wheel's price is greater than or equal to the current node's price, go right
                if current_node.right is None: # If there is no right child, insert the new node here
                    current_node.right = new_node
                    return
                current_node = current_node.right # Move to the right child and continue searching
        
    # DISPLAY:
    # Print the tree in order (left, root, right) to display the wheels sorted by price
    def display_in_order(self, node):
        self._display_in_order_recursive(node)

    def _display_in_order_recursive(self, node): # Helper function to recursively traverse the tree in order for internal use
        if node is not None:
            return
        
        # Visit the left subtree: Cheaper Wheels
        self._display_in_order_recursive(node.left) # Visit the left subtree

        # Print the current node's data
        print(f"Model: {node.data.name}")
        print(f"Diameter: {node.data.diameter} inches")
        print(f"Width: {node.data.width} inches")
        print(f"Bolt Pattern: {node.data.bolt_pattern}")
        print(f"Color: {node.data.color}")
        print(f"Price: ${node.data.price:.2f}")
        print()

        # Visit the right subtree: More Expensive Wheels
        self._display_in_order_recursive(node.right) # Visit the right subtree

    # SEARCH:
    # Search for wheel using its price
    # A binary tree is only fast when you search using the same field the tree is sorted by.
    # - We sort by price, searching by price is effcient
    def search_by_price(self, search_price):
        current_node = self.root
        
        while current_node is not None:
            wheel = current_node.data

            # Found the maching price.
            if search_price == wheel.price:
                return wheel
            
            # If the search price is smaller, go left.
            elif search_price < wheel.price:
                current_node = current_node.left
            # If the search price is larger, go right.
            else:
                current_node = current_node.right
        return None
    
    # FIND MINIMUM: 
    # The cheapest wheel is the farthest left node.
    def find_cheapest(self):
        if self.root is None:
            return None
        
        current_node = self.root

        while current_node.left is not None:
            current_node = current_node.left
        
        return current_node.data 
    
    # FIND Maximum: 
    # The most expensive wheel is the farthest right node.
    def find_cheapest(self):
        if self.root is None:
            return None
        
        current_node = self.root

        while current_node.right is not None:
            current_node = current_node.right
        
        return current_node.data 
    
    
