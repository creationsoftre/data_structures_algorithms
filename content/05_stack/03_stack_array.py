# ============================================================
# Stack Using an Array - High-Level Notes
# ============================================================
#
# DESCRIPTION
# ------------------------------------------------------------
#
# A stack can be built using an array.
#
# In Python, a list is commonly used as the array.
#
# The end of the list represents the top of the stack.
#
# Stack rule:
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
#   Array:
#
#   [Home Page, Car Wheels, TE37 Product Page, Shopping Cart]
#                                                       ^
#                                                       |
#                                                      Top
#
# The newest page is stored at the end of the list.
#
# When the user presses the Back button, the item at the end
# of the list is removed first.
#
#
# MAIN STACK OPERATIONS
# ------------------------------------------------------------
#
# push(item)
#     Adds an item to the end of the list.
#
# pop()
#     Removes and returns the item at the end of the list.
#
# peek()
#     Returns the last item without removing it.
#
# is_empty()
#     Checks whether the list contains any items.
#
# size()
#     Returns the number of items currently in the list.
#
#
# ============================================================
# TIME COMPLEXITY
# ============================================================
#
#   Operation       Time Complexity
#   -------------------------------
#   push()             O(1) average
#   pop()              O(1)
#   peek()             O(1)
#   is_empty()         O(1)
#   size()             O(1)
#
# push() is O(1) on average because Python lists sometimes
# need to create a larger internal array when they become full.
#
# Searching through the entire stack requires:
#
#   O(n)
#
#
# ============================================================
# SPACE COMPLEXITY
# ============================================================
#
#   O(n)
#
# The stack needs space for every item stored in the list.
#
#
# ============================================================
# STACK ARRAY IMPLEMENTATION
# ============================================================


class ArrayStack:
    def __init__(self):
        # Create an empty list to store the stack's items.
        self.items = []

    def push(self, item):
        # Add the new item to the end of the list.
        #
        # The end of the list represents the top of the stack.
        self.items.append(item)

    def pop(self):
        # A value cannot be removed from an empty stack.
        if self.is_empty():
            return None

        # Remove and return the item at the top of the stack.
        #
        # list.pop() removes the last item by default.
        return self.items.pop()

    def peek(self):
        # An empty stack does not have a top item.
        if self.is_empty():
            return None

        # Return the last item without removing it.
        #
        # Index -1 refers to the final item in the list.
        return self.items[-1]

    def is_empty(self):
        # The stack is empty when the list contains no items.
        return len(self.items) == 0

    def size(self):
        # Return the number of items currently in the stack.
        return len(self.items)


# ============================================================
# CODE EXAMPLE - BROWSER HISTORY
# ============================================================
#
# Create an array-based stack for browser history.
browser_history = ArrayStack()

# Visit the Home Page.
#
# Array:
#
#   [Home Page]
#         ^
#         |
#        Top
browser_history.push("Home Page")

# Visit the Car Wheels page.
#
# Array:
#
#   [Home Page, Car Wheels]
#                    ^
#                    |
#                   Top
browser_history.push("Car Wheels")

# Visit the TE37 Product Page.
#
# Array:
#
#   [Home Page, Car Wheels, TE37 Product Page]
#                                  ^
#                                  |
#                                 Top
browser_history.push("TE37 Product Page")

# Visit the Shopping Cart.
#
# Array:
#
#   [Home Page, Car Wheels, TE37 Product Page, Shopping Cart]
#                                                    ^
#                                                    |
#                                                   Top
browser_history.push("Shopping Cart")

# peek() returns the current page without removing it.
print("Current page:", browser_history.peek())

# size() returns the number of pages stored in the history.
print("Pages in history:", browser_history.size())

# Press the browser's Back button.
#
# pop() removes the current page from the end of the list.
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