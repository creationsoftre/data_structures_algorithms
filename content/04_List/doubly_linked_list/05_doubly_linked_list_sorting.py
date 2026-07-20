# ============================================================
# Doubly Linked List Sorting - High-Level Notes
# ============================================================
#
# DESCRIPTION
# ------------------------------------------------------------
#
# This example uses merge sort.
#
# Both next and prev references must remain correct after the
# sorted sections are combined.
#
#
# ============================================================
# TIME COMPLEXITY
# ============================================================
#
# Best, average, and worst case:
#
#   O(n log n)
#
#
# ============================================================
# SPACE COMPLEXITY
# ============================================================
#
# Recursive call stack:
#
#   O(log n)
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
    def sort(self):
        self.head = self._merge_sort(self.head)
#
        self.tail = self.head
#
        if self.tail is not None:
            while self.tail.next is not None:
                self.tail = self.tail.next
#
    def _merge_sort(self, head):
        if head is None or head.next is None:
            return head
#
        second = self._split(head)
        left = self._merge_sort(head)
        right = self._merge_sort(second)
#
        return self._merge(left, right)
#
    def _split(self, head):
        slow = head
        fast = head
#
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
#
        second = slow.next
        slow.next = None
#
        if second is not None:
            second.prev = None
#
        return second
#
    def _merge(self, left, right):
        if left is None:
            return right
#
        if right is None:
            return left
#
        if left.data <= right.data:
            left.next = self._merge(left.next, right)
            left.next.prev = left
            left.prev = None
            return left
#
        right.next = self._merge(left, right.next)
        right.next.prev = right
        right.prev = None
        return right
#
    def display(self):
        values = []
        current = self.head
#
        while current is not None:
            values.append(str(current.data))
            current = current.next
#
        print(" <-> ".join(values))
#
#
# ============================================================
# CODE EXAMPLE
# ============================================================
numbers = DoublyLinkedList()
#
for number in [40, 10, 30, 20, 50]:
    numbers.append(number)
#
print("Before sorting:")
numbers.display()
#
numbers.sort()
#
print("\nAfter merge sort:")
numbers.display()
