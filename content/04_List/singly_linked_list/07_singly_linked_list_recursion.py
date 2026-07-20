# ============================================================
# Singly Linked List Recursion - High-Level Notes
# ============================================================
#
# DESCRIPTION
# ------------------------------------------------------------
#
# A recursive function processes one node and then calls itself
# using the next node.
#
# The base case occurs when the current node is None.
#
#
# ============================================================
# TIME COMPLEXITY
# ============================================================
#
# Recursive traversal:
#
#   O(n)
#
# Recursive search:
#
#   O(n)
#
#
# ============================================================
# SPACE COMPLEXITY
# ============================================================
#
# Recursive call stack:
#
#   O(n)
#
# Complete linked list:
#
#   O(n)
#
#
# ============================================================
# IMPLEMENTATION
# ============================================================
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
#
#
class SinglyLinkedList:
    def __init__(self):
        self.head = None
#
    def append(self, data):
        new_node = Node(data)
#
        if self.head is None:
            self.head = new_node
            return
#
        current = self.head
#
        while current.next is not None:
            current = current.next
#
        current.next = new_node
#
    def recursive_traversal(self):
        self._traverse(self.head)
#
    def _traverse(self, current):
        if current is None:
            return
#
        print(current.data)
        self._traverse(current.next)
#
    def recursive_search(self, target):
        return self._search(self.head, target)
#
    def _search(self, current, target):
        if current is None:
            return False
#
        if current.data == target:
            return True
#
        return self._search(current.next, target)
#
#
# ============================================================
# CODE EXAMPLE
# ============================================================
vehicles = SinglyLinkedList()
#
for vehicle in ["Supra", "Skyline", "RX-7", "NSX"]:
    vehicles.append(vehicle)
#
print("Recursive traversal:")
vehicles.recursive_traversal()
#
print("\nRX-7 found:", vehicles.recursive_search("RX-7"))
print("Miata found:", vehicles.recursive_search("Miata"))
