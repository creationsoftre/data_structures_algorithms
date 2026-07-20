# ============================================================
# Doubly Linked List Recursion - High-Level Notes
# ============================================================
#
# DESCRIPTION
# ------------------------------------------------------------
#
# Recursive traversal can move:
#
#   Forward using next
#
#   Backward using prev
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
# Complete list:
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
        self.prev = None
        self.next = None
#
#
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
#
    def append(self, data):
        new_node = Node(data)
#
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
#
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
#
    def recursive_forward(self):
        self._forward(self.head)
#
    def _forward(self, current):
        if current is None:
            return
#
        print(current.data)
        self._forward(current.next)
#
    def recursive_backward(self):
        self._backward(self.tail)
#
    def _backward(self, current):
        if current is None:
            return
#
        print(current.data)
        self._backward(current.prev)
#
#
# ============================================================
# CODE EXAMPLE
# ============================================================
vehicles = DoublyLinkedList()
#
for vehicle in ["Supra", "Skyline", "RX-7", "NSX"]:
    vehicles.append(vehicle)
#
print("Recursive forward traversal:")
vehicles.recursive_forward()
#
print("\nRecursive backward traversal:")
vehicles.recursive_backward()
