# ============================================================
# Singly Linked List Sorting - High-Level Notes
# ============================================================
#
# DESCRIPTION
# ------------------------------------------------------------
#
# This example sorts a singly linked list using merge sort.
#
# Merge sort works well with linked lists because nodes can be
# divided and reconnected without shifting array elements.
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
    def sort(self):
        self.head = self._merge_sort(self.head)
#
    def _merge_sort(self, head):
        if head is None or head.next is None:
            return head
#
        middle = self._get_middle(head)
        right_head = middle.next
        middle.next = None
#
        left = self._merge_sort(head)
        right = self._merge_sort(right_head)
#
        return self._merge(left, right)
#
    def _get_middle(self, head):
        slow = head
        fast = head.next
#
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
#
        return slow
#
    def _merge(self, left, right):
        dummy = Node(None)
        current = dummy
#
        while left is not None and right is not None:
            if left.data <= right.data:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next
#
            current = current.next
#
        current.next = left if left is not None else right
        return dummy.next
#
    def display(self):
        values = []
        current = self.head
#
        while current is not None:
            values.append(str(current.data))
            current = current.next
#
        print(" -> ".join(values) + " -> None")
#
#
# ============================================================
# CODE EXAMPLE
# ============================================================
numbers = SinglyLinkedList()
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
