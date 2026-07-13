# ============================================================
# Breadth-First Search - High-Level Notes
# ============================================================
#
# DESCRIPTION
# ------------------------------------------------------------
#
# Breadth-First Search visits vertices one level at a time.
#
# It begins at a starting vertex.
#
# It then visits:
#
#   All vertices one edge away
#
#   All vertices two edges away
#
#   All vertices three edges away
#
# This continues until every reachable vertex has been visited.
#
#
# BFS USES A QUEUE
# ------------------------------------------------------------
#
# Breadth-First Search uses a queue.
#
# A queue follows:
#
#   First In, First Out
#
# This is commonly called:
#
#   FIFO
#
# The first vertex added to the queue is the first vertex
# removed and explored.
#
#
# EXAMPLE - AUTOMOTIVE WEBSITE
# ------------------------------------------------------------
#
#                         Home Page
#                        /         \
#                       v           v
#                 Car Parts       Wheels
#                  /    \          /    \
#                 v      v        v      v
#              Brakes  Exhaust  TE37    VSKF
#                                |
#                                v
#                         Shopping Cart
#                                |
#                                v
#                            Checkout
#
# Starting at the Home Page, BFS visits:
#
#   Home Page
#   Car Parts
#   Wheels
#   Brakes
#   Exhaust
#   TE37 Product Page
#   VSKF Product Page
#   Shopping Cart
#   Checkout
#
# BFS visits all nearby pages before moving deeper.
#
#
# WHEN TO USE BFS
# ------------------------------------------------------------
#
# Breadth-First Search is useful for:
#
#   Finding the shortest path in an unweighted graph
#
#   Finding nearby vertices
#
#   Finding the minimum number of edges between vertices
#
#   Searching a graph level by level
#
#
# VISITED SET
# ------------------------------------------------------------
#
# BFS uses a visited set.
#
# The visited set prevents:
#
#   Visiting the same vertex more than once
#
#   Adding duplicate vertices to the queue
#
#   Infinite loops caused by cycles
#
#
# ============================================================
# TIME COMPLEXITY
# ============================================================
#
#   O(V + E)
#
# V represents:
#
#   The number of vertices.
#
# E represents:
#
#   The number of edges.
#
# Each vertex is visited at most once.
#
# Each edge is examined at most once.
#
#
# ============================================================
# SPACE COMPLEXITY
# ============================================================
#
#   O(V)
#
# BFS stores vertices inside:
#
#   A queue
#
#   A visited set
#
#
# ============================================================
# BREADTH-FIRST SEARCH IMPLEMENTATION
# ============================================================
from collections import deque


class Graph:
    def __init__(self):
        # Create an empty adjacency list.
        self.graph = {}

    def add_vertex(self, vertex):
        # Do not add a duplicate vertex.
        if vertex in self.graph:
            return False

        # Add the vertex with an empty neighbor list.
        self.graph[vertex] = []

        # Return True to show that the vertex was added.
        return True

    def add_edge(self, source, destination):
        # Add the source when it does not already exist.
        if source not in self.graph:
            self.add_vertex(source)

        # Add the destination when it does not already exist.
        if destination not in self.graph:
            self.add_vertex(destination)

        # Add a directed edge from source to destination.
        if destination not in self.graph[source]:
            self.graph[source].append(destination)

    def breadth_first_search(self, start):
        # Return an empty list when the starting vertex does
        # not exist.
        if start not in self.graph:
            return []

        # Create a queue containing the starting vertex.
        queue = deque([start])

        # Mark the starting vertex as discovered.
        visited = {start}

        # Store the final visitation order.
        traversal_order = []

        # Track the current search step.
        step = 1

        print("=" * 65)
        print("BREADTH-FIRST SEARCH")
        print("=" * 65)
        print("Starting page:", start)
        print("Search rule: Visit nearby pages before moving deeper.")

        # Continue while vertices remain in the queue.
        while queue:
            print("\n" + "-" * 65)
            print(f"STEP {step}")
            print("-" * 65)

            # Show the queue before removing a vertex.
            print("Queue before visit:", list(queue))

            # Remove the oldest vertex from the front.
            current_vertex = queue.popleft()

            # Visit the removed vertex.
            print("Visiting:", current_vertex)

            # Add the vertex to the final order.
            traversal_order.append(current_vertex)

            # Track the neighbors discovered during this step.
            added_neighbors = []

            # Check each outgoing neighbor.
            for neighbor in self.graph[current_vertex]:
                # Only add neighbors that have not been seen.
                if neighbor not in visited:
                    # Mark the neighbor as visited immediately.
                    visited.add(neighbor)

                    # Add the neighbor to the rear of the queue.
                    queue.append(neighbor)

                    # Record the newly discovered neighbor.
                    added_neighbors.append(neighbor)

            # Display the neighbors discovered during this step.
            if added_neighbors:
                print("Pages added to queue:", added_neighbors)
            else:
                print("Pages added to queue: None")

            # Show the queue after processing the vertex.
            print("Queue after visit:", list(queue))

            # Show the complete visitation order so far.
            print("Visited so far:", traversal_order)

            # Move to the next search step.
            step += 1

        # Display the completed traversal.
        print("\n" + "=" * 65)
        print("BFS COMPLETE")
        print("=" * 65)
        print("Final visit order:")
        print(" -> ".join(traversal_order))

        # Return the visitation order.
        return traversal_order

    def shortest_path(self, start, destination):
        # Return None when either page does not exist.
        if start not in self.graph or destination not in self.graph:
            return None

        # Each queue item stores an entire possible path.
        queue = deque([[start]])

        # Mark the starting page as visited.
        visited = {start}

        print("=" * 65)
        print("SHORTEST PATH USING BFS")
        print("=" * 65)
        print("Starting page:", start)
        print("Destination:", destination)

        # Continue while possible paths remain.
        while queue:
            # Remove the oldest path.
            current_path = queue.popleft()

            # Get the final page in the current path.
            current_vertex = current_path[-1]

            # Display the path being checked.
            print("\nChecking:")
            print(" -> ".join(current_path))

            # Return the path when the destination is reached.
            if current_vertex == destination:
                print("\nDestination found.")
                print("Shortest path:")
                print(" -> ".join(current_path))
                print("Number of links:", len(current_path) - 1)
                return current_path

            # Create new paths using each unvisited neighbor.
            for neighbor in self.graph[current_vertex]:
                if neighbor not in visited:
                    # Mark the neighbor as visited.
                    visited.add(neighbor)

                    # Extend the current path.
                    new_path = current_path + [neighbor]

                    # Add the new path to the queue.
                    queue.append(new_path)

                    # Display the newly discovered path.
                    print(
                        "Added possible path:",
                        " -> ".join(new_path),
                    )

        # No path was found.
        print("\nNo path exists.")
        return None

    def display(self):
        # Display every vertex and its outgoing neighbors.
        for vertex in sorted(self.graph):
            neighbors = self.graph[vertex]

            if neighbors:
                print(f"{vertex} -> {', '.join(neighbors)}")
            else:
                print(f"{vertex} -> None")


# ============================================================
# CODE EXAMPLE - AUTOMOTIVE WEBSITE
# ============================================================

# Create a directed graph representing website navigation.
website = Graph()

# Add links leaving the Home Page.
website.add_edge("Home Page", "Car Parts")
website.add_edge("Home Page", "Wheels")

# Add links leaving the Car Parts page.
website.add_edge("Car Parts", "Brakes")
website.add_edge("Car Parts", "Exhaust")

# Add links leaving the Wheels page.
website.add_edge("Wheels", "TE37 Product Page")
website.add_edge("Wheels", "VSKF Product Page")

# Add links from product pages to the Shopping Cart.
website.add_edge("TE37 Product Page", "Shopping Cart")
website.add_edge("VSKF Product Page", "Shopping Cart")

# Add the final link to Checkout.
website.add_edge("Shopping Cart", "Checkout")

# Display the complete website structure.
print("=" * 65)
print("AUTOMOTIVE WEBSITE STRUCTURE")
print("=" * 65)
website.display()

# Run Breadth-First Search from the Home Page.
print("\n")
website.breadth_first_search("Home Page")

# Find the shortest path from the Home Page to Checkout.
print("\n")
website.shortest_path("Home Page", "Checkout")