# ============================================================
# Graph - High-Level Notes
# ============================================================
#
# DESCRIPTION
# ------------------------------------------------------------
#
# A graph is a data structure used to represent relationships
# or connections between different objects.
#
# A graph contains:
#
#   Vertices:
#       The objects stored in the graph.
#
#   Edges:
#       The connections between the vertices.
#
# Vertices are also commonly called:
#
#   Nodes
#
# A graph does not have a root node like a tree.
#
# A vertex can connect to:
#
#   One other vertex
#   Multiple vertices
#   No other vertices
#
#
# EXAMPLE - ROAD MAP
# ------------------------------------------------------------
#
# A graph can represent cities connected by roads.
#
#   Atlanta -------- Charlotte
#      |
#      |
#   Savannah -------- Charleston
#
# Vertices:
#
#   Atlanta
#   Charlotte
#   Savannah
#   Charleston
#
# Edges:
#
#   Atlanta - Charlotte
#   Atlanta - Savannah
#   Savannah - Charleston
#
#
# GRAPH TERMINOLOGY
# ------------------------------------------------------------
#
# Vertex:
#     An object or value stored in the graph.
#
# Edge:
#     A connection between two vertices.
#
# Neighbor:
#     A vertex connected directly to another vertex.
#
# Path:
#     A sequence of vertices connected by edges.
#
# Cycle:
#     A path that eventually returns to its starting vertex.
#
# Degree:
#     The number of edges connected to a vertex.
#
#
# THIS GRAPH
# ------------------------------------------------------------
#
# This example uses an undirected graph.
#
# In an undirected graph, an edge works in both directions.
#
# Example:
#
#   Atlanta -------- Charlotte
#
# Atlanta connects to Charlotte.
#
# Charlotte also connects to Atlanta.
#
#
# MAIN GRAPH OPERATIONS
# ------------------------------------------------------------
#
# add_vertex(vertex)
#     Adds a new vertex to the graph.
#
# add_edge(vertex1, vertex2)
#     Connects two vertices.
#
# remove_edge(vertex1, vertex2)
#     Removes the connection between two vertices.
#
# remove_vertex(vertex)
#     Removes a vertex and all edges connected to it.
#
# get_neighbors(vertex)
#     Returns the vertices connected directly to a vertex.
#
# has_vertex(vertex)
#     Checks whether a vertex exists.
#
# has_edge(vertex1, vertex2)
#     Checks whether two vertices are connected.
#
# size()
#     Returns the number of vertices in the graph.
#
#
# ============================================================
# TIME COMPLEXITY
# ============================================================
#
#   Operation                    Time Complexity
#   --------------------------------------------
#   add_vertex()                      O(1)
#   add_edge()                        O(1) average
#   has_vertex()                      O(1) average
#   has_edge()                        O(1) average
#   get_neighbors()                  O(d)
#   remove_edge()                     O(1) average
#   remove_vertex()                   O(V + E)
#
# V represents:
#
#   The number of vertices.
#
# E represents:
#
#   The number of edges.
#
# d represents:
#
#   The number of neighbors connected to a vertex.
#
#
# ============================================================
# SPACE COMPLEXITY
# ============================================================
#
#   O(V + E)
#
# The graph needs space for every vertex and edge it stores.
#
#
# ============================================================
# GRAPH IMPLEMENTATION
# ============================================================
class Graph:
    def __init__(self):
        # Create an empty dictionary for the adjacency list.
        #
        # Each dictionary key will represent a vertex.
        #
        # Each value will be a set of neighboring vertices.
        self.adjacency_list = {}
    def add_vertex(self, vertex):
        # Check whether the vertex is already in the graph.
        if vertex in self.adjacency_list:
            return False
        # Add the vertex with an empty neighbor set.
        self.adjacency_list[vertex] = set()
        # Return True to show that the vertex was added.
        return True
    def add_edge(self, vertex1, vertex2):
        # Add vertex1 if it does not already exist.
        if vertex1 not in self.adjacency_list:
            self.add_vertex(vertex1)
        # Add vertex2 if it does not already exist.
        if vertex2 not in self.adjacency_list:
            self.add_vertex(vertex2)
        # Add vertex2 to vertex1's neighbor set.
        self.adjacency_list[vertex1].add(vertex2)
        # Add vertex1 to vertex2's neighbor set.
        #
        # Adding both directions creates an undirected edge.
        self.adjacency_list[vertex2].add(vertex1)
    def remove_edge(self, vertex1, vertex2):
        # Check whether both vertices exist.
        if (
            vertex1 not in self.adjacency_list
            or vertex2 not in self.adjacency_list
        ):
            return False
        # Check whether the edge exists.
        if vertex2 not in self.adjacency_list[vertex1]:
            return False
        # Remove vertex2 from vertex1's neighbors.
        self.adjacency_list[vertex1].remove(vertex2)
        # Remove vertex1 from vertex2's neighbors.
        self.adjacency_list[vertex2].remove(vertex1)
        # Return True to show that the edge was removed.
        return True
    def remove_vertex(self, vertex):
        # Check whether the vertex exists.
        if vertex not in self.adjacency_list:
            return False
        # Visit every neighbor connected to the vertex.
        for neighbor in self.adjacency_list[vertex]:
            # Remove the vertex from each neighbor's set.
            self.adjacency_list[neighbor].remove(vertex)
        # Remove the vertex from the adjacency list.
        del self.adjacency_list[vertex]
        # Return True to show that the vertex was removed.
        return True
    def get_neighbors(self, vertex):
        # Return an empty list when the vertex does not exist.
        if vertex not in self.adjacency_list:
            return []
        # Return the neighbors as a sorted list.
        #
        # Sorting makes the output easier to read and gives it
        # a consistent order.
        return sorted(self.adjacency_list[vertex])
    def has_vertex(self, vertex):
        # Return True when the vertex exists in the dictionary.
        return vertex in self.adjacency_list
    def has_edge(self, vertex1, vertex2):
        # Return False when vertex1 does not exist.
        if vertex1 not in self.adjacency_list:
            return False
        # Check whether vertex2 is one of vertex1's neighbors.
        return vertex2 in self.adjacency_list[vertex1]
    def size(self):
        # Return the number of vertices in the graph.
        return len(self.adjacency_list)
    def display(self):
        # Visit every vertex in alphabetical order.
        for vertex in sorted(self.adjacency_list):
            # Get the vertex's neighbors in alphabetical order.
            neighbors = sorted(self.adjacency_list[vertex])
            # Display the vertex and its connections.
            print(f"{vertex}: {neighbors}")
# ============================================================
# CODE EXAMPLE - ROAD MAP
# ============================================================
#
# Create an undirected graph for a road map.
road_map = Graph()
#
# Add Atlanta to the graph.
#
# Graph:
#
#   Atlanta
road_map.add_vertex("Atlanta")
#
# Add a road between Atlanta and Charlotte.
#
# Graph:
#
#   Atlanta -------- Charlotte
road_map.add_edge("Atlanta", "Charlotte")
#
# Add a road between Atlanta and Savannah.
#
# Graph:
#
#   Charlotte
#       |
#       |
#   Atlanta -------- Savannah
road_map.add_edge("Atlanta", "Savannah")
#
# Add a road between Savannah and Charleston.
#
# Graph:
#
#   Charlotte
#       |
#       |
#   Atlanta -------- Savannah -------- Charleston
road_map.add_edge("Savannah", "Charleston")
#
# Add a road between Charlotte and Raleigh.
#
# Graph:
#
#   Raleigh -------- Charlotte
#                       |
#                       |
#                   Atlanta -------- Savannah -------- Charleston
road_map.add_edge("Charlotte", "Raleigh")
#
# Display the entire adjacency list.
print("Road map:")
road_map.display()
#
# Display the number of cities in the graph.
print("Number of cities:", road_map.size())
#
# Display every city connected directly to Atlanta.
print("Atlanta neighbors:", road_map.get_neighbors("Atlanta"))
#
# Check whether Atlanta and Charlotte are connected.
print(
    "Atlanta connects to Charlotte:",
    road_map.has_edge("Atlanta", "Charlotte"),
)
#
# Check whether Atlanta and Charleston are directly connected.
print(
    "Atlanta connects to Charleston:",
    road_map.has_edge("Atlanta", "Charleston"),
)
#
# Remove the road between Atlanta and Savannah.
road_map.remove_edge("Atlanta", "Savannah")
#
# Check the connection again after removing the road.
print(
    "Atlanta connects to Savannah:",
    road_map.has_edge("Atlanta", "Savannah"),
)
#
# Remove Raleigh and all roads connected to it.
road_map.remove_vertex("Raleigh")
#
# Display the updated graph.
print("Updated road map:")
road_map.display()
