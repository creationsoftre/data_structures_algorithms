# ============================================================
# Depth-First Search - High-Level Notes
# ============================================================
#
# DESCRIPTION
# ------------------------------------------------------------
#
# Depth-First Search follows one path as deeply as possible
# before returning to explore another path.
#
# It begins at a starting vertex.
#
# It then visits:
#
#   One unvisited neighbor
#
#   One of that neighbor's unvisited neighbors
#
#   The next unvisited neighbor deeper in the graph
#
# When the search reaches a vertex with no unvisited neighbors,
# it backtracks.
#
#
# DFS USES A STACK
# ------------------------------------------------------------
#
# Depth-First Search uses a stack.
#
# A stack follows:
#
#   Last In, First Out
#
# This is commonly called:
#
#   LIFO
#
# The most recently added vertex is the first vertex removed
# and explored.
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
# One possible DFS visitation order is:
#
#   Home Page
#   Car Parts
#   Brakes
#   Exhaust
#   Wheels
#   TE37 Product Page
#   Shopping Cart
#   Checkout
#   VSKF Product Page
#
# DFS explores one website section deeply before returning
# to another section.
#
#
# WHEN TO USE DFS
# ------------------------------------------------------------
#
# Depth-First Search is useful for:
#
#   Exploring every reachable vertex
#
#   Checking whether a path exists
#
#   Detecting cycles
#
#   Finding connected components
#
#   Solving mazes
#
#   Exploring dependency paths
#
#   Topological sorting
#
# DFS can find a path between two vertices.
#
# However, DFS does not guarantee the shortest path.
#
#
# VISITED SET
# ------------------------------------------------------------
#
# DFS uses a visited set.
#
# The visited set prevents:
#
#   Visiting the same vertex more than once
#
#   Adding duplicate work
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
# DFS stores vertices inside:
#
#   A stack
#
#   A visited set
#
#
# ============================================================
# DEPTH-FIRST SEARCH IMPLEMENTATION
# ============================================================
class Graph:
    def __init__(self):
        # Create an empty adjacency list.
        self.graph = {}
#
    def add_vertex(self, vertex):
        # Do not add a duplicate vertex.
        if vertex in self.graph:
            return False
#
        # Add the vertex with an empty neighbor list.
        self.graph[vertex] = []
#
        # Return True to show that the vertex was added.
        return True
#
    def add_edge(self, source, destination):
        # Add the source when it does not already exist.
        if source not in self.graph:
            self.add_vertex(source)
#
        # Add the destination when it does not already exist.
        if destination not in self.graph:
            self.add_vertex(destination)
#
        # Add a directed edge from source to destination.
        if destination not in self.graph[source]:
            self.graph[source].append(destination)
#
    def depth_first_search(self, start):
        # Return an empty list when the starting vertex does
        # not exist.
        if start not in self.graph:
            return []
#
        # Create a stack containing the starting vertex.
        stack = [start]
#
        # Create a set to track visited vertices.
        visited = set()
#
        # Store the final visitation order.
        traversal_order = []
#
        # Track the current search step.
        step = 1
#
        print("=" * 65)
        print("DEPTH-FIRST SEARCH")
        print("=" * 65)
        print("Starting page:", start)
        print("Search rule: Follow one path deeply, then backtrack.")
#
        # Continue while vertices remain in the stack.
        while stack:
            print("\n" + "-" * 65)
            print(f"STEP {step}")
            print("-" * 65)
#
            # Show the stack before removing a vertex.
            print("Stack before visit:", stack)
#
            # Remove the newest vertex from the top.
            current_vertex = stack.pop()
#
            # Skip the vertex when it was already visited.
            if current_vertex in visited:
                print("Skipping already visited page:", current_vertex)
                print("Stack after skip:", stack)
                step += 1
                continue
#
            # Visit the removed vertex.
            print("Visiting:", current_vertex)
#
            # Mark the vertex as visited.
            visited.add(current_vertex)
#
            # Add the vertex to the final order.
            traversal_order.append(current_vertex)
#
            # Track the neighbors added during this step.
            added_neighbors = []
#
            # Add neighbors in reverse order.
            #
            # The stack removes the last item first.
            #
            # Reversing the neighbors allows the first listed
            # neighbor to be visited first.
            for neighbor in reversed(self.graph[current_vertex]):
                if neighbor not in visited:
                    # Add the neighbor to the top of the stack.
                    stack.append(neighbor)
#
                    # Record the neighbor added during this step.
                    added_neighbors.append(neighbor)
#
            # Display the neighbors pushed onto the stack.
            if added_neighbors:
                print("Pages pushed onto stack:", added_neighbors)
            else:
                print("Pages pushed onto stack: None")
#
            # Show the stack after processing the vertex.
            print("Stack after visit:", stack)
#
            # Show the visitation order so far.
            print("Visited so far:", traversal_order)
#
            # Move to the next step.
            step += 1
#
        # Display the completed traversal.
        print("\n" + "=" * 65)
        print("DFS COMPLETE")
        print("=" * 65)
        print("Final visit order:")
        print(" -> ".join(traversal_order))
#
        # Return the visitation order.
        return traversal_order
#
    def find_path(self, start, destination):
        # Return None when either page does not exist.
        if start not in self.graph or destination not in self.graph:
            return None
#
        # Each stack item stores a complete possible path.
        stack = [[start]]
#
        # Track visited pages.
        visited = set()
#
        print("=" * 65)
        print("FIND PATH USING DFS")
        print("=" * 65)
        print("Starting page:", start)
        print("Destination:", destination)
#
        # Continue while possible paths remain.
        while stack:
            # Remove the newest path from the stack.
            current_path = stack.pop()
#
            # Get the final page in the current path.
            current_vertex = current_path[-1]
#
            # Skip paths ending at an already visited page.
            if current_vertex in visited:
                continue
#
            # Mark the current page as visited.
            visited.add(current_vertex)
#
            # Display the path currently being explored.
            print("\nExploring:")
            print(" -> ".join(current_path))
#
            # Return the path when the destination is reached.
            if current_vertex == destination:
                print("\nDestination found.")
                print("Path:")
                print(" -> ".join(current_path))
                print("Number of links:", len(current_path) - 1)
                return current_path
#
            # Add new paths in reverse neighbor order.
            for neighbor in reversed(self.graph[current_vertex]):
                if neighbor not in visited:
                    # Extend the current path.
                    new_path = current_path + [neighbor]
#
                    # Add the new path to the stack.
                    stack.append(new_path)
#
                    # Display the new possible path.
                    print(
                        "Added possible path:",
                        " -> ".join(new_path),
                    )
#
        # No path was found.
        print("\nNo path exists.")
        return None
#
    def has_path(self, start, destination):
        # Return False when either page does not exist.
        if start not in self.graph or destination not in self.graph:
            return False
#
        # Create a stack containing the starting vertex.
        stack = [start]
#
        # Track visited vertices.
        visited = set()
#
        # Continue while vertices remain in the stack.
        while stack:
            # Remove the top vertex.
            current_vertex = stack.pop()
#
            # Skip vertices already visited.
            if current_vertex in visited:
                continue
#
            # Return True when the destination is found.
            if current_vertex == destination:
                return True
#
            # Mark the current vertex as visited.
            visited.add(current_vertex)
#
            # Add unvisited neighbors to the stack.
            for neighbor in reversed(self.graph[current_vertex]):
                if neighbor not in visited:
                    stack.append(neighbor)
#
        # Return False when the destination cannot be reached.
        return False
#
    def display(self):
        # Display every vertex and its outgoing neighbors.
        for vertex in sorted(self.graph):
            neighbors = self.graph[vertex]
#
            if neighbors:
                print(f"{vertex} -> {', '.join(neighbors)}")
            else:
                print(f"{vertex} -> None")
#
#
# ============================================================
# CODE EXAMPLE - AUTOMOTIVE WEBSITE
# ============================================================
#
# Create a directed graph representing website navigation.
website = Graph()
#
# Add links leaving the Home Page.
website.add_edge("Home Page", "Car Parts")
website.add_edge("Home Page", "Wheels")
#
# Add links leaving the Car Parts page.
website.add_edge("Car Parts", "Brakes")
website.add_edge("Car Parts", "Exhaust")
#
# Add links leaving the Wheels page.
website.add_edge("Wheels", "TE37 Product Page")
website.add_edge("Wheels", "VSKF Product Page")
#
# Add links from product pages to the Shopping Cart.
website.add_edge("TE37 Product Page", "Shopping Cart")
website.add_edge("VSKF Product Page", "Shopping Cart")
#
# Add the final link to Checkout.
website.add_edge("Shopping Cart", "Checkout")
#
# Display the complete website structure.
print("=" * 65)
print("AUTOMOTIVE WEBSITE STRUCTURE")
print("=" * 65)
website.display()
#
# Run Depth-First Search from the Home Page.
print("\n")
website.depth_first_search("Home Page")
#
# Use DFS to find one path from Home Page to Checkout.
print("\n")
website.find_path("Home Page", "Checkout")
#
# Check whether specific directed paths exist.
print("\n" + "=" * 65)
print("PATH CHECKS")
print("=" * 65)
print(
    "Home Page can reach VSKF Product Page:",
    website.has_path("Home Page", "VSKF Product Page"),
)
print(
    "Checkout can reach Home Page:",
    website.has_path("Checkout", "Home Page"),
)