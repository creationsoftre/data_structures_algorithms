# ============================================================
# Adjacency List - High-Level Notes
# ============================================================
#
# DESCRIPTION
# ------------------------------------------------------------
#
# An adjacency list stores each vertex with a collection of
# its neighboring vertices.
#
# A neighbor is a vertex connected directly to another vertex.
#
# Example:
#
#   Atlanta -------- Charlotte
#      |
#      |
#   Savannah -------- Charleston
#
# Adjacency list:
#
#   Atlanta:
#       Charlotte, Savannah
#
#   Charlotte:
#       Atlanta
#
#   Savannah:
#       Atlanta, Charleston
#
#   Charleston:
#       Savannah
#
#
# PYTHON REPRESENTATION
# ------------------------------------------------------------
#
# A Python dictionary can be used to create an adjacency list.
#
# Each dictionary key represents a vertex.
#
# Each dictionary value stores that vertex's neighbors.
#
# Example:
#
#   {
#       "Atlanta": {"Charlotte", "Savannah"},
#       "Charlotte": {"Atlanta"},
#       "Savannah": {"Atlanta", "Charleston"},
#       "Charleston": {"Savannah"}
#   }
#
# This implementation uses sets for the neighbor collections.
#
# A set:
#
#   Prevents duplicate neighbors.
#
#   Provides fast membership checks.
#
#
# HOW CONNECTIONS ARE STORED
# ------------------------------------------------------------
#
# Each connection is stored in both vertices' neighbor sets.
#
# Example:
#
#   Atlanta -------- Charlotte
#
# Atlanta stores Charlotte as a neighbor:
#
#   "Atlanta": {"Charlotte"}
#
# Charlotte stores Atlanta as a neighbor:
#
#   "Charlotte": {"Atlanta"}
#
# This allows the connection to work in both directions.
#
#
# WHY USE AN ADJACENCY LIST?
# ------------------------------------------------------------
#
# An adjacency list stores only the connections that actually
# exist.
#
# A vertex with two neighbors only stores those two neighbors.
#
# Example:
#
#   "Supra": {"Skyline", "RX-7"}
#
# This makes it easy to:
#
#   Add vertices
#   Add connections
#   Remove connections
#   Find a vertex's neighbors
#
#
# MAIN ADJACENCY LIST OPERATIONS
# ------------------------------------------------------------
#
# add_vertex(vertex)
#     Adds a vertex with an empty neighbor set.
#
# add_edge(vertex1, vertex2)
#     Adds each vertex to the other's neighbor set.
#
# remove_edge(vertex1, vertex2)
#     Removes each vertex from the other's neighbor set.
#
# remove_vertex(vertex)
#     Removes a vertex and all references to it.
#
# get_neighbors(vertex)
#     Returns the selected vertex's neighbors.
#
# has_vertex(vertex)
#     Checks whether a vertex exists in the dictionary.
#
# has_edge(vertex1, vertex2)
#     Checks whether vertex2 is stored as vertex1's neighbor.
#
# vertex_count()
#     Returns the number of vertices.
#
# edge_count()
#     Returns the number of connections.
#
#
# ============================================================
# TIME COMPLEXITY
# ============================================================
#
# The following times assume neighbor sets are used.
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
# The adjacency list stores:
#
#   One dictionary entry for every vertex.
#
#   A neighbor entry for every connection.
#
# Each connection appears in two neighbor sets.
#
#
# ============================================================
# ADJACENCY LIST IMPLEMENTATION
# ============================================================

class AdjacencyList:
    def __init__(self):
        # Create an empty dictionary for the graph.
        #
        # Each key represents a vertex.
        #
        # Each value is a set containing the vertex's neighbors.
        self.graph = {}

    def add_vertex(self, vertex):
        # Do not add the vertex when it already exists.
        if vertex in self.graph:
            return False

        # Add the vertex with an empty neighbor set.
        self.graph[vertex] = set()

        # Return True to show that the vertex was added.
        return True

    def add_edge(self, vertex1, vertex2):
        # Add vertex1 when it does not already exist.
        if vertex1 not in self.graph:
            self.add_vertex(vertex1)

        # Add vertex2 when it does not already exist.
        if vertex2 not in self.graph:
            self.add_vertex(vertex2)

        # Add vertex2 to vertex1's neighbor set.
        self.graph[vertex1].add(vertex2)

        # Add vertex1 to vertex2's neighbor set.
        #
        # Adding both directions creates an undirected edge.
        self.graph[vertex2].add(vertex1)

    def remove_edge(self, vertex1, vertex2):
        # Return False when either vertex does not exist.
        if vertex1 not in self.graph or vertex2 not in self.graph:
            return False

        # Return False when the edge does not exist.
        if vertex2 not in self.graph[vertex1]:
            return False

        # Remove vertex2 from vertex1's neighbors.
        self.graph[vertex1].remove(vertex2)

        # Remove vertex1 from vertex2's neighbors.
        self.graph[vertex2].remove(vertex1)

        # Return True to show that the edge was removed.
        return True

    def remove_vertex(self, vertex):
        # Return False when the vertex does not exist.
        if vertex not in self.graph:
            return False

        # Visit each neighbor connected to the vertex.
        for neighbor in self.graph[vertex]:
            # Remove the vertex from the neighbor's set.
            self.graph[neighbor].remove(vertex)

        # Remove the vertex from the dictionary.
        del self.graph[vertex]

        # Return True to show that the vertex was removed.
        return True

    def get_neighbors(self, vertex):
        # Return an empty list when the vertex does not exist.
        if vertex not in self.graph:
            return []

        # Return the neighbors in a consistent sorted order.
        return sorted(self.graph[vertex])

    def has_vertex(self, vertex):
        # Return True when the vertex exists.
        return vertex in self.graph

    def has_edge(self, vertex1, vertex2):
        # Return False when vertex1 does not exist.
        if vertex1 not in self.graph:
            return False

        # Check whether vertex2 is one of vertex1's neighbors.
        return vertex2 in self.graph[vertex1]

    def vertex_count(self):
        # Return the number of vertices in the graph.
        return len(self.graph)

    def edge_count(self):
        # Count every neighbor entry.
        total_connections = sum(
            len(neighbors) for neighbors in self.graph.values()
        )

        # Each undirected edge is stored twice.
        #
        # Divide by two to get the actual number of edges.
        return total_connections // 2

    def display(self):
        # Visit each vertex in alphabetical order.
        for vertex in sorted(self.graph):
            # Convert the neighbor set into a sorted list.
            neighbors = sorted(self.graph[vertex])

            # Display the vertex and its neighbors.
            print(f"{vertex}: {neighbors}")

# ============================================================
# CODE EXAMPLE - CAR BRANDS AND VEHICLES
# ============================================================
#
# Create an adjacency list that connects car brands to the
# vehicles they manufacture.
car_catalog = AdjacencyList()
#
# Add Toyota and its vehicles.
car_catalog.add_edge("Toyota", "Supra")
car_catalog.add_edge("Toyota", "Corolla")
#
# Add Nissan and its vehicles.
car_catalog.add_edge("Nissan", "Skyline")
car_catalog.add_edge("Nissan", "Silvia")
#
# Add Mazda and its vehicle.
car_catalog.add_edge("Mazda", "RX-7")
#
# Add Honda and its vehicle.
car_catalog.add_edge("Honda", "NSX")
#
# Display the complete adjacency list.
print("=" * 50)
print("CAR BRANDS AND VEHICLES")
print("=" * 50)
car_catalog.display()
#
# Display vehicles connected to specific brands.
print("\n" + "=" * 50)
print("VEHICLES BY BRAND")
print("=" * 50)
print("Toyota:", car_catalog.get_neighbors("Toyota"))
print("Nissan:", car_catalog.get_neighbors("Nissan"))
print("Mazda:", car_catalog.get_neighbors("Mazda"))
print("Honda:", car_catalog.get_neighbors("Honda"))
#
# Display graph totals.
print("\n" + "=" * 50)
print("CATALOG TOTALS")
print("=" * 50)
print("Total vertices:", car_catalog.vertex_count())
print("Total connections:", car_catalog.edge_count())
#
# Check whether specific brand-to-vehicle connections exist.
print("\n" + "=" * 50)
print("CONNECTION CHECKS")
print("=" * 50)
print(
    "Toyota makes Supra:",
    car_catalog.has_edge("Toyota", "Supra"),
)
print(
    "Toyota makes Skyline:",
    car_catalog.has_edge("Toyota", "Skyline"),
)
#
# Remove the connection between Toyota and Corolla.
car_catalog.remove_edge("Toyota", "Corolla")
#
# Check whether the connection still exists.
print(
    "Toyota makes Corolla after removal:",
    car_catalog.has_edge("Toyota", "Corolla"),
)
#
# Remove Silvia and its connection to Nissan.
car_catalog.remove_vertex("Silvia")
#
# Display the updated adjacency list.
print("\n" + "=" * 50)
print("UPDATED CAR CATALOG")
print("=" * 50)
car_catalog.display()