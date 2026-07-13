# ============================================================
# Minimum Spanning Tree - High-Level Notes
# ============================================================
#
# DESCRIPTION
# ------------------------------------------------------------
#
# A minimum spanning tree connects every vertex in a weighted,
# undirected graph using the smallest possible total weight.
#
# Minimum spanning tree is commonly shortened to:
#
#   MST
#
# A minimum spanning tree must:
#
#   Connect every vertex
#
#   Contain no cycles
#
#   Use the smallest possible total edge weight
#
#
# SPANNING TREE
# ------------------------------------------------------------
#
# A spanning tree connects every vertex in the graph.
#
# It does not contain any cycles.
#
# If a graph contains V vertices, a spanning tree contains:
#
#   V - 1 edges
#
# Example:
#
# A graph with five buildings needs exactly:
#
#   5 - 1 = 4 edges
#
# to create a spanning tree.
#
#
# MINIMUM SPANNING TREE
# ------------------------------------------------------------
#
# A graph may have multiple possible spanning trees.
#
# The minimum spanning tree is the spanning tree with the
# smallest total edge weight.
#
# The edge weights could represent:
#
#   Cable length
#
#   Construction cost
#
#   Road distance
#
#   Installation time
#
#   Network cost
#
#
# EXAMPLE - NETWORK CABLE INSTALLATION
# ------------------------------------------------------------
#
# A company needs to connect five buildings with network
# cables.
#
# Each edge weight represents the cable length in meters.
#
#   Office -------- 4 -------- Server Room
#      |                           |
#      7                           3
#      |                           |
#   Warehouse ----- 2 -------- Workshop
#      |
#      6
#      |
#   Security Office
#
# The goal is not to use every possible cable connection.
#
# The goal is to:
#
#   Connect every building
#
#   Avoid unnecessary loops
#
#   Use the least total cable
#
#
# CYCLE
# ------------------------------------------------------------
#
# A cycle is a path that returns to its starting vertex.
#
# Example:
#
#   Office -> Server Room -> Workshop -> Office
#
# A cycle adds an unnecessary connection to a spanning tree.
#
# Removing one edge from the cycle still leaves the buildings
# connected.
#
# Therefore, a minimum spanning tree never contains a cycle.
#
#
# MINIMUM SPANNING TREE VS. SHORTEST PATH
# ------------------------------------------------------------
#
# A minimum spanning tree and a shortest-path algorithm solve
# different problems.
#
# Minimum spanning tree:
#
#   Connects every vertex with the smallest total network cost.
#
# Dijkstra's shortest path:
#
#   Finds the shortest route from one starting vertex to
#   another vertex.
#
# An MST minimizes the cost of the complete network.
#
# It does not guarantee the shortest route between every pair
# of vertices.
#
#
# COMMON MST ALGORITHMS
# ------------------------------------------------------------
#
# Two common minimum-spanning-tree algorithms are:
#
#   Kruskal's algorithm
#
#   Prim's algorithm
#
#
# ============================================================
# KRUSKAL'S ALGORITHM
# ============================================================
#
# DESCRIPTION
# ------------------------------------------------------------
#
# Kruskal's algorithm finds a minimum spanning tree by checking
# edges from the smallest weight to the largest weight.
#
# It adds an edge only when the edge does not create a cycle.
#
#
# KRUSKAL'S STEPS
# ------------------------------------------------------------
#
#   1. Sort every edge from smallest weight to largest.
#
#   2. Begin with no selected edges.
#
#   3. Check the smallest remaining edge.
#
#   4. Add the edge if it does not create a cycle.
#
#   5. Skip the edge if it creates a cycle.
#
#   6. Stop after selecting V - 1 edges.
#
#
# SORTED EDGE EXAMPLE
# ------------------------------------------------------------
#
# Original edges:
#
#   Office - Warehouse:          7
#   Office - Server Room:        4
#   Warehouse - Workshop:        2
#   Server Room - Workshop:      3
#
# Sorted edges:
#
#   Warehouse - Workshop:        2
#   Server Room - Workshop:      3
#   Office - Server Room:        4
#   Office - Warehouse:          7
#
# Kruskal's algorithm checks weight 2 first.
#
#
# DISJOINT SET
# ------------------------------------------------------------
#
# Kruskal's algorithm commonly uses a disjoint-set structure.
#
# A disjoint set keeps track of which vertices are already
# connected.
#
# It provides two main operations:
#
# find(vertex)
#     Finds the group containing a vertex.
#
# union(vertex1, vertex2)
#     Combines two separate groups.
#
#
# CYCLE CHECK
# ------------------------------------------------------------
#
# Before adding an edge, Kruskal's algorithm compares the two
# vertices' groups.
#
# Different groups:
#
#   The edge can be added.
#
# Same group:
#
#   The vertices are already connected.
#
#   Adding the edge would create a cycle.
#
#   The edge must be skipped.
#
#
# UNION BY RANK
# ------------------------------------------------------------
#
# Union by rank attaches the smaller disjoint-set tree beneath
# the larger tree.
#
# This helps keep the structure shallow.
#
#
# PATH COMPRESSION
# ------------------------------------------------------------
#
# Path compression makes vertices point more directly to their
# group representative.
#
# This makes future find operations faster.
#
#
# ============================================================
# TIME COMPLEXITY
# ============================================================
#
#   O(E log E)
#
# E represents:
#
#   The number of edges.
#
# Sorting the edges requires:
#
#   O(E log E)
#
# The disjoint-set operations are extremely fast and are
# nearly constant time in practice.
#
#
# ============================================================
# SPACE COMPLEXITY
# ============================================================
#
#   O(V + E)
#
# The algorithm stores:
#
#   Every vertex
#
#   Every weighted edge
#
#   The disjoint-set parent dictionary
#
#   The rank dictionary
#
#   The selected MST edges
#
#
# ============================================================
# DISJOINT-SET IMPLEMENTATION
# ============================================================
class DisjointSet:
    def __init__(self, vertices):
        # Every vertex begins as the parent of its own group.
        self.parent = {
            vertex: vertex
            for vertex in vertices
        }

        # Rank estimates the height of each disjoint-set tree.
        self.rank = {
            vertex: 0
            for vertex in vertices
        }

    def find(self, vertex):
        # Continue until the group's representative is found.
        if self.parent[vertex] != vertex:
            # Path compression makes the vertex point directly
            # toward the group representative.
            self.parent[vertex] = self.find(
                self.parent[vertex]
            )

        # Return the group's representative.
        return self.parent[vertex]

    def union(self, vertex1, vertex2):
        # Find the group containing each vertex.
        root1 = self.find(vertex1)
        root2 = self.find(vertex2)

        # The vertices are already in the same group.
        #
        # Adding an edge between them would create a cycle.
        if root1 == root2:
            return False

        # Attach the lower-rank tree beneath the higher-rank
        # tree.
        if self.rank[root1] < self.rank[root2]:
            self.parent[root1] = root2
        elif self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        else:
            # Both trees have the same rank.
            #
            # Attach root2 beneath root1.
            self.parent[root2] = root1

            # The resulting tree becomes one level taller.
            self.rank[root1] += 1

        # Return True because the groups were combined.
        return True


# ============================================================
# KRUSKAL'S MINIMUM SPANNING TREE IMPLEMENTATION
# ============================================================
class WeightedGraph:
    def __init__(self):
        # Store every vertex in a set.
        self.vertices = set()

        # Store every undirected weighted edge.
        #
        # Each edge is stored as:
        #
        #   (weight, vertex1, vertex2)
        self.edges = []

    def add_vertex(self, vertex):
        # Do not add a duplicate vertex.
        if vertex in self.vertices:
            return False

        # Add the vertex to the graph.
        self.vertices.add(vertex)

        # Return True to show that the vertex was added.
        return True

    def add_edge(self, vertex1, vertex2, weight):
        # Minimum spanning tree examples normally use
        # nonnegative physical costs.
        if weight < 0:
            raise ValueError("Edge weight cannot be negative.")

        # Add both vertices when they do not already exist.
        self.vertices.add(vertex1)
        self.vertices.add(vertex2)

        # Store one copy of the undirected edge.
        self.edges.append((weight, vertex1, vertex2))

    def kruskal_mst(self, show_steps=False):
        # An empty graph does not have a spanning tree.
        if not self.vertices:
            return [], 0

        # Create a separate group for every vertex.
        disjoint_set = DisjointSet(self.vertices)

        # Sort edges from smallest weight to largest weight.
        sorted_edges = sorted(self.edges)

        # Store the edges selected for the MST.
        mst_edges = []

        # Store the total weight of the MST.
        total_weight = 0

        # Track the current step for readable output.
        step = 1

        if show_steps:
            print("=" * 70)
            print("KRUSKAL'S MINIMUM SPANNING TREE TRACE")
            print("=" * 70)
            print("Goal: Connect every building using the least cable.")
            print("\nEdges sorted from shortest to longest:")

            for weight, vertex1, vertex2 in sorted_edges:
                print(
                    f"  {vertex1} <-> {vertex2}: "
                    f"{weight} meters"
                )

        # Check every edge from smallest to largest.
        for weight, vertex1, vertex2 in sorted_edges:
            if show_steps:
                print("\n" + "-" * 70)
                print(f"STEP {step}")
                print("-" * 70)
                print(
                    f"Checking: {vertex1} <-> {vertex2}"
                )
                print("Cable length:", weight, "meters")

            # union() returns True only when the vertices were
            # previously in different groups.
            if disjoint_set.union(vertex1, vertex2):
                # Add the edge because it does not create a
                # cycle.
                mst_edges.append(
                    (vertex1, vertex2, weight)
                )

                # Add the edge weight to the total.
                total_weight += weight

                if show_steps:
                    print("Decision: ADD EDGE")
                    print("Reason: No cycle was created.")
                    print(
                        "Current total cable:",
                        total_weight,
                        "meters",
                    )
            else:
                # Skip the edge because both vertices are
                # already connected.
                if show_steps:
                    print("Decision: SKIP EDGE")
                    print("Reason: This edge creates a cycle.")

            if show_steps:
                print("Selected MST edges:")

                if mst_edges:
                    for (
                        selected_vertex1,
                        selected_vertex2,
                        selected_weight,
                    ) in mst_edges:
                        print(
                            f"  {selected_vertex1} <-> "
                            f"{selected_vertex2}: "
                            f"{selected_weight} meters"
                        )
                else:
                    print("  None")

            # A spanning tree for V vertices needs V - 1 edges.
            if len(mst_edges) == len(self.vertices) - 1:
                break

            step += 1

        # Fewer than V - 1 selected edges means the graph was
        # disconnected.
        if len(mst_edges) != len(self.vertices) - 1:
            if show_steps:
                print("\nThe graph is disconnected.")
                print("A complete spanning tree does not exist.")

            return None, None

        if show_steps:
            print("\n" + "=" * 70)
            print("MINIMUM SPANNING TREE COMPLETE")
            print("=" * 70)
            print(
                "Edges selected:",
                len(mst_edges),
            )
            print(
                "Required edges:",
                len(self.vertices) - 1,
            )
            print(
                "Minimum total cable:",
                total_weight,
                "meters",
            )

        # Return the selected edges and total weight.
        return mst_edges, total_weight

    def display(self):
        # Display every edge from smallest to largest.
        for weight, vertex1, vertex2 in sorted(self.edges):
            print(
                f"{vertex1} <-> {vertex2}: "
                f"{weight} meters"
            )


# ============================================================
# CODE EXAMPLE - OFFICE NETWORK INSTALLATION
# ============================================================
#
# A company needs to connect every building to the same
# physical network.
#
# Each edge weight represents the cable length in meters.
#
# The objective is to connect every building using the least
# total amount of network cable.
office_network = WeightedGraph()

# Add all possible cable connections.
office_network.add_edge(
    "Main Office",
    "Server Room",
    4,
)
office_network.add_edge(
    "Main Office",
    "Warehouse",
    7,
)
office_network.add_edge(
    "Main Office",
    "Workshop",
    8,
)
office_network.add_edge(
    "Server Room",
    "Warehouse",
    5,
)
office_network.add_edge(
    "Server Room",
    "Workshop",
    3,
)
office_network.add_edge(
    "Warehouse",
    "Workshop",
    2,
)
office_network.add_edge(
    "Warehouse",
    "Security Office",
    6,
)
office_network.add_edge(
    "Workshop",
    "Security Office",
    9,
)


# ============================================================
# DISPLAY EVERY POSSIBLE CONNECTION
# ============================================================
print("=" * 70)
print("POSSIBLE NETWORK CABLE CONNECTIONS")
print("=" * 70)
office_network.display()


# ============================================================
# FIND THE MINIMUM SPANNING TREE
# ============================================================
#
# show_steps=True shows why each edge is added or skipped.
print("\n")
mst_edges, total_cable = office_network.kruskal_mst(
    show_steps=True
)


# ============================================================
# DISPLAY THE FINAL NETWORK DESIGN
# ============================================================
print("\n" + "=" * 70)
print("FINAL MINIMUM-COST NETWORK")
print("=" * 70)

if mst_edges is None:
    print("The buildings cannot all be connected.")
else:
    print("Install these cable connections:")

    for position, (building1, building2, length) in enumerate(
        mst_edges,
        start=1,
    ):
        print(
            f"{position}. {building1} <-> {building2}: "
            f"{length} meters"
        )

    print("\nBuildings connected:", len(office_network.vertices))
    print("Cables required:", len(mst_edges))
    print("Minimum total cable:", total_cable, "meters")