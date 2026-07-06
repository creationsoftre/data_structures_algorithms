# ============================================================
# Huffman Coding - Frequency Table and Leaf Nodes
# ============================================================
#
# Huffman Coding is a compression algorithm.
#
# The idea:
#
#   Characters that appear more often should get shorter codes.
#   Characters that appear less often can get longer codes.
#
# Before we can build the Huffman Tree, we need two steps:
#
#   1. Build a frequency table.
#   2. Create leaf nodes from that frequency table.
#
# ------------------------------------------------------------
# FREQUENCY TABLE
# ------------------------------------------------------------
#
# A frequency table counts how often each character appears.
#
# Example:
#
#   text = "AAAABBBCCDAA"
#
# Frequency table:
#
#   A -> 6
#   B -> 3
#   C -> 2
#   D -> 1
#
# ------------------------------------------------------------
# HUFFMAN TREE NODE
# ------------------------------------------------------------
#
# A Huffman Tree is made of nodes.
#
# Each character starts as a leaf node.
#
# Leaf node:
#
#   A node that stores a real character.
#   It has no children.
#
# Internal node:
#
#   A node that does not store a real character.
#   It connects other nodes together.
#   Its character is None.
#
# ------------------------------------------------------------
# BIG O / SPEED
# ------------------------------------------------------------
#
# Building the frequency table:
#
#   Time Complexity:
#       O(n)
#
#   Speed:
#       Fast.
#
#   Why?
#       We scan through the text one time.
#
# Creating leaf nodes:
#
#   Time Complexity:
#       O(k)
#
#   Speed:
#       Fast.
#
#   Why?
#       We create one node for each unique character.
#
#   n = total number of characters
#   k = number of unique characters
#
# ------------------------------------------------------------
# SPACE COMPLEXITY
# ------------------------------------------------------------
#
# Frequency table:
#
#   O(k)
#
# Leaf nodes:
#
#   O(k)
#
# Why?
#   We store information for each unique character.
#
# ------------------------------------------------------------
# IMPORTANT NOTE
# ------------------------------------------------------------
#
# This file does not fully compress the text yet.
#
# It prepares the data needed for Huffman Coding.
#
# Next steps:
#
#   1. Build the frequency table.
#   2. Create leaf nodes.
#   3. Repeatedly combine the two lowest-frequency nodes.
#   4. Build Huffman codes from the final tree.
# ============================================================


# ------------------------------------------------------------
# Step 1: Build frequency table
# ------------------------------------------------------------
#
# This function counts how often each character appears.
#
# Example:
#
#   "AAAABBBCCDAA"
#
# becomes:
#
#   {
#       "A": 6,
#       "B": 3,
#       "C": 2,
#       "D": 1
#   }
# ------------------------------------------------------------

def build_frequency_table(text):
    # Create an empty dictionary.
    #
    # Key:
    #   character
    #
    # Value:
    #   how many times that character appears
    frequency_table = {}

    # Go through each character in the text.
    for char in text:

        # If the character already exists in the table,
        # increase its count by 1.
        if char in frequency_table:
            frequency_table[char] += 1

        # If this is the first time seeing the character,
        # add it to the table with a count of 1.
        else:
            frequency_table[char] = 1

    # Return the completed frequency table.
    return frequency_table


# ------------------------------------------------------------
# Step 2: Print frequency table
# ------------------------------------------------------------
#
# This helper prints the frequency table in a clean format.
# ------------------------------------------------------------

def print_frequency_table(frequency_table):
    print("Frequency Table")
    print("-" * 40)
    print(f"{'Character':<15}{'Frequency':<10}")
    print("-" * 40)

    for character, frequency in frequency_table.items():
        print(f"{character:<15}{frequency:<10}")


# ------------------------------------------------------------
# Step 3: HuffmanTreeNode class
# ------------------------------------------------------------
#
# This class represents one node in a Huffman Tree.
#
# In Huffman Coding, each character starts as its own node.
#
# Later, nodes are combined to build the full Huffman Tree.
#
# A node can be one of two types:
#
#   1. Leaf node
#      - Stores an actual character
#      - Has no children
#
#   2. Internal node
#      - Does not store an actual character
#      - Stores the combined frequency of its children
#      - Has left and right children
# ------------------------------------------------------------

class HuffmanTreeNode:
    def __init__(self, character, frequency):
        # Store the character for this node.
        #
        # Leaf nodes store real characters.
        #
        # Example:
        #   "A"
        #   "B"
        #   "C"
        #
        # Internal nodes use None because they only connect
        # other nodes.
        self.character = character

        # Store how often the character appears.
        #
        # Example:
        #   If "A" appears 6 times, frequency = 6.
        #
        # For internal nodes, this will later become the combined
        # frequency of the left and right children.
        self.frequency = frequency

        # Store the left child.
        #
        # Leaf nodes start with no children, so this is None.
        self.left = None

        # Store the right child.
        #
        # Leaf nodes start with no children, so this is None.
        self.right = None

    def __repr__(self):
        # This controls how the node looks when printed.
        #
        # Without this method, Python would print something like:
        #
        #   <__main__.HuffmanTreeNode object at 0x000...>
        #
        # This makes test output easier to read.
        return f"HuffmanTreeNode(character={self.character}, frequency={self.frequency})"


# ------------------------------------------------------------
# Step 4: Create leaf nodes from a frequency table
# ------------------------------------------------------------
#
# A leaf node is a node with no children.
#
# In Huffman Coding, every character starts as its own leaf node.
#
# Example frequency table:
#
#   {
#       "A": 6,
#       "B": 3,
#       "C": 2,
#       "D": 1
#   }
#
# This function turns that table into nodes:
#
#   HuffmanTreeNode("A", 6)
#   HuffmanTreeNode("B", 3)
#   HuffmanTreeNode("C", 2)
#   HuffmanTreeNode("D", 1)
#
# These nodes will later be combined to build the Huffman Tree.
# ------------------------------------------------------------

def create_leaf_nodes(frequency_table):
    # Create an empty list to store the nodes.
    nodes = []

    # Go through each character and frequency in the table.
    #
    # character:
    #   the letter, number, symbol, or space
    #
    # frequency:
    #   how many times it appears in the original text
    for character, frequency in frequency_table.items():

        # Create one node for this character.
        #
        # Since this is the first node for the character,
        # it starts as a leaf node.
        #
        # Its left and right children are None.
        node = HuffmanTreeNode(character, frequency)

        # Add the new node to the list.
        nodes.append(node)

    # Return the list of leaf nodes.
    return nodes


# ------------------------------------------------------------
# Step 5: Print leaf nodes
# ------------------------------------------------------------
#
# This helper prints all created Huffman leaf nodes.
# ------------------------------------------------------------

def print_leaf_nodes(nodes):
    print("Huffman Leaf Nodes")
    print("-" * 40)

    for node in nodes:
        print(node)


# ------------------------------------------------------------
# Step 6: Trace version for building the frequency table
# ------------------------------------------------------------
#
# This version shows how the frequency table is built step by step.
# ------------------------------------------------------------

def build_frequency_table_with_trace(text):
    frequency_table = {}

    print("Frequency Table Trace")
    print("=" * 50)
    print(f"Text: {text}")
    print()
    print("Goal:")
    print("  Count how many times each character appears.")
    print("-" * 50)
    print()

    for index, char in enumerate(text):
        print(f"Index {index}: character '{char}'")

        if char in frequency_table:
            frequency_table[char] += 1
            print(f"  '{char}' already exists.")
            print(f"  Increase count to {frequency_table[char]}.")
        else:
            frequency_table[char] = 1
            print(f"  First time seeing '{char}'.")
            print(f"  Add '{char}' to the table with count 1.")

        print(f"  Table now: {frequency_table}")
        print()

    print("Final Frequency Table")
    print("-" * 50)
    print_frequency_table(frequency_table)

    return frequency_table


# ------------------------------------------------------------
# Step 7: Trace version for creating leaf nodes
# ------------------------------------------------------------
#
# This version shows how each character becomes a Huffman node.
# ------------------------------------------------------------

def create_leaf_nodes_with_trace(frequency_table):
    nodes = []

    print("Create Huffman Leaf Nodes Trace")
    print("=" * 50)
    print("Goal:")
    print("  Turn each character in the frequency table into a leaf node.")
    print("-" * 50)
    print()

    for character, frequency in frequency_table.items():
        print(f"Create node for character '{character}'")
        print(f"Frequency: {frequency}")

        node = HuffmanTreeNode(character, frequency)

        print(f"Created: {node}")
        print("Left child: None")
        print("Right child: None")
        print()

        nodes.append(node)

    print("All leaf nodes created.")
    print("-" * 50)

    for node in nodes:
        print(node)

    return nodes


# ------------------------------------------------------------
# Step 8: Test example
# ------------------------------------------------------------

text = "AAAABBBCCDAA"

print("Huffman Coding Setup Example")
print("=" * 50)
print(f"Original text: {text}")
print()

# Build the frequency table.
frequency_table = build_frequency_table(text)

print("Regular Frequency Table Result")
print("-" * 50)
print_frequency_table(frequency_table)

print()

# Create the leaf nodes.
nodes = create_leaf_nodes(frequency_table)

print("Regular Leaf Node Result")
print("-" * 50)
print_leaf_nodes(nodes)

print()
print("Trace: Build Frequency Table")
print("-" * 50)
trace_frequency_table = build_frequency_table_with_trace(text)

print()
print("Trace: Create Leaf Nodes")
print("-" * 50)
create_leaf_nodes_with_trace(trace_frequency_table)