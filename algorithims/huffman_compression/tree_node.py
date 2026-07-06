# ============================================================
# Huffman Tree Node
# ============================================================
#
# Huffman Coding uses a binary tree to create compressed codes.
#
# Each node stores:
#
#   1. A character
#   2. The character's frequency
#   3. A left child
#   4. A right child
#
# Leaf nodes store real characters.
#
# Internal nodes do not store a real character.
# They only store the combined frequency of their children.
#
# ------------------------------------------------------------
# EXAMPLE
# ------------------------------------------------------------
#
# Frequency table:
#
#   A -> 6
#   B -> 3
#   C -> 2
#   D -> 1
#
# A leaf node might look like:
#
#   character = "A"
#   frequency = 6
#
# An internal node might combine C and D:
#
#        None:3
#        /    \
#     D:1      C:2
#
# The internal node has:
#
#   character = None
#   frequency = 3
#
# Why frequency 3?
#
#   D frequency 1 + C frequency 2 = 3
#
# ------------------------------------------------------------
# IMPORTANT NOTE
# ------------------------------------------------------------
#
# Huffman Coding builds the tree by repeatedly combining the two
# lowest-frequency nodes.
#
# This helps give shorter codes to characters that appear more often.
# ============================================================


# ------------------------------------------------------------
# HuffmanTreeNode class
# ------------------------------------------------------------
#
# This class represents one node in the Huffman tree.
#
# character:
#   The character stored in the node.
#   Example: "A", "B", "C"
#
# frequency:
#   How often the character appears.
#
# left:
#   The left child node.
#
# right:
#   The right child node.
#
# For internal nodes:
#
#   character will be None.
#   frequency will be the combined frequency of the children.
# ------------------------------------------------------------
class HuffmanTreeNode:
    def __init__(self, character, frequency):
        self.character = character
        self.frequency = frequency
        self.left = None
        self.right = None