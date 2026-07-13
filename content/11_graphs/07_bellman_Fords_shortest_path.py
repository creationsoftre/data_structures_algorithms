# ============================================================
# Bellman-Ford Shortest Path - High-Level Notes
# ============================================================
#
# DESCRIPTION
# ------------------------------------------------------------
#
# The Bellman-Ford algorithm finds the shortest path from one
# starting vertex to every other reachable vertex.
#
# It is used with a weighted graph.
#
# Unlike Dijkstra's algorithm, Bellman-Ford can handle:
#
#   Positive edge weights
#
#   Zero edge weights
#
#   Negative edge weights
#
# Bellman-Ford can also detect a negative-weight cycle.
#
#
# EXAMPLE - AIRLINE TRAVEL COSTS
# ------------------------------------------------------------
#
# A directed weighted graph can represent flights between
# cities.
#
# Each edge weight represents the net cost of a flight.
#
# A positive weight represents:
#
#   Money paid
#
# A negative weight represents:
#
#   A travel credit or rebate
#
# Example:
#
#   Atlanta ------ $120 ------> Charlotte
#
#   Charlotte ----- $80 ------> Washington
#
#   Atlanta ------- $250 -----> Washington
#
#   Charlotte ---- -$30 ------> Raleigh
#
# The flight from Charlotte to Raleigh provides a $30 credit.
#
#
# WHY NEGATIVE WEIGHTS MATTER
# ------------------------------------------------------------
#
# Consider these two routes:
#
# Direct route:
#
#   Atlanta -> Washington
#
# Cost:
#
#   $250
#
# Connecting route:
#
#   Atlanta -> Charlotte -> Raleigh -> Washington
#
# Costs:
#
#   Atlanta -> Charlotte:
#
#       $120
#
#   Charlotte -> Raleigh:
#
#       -$30 travel credit
#
#   Raleigh -> Washington:
#
#       $70
#
# Total cost:
#
#   120 + (-30) + 70 = $160
#
# Bellman-Ford finds the $160 route because it considers the
# negative travel credit.
#
#
# DIRECTED WEIGHTED GRAPH
# ------------------------------------------------------------
#
# This example uses a directed weighted graph.
#
# A flight from Atlanta to Charlotte does not automatically
# create a flight from Charlotte back to Atlanta.
#
# Example:
#
#   Atlanta -> Charlotte
#
# does not automatically mean:
#
#   Charlotte -> Atlanta
#
# Each direction must be added separately.
#
#
# HOW BELLMAN-FORD WORKS
# ------------------------------------------------------------
#
# Bellman-Ford repeatedly checks every edge in the graph.
#
# Checking an edge to find a shorter path is called:
#
#   Relaxation
#
# The algorithm performs these main steps:
#
#   1. Set the starting vertex's distance to 0.
#
#   2. Set every other distance to infinity.
#
#   3. Relax every edge V - 1 times.
#
#   4. Check every edge one more time.
#
#   5. If another update is possible, a negative cycle exists.
#
#
# STARTING DISTANCES
# ------------------------------------------------------------
#
# Starting city:
#
#   Atlanta
#
# Initial distances:
#
#   Atlanta:
#       0
#
#   Charlotte:
#       Infinity
#
#   Raleigh:
#       Infinity
#
#   Washington:
#       Infinity
#
# Infinity means no route has been discovered yet.
#
#
# RELAXING AN EDGE
# ------------------------------------------------------------
#
# Relaxing an edge means checking whether traveling through
# the current vertex creates a cheaper route.
#
# Formula:
#
#   New cost =
#
#       Current cost + Edge weight
#
# Example:
#
# Known cost to Atlanta:
#
#   $0
#
# Flight:
#
#   Atlanta -> Charlotte
#
# Flight cost:
#
#   $120
#
# Possible cost to Charlotte:
#
#   0 + 120 = $120
#
# Because $120 is less than infinity, Charlotte's distance is
# updated.
#
#
# WHY V - 1 PASSES?
# ------------------------------------------------------------
#
# V represents the number of vertices.
#
# A shortest path without a cycle can contain at most:
#
#   V - 1 edges
#
# Each complete pass allows shorter path information to move
# farther through the graph.
#
#
# EARLY STOPPING
# ------------------------------------------------------------
#
# Bellman-Ford can stop early when an entire pass finishes
# without updating any distance.
#
# No updates mean:
#
#   Every shortest distance has already been found.
#
#
# NEGATIVE-WEIGHT CYCLE
# ------------------------------------------------------------
#
# A negative-weight cycle is a loop whose total weight is
# negative.
#
# Example:
#
#   City A -> City B:
#       $20
#
#   City B -> City C:
#       -$50
#
#   City C -> City A:
#       $10
#
# Total:
#
#   20 + (-50) + 10 = -20
#
# Each trip around the cycle lowers the total cost by $20.
#
# This means there is no final shortest cost because the route
# can continue becoming cheaper.
#
# Bellman-Ford detects this problem.
#
#
# BELLMAN-FORD VS. DIJKSTRA
# ------------------------------------------------------------
#
#   Bellman-Ford                 Dijkstra
#   ----------------------------------------------------------
#   Supports negative weights   Does not support negative
#                               weights
#
#   Detects negative cycles     Does not detect negative
#                               cycles
#
#   Usually slower              Usually faster
#
#   Checks every edge           Uses a priority queue
#   repeatedly
#
#
# MAIN OPERATIONS
# ------------------------------------------------------------
#
# add_vertex(vertex)
#     Adds a new vertex to the graph.
#
# add_edge(source, destination, weight)
#     Adds a directed weighted edge.
#
# bellman_ford(start)
#     Finds the shortest cost from the starting vertex to every
#     reachable vertex.
#
# shortest_path(start, destination)
#     Returns the cheapest path and its total cost.
#
# display()
#     Displays every directed weighted edge.
#
#
# ============================================================
# TIME COMPLEXITY
# ============================================================
#
#   O(V * E)
#
# V represents:
#
#   The number of vertices.
#
# E represents:
#
#   The number of edges.
#
# Every edge may be checked during each of the V - 1 passes.
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
#   Every vertex
#
#   Every directed weighted edge
#
# The algorithm also stores:
#
#   A distance dictionary
#
#   A previous-vertex dictionary
#
#
# ============================================================
# BELLMAN-FORD IMPLEMENTATION
# ============================================================
class WeightedDirectedGraph:
    def __init__(self):
        # Store every vertex in a set.
        self.vertices = set()
#
        # Store every directed weighted edge.
        #
        # Each edge is stored as:
        #
        #   (source, destination, weight)
        self.edges = []
#
    def add_vertex(self, vertex):
        # Do not add a duplicate vertex.
        if vertex in self.vertices:
            return False
#
        # Add the vertex to the graph.
        self.vertices.add(vertex)
#
        # Return True to show that the vertex was added.
        return True
#
    def add_edge(self, source, destination, weight):
        # Add the source when it does not already exist.
        if source not in self.vertices:
            self.add_vertex(source)
#
        # Add the destination when it does not already exist.
        if destination not in self.vertices:
            self.add_vertex(destination)
#
        # Store the directed weighted edge.
        self.edges.append((source, destination, weight))
#
    def bellman_ford(self, start, show_steps=False):
        # Return empty results when the starting vertex does
        # not exist.
        if start not in self.vertices:
            return {}, {}, False
#
        # Give every vertex an initial distance of infinity.
        distances = {
            vertex: float("inf")
            for vertex in self.vertices
        }
#
        # The starting vertex has a cost of zero.
        distances[start] = 0
#
        # Store the previous vertex used to reach each vertex.
        previous = {
            vertex: None
            for vertex in self.vertices
        }
#
        # The algorithm performs at most V - 1 passes.
        pass_count = len(self.vertices) - 1
#
        if show_steps:
            print("=" * 70)
            print("BELLMAN-FORD ALGORITHM TRACE")
            print("=" * 70)
            print("Starting city:", start)
            print("Maximum passes:", pass_count)
#
        # Repeat the relaxation process V - 1 times.
        for current_pass in range(1, pass_count + 1):
            # Track whether any distance changed.
            updated = False
#
            if show_steps:
                print("\n" + "=" * 70)
                print(f"PASS {current_pass}")
                print("=" * 70)
#
            # Check every directed edge.
            for source, destination, weight in self.edges:
                # A route cannot continue from an unreachable
                # source vertex.
                if distances[source] == float("inf"):
                    if show_steps:
                        print(
                            f"{source} -> {destination} "
                            f"({weight:+})"
                        )
                        print("Skipped: Source is not reachable yet.")
#
                    continue
#
                # Calculate the cost of traveling through the
                # source vertex.
                possible_cost = distances[source] + weight
#
                if show_steps:
                    print(
                        f"{source} -> {destination} "
                        f"({weight:+})"
                    )
                    print(
                        "Current source cost:",
                        distances[source],
                    )
                    print(
                        "Possible destination cost:",
                        possible_cost,
                    )
#
                    known_cost = distances[destination]
#
                    if known_cost == float("inf"):
                        known_cost = "Infinity"
#
                    print("Known destination cost:", known_cost)
#
                # Update the destination when a cheaper route
                # has been found.
                if possible_cost < distances[destination]:
                    old_cost = distances[destination]
#
                    # Save the cheaper cost.
                    distances[destination] = possible_cost
#
                    # Remember how the destination was reached.
                    previous[destination] = source
#
                    # Record that this pass changed a distance.
                    updated = True
#
                    if show_steps:
                        if old_cost == float("inf"):
                            old_cost = "Infinity"
#
                        print(
                            "Updated:",
                            old_cost,
                            "->",
                            possible_cost,
                        )
                        print("Previous city:", source)
                elif show_steps:
                    print("No update needed.")
#
                if show_steps:
                    print("-" * 70)
#
            if show_steps:
                print("Distances after this pass:")
#
                for vertex in sorted(self.vertices):
                    distance = distances[vertex]
#
                    if distance == float("inf"):
                        distance = "Infinity"
#
                    print(f"  {vertex}: {distance}")
#
            # Stop early when no distances changed.
            if not updated:
                if show_steps:
                    print("\nNo distances changed.")
                    print("The shortest costs are complete.")
#
                break
#
        # Check every edge one more time for a negative cycle.
        negative_cycle = False
#
        for source, destination, weight in self.edges:
            # Skip unreachable source vertices.
            if distances[source] == float("inf"):
                continue
#
            # Another possible update means a negative cycle
            # is reachable from the starting vertex.
            if (
                distances[source] + weight
                < distances[destination]
            ):
                negative_cycle = True
                break
#
        if show_steps:
            print("\n" + "=" * 70)
            print("NEGATIVE-CYCLE CHECK")
            print("=" * 70)
#
            if negative_cycle:
                print("Negative-weight cycle detected.")
                print("Shortest paths are not reliable.")
            else:
                print("No negative-weight cycle detected.")
#
        # Return the results and cycle status.
        return distances, previous, negative_cycle
#
    def shortest_path(
        self,
        start,
        destination,
        show_steps=False,
    ):
        # Return empty results when either vertex does not
        # exist.
        if (
            start not in self.vertices
            or destination not in self.vertices
        ):
            return None, None, False
#
        # Run the Bellman-Ford algorithm.
        distances, previous, negative_cycle = self.bellman_ford(
            start,
            show_steps=show_steps,
        )
#
        # A reliable shortest path cannot be returned when a
        # reachable negative cycle exists.
        if negative_cycle:
            return None, None, True
#
        # Return no path when the destination is unreachable.
        if distances[destination] == float("inf"):
            return None, None, False
#
        # Reconstruct the path from destination to start.
        path = []
        current_vertex = destination
#
        while current_vertex is not None:
            path.append(current_vertex)
            current_vertex = previous[current_vertex]
#
        # Reverse the path so it begins at the starting city.
        path.reverse()
#
        # Return the path, total cost, and cycle status.
        return path, distances[destination], False
#
    def display(self):
        # Sort edges to produce consistent output.
        sorted_edges = sorted(
            self.edges,
            key=lambda edge: (edge[0], edge[1]),
        )
#
        # Display each directed weighted connection.
        for source, destination, weight in sorted_edges:
            # Describe negative weights as travel credits.
            if weight < 0:
                print(
                    f"{source} -> {destination}: "
                    f"${abs(weight)} credit"
                )
            else:
                print(
                    f"{source} -> {destination}: "
                    f"${weight} cost"
                )
#
#
# ============================================================
# CODE EXAMPLE - AIRLINE TRAVEL COSTS
# ============================================================
#
# Create a directed weighted graph for airline routes.
#
# Positive weights represent ticket costs.
#
# Negative weights represent travel credits.
flight_network = WeightedDirectedGraph()
#
# Add flights leaving Atlanta.
flight_network.add_edge("Atlanta", "Charlotte", 120)
flight_network.add_edge("Atlanta", "Washington", 250)
flight_network.add_edge("Atlanta", "Raleigh", 180)
#
# Add flights leaving Charlotte.
flight_network.add_edge("Charlotte", "Washington", 80)
#
# This flight provides a $30 travel credit.
flight_network.add_edge("Charlotte", "Raleigh", -30)
#
# Add flights leaving Raleigh.
flight_network.add_edge("Raleigh", "Washington", 70)
flight_network.add_edge("Raleigh", "Richmond", 60)
#
# Add a flight from Richmond to Washington.
flight_network.add_edge("Richmond", "Washington", 40)
#
#
# ============================================================
# DISPLAY THE FLIGHT NETWORK
# ============================================================
print("=" * 70)
print("AIRLINE TRAVEL COST NETWORK")
print("=" * 70)
flight_network.display()
#
#
# ============================================================
# FIND THE CHEAPEST ROUTE
# ============================================================
#
# Find the cheapest route from Atlanta to Washington.
#
# show_steps=True displays every relaxation pass.
print("\n")
cheapest_route, total_cost, negative_cycle = (
    flight_network.shortest_path(
        "Atlanta",
        "Washington",
        show_steps=True,
    )
)
#
#
# ============================================================
# DISPLAY THE FINAL RESULT
# ============================================================
print("\n" + "=" * 70)
print("CHEAPEST ROUTE RESULT")
print("=" * 70)
#
if negative_cycle:
    print("A negative-weight cycle affects the route.")
    print("A reliable cheapest route cannot be calculated.")
elif cheapest_route is None:
    print("No route exists from Atlanta to Washington.")
else:
    print("Starting city: Atlanta")
    print("Destination: Washington")
    print("Cheapest route:", " -> ".join(cheapest_route))
    print("Total cost:", f"${total_cost}")
#
#
# ============================================================
# DISPLAY EVERY SHORTEST COST FROM ATLANTA
# ============================================================
distances, previous, negative_cycle = (
    flight_network.bellman_ford("Atlanta")
)
#
print("\n" + "=" * 70)
print("LOWEST TRAVEL COSTS FROM ATLANTA")
print("=" * 70)
#
for city in sorted(distances):
    cost = distances[city]
#
    if cost == float("inf"):
        print(f"Atlanta -> {city}: Unreachable")
    else:
        print(f"Atlanta -> {city}: ${cost}")
