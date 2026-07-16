# ============================================================
# B-Tree Removal - High-Level Notes
# ============================================================
#
# Removing a key must preserve the B-tree rules:
#
#   Keys remain sorted.
#   Every non-root node keeps at least t - 1 keys.
#   Every leaf remains at the same depth.
#
# This file uses t = 2, so it represents a 2-3-4 tree.
#
# Main removal cases:
#
#   1. Remove directly from a leaf.
#   2. Replace an internal key with a predecessor or successor.
#   3. Rotate from a sibling before descending.
#   4. Fuse children when neither sibling has an extra key.
#
# ============================================================
# TIME COMPLEXITY
# ============================================================
#
# Search for the key:
#
#   O(log n)
#
# Removal:
#
#   O(log n)
#
# Rotation and fusion take constant time in a 2-3-4 tree
# because each node contains at most three keys.
#
# Removal follows one root-to-leaf path while repairing nodes
# as needed.
#
#
# ============================================================
# SPACE COMPLEXITY
# ============================================================
#
# Entire tree:
#
#   O(n)
#
# Recursive removal call stack:
#
#   O(log n)
#
# The tree stores every remaining key, while recursion uses one
# call for each level visited.
#
# ============================================================
# B-TREE REMOVAL IMPLEMENTATION
# ============================================================
class BTreeNode:
    def __init__(self, leaf=False):
        self.keys = []
        self.children = []
        self.leaf = leaf
#
#
class BTree:
    def __init__(self, minimum_degree=2):
        self.t = minimum_degree
        self.root = BTreeNode(leaf=True)
#
    def insert(self, key):
        root = self.root
#
        if len(root.keys) == (2 * self.t) - 1:
            new_root = BTreeNode(leaf=False)
            new_root.children.append(root)
            self._split_child(new_root, 0)
            self.root = new_root
            self._insert_non_full(new_root, key)
        else:
            self._insert_non_full(root, key)
#
    def _insert_non_full(self, node, key):
        index = len(node.keys) - 1
#
        if node.leaf:
            node.keys.append(None)
#
            while index >= 0 and key < node.keys[index]:
                node.keys[index + 1] = node.keys[index]
                index -= 1
#
            node.keys[index + 1] = key
            return
#
        while index >= 0 and key < node.keys[index]:
            index -= 1
#
        child_index = index + 1
#
        if len(node.children[child_index].keys) == (2 * self.t) - 1:
            self._split_child(node, child_index)
#
            if key > node.keys[child_index]:
                child_index += 1
#
        self._insert_non_full(node.children[child_index], key)
#
    def _split_child(self, parent, child_index):
        full_child = parent.children[child_index]
        right_child = BTreeNode(leaf=full_child.leaf)
        middle_key = full_child.keys[self.t - 1]
#
        right_child.keys = full_child.keys[self.t:]
        full_child.keys = full_child.keys[:self.t - 1]
#
        if not full_child.leaf:
            right_child.children = full_child.children[self.t:]
            full_child.children = full_child.children[:self.t]
#
        parent.keys.insert(child_index, middle_key)
        parent.children.insert(child_index + 1, right_child)
#
    def remove(self, key):
        self._remove(self.root, key)
#
        # Replace an empty internal root with its only child.
        if not self.root.keys and not self.root.leaf:
            self.root = self.root.children[0]
#
    def _remove(self, node, key):
        index = 0
#
        while index < len(node.keys) and key > node.keys[index]:
            index += 1
#
        # The key is stored in this node.
        if index < len(node.keys) and node.keys[index] == key:
            if node.leaf:
                node.keys.pop(index)
            else:
                self._remove_internal(node, index)
            return
#
        # The key is not present below a leaf.
        if node.leaf:
            return
#
        child_index = index
#
        # Strengthen a minimum-size child before descending.
        if len(node.children[child_index].keys) < self.t:
            self._fill_child(node, child_index)
#
            if child_index > len(node.keys):
                child_index -= 1
#
        self._remove(node.children[child_index], key)
#
    def _remove_internal(self, node, index):
        key = node.keys[index]
        left_child = node.children[index]
        right_child = node.children[index + 1]
#
        if len(left_child.keys) >= self.t:
            predecessor = self._predecessor(left_child)
            node.keys[index] = predecessor
            self._remove(left_child, predecessor)
        elif len(right_child.keys) >= self.t:
            successor = self._successor(right_child)
            node.keys[index] = successor
            self._remove(right_child, successor)
        else:
            self._merge(node, index)
            self._remove(left_child, key)
#
    def _predecessor(self, node):
        current = node
        while not current.leaf:
            current = current.children[-1]
        return current.keys[-1]
#
    def _successor(self, node):
        current = node
        while not current.leaf:
            current = current.children[0]
        return current.keys[0]
#
    def _fill_child(self, parent, child_index):
        if (
            child_index > 0
            and len(parent.children[child_index - 1].keys) >= self.t
        ):
            self._borrow_left(parent, child_index)
        elif (
            child_index < len(parent.children) - 1
            and len(parent.children[child_index + 1].keys) >= self.t
        ):
            self._borrow_right(parent, child_index)
        elif child_index < len(parent.children) - 1:
            self._merge(parent, child_index)
        else:
            self._merge(parent, child_index - 1)
#
    def _borrow_left(self, parent, child_index):
        child = parent.children[child_index]
        sibling = parent.children[child_index - 1]
#
        child.keys.insert(0, parent.keys[child_index - 1])
        parent.keys[child_index - 1] = sibling.keys.pop()
#
        if not sibling.leaf:
            child.children.insert(0, sibling.children.pop())
#
    def _borrow_right(self, parent, child_index):
        child = parent.children[child_index]
        sibling = parent.children[child_index + 1]
#
        child.keys.append(parent.keys[child_index])
        parent.keys[child_index] = sibling.keys.pop(0)
#
        if not sibling.leaf:
            child.children.append(sibling.children.pop(0))
#
    def _merge(self, parent, index):
        left_child = parent.children[index]
        right_child = parent.children[index + 1]
#
        left_child.keys.append(parent.keys.pop(index))
        left_child.keys.extend(right_child.keys)
#
        if not left_child.leaf:
            left_child.children.extend(right_child.children)
#
        parent.children.pop(index + 1)
#
    def display(self):
        current_level = [self.root]
        level = 0
#
        while current_level:
            next_level = []
            node_text = []
#
            for node in current_level:
                node_text.append(str(node.keys))
                next_level.extend(node.children)
#
            print(f"Level {level}: " + " | ".join(node_text))
            current_level = next_level
            level += 1
#
#
# ============================================================
# CODE EXAMPLE
# ============================================================
tree = BTree(minimum_degree=2)
values = [10, 20, 5, 6, 12, 30, 7, 17]
#
for value in values:
    tree.insert(value)
#
print("=" * 60)
print("STARTING B-TREE")
print("=" * 60)
tree.display()
#
for value in [6, 7, 5, 10]:
    print("\n" + "=" * 60)
    print(f"REMOVE: {value}")
    print("=" * 60)
    tree.remove(value)
    tree.display()

