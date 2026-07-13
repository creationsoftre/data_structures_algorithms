# ============================================================
# Dijkstra's Shortest Path - High-Level Notes
# ============================================================
#
# DESCRIPTION
# ------------------------------------------------------------
#
# Dijkstra's algorithm finds the shortest path from one
# starting vertex to every other reachable vertex.
#
# It is used with a weighted graph.
#
# Each edge must have a numeric weight.
#
# A weight could represent:
#
#   Distance
#   Travel time
#   Fuel cost
#   Toll cost
#   Network delay
#
# Dijkstra's algorithm chooses the path with the smallest
# total weight.
#
#
# EXAMPLE - ROAD NETWORK
# ------------------------------------------------------------
#
# The graph represents roads between locations.
#
# Each weight represents distance in miles.
#
#                         8
#              Home ------------ Gas Station
#                |                    |
#             12 |                    | 7
#                |                    |
#          Wheel Shop ------------ Car Meet
#                       6
#
# Possible route 1:
#
#   Home -> Wheel Shop -> Car Meet
#
# Total distance:
#
#   12 + 6 = 18 miles
#
# Possible route 2:
#
#   Home -> Gas Station -> Car Meet
#
# Total distance:
#
#   8 + 7 = 15 miles
#
# Dijkstra's algorithm chooses:
#
#   Home -> Gas Station -> Car Meet
#
# because 15 miles is shorter than 18 miles.
#
#
# HOW DIJKSTRA'S ALGORITHM WORKS
# ------------------------------------------------------------
#
# Dijkstra's algorithm keeps track of:
#
#   Distance:
#       The shortest known distance from the starting vertex.
#
#   Previous:
#       The previous vertex used to reach the current vertex.
#
#   Priority queue:
#       Stores vertices based on their shortest known distance.
#
#
# STARTING DISTANCES
# ------------------------------------------------------------
#
# The starting vertex receives a distance of:
#
#   0
#
# Every other vertex begins with:
#
#   Infinity
#
# Example:
#
#   Home:          0
#   Gas Station:   Infinity
#   Wheel Shop:    Infinity
#   Car Meet:      Infinity
#
# Infinity means a route has not been found yet.
#
#
# RELAXING AN EDGE
# ------------------------------------------------------------
#
# Relaxing an edge means checking whether a shorter route has
# been found.
#
# Formula:
#
#   New distance =
#
#       Current distance + Edge weight
#
# Example:
#
# Current location:
#
#   Home
#
# Current distance:
#
#   0
#
# Edge:
#
#   Home -> Gas Station
#
# Edge weight:
#
#   8
#
# New distance:
#
#   0 + 8 = 8
#
# Because 8 is less than Infinity, the Gas Station's distance
# is updated to 8.
#
#
# PRIORITY QUEUE
# ------------------------------------------------------------
#
# Dijkstra's algorithm uses a priority queue.
#
# The vertex with the smallest known distance is removed first.
#
# Python's heapq module provides a min-heap priority queue.
#
# Each heap entry stores:
#
#   (distance, vertex)
#
# Example:
#
#   (8, "Gas Station")
#
# The smallest distance is stored at the top of the heap.
#
#
# PATH RECONSTRUCTION
# ------------------------------------------------------------
#
# The previous dictionary remembers how each vertex was
# reached.
#
# Example:
#
#   Gas Station:
#       Previous vertex is Home
#
#   Car Meet:
#       Previous vertex is Gas Station
#
# To reconstruct the path, begin at the destination and follow
# the previous vertices backward.
#
# Backward:
#
#   Car Meet <- Gas Station <- Home
#
# Reverse the result:
#
#   Home -> Gas Station -> Car Meet
#
#
# IMPORTANT LIMITATION
# ------------------------------------------------------------
#
# Dijkstra's algorithm cannot safely handle negative edge
# weights.
#
# Valid weights:
#
#   0
#   5
#   12
#
# Invalid weight:
#
#   -4
#
# Use Dijkstra's algorithm only when every edge weight is:
#
#   Greater than or equal to 0
#
#
# MAIN OPERATIONS
# ------------------------------------------------------------
#
# add_vertex(vertex)
#     Adds a new vertex to the graph.
#
# add_edge(vertex1, vertex2, weight)
#     Adds a weighted road between two vertices.
#
# dijkstra(start)
#     Finds the shortest distance from the starting vertex to
#     every reachable vertex.
#
# shortest_path(start, destination)
#     Returns the shortest path and total distance.
#
# display()
#     Displays every weighted connection.
#
#
# ============================================================
# TIME COMPLEXITY
# ============================================================
#
# Using an adjacency list and a min-heap:
#
#   O((V + E) log V)
#
# This is commonly simplified to:
#
#   O(E log V)
#
# V represents:
#
#   The number of vertices.
#
# E represents:
#
#   The number of edges.
#
# Heap insertion and removal require:
#
#   O(log V)
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
#   The weighted adjacency list
#
#   The distance dictionary
#
#   The previous dictionary
#
#   The priority queue
#
#
# ============================================================
# DIJKSTRA'S SHORTEST PATH IMPLEMENTATION
# ============================================================
import heapq


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
        # Dijkstra's algorithm does not support negative
        # edge weights.
        if weight < 0:
            raise ValueError("Dijkstra's algorithm requires nonnegative weights.")

        # Add vertex1 when it does not already exist.
        if vertex1 not in self.graph:
            self.add_vertex(vertex1)

        # Add vertex2 when it does not already exist.
        if vertex2 not in self.graph:
            self.add_vertex(vertex2)

        # Add the weighted connection from vertex1 to vertex2.
        self.graph[vertex1][vertex2] = weight

        # Add the weighted connection from vertex2 to vertex1.
        #
        # Adding both directions creates an undirected road.
        self.graph[vertex2][vertex1] = weight

    def dijkstra(self, start, show_steps=False):
        # Return empty results when the start does not exist.
        if start not in self.graph:
            return {}, {}

        # Give every vertex an initial distance of infinity.
        distances = {
            vertex: float("inf")
            for vertex in self.graph
        }

        # The starting vertex has a distance of zero.
        distances[start] = 0

        # Store the previous vertex used for each shortest path.
        previous = {
            vertex: None
            for vertex in self.graph
        }

        # Create a min-heap containing the starting vertex.
        #
        # Each entry stores:
        #
        #   (distance, vertex)
        priority_queue = [(0, start)]

        # Track the search step for readable output.
        step = 1

        if show_steps:
            print("=" * 65)
            print("DIJKSTRA'S ALGORITHM TRACE")
            print("=" * 65)
            print("Starting location:", start)
            print("Goal: Find the shortest distance to every location.")

        # Continue while vertices remain in the priority queue.
        while priority_queue:
            # Remove the vertex with the smallest distance.
            current_distance, current_vertex = heapq.heappop(
                priority_queue
            )

            # Skip outdated entries.
            #
            # A vertex may appear in the heap more than once
            # when a shorter route is discovered later.
            if current_distance > distances[current_vertex]:
                continue

            if show_steps:
                print("\n" + "-" * 65)
                print(f"STEP {step}")
                print("-" * 65)
                print("Visiting:", current_vertex)
                print("Current shortest distance:", current_distance)

            # Examine every neighboring vertex.
            for neighbor, weight in self.graph[current_vertex].items():
                # Calculate the distance through the current
                # vertex.
                new_distance = current_distance + weight

                if show_steps:
                    print(
                        f"\nChecking road: {current_vertex} "
                        f"-> {neighbor}"
                    )
                    print("Road distance:", weight)
                    print(
                        "Possible total distance:",
                        new_distance,
                    )
                    print(
                        "Known distance:",
                        distances[neighbor],
                    )

                # Update the neighbor when a shorter route is
                # found.
                if new_distance < distances[neighbor]:
                    old_distance = distances[neighbor]

                    # Save the shorter distance.
                    distances[neighbor] = new_distance

                    # Remember how the neighbor was reached.
                    previous[neighbor] = current_vertex

                    # Add the updated route to the priority queue.
                    heapq.heappush(
                        priority_queue,
                        (new_distance, neighbor),
                    )

                    if show_steps:
                        print(
                            "Updated:",
                            old_distance,
                            "->",
                            new_distance,
                        )
                        print(
                            "Previous location:",
                            current_vertex,
                        )
                elif show_steps:
                    print("No update needed.")

            if show_steps:
                queue_view = sorted(priority_queue)
                print("\nPriority queue:", queue_view)
                print("Shortest distances so far:")

                for vertex in sorted(distances):
                    distance = distances[vertex]

                    if distance == float("inf"):
                        distance = "Infinity"

                    print(f"  {vertex}: {distance}")

            step += 1

        if show_steps:
            print("\n" + "=" * 65)
            print("DIJKSTRA COMPLETE")
            print("=" * 65)

        # Return the shortest distances and path information.
        return distances, previous

    def shortest_path(self, start, destination, show_steps=False):
        # Return None when either vertex does not exist.
        if start not in self.graph or destination not in self.graph:
            return None, None

        # Find the shortest distances and previous vertices.
        distances, previous = self.dijkstra(
            start,
            show_steps=show_steps,
        )

        # No path exists when the destination remains infinity.
        if distances[destination] == float("inf"):
            return None, None

        # Reconstruct the path backward from the destination.
        path = []
        current_vertex = destination

        while current_vertex is not None:
            path.append(current_vertex)
            current_vertex = previous[current_vertex]

        # Reverse the path so it begins at the starting vertex.
        path.reverse()

        # Return the path and total distance.
        return path, distances[destination]

    def display(self):
        # Display every vertex in alphabetical order.
        for vertex in sorted(self.graph):
            connections = []

            # Format each neighboring location and road distance.
            for neighbor, weight in sorted(
                self.graph[vertex].items()
            ):
                connections.append(
                    f"{neighbor} ({weight} miles)"
                )

            # Display the vertex and all weighted connections.
            if connections:
                print(f"{vertex}: {', '.join(connections)}")
            else:
                print(f"{vertex}: No connections")


# ============================================================
# CODE EXAMPLE - CAR MEET ROAD NETWORK
# ============================================================
#
# Create a weighted road network.
#
# Each edge weight represents distance in miles.
road_network = WeightedGraph()

# Add roads leaving Home.
road_network.add_edge("Home", "Gas Station", 8)
road_network.add_edge("Home", "Wheel Shop", 12)

# Add roads connected to the Gas Station.
road_network.add_edge("Gas Station", "Parts Store", 5)
road_network.add_edge("Gas Station", "Car Meet", 7)

# Add roads connected to the Wheel Shop.
road_network.add_edge("Wheel Shop", "Parts Store", 4)
road_network.add_edge("Wheel Shop", "Car Meet", 6)

# Add a road from the Parts Store to the Car Meet.
road_network.add_edge("Parts Store", "Car Meet", 9)


# ============================================================
# DISPLAY THE ROAD NETWORK
# ============================================================
print("=" * 65)
print("CAR MEET ROAD NETWORK")
print("=" * 65)
road_network.display()


# ============================================================
# FIND THE SHORTEST PATH
# ============================================================
#
# Find the shortest route from Home to the Car Meet.
#
# show_steps=True displays how Dijkstra's algorithm updates
# the distances and priority queue.
print("\n")
shortest_route, total_distance = road_network.shortest_path(
    "Home",
    "Car Meet",
    show_steps=True,
)


# ============================================================
# DISPLAY THE FINAL RESULT
# ============================================================
print("\n" + "=" * 65)
print("SHORTEST ROUTE RESULT")
print("=" * 65)

if shortest_route is not None:
    print("Starting location: Home")
    print("Destination: Car Meet")
    print("Shortest route:", " -> ".join(shortest_route))
    print("Total distance:", total_distance, "miles")
else:
    print("No route exists from Home to the Car Meet.")


# ============================================================
# DISPLAY EVERY SHORTEST DISTANCE FROM HOME
# ============================================================
#
# Run Dijkstra again without the detailed trace.
distances, previous = road_network.dijkstra("Home")

print("\n" + "=" * 65)
print("SHORTEST DISTANCES FROM HOME")
print("=" * 65)

for location, distance in sorted(distances.items()):
    print(f"Home -> {location}: {distance} miles")


