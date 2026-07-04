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


# GRAPH VISUAL:
#
# A graph is made of nodes and edges.
#
# Node:
# A thing in the graph.
#
# Edge:
# A connection between two nodes.
#
# In this project:
# Nodes = wheels and cars
# Edges = compatibility connections
#
# Example:
#
#            Toyota Supra
#                |
#                |
# Volk Racing TE37 ----- Nissan 350Z
#                |
#                |
#             Mazda RX-7
#
# Another example with shared connections:
#
# Volk Racing TE37 ----- Toyota Supra ----- BBS LM
#
# This means:
# - TE37 is connected to Toyota Supra.
# - BBS LM is also connected to Toyota Supra.
# - TE37 is indirectly connected to BBS LM through Toyota Supra.
#
# Mental model:
#
# A network of relationships.
#
# Graph = connected things

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


    # =========================================
    # BFS SEARCH
    # =========================================

    # BFS:
    # Breadth-First Search.
    #
    # BFS is used to search through a graph.
    #
    # It starts at one node and explores nearby nodes first.
    #
    # Real-world example:
    # In a map app, BFS-style logic can help find paths between places.
    #
    # In this project:
    # We use BFS to check if one node is connected to another node.

    def bfs_search(self, start_node, target_node):
        # If the start node is not in the graph,
        # there is nowhere to start from.
        if start_node not in self.adjacency_list:
            return False

        # visited keeps track of nodes we already checked.
        #
        # This prevents infinite loops.
        #
        # Example:
        # TE37 connects to Supra.
        # Supra connects back to TE37.
        #
        # Without visited, we could keep bouncing back and forth forever.
        visited = set()

        # A queue stores which nodes we need to check next.
        #
        # BFS uses a queue because it checks nodes in the order they were discovered.
        queue = deque()

        # Start by adding the start node to the queue.
        queue.append(start_node)

        # Keep searching while there are nodes waiting in the queue.
        while queue:
            # Remove the next node from the front of the queue.
            current_node = queue.popleft()

            # If this is the node we are looking for, we found a connection.
            if current_node == target_node:
                return True

            # Only process this node if we have not visited it yet.
            if current_node not in visited:
                visited.add(current_node)

                # Add all unvisited neighbors to the queue.
                for neighbor in self.adjacency_list[current_node]:
                    if neighbor not in visited:
                        queue.append(neighbor)

        # If the queue becomes empty, we searched everything reachable
        # and did not find the target.
        return False


# =========================================
# HELPER FUNCTIONS
# =========================================

# Print the title of the section for visual separation.
def show_section_title(title):
    print("\n" + "=" * len(title))
    print(title)
    print("=" * len(title) + "\n")


# =========================================
# CREATE GRAPH
# =========================================

# CREATE GRAPH:
# This function creates a graph of wheels and compatible cars.
#
# Each add_edge() call creates a connection between a wheel and a car.
#
# Since our graph is undirected:
# - the wheel points to the car
# - the car points back to the wheel

def create_wheel_fitment_graph():
    graph = Graph()

    graph.add_edge("Volk Racing TE37", "Nissan 350Z")
    graph.add_edge("Volk Racing TE37", "Toyota Supra")
    graph.add_edge("Volk Racing TE37", "Mazda RX-7")

    graph.add_edge("Work VSKF", "Lexus IS300")
    graph.add_edge("Work VSKF", "Nissan 240SX")
    graph.add_edge("Work VSKF", "Toyota Chaser")

    graph.add_edge("Work Emitz", "Lexus LS400")
    graph.add_edge("Work Emitz", "Toyota Celsior")

    graph.add_edge("BBS LM", "BMW E46")
    graph.add_edge("BBS LM", "Volkswagen GTI")
    graph.add_edge("BBS LM", "Audi A4")

    # Add a shared car connection to show that graphs can have many connections.
    #
    # This means Toyota Supra is connected to both TE37 and BBS LM.
    graph.add_edge("BBS LM", "Toyota Supra")

    return graph


# =========================================
# MAIN PROGRAM
# =========================================

# Create the starting graph.
fitment_graph = create_wheel_fitment_graph()


# SECTION 1:
# Display the full graph.
show_section_title("1. DISPLAY WHEEL FITMENT GRAPH")
fitment_graph.display()


# SECTION 2:
# Get connections for one wheel.
show_section_title("2. GET CONNECTIONS FOR A WHEEL")

wheel_name = "Volk Racing TE37"
connections = fitment_graph.get_connections(wheel_name)

print(f"{wheel_name} is connected to:")

for connection in connections:
    print(f"- {connection}")


# SECTION 3:
# Add a new connection.
show_section_title("3. ADD NEW GRAPH CONNECTION")

fitment_graph.add_edge("Enkei RPF1", "Honda S2000")
fitment_graph.add_edge("Enkei RPF1", "Mazda Miata")

print("Added new wheel fitment connections:")
print("- Enkei RPF1 <-> Honda S2000")
print("- Enkei RPF1 <-> Mazda Miata")


# SECTION 4:
# Search for a connection using BFS.
show_section_title("4. SEARCH GRAPH WITH BFS")

start_node = "Work VSKF"
target_node = "Toyota Chaser"

is_connected = fitment_graph.bfs_search(start_node, target_node)

if is_connected:
    print(f"Path found: {start_node} is connected to {target_node}")
else:
    print(f"No path found between {start_node} and {target_node}")


# SECTION 5:
# Search for an indirect connection.
#
# Since Toyota Supra connects to both TE37 and BBS LM,
# BFS can find a path from TE37 to BBS LM through Toyota Supra.
show_section_title("5. SEARCH INDIRECT CONNECTION WITH BFS")

start_node = "Volk Racing TE37"
target_node = "BBS LM"

is_connected = fitment_graph.bfs_search(start_node, target_node)

if is_connected:
    print(f"Path found: {start_node} is indirectly connected to {target_node}")
else:
    print(f"No path found between {start_node} and {target_node}")


# SECTION 6:
# Display the final graph.
show_section_title("6. FINAL WHEEL FITMENT GRAPH")
fitment_graph.display()