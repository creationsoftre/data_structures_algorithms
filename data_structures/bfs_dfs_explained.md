# BFS & DFS Explained

Graphs can be searched in different ways. Two common search methods are:

```text
BFS = Breadth-First Search
DFS = Depth-First Search
```

---

## BFS: Breadth-First Search

BFS searches level by level.

A simple way to think about BFS:

```text
Check every nearby room first.
Then move farther out.
```

Example:

```text
Start
 ├── Room A
 ├── Room B
 └── Room C
```

BFS checks:

```text
Start -> Room A -> Room B -> Room C
```

Then it checks the rooms connected to those rooms.

### Mental Model

```text
BFS = search outward in layers
```

### Real-World Example

BFS is useful when you want the **shortest path** in an unweighted graph.

Examples:

```text
Finding the shortest path in a maze
Finding the fewest connections between people
Finding the closest matching result
```

---

## DFS: Depth-First Search

DFS chooses one path and follows it as far as it can.

A simple way to think about DFS:

```text
Pick one hallway and keep going until you cannot go anymore.
Then go back and try another hallway.
```

Example:

```text
Start
 ├── Room A
 │    └── Room D
 │         └── Room E
 └── Room B
```

DFS might check:

```text
Start -> Room A -> Room D -> Room E
```

Then it backs up and checks another path.

### Mental Model

```text
DFS = go deep first, then backtrack
```

### Real-World Example

DFS is useful when you want to fully explore one path before trying another.

Examples:

```text
Solving puzzles
Checking all possible paths
Traversing file folders
Detecting cycles in a graph
```

---

## Quick Difference

```text
BFS checks wide first.
DFS checks deep first.
```

Another way to remember it:

```text
BFS = check your neighbors first
DFS = follow one path first
```

---

## Simple Visual

```text
        Start
       /  |  \
      A   B   C
     /         \
    D           E
```

BFS order:

```text
Start -> A -> B -> C -> D -> E
```

DFS order:

```text
Start -> A -> D -> B -> C -> E
```

The exact DFS order can change depending on which neighbor is picked first.
