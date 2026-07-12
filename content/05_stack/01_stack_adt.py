#============================================================
#Stack ADT - High Level Notes
#============================================================
#
#DESCRIPTION
#
#A stack stores data using:
#
#Last In, First Out
#
#This is called LIFO.
#
#The last item added is the first item removed.
#
#Think of a stack of plates:
#
#Plate C <- top
#Plate B
#Plate A
#
#Plate C was added last, so Plate C is removed first.
#
#Main stack operations:
#
#push(item)
#Adds an item to the top.
#
#pop()
#Removes and returns the top item.
#
#peek()
#Returns the top item without removing it.
#
#is_empty()
#Checks whether the stack is empty.
#
#size()
#Returns the number of items in the stack.
#
#============================================================
#TIME COMPLEXITY
#============================================================
#
#push:     O(1)
#pop:      O(1)
#peek:     O(1)
#is_empty: O(1)
#size:     O(1)
#
#These operations are fast because they work with the top
#of the stack.
#
#Searching through the stack is:
#
#O(n)
#
#============================================================
#SPACE COMPLEXITY
#============================================================
#
#O(n)
#
#The stack needs space for every item it stores.
#
#============================================================
#CODE EXAMPLE - BROWSER HISTORY
#============================================================

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


#Create a stack for browser history.
browser_history = Stack()

#Visit different pages.
browser_history.push("Home Page")
browser_history.push("Car Wheels")
browser_history.push("TE37 Product Page")
browser_history.push("Shopping Cart")

print("Current page:", browser_history.peek())
print("Pages in history:", browser_history.size())

#Press the browser's Back button.
previous_page = browser_history.pop()

print("Leaving:", previous_page)
print("Back to:", browser_history.peek())

#Expected output:
#Current page: Shopping Cart
#Pages in history: 4
#Leaving: Shopping Cart
#Back to: TE37 Product Page
#============================================================