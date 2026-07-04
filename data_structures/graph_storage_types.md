# Graph Storage Types

Graphs can be stored in different ways depending on what you need the graph to do.

A graph is made of:

* **Vertices / Nodes**: the things in the graph
* **Edges / Connections**: the relationships between those things

Example:

```text
Volk Racing TE37 ----- Toyota Supra
BBS LM --------------- Toyota Supra
Work VSKF ------------ Nissan 240SX
```

In this project:

```text
Nodes = wheels and cars
Edges = fitment or compatibility connections
```

---

## 1. Adjacency List

An adjacency list stores each node with a list or set of its neighbors.

This is the version used in `07_graph.py`.

```python
graph = {
    "Volk Racing TE37": {"Nissan 350Z", "Toyota Supra", "Mazda RX-7"},
    "BBS LM": {"Toyota Supra", "BMW E46"},
    "Work VSKF": {"Nissan 240SX", "Lexus IS300"}
}
```

### Visual

```text
Volk Racing TE37
    ├── Nissan 350Z
    ├── Toyota Supra
    └── Mazda RX-7

BBS LM
    ├── Toyota Supra
    └── BMW E46

Work VSKF
    ├── Nissan 240SX
    └── Lexus IS300
```

### Time Complexity

```text
Add node:              O(1)
Add edge:              O(1) average with sets
Check if node exists:  O(1)
Get neighbors:         O(1)
Check if edge exists:  O(1) average with sets
BFS/DFS traversal:     O(V + E)
Space complexity:      O(V + E)
```

### Best Use Case

Use an adjacency list when the graph is **sparse**.

Sparse means there are not too many connections compared to the number of nodes.

Good for:

```text
Social networks
Maps
Recommendation systems
Dependency graphs
Computer networks
Most real-world graph problems
```

### Why We Used It

The wheel fitment graph does not need every wheel connected to every car.

Only some wheels connect to some cars.

That makes an adjacency list a good fit.

---

## 2. Adjacency Matrix

An adjacency matrix stores graph connections in a 2D table.

Each row and column represents a node.

A `1` means connected.

A `0` means not connected.

### Example Nodes

```text
0 = Volk Racing TE37
1 = Toyota Supra
2 = BBS LM
3 = Nissan 350Z
```

### Matrix

```text
                    TE37   Supra   BBS LM   350Z
Volk Racing TE37      0      1       0       1
Toyota Supra          1      0       1       0
BBS LM                0      1       0       0
Nissan 350Z           1      0       0       0
```

### Visual

```text
Volk Racing TE37 ----- Toyota Supra ----- BBS LM
        |
        |
   Nissan 350Z
```

### Time Complexity

```text
Add node:              O(V^2)
Add edge:              O(1)
Check if edge exists:  O(1)
Get all neighbors:     O(V)
BFS/DFS traversal:     O(V^2)
Space complexity:      O(V^2)
```

### Best Use Case

Use an adjacency matrix when the graph is **dense**.

Dense means many nodes are connected to many other nodes.

Good for:

```text
Small graphs with many connections
Fast edge checks
Math-heavy graph problems
Relationship tables
Dense network maps
```

### Tradeoff

Adjacency matrices are fast for checking if two nodes are connected, but they use more memory.

Even if two nodes are not connected, the matrix still stores a `0`.

---

## 3. Edge List

An edge list stores only the connections.

Each edge is stored as a pair.

```python
edges = [
    ("Volk Racing TE37", "Nissan 350Z"),
    ("Volk Racing TE37", "Toyota Supra"),
    ("BBS LM", "Toyota Supra"),
    ("Work VSKF", "Nissan 240SX")
]
```

### Visual

```text
Each row is one connection:

Volk Racing TE37 ----- Nissan 350Z
Volk Racing TE37 ----- Toyota Supra
BBS LM --------------- Toyota Supra
Work VSKF ------------ Nissan 240SX
```

### Time Complexity

```text
Add edge:              O(1)
Check if edge exists:  O(E)
Get all neighbors:     O(E)
BFS/DFS traversal:     O(V * E) if used directly
Space complexity:      O(E)
```

### Best Use Case

Use an edge list when you mainly care about the connections themselves.

Good for:

```text
Importing graph data
Exporting graph data
CSV-style storage
Simple relationship lists
Algorithms that process edges directly
Minimum spanning tree algorithms
```

### Tradeoff

Edge lists are simple, but they are not great for quickly finding all neighbors of a node.

To find everything connected to `"Volk Racing TE37"`, you may need to scan the whole list.

---

## 4. Incidence Matrix

An incidence matrix shows which nodes belong to which edges.

Rows are nodes.

Columns are edges.

### Example Edges

```text
Edge 0 = Volk Racing TE37 -- Toyota Supra
Edge 1 = Toyota Supra -- BBS LM
Edge 2 = Volk Racing TE37 -- Nissan 350Z
```

### Matrix

```text
                    Edge 0   Edge 1   Edge 2
Volk Racing TE37       1        0        1
Toyota Supra           1        1        0
BBS LM                 0        1        0
Nissan 350Z            0        0        1
```

### Visual

```text
Volk Racing TE37 ----- Toyota Supra ----- BBS LM
        |
        |
   Nissan 350Z
```

### Time Complexity

```text
Add edge:                         O(V)
Check if two nodes are connected: O(E)
Get all edges for a node:         O(E)
BFS/DFS traversal:                Usually inefficient compared to adjacency lists
Space complexity:                 O(V * E)
```

### Best Use Case

Use an incidence matrix when you care about the relationship between nodes and edges.

Good for:

```text
Graph theory
Network flow
Electrical network modeling
Math-heavy graph analysis
Specialized graph algorithms
```

### Tradeoff

Incidence matrices are useful in theory and certain algorithms, but they are not usually the first choice for everyday application code.

---

# Quick Comparison

| Storage Type     | Best For                    |    Space | Fast Edge Check |          Good for BFS/DFS |
| ---------------- | --------------------------- | -------: | --------------: | ------------------------: |
| Adjacency List   | Most real-world graphs      | O(V + E) |  Yes, with sets |                       Yes |
| Adjacency Matrix | Dense graphs                |    O(V²) |             Yes | Okay, but can be wasteful |
| Edge List        | Simple connection storage   |     O(E) |              No |              Not directly |
| Incidence Matrix | Graph theory / network flow | O(V * E) |              No |               Not usually |

---

# Which One Should I Use?

For most projects, start with an **adjacency list**.

Use this when:

```text
You need to find neighbors quickly
You need BFS or DFS
The graph is not fully connected
You want clean, readable code
```

Use an **adjacency matrix** when:

```text
The graph is small
The graph is dense
You need very fast checks like "are these two nodes connected?"
```

Use an **edge list** when:

```text
You are importing or exporting graph data
You are storing relationships in a simple format
You are working with algorithms that process edges directly
```

Use an **incidence matrix** when:

```text
You are doing graph theory
You are modeling flows or circuits
You need to analyze node-edge relationships directly
```


