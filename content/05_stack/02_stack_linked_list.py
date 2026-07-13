# ============================================================
# Stack Using a Linked List - High-Level Notes
# ============================================================
#
# DESCRIPTION
# ------------------------------------------------------------
#
# A stack can be built using a linked list.
#
# Each item is stored inside a node.
#
# Each node contains:
#
#   Data:
#       The value being stored.
#
#   Next:
#       A reference to the node directly below it.
#
# The head of the linked list is used as the top of the stack.
#
#
# STACK RULE
# ------------------------------------------------------------
#
# A stack follows:
#
#   Last In, First Out
#
# This is commonly called:
#
#   LIFO
#
#
# EXAMPLE - BROWSER HISTORY
# ------------------------------------------------------------
#
#   Top
#    |
#    v
#   Shopping Cart -> TE37 Product Page -> Car Wheels
#                 -> Home Page -> None
#
# The newest page is stored at the top of the stack.
#
# When the user presses the Back button, the newest page is
# removed first.
#
#
# MAIN STACK OPERATIONS
# ------------------------------------------------------------
#
# push(item)
#     Creates a new node and places it at the top of the stack.
#
# pop()
#     Removes and returns the item at the top of the stack.
#
# peek()
#     Returns the top item's data without removing it.
#
# is_empty()
#     Checks whether the top of the stack is None.
#
# size()
#     Returns the number of nodes currently in the stack.
#
#
# ============================================================
# TIME COMPLEXITY
# ============================================================
#
#   Operation       Time Complexity
#   -------------------------------
#   push()                O(1)
#   pop()                 O(1)
#   peek()                O(1)
#   is_empty()            O(1)
#   size()                O(1)
#
# These operations are fast because they only access or modify
# the head node.
#
# Searching through the entire stack requires:
#
#   O(n)
#
# This is because every node may need to be visited.
#
#
# ============================================================
# SPACE COMPLEXITY
# ============================================================
#
#   O(n)
#
# The stack stores one node for every item.
#
# Each node stores:
#
#   - The item's data
#   - A reference to the next node
#
#
# ============================================================
# CODE EXAMPLE - BROWSER HISTORY
# ============================================================

class Node:
    def __init__(self, data):
        # Store the value inside the node.
        self.data = data

        # Point to the node directly below this node.
        # None means there is no next node yet.
        self.next = None


class LinkedListStack:
    def __init__(self):
        # The top variable points to the first node in the stack.
        # None means the stack is currently empty.
        self.top = None

        # Keep track of how many items are in the stack.
        self.count = 0

    def push(self, item):
        # Create a new node containing the item.
        new_node = Node(item)

        # Point the new node to the current top node.
        new_node.next = self.top

        # Make the new node the top of the stack.
        self.top = new_node

        # Increase the stack size.
        self.count += 1

    def pop(self):
        # A value cannot be removed from an empty stack.
        if self.is_empty():
            return None

        # Save the top node's data before removing the node.
        removed_item = self.top.data

        # Move the top reference down to the next node.
        self.top = self.top.next

        # Decrease the stack size.
        self.count -= 1

        # Return the value that was removed.
        return removed_item

    def peek(self):
        # An empty stack does not have a top item.
        if self.is_empty():
            return None

        # Return the top item's data without removing it.
        return self.top.data

    def is_empty(self):
        # The stack is empty when top does not reference a node.
        return self.top is None

    def size(self):
        # Return the number of items currently in the stack.
        return self.count


# ============================================================
# CODE EXAMPLE - BROWSER HISTORY
# ============================================================
#
# Create a linked-list stack for browser history.
browser_history = LinkedListStack()

# Visit the Home Page.
#
# Stack:
#
#   Home Page   <- Top
browser_history.push("Home Page")

# Visit the Car Wheels page.
#
# Stack:
#
#   Car Wheels  <- Top
#   Home Page
browser_history.push("Car Wheels")

# Visit the TE37 Product Page.
#
# Stack:
#
#   TE37 Product Page  <- Top
#   Car Wheels
#   Home Page
browser_history.push("TE37 Product Page")

# Visit the Shopping Cart.
#
# Stack:
#
#   Shopping Cart       <- Top
#   TE37 Product Page
#   Car Wheels
#   Home Page
browser_history.push("Shopping Cart")

# peek() shows the current page without removing it.
print("Current page:", browser_history.peek())

# size() shows how many pages are stored in the history.
print("Pages in history:", browser_history.size())

# Press the browser's Back button.
#
# pop() removes the current page from the top of the stack.
previous_page = browser_history.pop()

# Shopping Cart was removed from the stack.
print("Leaving:", previous_page)

# TE37 Product Page is now at the top of the stack.
print("Back to:", browser_history.peek())

# ============================================================
# EXPECTED OUTPUT
# ============================================================
#
# Current page: Shopping Cart
# Pages in history: 4
# Leaving: Shopping Cart
# Back to: TE37 Product Page
# ============================================================