# ============================================================
# Shortest Path in an Unweighted Graph
# ============================================================
#
# Shortest path means:
#
#   Find the path from a start node to a target node
#   using the fewest number of steps.
#
# This example uses an unweighted graph.
#
# Unweighted means:
#
#   Every connection has the same cost.
#
# Example graph:
#
#        A
#      /   \
#     B     C
#     |     |
#     D --- E
#      \   /
#        F
#
# Graph as an adjacency list:
#
#   A -> B, C
#   B -> A, D
#   C -> A, E
#   D -> B, E, F
#   E -> C, D, F
#   F -> D, E
#
# Shortest path from A to F:
#
#   A -> B -> D -> F
#
# or
#
#   A -> C -> E -> F
#
# Both paths have 3 steps.
#
# ------------------------------------------------------------
# BIG O / SPEED
# ------------------------------------------------------------
#
# Time Complexity:
#   O(V + E)
#
# Speed:
#   Usually fast for normal graph searches.
#
# Why?
#   BFS may check every vertex and every edge once.
#
#   V = vertices/nodes
#   E = edges/connections
#
# ------------------------------------------------------------
# SPACE COMPLEXITY
# ------------------------------------------------------------
#
# Space Complexity:
#   O(V)
#
# Why?
#   We store visited nodes, previous nodes, and a queue.
#
# ------------------------------------------------------------
# IMPORTANT NOTE
# ------------------------------------------------------------
#
# BFS works for shortest path when the graph is unweighted.
#
# If the graph has weighted edges, use a different algorithm.
#
# Example weighted graph:
#
#   A --5-- B
#   A --1-- C
#
# In a weighted graph, the shortest path may not be the path
# with the fewest steps.
#
# For weighted graphs, Dijkstra's algorithm is usually used.
# ============================================================


# ------------------------------------------------------------
# Step 1: Create the graph
# ------------------------------------------------------------
#
# We will use an adjacency list.
#
# An adjacency list stores each node and the nodes connected to it.
# ------------------------------------------------------------

graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "E"],
    "D": ["B", "E", "F"],
    "E": ["C", "D", "F"],
    "F": ["D", "E"]
}


# ------------------------------------------------------------
# Step 2: Find the shortest path using BFS
# ------------------------------------------------------------
#
# BFS means Breadth-First Search.
#
# BFS checks nodes level by level.
#
# That makes BFS useful for shortest path in an unweighted graph.
#
# Example:
#
#   Start at A.
#
#   Step 0:
#       A
#
#   Step 1:
#       B, C
#
#   Step 2:
#       D, E
#
#   Step 3:
#       F
#
# The first time BFS reaches the target, it has found the
# shortest path.
# ------------------------------------------------------------

def shortest_path(graph, start, target):
    # Queue stores the paths we still need to explore.
    #
    # We start with a path that only contains the start node.
    queue = [[start]]

    # Visited stores nodes we have already checked.
    visited = set()

    # Keep searching while there are paths in the queue.
    while queue:

        # Remove the first path from the queue.
        path = queue.pop(0)

        # Get the last node in the current path.
        current = path[-1]

        # If we already checked this node, skip it.
        if current in visited:
            continue

        # Mark the current node as visited.
        visited.add(current)

        # If the current node is the target, return the path.
        if current == target:
            return path

        # Check each neighbor connected to the current node.
        for neighbor in graph[current]:

            # Only build a new path if the neighbor was not visited.
            if neighbor not in visited:

                # Create a new path by adding the neighbor.
                new_path = path + [neighbor]

                # Add the new path to the queue.
                queue.append(new_path)

    # If the loop ends, there is no path to the target.
    return None


# ------------------------------------------------------------
# Step 3: Shortest path with trace
# ------------------------------------------------------------
#
# This version prints what BFS is doing.
#
# It helps us see:
#
#   Which path is being checked
#   Which neighbors are discovered
#   When the target is found
# ------------------------------------------------------------

def shortest_path_with_trace(graph, start, target):
    queue = [[start]]
    visited = set()

    print(f"Finding shortest path from {start} to {target}")
    print("-" * 40)

    while queue:
        path = queue.pop(0)
        current = path[-1]

        print(f"Checking path: {path}")

        if current in visited:
            print(f"{current} was already visited. Skip it.")
            print()
            continue

        visited.add(current)

        if current == target:
            print(f"Found target: {target}")
            print(f"Shortest path: {path}")
            return path

        print(f"Current node: {current}")
        print(f"Neighbors: {graph[current]}")

        for neighbor in graph[current]:
            if neighbor not in visited:
                new_path = path + [neighbor]
                print(f"Add new path to queue: {new_path}")
                queue.append(new_path)

        print(f"Queue now: {queue}")
        print()

    print(f"No path found from {start} to {target}")
    return None


# ------------------------------------------------------------
# Step 4: Test shortest path
# ------------------------------------------------------------

start = "A"
target = "F"

print("Shortest Path Example")
print("-" * 40)

print("Graph:")
for node, neighbors in graph.items():
    print(f"  {node} -> {neighbors}")

print()
print(f"Goal: Find the shortest path from {start} to {target}")
print()

path = shortest_path(graph, start, target)

print(f"Shortest path: {path}")

print()
shortest_path_with_trace(graph, start, target)