# ============================================================
# Stack ADT - High-Level Notes
# ============================================================
#
# DESCRIPTION
# ------------------------------------------------------------
#
# A stack stores data using:
#
#   Last In, First Out
#
# This is commonly called:
#
#   LIFO
#
# The last item added is the first item removed.
#
#
# EXAMPLE - STACK OF PLATES
# ------------------------------------------------------------
#
#   Plate C   <- Top
#   Plate B
#   Plate A
#
# Plate C was added last, so Plate C is removed first.
#
#
# MAIN STACK OPERATIONS
# ------------------------------------------------------------
#
# push(item)
#     Adds an item to the top of the stack.
#
# pop()
#     Removes and returns the item at the top of the stack.
#
# peek()
#     Returns the top item without removing it.
#
# is_empty()
#     Checks whether the stack is empty.
#
# size()
#     Returns the number of items currently in the stack.
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
# These operations are fast because they only work with the
# item at the top of the stack.
#
# Searching through the entire stack requires:
#
#   O(n)
#
# This is because each item may need to be checked.
#
#
# ============================================================
# SPACE COMPLEXITY
# ============================================================
#
#   O(n)
#
# The stack needs space for every item it stores.
#
#
# ============================================================
# CODE EXAMPLE - BROWSER HISTORY
# ============================================================
class Stack:
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
        # Index -1 refers to the last item in a list.
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
# Create a stack for browser history.
browser_history = Stack()

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

# peek() returns the current page without removing it.
print("Current page:", browser_history.peek())

# size() returns the number of pages stored in the history.
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