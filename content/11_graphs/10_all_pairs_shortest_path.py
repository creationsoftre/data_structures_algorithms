# ============================================================
# All-Pairs Shortest Path - High-Level Notes
# ============================================================
#
# DESCRIPTION
# ------------------------------------------------------------
#
# An all-pairs shortest-path algorithm finds the shortest path
# between every possible pair of vertices in a weighted graph.
#
# Instead of choosing one starting vertex, it calculates:
#
#   Every vertex -> Every other vertex
#
# Example:
#
#   Warehouse -> Parts Store
#   Warehouse -> Repair Shop
#   Warehouse -> Customer
#   Parts Store -> Warehouse
#   Parts Store -> Repair Shop
#   Parts Store -> Customer
#
# The result is commonly stored inside a distance matrix.
#
#
# EXAMPLE - DELIVERY NETWORK
# ------------------------------------------------------------
#
# A delivery company needs the shortest travel time between
# every location in its network.
#
# Each edge weight represents travel time in minutes.
#
#   Warehouse ------ 8 ------> Parts Store
#       |                            |
#      20                            5
#       |                            |
#       v                            v
#   Customer <------ 4 ------- Repair Shop
#
# There may be a direct route between two locations.
#
# However, traveling through another location may be faster.
#
# Example:
#
# Direct route:
#
#   Warehouse -> Customer
#
# Travel time:
#
#   20 minutes
#
# Indirect route:
#
#   Warehouse -> Parts Store -> Repair Shop -> Customer
#
# Travel time:
#
#   8 + 5 + 4 = 17 minutes
#
# The indirect route is shorter.
#
#
# ALL-PAIRS VS. SINGLE-SOURCE
# ------------------------------------------------------------
#
# Dijkstra's algorithm:
#
#   Finds shortest paths from one starting vertex.
#
# Bellman-Ford:
#
#   Finds shortest paths from one starting vertex.
#
# Floyd-Warshall:
#
#   Finds shortest paths between every pair of vertices.
#
#
# DISTANCE MATRIX
# ------------------------------------------------------------
#
# Floyd-Warshall stores shortest distances inside a matrix.
#
# Each row represents:
#
#   Starting vertex
#
# Each column represents:
#
#   Destination vertex
#
# Example:
#
#                 Warehouse  Parts Store  Repair Shop  Customer
#
# Warehouse           0           8            13          17
# Parts Store       Infinity       0             5           9
# Repair Shop       Infinity    Infinity          0           4
# Customer          Infinity    Infinity       Infinity        0
#
# A distance of 0 means:
#
#   The starting vertex and destination are the same.
#
# Infinity means:
#
#   No route currently exists.
#
#
# ============================================================
# FLOYD-WARSHALL ALGORITHM
# ============================================================
#
# DESCRIPTION
# ------------------------------------------------------------
#
# The Floyd-Warshall algorithm finds the shortest path between
# every pair of vertices.
#
# It repeatedly checks whether traveling through another
# vertex creates a shorter route.
#
# The intermediate vertex is commonly called:
#
#   k
#
#
# MAIN QUESTION
# ------------------------------------------------------------
#
# For every pair of vertices, Floyd-Warshall asks:
#
#   Is the current direct route shorter?
#
# or:
#
#   Is traveling through another vertex shorter?
#
#
# UPDATE FORMULA
# ------------------------------------------------------------
#
# The algorithm compares:
#
#   Current distance from i to j
#
# with:
#
#   Distance from i to k
#   +
#   Distance from k to j
#
# Formula:
#
#   distance[i][j] = min(
#       distance[i][j],
#       distance[i][k] + distance[k][j]
#   )
#
# i represents:
#
#   Starting vertex
#
# j represents:
#
#   Destination vertex
#
# k represents:
#
#   Possible intermediate vertex
#
#
# UPDATE EXAMPLE
# ------------------------------------------------------------
#
# Current direct route:
#
#   Warehouse -> Repair Shop
#
# Distance:
#
#   18 minutes
#
# Possible route through the Parts Store:
#
#   Warehouse -> Parts Store:
#
#       8 minutes
#
#   Parts Store -> Repair Shop:
#
#       5 minutes
#
# Total:
#
#   8 + 5 = 13 minutes
#
# Because 13 is less than 18, the distance is updated:
#
#   18 -> 13
#
#
# THREE NESTED LOOPS
# ------------------------------------------------------------
#
# Floyd-Warshall uses three nested loops:
#
#   Intermediate vertex
#
#   Starting vertex
#
#   Destination vertex
#
# The intermediate-vertex loop must be the outermost loop.
#
# This allows the algorithm to gradually consider more
# possible intermediate locations.
#
#
# PATH RECONSTRUCTION
# ------------------------------------------------------------
#
# A next-vertex matrix can remember how each shortest route
# begins.
#
# Example shortest route:
#
#   Warehouse -> Parts Store -> Repair Shop -> Customer
#
# The next matrix remembers:
#
#   From Warehouse toward Customer:
#
#       Go to Parts Store first.
#
# This allows the complete shortest path to be reconstructed.
#
#
# NEGATIVE EDGE WEIGHTS
# ------------------------------------------------------------
#
# Floyd-Warshall can handle negative edge weights.
#
# However, it cannot produce reliable shortest paths when a
# negative-weight cycle exists.
#
#
# NEGATIVE-CYCLE DETECTION
# ------------------------------------------------------------
#
# After the algorithm finishes, check the matrix diagonal.
#
# Normally:
#
#   distance[vertex][vertex] = 0
#
# If any diagonal value becomes negative:
#
#   distance[vertex][vertex] < 0
#
# then a negative-weight cycle exists.
#
#
# WHEN TO USE FLOYD-WARSHALL
# ------------------------------------------------------------
#
# Floyd-Warshall is useful when:
#
#   Shortest paths are needed between every pair of vertices
#
#   The graph is relatively small
#
#   The graph contains many edges
#
#   Negative edges may exist
#
#   A complete distance matrix is useful
#
# Examples:
#
#   Delivery networks
#
#   Airline route comparisons
#
#   Computer network routing tables
#
#   City travel-time matrices
#
#   Game-map movement costs
#
#
# ============================================================
# TIME COMPLEXITY
# ============================================================
#
#   O(V^3)
#
# V represents:
#
#   The number of vertices.
#
# The algorithm uses three nested loops over all vertices.
#
# Floyd-Warshall can become slow for very large graphs.
#
#
# ============================================================
# SPACE COMPLEXITY
# ============================================================
#
#   O(V^2)
#
# The algorithm stores:
#
#   A distance matrix
#
#   A next-vertex matrix
#
# Each matrix contains one position for every possible pair
# of vertices.
#
#
# ============================================================
# FLOYD-WARSHALL IMPLEMENTATION
# ============================================================
class WeightedDirectedGraph:
    def __init__(self):
        # Store vertices in insertion order.
        self.vertices = []
        #
        # Store each vertex's matrix index.
        self.vertex_indexes = {}
        #
        # Store directed weighted edges.
        #
        # Each edge is stored as:
        #
        #   (source, destination, weight)
        self.edges = []
    #
    def add_vertex(self, vertex):
        # Do not add a duplicate vertex.
        if vertex in self.vertex_indexes:
            return False
        #
        # Store the vertex's matrix index.
        self.vertex_indexes[vertex] = len(self.vertices)
        #
        # Add the vertex to the ordered vertex list.
        self.vertices.append(vertex)
        #
        # Return True to show that the vertex was added.
        return True
    #
    def add_edge(self, source, destination, weight):
        # Add the source when it does not already exist.
        if source not in self.vertex_indexes:
            self.add_vertex(source)
        #
        # Add the destination when it does not already exist.
        if destination not in self.vertex_indexes:
            self.add_vertex(destination)
        #
        # Store the directed weighted edge.
        self.edges.append((source, destination, weight))
    #
    def floyd_warshall(self, show_steps=False):
        # Store the number of vertices.
        vertex_count = len(self.vertices)
        #
        # Create a distance matrix filled with infinity.
        distances = [
            [float("inf")] * vertex_count
            for _ in range(vertex_count)
        ]
        #
        # Create a matrix used to reconstruct shortest paths.
        next_vertex = [
            [None] * vertex_count
            for _ in range(vertex_count)
        ]
        #
        # The distance from a vertex to itself is zero.
        for index in range(vertex_count):
            distances[index][index] = 0
            next_vertex[index][index] = index
        #
        # Add every direct edge to the matrices.
        for source, destination, weight in self.edges:
            source_index = self.vertex_indexes[source]
            destination_index = self.vertex_indexes[destination]
            #
            # Keep the smallest weight when duplicate edges
            # connect the same two vertices.
            if weight < distances[source_index][destination_index]:
                distances[source_index][destination_index] = weight
                next_vertex[source_index][destination_index] = (
                    destination_index
                )
        #
        if show_steps:
            print("=" * 75)
            print("FLOYD-WARSHALL ALGORITHM TRACE")
            print("=" * 75)
            print("Initial distance matrix:")
            self.display_distance_matrix(distances)
        #
        # Consider each vertex as a possible intermediate
        # location.
        for intermediate in range(vertex_count):
            intermediate_name = self.vertices[intermediate]
            updated_routes = []
            #
            if show_steps:
                print("\n" + "=" * 75)
                print(
                    "USING INTERMEDIATE LOCATION:",
                    intermediate_name,
                )
                print("=" * 75)
            #
            # Visit every possible starting vertex.
            for start in range(vertex_count):
                # Visit every possible destination vertex.
                for destination in range(vertex_count):
                    # Skip the calculation when either half of
                    # the possible route does not exist.
                    if (
                        distances[start][intermediate]
                        == float("inf")
                        or distances[intermediate][destination]
                        == float("inf")
                    ):
                        continue
                    #
                    # Calculate the distance through the
                    # intermediate vertex.
                    possible_distance = (
                        distances[start][intermediate]
                        + distances[intermediate][destination]
                    )
                    #
                    # Update the route when it is shorter.
                    if possible_distance < distances[start][destination]:
                        old_distance = distances[start][destination]
                        #
                        # Save the shorter distance.
                        distances[start][destination] = (
                            possible_distance
                        )
                        #
                        # The first step is the same first step
                        # used to travel from start to the
                        # intermediate vertex.
                        next_vertex[start][destination] = (
                            next_vertex[start][intermediate]
                        )
                        #
                        updated_routes.append(
                            (
                                self.vertices[start],
                                self.vertices[destination],
                                old_distance,
                                possible_distance,
                            )
                        )
            #
            if show_steps:
                if updated_routes:
                    print("Routes improved:")
                    #
                    for (
                        start_name,
                        destination_name,
                        old_distance,
                        new_distance,
                    ) in updated_routes:
                        if old_distance == float("inf"):
                            old_distance = "Infinity"
                        #
                        print(
                            f"  {start_name} -> "
                            f"{destination_name}: "
                            f"{old_distance} -> "
                            f"{new_distance} minutes"
                        )
                else:
                    print("Routes improved: None")
                #
                print("\nDistance matrix now:")
                self.display_distance_matrix(distances)
        #
        # Detect whether a negative-weight cycle exists.
        negative_cycle = any(
            distances[index][index] < 0
            for index in range(vertex_count)
        )
        #
        return distances, next_vertex, negative_cycle
    #
    def reconstruct_path(
        self,
        start,
        destination,
        next_vertex,
    ):
        # Return None when either vertex does not exist.
        if (
            start not in self.vertex_indexes
            or destination not in self.vertex_indexes
        ):
            return None
        #
        start_index = self.vertex_indexes[start]
        destination_index = self.vertex_indexes[destination]
        #
        # Return None when no path exists.
        if next_vertex[start_index][destination_index] is None:
            return None
        #
        # Begin the path with the starting vertex.
        path = [start]
        current_index = start_index
        #
        # Follow the next-vertex matrix until the destination
        # is reached.
        while current_index != destination_index:
            current_index = next_vertex[
                current_index
            ][destination_index]
            #
            # Protect against invalid path data.
            if current_index is None:
                return None
            #
            path.append(self.vertices[current_index])
        #
        return path
    #
    def get_distance(
        self,
        start,
        destination,
        distances,
    ):
        # Return None when either vertex does not exist.
        if (
            start not in self.vertex_indexes
            or destination not in self.vertex_indexes
        ):
            return None
        #
        start_index = self.vertex_indexes[start]
        destination_index = self.vertex_indexes[destination]
        distance = distances[start_index][destination_index]
        #
        # Return None when the destination is unreachable.
        if distance == float("inf"):
            return None
        #
        return distance
    #
    def display_distance_matrix(self, distances):
        # Create a width large enough for the location names.
        column_width = max(
            14,
            max(len(vertex) for vertex in self.vertices) + 2,
        )
        #
        # Display the destination headings.
        print(
            "From / To".ljust(column_width),
            end="",
        )
        #
        for vertex in self.vertices:
            print(
                vertex.ljust(column_width),
                end="",
            )
        #
        print()
        print("-" * (column_width * (len(self.vertices) + 1)))
        #
        # Display each starting vertex and its distances.
        for row_index, start in enumerate(self.vertices):
            print(
                start.ljust(column_width),
                end="",
            )
            #
            for distance in distances[row_index]:
                if distance == float("inf"):
                    display_value = "INF"
                else:
                    display_value = str(distance)
                #
                print(
                    display_value.ljust(column_width),
                    end="",
                )
            #
            print()
    #
    def display_edges(self):
        # Display every directed route.
        for source, destination, weight in sorted(self.edges):
            print(
                f"{source} -> {destination}: "
                f"{weight} minutes"
            )
#
#
# ============================================================
# CODE EXAMPLE - DELIVERY TRAVEL-TIME NETWORK
# ============================================================
#
# Create a directed weighted graph for delivery routes.
#
# Each edge weight represents travel time in minutes.
delivery_network = WeightedDirectedGraph()
#
# Add routes leaving the Warehouse.
delivery_network.add_edge(
    "Warehouse",
    "Parts Store",
    8,
)
delivery_network.add_edge(
    "Warehouse",
    "Repair Shop",
    18,
)
delivery_network.add_edge(
    "Warehouse",
    "Customer",
    20,
)
#
# Add routes leaving the Parts Store.
delivery_network.add_edge(
    "Parts Store",
    "Repair Shop",
    5,
)
delivery_network.add_edge(
    "Parts Store",
    "Customer",
    12,
)
#
# Add routes leaving the Repair Shop.
delivery_network.add_edge(
    "Repair Shop",
    "Customer",
    4,
)
delivery_network.add_edge(
    "Repair Shop",
    "Warehouse",
    10,
)
#
# Add routes leaving the Customer.
delivery_network.add_edge(
    "Customer",
    "Warehouse",
    15,
)
#
#
# ============================================================
# DISPLAY THE DIRECT ROUTES
# ============================================================
print("=" * 75)
print("DIRECT DELIVERY ROUTES")
print("=" * 75)
delivery_network.display_edges()
#
#
# ============================================================
# RUN FLOYD-WARSHALL
# ============================================================
#
# show_steps=True displays every intermediate location and
# every route that becomes shorter.
print("\n")
distances, next_vertex, negative_cycle = (
    delivery_network.floyd_warshall(show_steps=True)
)
#
#
# ============================================================
# DISPLAY THE FINAL DISTANCE MATRIX
# ============================================================
print("\n" + "=" * 75)
print("SHORTEST TRAVEL TIMES BETWEEN ALL LOCATIONS")
print("=" * 75)
#
if negative_cycle:
    print("A negative-weight cycle was detected.")
    print("Shortest travel times are not reliable.")
else:
    delivery_network.display_distance_matrix(distances)
#
#
# ============================================================
# DISPLAY SELECTED SHORTEST ROUTES
# ============================================================
print("\n" + "=" * 75)
print("SELECTED SHORTEST ROUTES")
print("=" * 75)
#
# Define location pairs to examine.
route_requests = [
    ("Warehouse", "Customer"),
    ("Warehouse", "Repair Shop"),
    ("Parts Store", "Customer"),
    ("Customer", "Repair Shop"),
]
#
# Reconstruct and display each requested route.
for start, destination in route_requests:
    path = delivery_network.reconstruct_path(
        start,
        destination,
        next_vertex,
    )
    #
    distance = delivery_network.get_distance(
        start,
        destination,
        distances,
    )
    #
    print(
        f"\nStart: {start}"
    )
    print(
        f"Destination: {destination}"
    )
    #
    if path is None:
        print("Route: No route exists")
        print("Travel time: Unreachable")
    else:
        print(
            "Route:",
            " -> ".join(path),
        )
        print(
            "Travel time:",
            distance,
            "minutes",
        )
#
#
# ============================================================
# DIRECT ROUTE VS. SHORTEST ROUTE
# ============================================================
print("\n" + "=" * 75)
print("DIRECT ROUTE VS. SHORTEST ROUTE")
print("=" * 75)
#
# The direct Warehouse-to-Customer route takes 20 minutes.
direct_time = 20
#
# Get the shortest calculated travel time.
shortest_time = delivery_network.get_distance(
    "Warehouse",
    "Customer",
    distances,
)
#
# Reconstruct the shortest route.
shortest_path = delivery_network.reconstruct_path(
    "Warehouse",
    "Customer",
    next_vertex,
)
#
print("Direct route:")
print("  Warehouse -> Customer")
print("  Travel time:", direct_time, "minutes")
#
print("\nShortest route:")
print(" ", " -> ".join(shortest_path))
print("  Travel time:", shortest_time, "minutes")
#
print(
    "\nTime saved:",
    direct_time - shortest_time,
    "minutes",
)
