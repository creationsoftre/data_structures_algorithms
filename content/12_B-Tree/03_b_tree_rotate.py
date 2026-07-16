# ============================================================
# B-Tree Rotation - High-Level Notes
# ============================================================
#
# Rotation moves one key from a sibling, through the parent,
# into a child that needs another key.
#
# Rotation is used during removal when a sibling has more than
# the minimum number of keys.
#
# Rotate from left:
#
#        [20]              [10]
#       /    \            /    \
# [5, 10]   [30]   ->   [5]   [20, 30]
#
# Rotate from right:
#
#      [20]                 [30]
#     /    \               /    \
#   [5]  [30, 40]   ->  [5, 20] [40]
#
#
# ============================================================
# TIME COMPLEXITY
# ============================================================
#
# Rotate from left:
#
#   O(1) for a 2-3-4 tree
#
# Rotate from right:
#
#   O(1) for a 2-3-4 tree
#
# Each node contains at most three keys, so moving one key and
# one child reference requires constant time.
#
# In a general B-tree with larger nodes, rotation can require
# shifting keys and may take O(t), where t is the minimum
# degree.
#
#
# ============================================================
# SPACE COMPLEXITY
# ============================================================
#
# Auxiliary space:
#
#   O(1)
#
# Rotation rearranges existing keys and references without
# creating a second tree or using recursion.
#
# ============================================================
# ROTATION IMPLEMENTATION
# ============================================================
class BTreeNode:
    def __init__(self, keys=None, leaf=True):
        self.keys = keys or []
        self.children = []
        self.leaf = leaf
#
#
def rotate_from_left(parent, child_index):
    child = parent.children[child_index]
    left_sibling = parent.children[child_index - 1]
#
    # Move the parent separator into the front of the child.
    child.keys.insert(0, parent.keys[child_index - 1])
#
    # Move the sibling's largest key into the parent.
    parent.keys[child_index - 1] = left_sibling.keys.pop()
#
    if not left_sibling.leaf:
        child.children.insert(0, left_sibling.children.pop())
#
#
def rotate_from_right(parent, child_index):
    child = parent.children[child_index]
    right_sibling = parent.children[child_index + 1]
#
    # Move the parent separator into the end of the child.
    child.keys.append(parent.keys[child_index])
#
    # Move the sibling's smallest key into the parent.
    parent.keys[child_index] = right_sibling.keys.pop(0)
#
    if not right_sibling.leaf:
        child.children.append(right_sibling.children.pop(0))
#
#
def display(parent):
    print("Parent:", parent.keys)
    for index, child in enumerate(parent.children):
        print(f"Child {index}:", child.keys)
#
#
# ============================================================
# EXAMPLE 1 - ROTATE FROM LEFT
# ============================================================
parent = BTreeNode([20], leaf=False)
parent.children = [
    BTreeNode([5, 10]),
    BTreeNode([30]),
]
#
print("=" * 60)
print("ROTATE FROM LEFT")
print("=" * 60)
print("Before:")
display(parent)
#
rotate_from_left(parent, 1)
#
print("\nAfter:")
display(parent)
#
#
# ============================================================
# EXAMPLE 2 - ROTATE FROM RIGHT
# ============================================================
parent = BTreeNode([20], leaf=False)
parent.children = [
    BTreeNode([5]),
    BTreeNode([30, 40]),
]
#
print("\n" + "=" * 60)
print("ROTATE FROM RIGHT")
print("=" * 60)
print("Before:")
display(parent)
#
rotate_from_right(parent, 0)
#
print("\nAfter:")
display(parent)

