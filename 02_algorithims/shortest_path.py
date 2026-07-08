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
# BFS finds the shortest path by checking paths level by level.
#
# If more than one shortest path exists, the path returned depends
# on the order of the neighbors in the graph.
#
# In this graph, A lists B before C:
#
#   "A": ["B", "C"]
#
# So BFS checks the B side first and finds:
#
#   A -> B -> D -> F
#
# If A listed C before B, BFS may find:
#
#   A -> C -> E -> F
#
# Both paths are valid because they have the same number of steps.


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
    print("BFS checks paths in the order they are added to the queue.")
    print("The first time we reach the target, that path is the shortest.")
    print("-" * 40)
    print()

    while queue:
        path = queue.pop(0)
        current = path[-1]

        print(f"Current path being checked: {path}")
        print(f"Current node: {current}")

        if current in visited:
            print(f"{current} was already visited, so we skip this path.")
            print()
            continue

        visited.add(current)

        if current == target:
            print(f"{current} is the target.")
            print("Because BFS checks shortest paths first, this is the shortest path.")
            return path

        print(f"{current} is not the target.")
        print(f"Now we look at {current}'s neighbors: {graph[current]}")

        for neighbor in graph[current]:
            if neighbor not in visited:
                new_path = path + [neighbor]

                print()
                print(f"Why add {neighbor}?")
                print(f"{neighbor} is connected to {current}.")
                print(f"So we create a new possible path: {new_path}")

                queue.append(new_path)
            else:
                print()
                print(f"Why skip {neighbor}?")
                print(f"{neighbor} was already visited.")

        print()
        print(f"Queue after checking {current}:")
        for queued_path in queue:
            print(f"  {queued_path}")

        print("-" * 40)
        print()

    print(f"No path found from {start} to {target}")
    return None


# ------------------------------------------------------------
# Step 4: Test shortest path
# ------------------------------------------------------------

start = "A"
target = "F"

print("Shortest Path Example")
print("=" * 40)

print("Graph:")
for node, neighbors in graph.items():
    print(f"  {node} -> {neighbors}")

print()
print(f"Goal: Find the shortest path from {start} to {target}")
print()


# ------------------------------------------------------------
# Regular shortest path result
# ------------------------------------------------------------

print("Regular Shortest Path Result")
print("-" * 40)

path = shortest_path(graph, start, target)

print(f"Shortest path from {start} to {target}: {path}")


# ------------------------------------------------------------
# Trace shortest path result
# ------------------------------------------------------------

print()
print("Trace: How BFS Finds the Shortest Path")
print("-" * 40)

trace_path = shortest_path_with_trace(graph, start, target)

print()
print("Trace Result")
print("-" * 40)
print(f"Shortest path from {start} to {target}: {trace_path}")