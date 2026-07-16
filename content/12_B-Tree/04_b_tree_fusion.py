# ============================================================
# B-Tree Fusion - High-Level Notes
# ============================================================
#
# Fusion combines:
#
#   Left child + parent separator + right child
#
# into one larger node.
#
# Fusion is used during removal when neither sibling has an
# extra key available for rotation.
#
# Before:
#
#        [20]
#       /    \
#    [10]    [30]
#
# After:
#
#   [10, 20, 30]
#
# If the root becomes empty, the merged child becomes the new
# root and the tree height decreases.
#
#
# ============================================================
# TIME COMPLEXITY
# ============================================================
#
# Fusion:
#
#   O(1) for a 2-3-4 tree
#
# A 2-3-4 node contains at most three keys, so combining two
# children and one parent key takes constant time.
#
# In a general B-tree with larger nodes, fusion may copy up to
# O(t) keys and child references.
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
# Fusion reuses the existing left child and moves keys and
# references into it. No second tree is created.
#
# ============================================================
# FUSION IMPLEMENTATION
# ============================================================
class BTreeNode:
    def __init__(self, keys=None, leaf=True):
        self.keys = keys or []
        self.children = []
        self.leaf = leaf
#
#
def fuse_children(parent, separator_index):
    left_child = parent.children[separator_index]
    right_child = parent.children[separator_index + 1]
#
    # Move the separator key from the parent into the left child.
    left_child.keys.append(parent.keys.pop(separator_index))
#
    # Move all right-child keys into the left child.
    left_child.keys.extend(right_child.keys)
#
    # Internal nodes must also combine child references.
    if not left_child.leaf:
        left_child.children.extend(right_child.children)
#
    # Remove the old right-child reference.
    parent.children.pop(separator_index + 1)
#
    return left_child
#
#
def display(parent):
    print("Parent:", parent.keys)
    for index, child in enumerate(parent.children):
        print(f"Child {index}:", child.keys)
#
#
# ============================================================
# CODE EXAMPLE
# ============================================================
parent = BTreeNode([20], leaf=False)
parent.children = [
    BTreeNode([10]),
    BTreeNode([30]),
]
#
print("=" * 60)
print("B-TREE FUSION")
print("=" * 60)
print("Before fusion:")
display(parent)
#
merged_child = fuse_children(parent, 0)
#
print("\nAfter fusion:")
display(parent)
print("Merged node:", merged_child.keys)
#
# Replace an empty root with its merged child.
root = merged_child if not parent.keys else parent
print("New root:", root.keys)
