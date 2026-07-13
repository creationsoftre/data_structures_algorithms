# ============================================================
# Directed Graph - High-Level Notes
# ============================================================
#
# DESCRIPTION
# ------------------------------------------------------------
#
# A directed graph stores connections that move in a specific
# direction.
#
# Each connection is represented using an arrow.
#
# Example:
#
#   Toyota -> Supra
#
# This means:
#
#   Toyota connects to Supra.
#
# It does not automatically mean:
#
#   Supra connects to Toyota.
#
# The direction of each edge matters.
#
#
# DIRECTED EDGES
# ------------------------------------------------------------
#
# An edge in a directed graph has:
#
#   Source:
#       The vertex where the edge begins.
#
#   Destination:
#       The vertex where the edge ends.
#
# Example:
#
#   Nissan -> Skyline
#
# Source:
#
#   Nissan
#
# Destination:
#
#   Skyline
#
#
# EXAMPLE - CAR BRANDS AND VEHICLES
# ------------------------------------------------------------
#
# Car brands can point to the vehicles they manufacture.
#
#   Toyota -----> Supra
#      |
#      +--------> Corolla
#
#   Nissan -----> Skyline
#      |
#      +--------> Silvia
#
# Toyota has outgoing edges to:
#
#   Supra
#   Corolla
#
# The Supra does not automatically have an outgoing edge back
# to Toyota.
#
#
# OUTGOING NEIGHBORS
# ------------------------------------------------------------
#
# A vertex's outgoing neighbors are the vertices it points to.
#
# Example:
#
#   Toyota -> Supra
#   Toyota -> Corolla
#
# Toyota's outgoing neighbors are:
#
#   Supra
#   Corolla
#
#
# IN-DEGREE
# ------------------------------------------------------------
#
# In-degree is the number of edges pointing into a vertex.
#
# Example:
#
#   Toyota -> Supra
#
# The Supra has an in-degree of:
#
#   1
#
#
# OUT-DEGREE
# ------------------------------------------------------------
#
# Out-degree is the number of edges leaving a vertex.
#
# Example:
#
#   Toyota -> Supra
#   Toyota -> Corolla
#
# Toyota has an out-degree of:
#
#   2
#
#
# ADJACENCY LIST
# ------------------------------------------------------------
#
# A directed graph can be stored using an adjacency list.
#
# Each vertex stores only its outgoing neighbors.
#
# Example:
#
#   {
#       "Toyota": {"Supra", "Corolla"},
#       "Supra": set(),
#       "Corolla": set()
#   }
#
# Toyota points to the Supra and Corolla.
#
# The Supra and Corolla do not point back to Toyota.
#
#
# MAIN DIRECTED GRAPH OPERATIONS
# ------------------------------------------------------------
#
# add_vertex(vertex)
#     Adds a new vertex to the graph.
#
# add_edge(source, destination)
#     Adds a directed edge from the source to the destination.
#
# remove_edge(source, destination)
#     Removes a directed edge.
#
# remove_vertex(vertex)
#     Removes a vertex and every edge connected to it.
#
# get_neighbors(vertex)
#     Returns the vertices the selected vertex points to.
#
# has_vertex(vertex)
#     Checks whether a vertex exists.
#
# has_edge(source, destination)
#     Checks whether a directed edge exists.
#
# in_degree(vertex)
#     Returns the number of edges pointing into a vertex.
#
# out_degree(vertex)
#     Returns the number of edges leaving a vertex.
#
# vertex_count()
#     Returns the number of vertices.
#
# edge_count()
#     Returns the number of directed edges.
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
#   out_degree()                     O(1)
#   in_degree()                      O(V)
#   remove_edge()                    O(1) average
#   remove_vertex()                  O(V + E)
#
# V represents:
#
#   The number of vertices.
#
# E represents:
#
#   The number of directed edges.
#
# d represents:
#
#   The number of outgoing neighbors.
#
#
# ============================================================
# SPACE COMPLEXITY
# ============================================================
#
#   O(V + E)
#
# The directed graph stores:
#
#   One dictionary entry for every vertex.
#
#   One neighbor entry for every directed edge.
#
# A directed edge is stored only once.
#
#
# ============================================================
# DIRECTED GRAPH IMPLEMENTATION
# ============================================================
class DirectedGraph:
    def __init__(self):
        # Create an empty adjacency list.
        #
        # Each dictionary key represents a vertex.
        #
        # Each set contains the vertices that the key points to.
        self.graph = {}

    def add_vertex(self, vertex):
        # Do not add the vertex when it already exists.
        if vertex in self.graph:
            return False

        # Add the vertex with no outgoing neighbors.
        self.graph[vertex] = set()

        # Return True to show that the vertex was added.
        return True

    def add_edge(self, source, destination):
        # Add the source vertex when it does not exist.
        if source not in self.graph:
            self.add_vertex(source)

        # Add the destination vertex when it does not exist.
        if destination not in self.graph:
            self.add_vertex(destination)

        # Add the destination to the source's neighbor set.
        #
        # Only one direction is added:
        #
        #   source -> destination
        self.graph[source].add(destination)

    def remove_edge(self, source, destination):
        # Return False when the source does not exist.
        if source not in self.graph:
            return False

        # Return False when the directed edge does not exist.
        if destination not in self.graph[source]:
            return False

        # Remove the destination from the source's neighbors.
        self.graph[source].remove(destination)

        # Return True to show that the edge was removed.
        return True

    def remove_vertex(self, vertex):
        # Return False when the vertex does not exist.
        if vertex not in self.graph:
            return False

        # Remove the vertex and its outgoing edges.
        del self.graph[vertex]

        # Visit every remaining vertex.
        for neighbors in self.graph.values():
            # Remove any edge pointing to the deleted vertex.
            neighbors.discard(vertex)

        # Return True to show that the vertex was removed.
        return True

    def get_neighbors(self, vertex):
        # Return an empty list when the vertex does not exist.
        if vertex not in self.graph:
            return []

        # Return the outgoing neighbors in sorted order.
        return sorted(self.graph[vertex])

    def has_vertex(self, vertex):
        # Return True when the vertex exists.
        return vertex in self.graph

    def has_edge(self, source, destination):
        # Return False when the source does not exist.
        if source not in self.graph:
            return False

        # Check whether the source points to the destination.
        return destination in self.graph[source]

    def out_degree(self, vertex):
        # Return 0 when the vertex does not exist.
        if vertex not in self.graph:
            return 0

        # Count the edges leaving the vertex.
        return len(self.graph[vertex])

    def in_degree(self, vertex):
        # Return 0 when the vertex does not exist.
        if vertex not in self.graph:
            return 0

        # Count how many vertices point to the selected vertex.
        return sum(
            vertex in neighbors
            for neighbors in self.graph.values()
        )

    def vertex_count(self):
        # Return the number of vertices.
        return len(self.graph)

    def edge_count(self):
        # Each directed edge is stored only once.
        return sum(
            len(neighbors)
            for neighbors in self.graph.values()
        )

    def display(self):
        # Visit every vertex in alphabetical order.
        for vertex in sorted(self.graph):
            # Get the vertex's outgoing neighbors.
            neighbors = sorted(self.graph[vertex])

            # Display an empty message when there are no edges.
            if not neighbors:
                print(f"{vertex} -> None")
            else:
                print(f"{vertex} -> {', '.join(neighbors)}")


# ============================================================
# CODE EXAMPLE - AUTOMOTIVE WEBSITE NAVIGATION
# ============================================================
#
# Create a directed graph representing links between pages
# on an automotive parts website.
website = DirectedGraph()
#
# Add links leaving the Home Page.
website.add_edge("Home Page", "Car Parts")
website.add_edge("Home Page", "Wheels")
#
# Add links from the Wheels page.
website.add_edge("Wheels", "TE37 Product Page")
website.add_edge("Wheels", "VSKF Product Page")
#
# Add links from individual product pages.
website.add_edge("TE37 Product Page", "Shopping Cart")
website.add_edge("VSKF Product Page", "Shopping Cart")
#
# Add the final checkout link.
website.add_edge("Shopping Cart", "Checkout")
#
# Display the complete navigation graph.
print("=" * 50)
print("AUTOMOTIVE WEBSITE NAVIGATION")
print("=" * 50)
website.display()
#
# Display the pages linked from the Home Page.
print("\n" + "=" * 50)
print("OUTGOING PAGE LINKS")
print("=" * 50)
print("Home Page:", website.get_neighbors("Home Page"))
print("Wheels:", website.get_neighbors("Wheels"))
print(
    "TE37 Product Page:",
    website.get_neighbors("TE37 Product Page"),
)
#
# Check whether specific navigation paths exist directly.
print("\n" + "=" * 50)
print("DIRECTION CHECKS")
print("=" * 50)
print(
    "Home Page links to Wheels:",
    website.has_edge("Home Page", "Wheels"),
)
print(
    "Wheels links to Home Page:",
    website.has_edge("Wheels", "Home Page"),
)
print(
    "TE37 Product Page links to Shopping Cart:",
    website.has_edge("TE37 Product Page", "Shopping Cart"),
)
print(
    "Shopping Cart links to TE37 Product Page:",
    website.has_edge("Shopping Cart", "TE37 Product Page"),
)
#
# Display incoming and outgoing edge counts.
print("\n" + "=" * 50)
print("PAGE DEGREES")
print("=" * 50)
print(
    "Wheels incoming links:",
    website.in_degree("Wheels"),
)
print(
    "Wheels outgoing links:",
    website.out_degree("Wheels"),
)
print(
    "Shopping Cart incoming links:",
    website.in_degree("Shopping Cart"),
)
print(
    "Shopping Cart outgoing links:",
    website.out_degree("Shopping Cart"),
)
#
# Display graph totals.
print("\n" + "=" * 50)
print("GRAPH TOTALS")
print("=" * 50)
print("Total pages:", website.vertex_count())
print("Total directed links:", website.edge_count())
#
# Remove the VSKF product page and all links connected to it.
website.remove_vertex("VSKF Product Page")
#
# Display the updated website navigation.
print("\n" + "=" * 50)
print("UPDATED WEBSITE NAVIGATION")
print("=" * 50)
website.display()
