## TIME COMPLEXITY:
# Big O describes how the work grows as the amount of data grows.
#
# From fastest to slower:
# O(1)     -> Constant time
#             The operation takes about the same amount of work no matter how much data exists.
#
# O(log n) -> Logarithmic time
#             The operation gets faster than O(n) because the data is split into smaller parts.
#
# O(n)     -> Linear time
#             The operation gets slower as the amount of data grows because you may need to check each item.
#
# O(V + E) -> Graph traversal time
#             V means vertices/nodes.
#             E means edges/connections.
#             A graph traversal may need to visit every node and every connection.
#
# Simple rule:
# O(1) is usually better/faster than O(log n), and O(log n) is usually better/faster than O(n).
#
# GRAPH TIME COMPLEXITY:
#
# - Add node: O(1)
#   Adding a node to an adjacency list is usually constant time.
#
# - Add edge/connection: O(1)
#   Adding a connection is usually constant time when using sets or lists.
#
# - Check if a node exists: O(1)
#   Dictionary lookup is usually constant time.
#
# - Get neighbors/connections: O(1)
#   You can directly access a node's connection list.
#
# - Search/traverse graph with BFS or DFS: O(V + E)
#   You may need to visit every node and every edge.
#
# - Remove node: O(V + E)
#   You must remove the node and also remove connections pointing to it.
#
# - Remove edge/connection: O(1) average with sets
#   Removing a connection is usually fast if neighbors are stored in a set.


# A graph is a data structure made of nodes and edges.
#
# Node:
# A thing in the graph.
#
# Edge:
# A connection between two nodes.
#
# In this project:
# Nodes are wheels and cars.
# Edges are compatibility connections.
#
# Example:
# "Volk Racing TE37" is connected to "Nissan 350Z"

from collections import deque


# =========================================
# GRAPH
# =========================================

# GRAPH:
# This graph uses an adjacency list.
#
# The adjacency list is a dictionary:
#
# key   = a node
# value = a set of neighboring nodes
#
# Example:
#
# {
#     "Volk Racing TE37": {"Nissan 350Z", "Toyota Supra"},
#     "Nissan 350Z": {"Volk Racing TE37"}
# }
#
# This graph is undirected.
#
# Undirected means the connection goes both ways:
#
# If TE37 connects to Nissan 350Z,
# then Nissan 350Z also connects back to TE37.

class Graph:
    def __init__(self):
        # Start with an empty dictionary.
        # No nodes or edges exist yet.
        self.adjacency_list = {}


# =========================================
# ADD NODE
# =========================================

# ADD NODE:
# Add a new node to the graph.
#
# If the node already exists, we do not overwrite it.
#
# Each node starts with an empty set of connections.

def add_node(self, node):
    if node not in self.adjacency_list:
        self.adjacency_list[node] = set()


# =========================================
# ADD EDGE
# =========================================

# ADD EDGE:
# Add a connection between two nodes.
#
# Since this is an undirected graph,
# we connect both directions.
#
# Example:
# wheel -> car
# car   -> wheel

def add_edge(self, node1, node2):
    # Make sure both nodes exist before connecting them.
    self.add_node(node1)
    self.add_node(node2)

    # Connect node1 to node2.
    self.adjacency_list[node1].add(node2)

    # Connect node2 back to node1.
    self.adjacency_list[node2].add(node1)

# =========================================
# DISPLAY
# =========================================

# DISPLAY:
# Print every node and its connections.
#
# This helps us see the full graph.

def display(self):
    for node, neighbors in self.adjacency_list.items():
        print(f"{node} is connected to:")

        for neighbor in neighbors:
            print(f"  - {neighbor}")

        print()

# =========================================
# GET CONNECTIONS
# =========================================

# GET CONNECTIONS:
# Return all neighbors connected to a node.
#
# This is useful when we want to ask:
# "What cars are compatible with this wheel?"
#
# If the node does not exist, return an empty set.

def get_connections(self, node):
    return self.adjacency_list.get(node, set())
