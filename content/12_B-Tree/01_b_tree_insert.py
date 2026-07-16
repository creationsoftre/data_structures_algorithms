# ============================================================
# B-Tree Insertion - High-Level Notes
# ============================================================
#
# A B-tree is a balanced search tree that stores multiple keys
# in each node.
#
# This file uses minimum degree t = 2, which is a 2-3-4 tree.
#
# A node can contain:
#
#   1 key = 2-node
#   2 keys = 3-node
#   3 keys = 4-node
#
# New keys are inserted into leaf nodes. Before entering a
# full child, the child is split and its middle key is promoted.
#
# ============================================================
# TIME COMPLEXITY
# ============================================================
#
# Search:
#
#   O(log n)
#
# Insertion:
#
#   O(log n)
#
# Splitting one 2-3-4 node takes constant time because the
# node can contain at most three keys.
#
# The tree remains balanced, so insertion follows only one
# root-to-leaf path.
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
# Recursive insertion call stack:
#
#   O(log n)
#
# The tree stores every inserted key, while recursion uses one
# call for each level of the tree.
#
# ============================================================
# B-TREE INSERTION IMPLEMENTATION
# ============================================================
class BTreeNode:
    def __init__(self, leaf=False):
        # Store keys in sorted order.
        self.keys = []
#
        # Store references to child nodes.
        self.children = []
#
        # A leaf node has no children.
        self.leaf = leaf
#
#
class BTree:
    def __init__(self, minimum_degree=2):
        # For a 2-3-4 tree, minimum_degree is 2.
        self.t = minimum_degree
        self.root = BTreeNode(leaf=True)
#
    def insert(self, key):
        root = self.root
#
        # Split a full root before inserting.
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
        # Insert directly into a leaf.
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
        # Find the child that should receive the key.
        while index >= 0 and key < node.keys[index]:
            index -= 1
#
        child_index = index + 1
#
        # Split a full child before descending into it.
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
#
        # Promote the middle key to the parent.
        middle_key = full_child.keys[self.t - 1]
#
        # Divide the remaining keys.
        right_child.keys = full_child.keys[self.t:]
        full_child.keys = full_child.keys[:self.t - 1]
#
        # Internal nodes must also divide child references.
        if not full_child.leaf:
            right_child.children = full_child.children[self.t:]
            full_child.children = full_child.children[:self.t]
#
        parent.keys.insert(child_index, middle_key)
        parent.children.insert(child_index + 1, right_child)
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
print("=" * 60)
print("B-TREE INSERTION")
print("=" * 60)
#
for value in values:
    print(f"\nInsert: {value}")
    tree.insert(value)
    tree.display()

