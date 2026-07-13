# ============================================================
# Weighted Graph - High-Level Notes
# ============================================================
#
# DESCRIPTION
# ------------------------------------------------------------
#
# A weighted graph stores connections between vertices.
#
# Each connection also stores a weight.
#
# The weight represents the cost of traveling across an edge.
#
# A weight could represent:
#
#   Distance
#   Travel time
#   Fuel cost
#   Toll cost
#   Network delay
#
#
# EXAMPLE - ROAD NETWORK
# ------------------------------------------------------------
#
# A weighted graph can represent locations connected by roads.
#
# The edge weights represent distance in miles.
#
#   Home -------- 8 miles -------- Gas Station
#     |
#     |
#   12 miles
#     |
#     |
#   Wheel Shop ---- 6 miles ---- Car Meet
#
# Vertices:
#
#   Home
#   Gas Station
#   Wheel Shop
#   Car Meet
#
# Weighted edges:
#
#   Home <-> Gas Station:
#       8 miles
#
#   Home <-> Wheel Shop:
#       12 miles
#
#   Wheel Shop <-> Car Meet:
#       6 miles
#
#
# WHY THE WEIGHT MATTERS
# ------------------------------------------------------------
#
# An unweighted graph only shows whether two locations are
# connected.
#
# Example:
#
#   Home <-> Gas Station
#
# A weighted graph also shows the cost of the connection.
#
# Example:
#
#   Home <-> Gas Station: 8 miles
#
# This allows programs to compare routes.
#
# Example:
#
# Route 1:
#
#   Home -> Wheel Shop -> Car Meet
#
# Distance:
#
#   12 + 6 = 18 miles
#
# Route 2:
#
#   Home -> Gas Station -> Car Meet
#
# Distance:
#
#   8 + 7 = 15 miles
#
# Route 2 is shorter even though both routes use two edges.
#
#
# UNDIRECTED WEIGHTED EDGES
# ------------------------------------------------------------
#
# This implementation uses an undirected weighted graph.
#
# Each road works in both directions.
#
# Example:
#
#   Home <---- 8 miles ----> Gas Station
#
# Home connects to the Gas Station.
#
# The Gas Station also connects back to Home.
#
# Both directions use the same weight.
#
#
# ADJACENCY LIST REPRESENTATION
# ------------------------------------------------------------
#
# Each vertex stores its neighbors and edge weights.
#
# Example:
#
#   {
#       "Home": {
#           "Gas Station": 8,
#           "Wheel Shop": 12
#       },
#       "Gas Station": {
#           "Home": 8
#       },
#       "Wheel Shop": {
#           "Home": 12
#       }
#   }
#
# The outer dictionary stores the vertices.
#
# Each inner dictionary stores:
#
#   Neighbor: Weight
#
#
# MAIN WEIGHTED GRAPH OPERATIONS
# ------------------------------------------------------------
#
# add_vertex(vertex)
#     Adds a new vertex to the graph.
#
# add_edge(vertex1, vertex2, weight)
#     Adds a weighted connection between two vertices.
#
# remove_edge(vertex1, vertex2)
#     Removes the connection between two vertices.
#
# remove_vertex(vertex)
#     Removes a vertex and every connected edge.
#
# get_neighbors(vertex)
#     Returns the selected vertex's neighbors and weights.
#
# get_weight(vertex1, vertex2)
#     Returns the weight between two connected vertices.
#
# has_vertex(vertex)
#     Checks whether a vertex exists.
#
# has_edge(vertex1, vertex2)
#     Checks whether two vertices are connected.
#
# calculate_route(route)
#     Calculates the total weight of a specific route.
#
# vertex_count()
#     Returns the number of vertices.
#
# edge_count()
#     Returns the number of weighted edges.
#
#
# ============================================================
# TIME COMPLEXITY
# ============================================================
#
# The following times assume dictionaries are used.
#
#   Operation                    Time Complexity
#   --------------------------------------------
#   add_vertex()                      O(1)
#   add_edge()                        O(1) average
#   has_vertex()                      O(1) average
#   has_edge()                        O(1) average
#   get_weight()                      O(1) average
#   get_neighbors()                  O(d)
#   remove_edge()                     O(1) average
#   calculate_route()                O(r)
#   remove_vertex()                  O(V + E)
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
# r represents:
#
#   The number of vertices in the route.
#
#
# ============================================================
# SPACE COMPLEXITY
# ============================================================
#
#   O(V + E)
#
# The graph stores:
#
#   One dictionary entry for every vertex.
#
#   One neighbor and weight entry for every connection.
#
# Each undirected edge is stored in both directions.
#
#
# ============================================================
# WEIGHTED GRAPH IMPLEMENTATION
# ============================================================
class WeightedGraph:
    def __init__(self):
        # Create an empty weighted adjacency list.
        #
        # Each vertex maps to a dictionary containing:
        #
        #   Neighbor: Weight
        self.graph = {}

    def add_vertex(self, vertex):
        # Do not add the vertex when it already exists.
        if vertex in self.graph:
            return False

        # Add the vertex with no weighted connections.
        self.graph[vertex] = {}

        # Return True to show that the vertex was added.
        return True

    def add_edge(self, vertex1, vertex2, weight):
        # A road distance cannot be negative.
        if weight < 0:
            return False

        # Add vertex1 when it does not already exist.
        if vertex1 not in self.graph:
            self.add_vertex(vertex1)

        # Add vertex2 when it does not already exist.
        if vertex2 not in self.graph:
            self.add_vertex(vertex2)

        # Store the connection from vertex1 to vertex2.
        self.graph[vertex1][vertex2] = weight

        # Store the connection from vertex2 to vertex1.
        #
        # Adding both directions creates an undirected edge.
        self.graph[vertex2][vertex1] = weight

        # Return True to show that the edge was added.
        return True

    def remove_edge(self, vertex1, vertex2):
        # Return False when either vertex does not exist.
        if vertex1 not in self.graph or vertex2 not in self.graph:
            return False

        # Return False when the edge does not exist.
        if vertex2 not in self.graph[vertex1]:
            return False

        # Remove the edge in both directions.
        del self.graph[vertex1][vertex2]
        del self.graph[vertex2][vertex1]

        # Return True to show that the edge was removed.
        return True

    def remove_vertex(self, vertex):
        # Return False when the vertex does not exist.
        if vertex not in self.graph:
            return False

        # Visit every neighbor connected to the vertex.
        for neighbor in list(self.graph[vertex]):
            # Remove the vertex from each neighbor's dictionary.
            del self.graph[neighbor][vertex]

        # Remove the vertex and its outgoing connections.
        del self.graph[vertex]

        # Return True to show that the vertex was removed.
        return True

    def get_neighbors(self, vertex):
        # Return an empty dictionary when the vertex does not
        # exist.
        if vertex not in self.graph:
            return {}

        # Return a copy so the original graph is not changed.
        return dict(sorted(self.graph[vertex].items()))

    def get_weight(self, vertex1, vertex2):
        # Return None when vertex1 does not exist.
        if vertex1 not in self.graph:
            return None

        # Return the edge weight when the connection exists.
        #
        # Return None when the edge does not exist.
        return self.graph[vertex1].get(vertex2)

    def has_vertex(self, vertex):
        # Return True when the vertex exists.
        return vertex in self.graph

    def has_edge(self, vertex1, vertex2):
        # Return False when vertex1 does not exist.
        if vertex1 not in self.graph:
            return False

        # Check whether vertex2 is connected to vertex1.
        return vertex2 in self.graph[vertex1]

    def calculate_route(self, route):
        # A route needs at least two locations.
        if len(route) < 2:
            return 0

        # Store the total weight of the route.
        total_weight = 0

        # Visit each pair of consecutive locations.
        for index in range(len(route) - 1):
            current_location = route[index]
            next_location = route[index + 1]

            # Get the weight between the two locations.
            weight = self.get_weight(
                current_location,
                next_location,
            )

            # Return None when part of the route does not exist.
            if weight is None:
                return None

            # Add the edge weight to the route total.
            total_weight += weight

        # Return the total weight of the complete route.
        return total_weight

    def vertex_count(self):
        # Return the number of locations in the graph.
        return len(self.graph)

    def edge_count(self):
        # Count every stored neighbor connection.
        total_connections = sum(
            len(neighbors)
            for neighbors in self.graph.values()
        )

        # Each undirected edge is stored twice.
        return total_connections // 2

    def display(self):
        # Visit every location in alphabetical order.
        for vertex in sorted(self.graph):
            # Get the location's neighbors and distances.
            neighbors = self.graph[vertex]

            # Display None when the location has no roads.
            if not neighbors:
                print(f"{vertex}: No connections")
                continue

            # Format each neighbor and its distance.
            connections = [
                f"{neighbor} ({weight} miles)"
                for neighbor, weight in sorted(neighbors.items())
            ]

            # Display the weighted connections.
            print(f"{vertex}: {', '.join(connections)}")


# ============================================================
# CODE EXAMPLE - CAR MEET ROAD NETWORK
# ============================================================
#
# Create a weighted graph representing roads between locations.
#
# Each weight represents distance in miles.
road_network = WeightedGraph()
#
# Add roads leaving Home.
road_network.add_edge("Home", "Gas Station", 8)
road_network.add_edge("Home", "Wheel Shop", 12)
#
# Add roads leaving the Gas Station.
road_network.add_edge("Gas Station", "Car Meet", 7)
road_network.add_edge("Gas Station", "Parts Store", 5)
#
# Add roads leaving the Wheel Shop.
road_network.add_edge("Wheel Shop", "Car Meet", 6)
road_network.add_edge("Wheel Shop", "Parts Store", 4)
#
# Add a road between the Parts Store and Car Meet.
road_network.add_edge("Parts Store", "Car Meet", 9)
#
# Display the complete road network.
print("=" * 55)
print("CAR MEET ROAD NETWORK")
print("=" * 55)
road_network.display()
#
# Display every location connected directly to Home.
print("\n" + "=" * 55)
print("ROADS LEAVING HOME")
print("=" * 55)
for location, distance in road_network.get_neighbors("Home").items():
    print(f"Home -> {location}: {distance} miles")
#
# Display the distance of one direct road.
print("\n" + "=" * 55)
print("DIRECT ROAD DISTANCE")
print("=" * 55)
print(
    "Home to Wheel Shop:",
    road_network.get_weight("Home", "Wheel Shop"),
    "miles",
)
#
# Create two possible routes from Home to the Car Meet.
route_through_wheel_shop = [
    "Home",
    "Wheel Shop",
    "Car Meet",
]
route_through_gas_station = [
    "Home",
    "Gas Station",
    "Car Meet",
]
#
# Calculate the total distance of each route.
wheel_shop_distance = road_network.calculate_route(
    route_through_wheel_shop
)
gas_station_distance = road_network.calculate_route(
    route_through_gas_station
)
#
# Compare the two routes.
print("\n" + "=" * 55)
print("ROUTE COMPARISON")
print("=" * 55)
print(
    "Home -> Wheel Shop -> Car Meet:",
    wheel_shop_distance,
    "miles",
)
print(
    "Home -> Gas Station -> Car Meet:",
    gas_station_distance,
    "miles",
)
#
# Determine which route is shorter.
if wheel_shop_distance < gas_station_distance:
    print("Shorter route: Through the Wheel Shop")
elif gas_station_distance < wheel_shop_distance:
    print("Shorter route: Through the Gas Station")
else:
    print("Both routes have the same distance")
#
# Display graph totals.
print("\n" + "=" * 55)
print("ROAD NETWORK TOTALS")
print("=" * 55)
print("Total locations:", road_network.vertex_count())
print("Total roads:", road_network.edge_count())
#
# Check whether two locations have a direct road.
print("\n" + "=" * 55)
print("CONNECTION CHECKS")
print("=" * 55)
print(
    "Home connects directly to Gas Station:",
    road_network.has_edge("Home", "Gas Station"),
)
print(
    "Home connects directly to Car Meet:",
    road_network.has_edge("Home", "Car Meet"),
)
#
# Remove the road between the Parts Store and Car Meet.
road_network.remove_edge("Parts Store", "Car Meet")
#
# Display the updated road network.
print("\n" + "=" * 55)
print("UPDATED ROAD NETWORK")
print("=" * 55)
road_network.display()
