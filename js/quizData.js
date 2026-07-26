(function () {
  "use strict";

  window.QuizQuestions = [
    {
      id: "d777-01",
      competency: "Explains Algorithms",
      topic: "Foundations",
      prompt: "What does an abstract data type (ADT) define?",
      choices: ["The exact memory layout", "The available operations and expected behavior", "The implementation language", "The processor instructions"],
      answer: 1,
      explanation: "An ADT defines what operations are available and how they behave without requiring a particular implementation."
    },
    {
      id: "d777-02",
      competency: "Determines Data Structure Impact",
      topic: "Foundations",
      prompt: "Why can two implementations of the same ADT have different performance?",
      choices: ["ADTs require random operations", "They may use different underlying structures", "Big-O does not apply to structures", "An ADT defines only space use"],
      answer: 1,
      explanation: "The ADT defines behavior, while the underlying representation determines the cost of each operation."
    },
    {
      id: "d777-03",
      competency: "Explains Algorithms",
      topic: "Algorithm Design",
      prompt: "Which technique stores solutions to overlapping subproblems to avoid repeated work?",
      choices: ["Greedy selection", "Dynamic programming", "Linear probing", "Heuristic search"],
      answer: 1,
      explanation: "Dynamic programming saves and reuses solutions to overlapping subproblems."
    },
    {
      id: "d777-04",
      competency: "Applies Algorithms",
      topic: "Complexity",
      prompt: "Which complexity commonly describes an algorithm that repeatedly divides a problem in half?",
      choices: ["O(1)", "O(log n)", "O(n)", "O(n²)"],
      answer: 1,
      explanation: "Repeated division of the remaining problem produces logarithmic growth."
    },
    {
      id: "d777-05",
      competency: "Determines Data Structure Impact",
      topic: "Lists",
      prompt: "Which structure provides O(1) indexed access?",
      choices: ["Array-based list", "Singly linked list", "Linked-list queue", "Binary search tree"],
      answer: 0,
      explanation: "An array-based list calculates an element's address directly from its index."
    },
    {
      id: "d777-06",
      competency: "Determines Data Structure Impact",
      topic: "Lists",
      prompt: "Why is indexed access O(n) in a linked list?",
      choices: ["Nodes must be sorted", "The list must be rehashed", "Nodes must be followed sequentially from the head", "Every node must be copied"],
      answer: 2,
      explanation: "Linked-list nodes are reached by following references, so reaching an arbitrary position may require traversing the list."
    },
    {
      id: "d777-07",
      competency: "Explains Algorithms",
      topic: "Lists",
      prompt: "What is a primary benefit of dummy nodes in a linked list?",
      choices: ["They provide O(1) search", "They reduce special cases at the ends", "They eliminate references", "They keep the list sorted"],
      answer: 1,
      explanation: "Dummy or sentinel nodes simplify insertion and removal logic at the head and tail."
    },
    {
      id: "d777-08",
      competency: "Explains Algorithms",
      topic: "Stacks and Queues",
      prompt: "Which rule describes a stack?",
      choices: ["FIFO", "LIFO", "Lowest priority first", "Sorted order"],
      answer: 1,
      explanation: "A stack is last in, first out: the newest item is removed first."
    },
    {
      id: "d777-09",
      competency: "Applies Algorithms",
      topic: "Stacks and Queues",
      prompt: "Which structure is normally used by breadth-first search?",
      choices: ["Stack", "Queue", "Heap", "Trie"],
      answer: 1,
      explanation: "BFS uses a queue to process vertices level by level."
    },
    {
      id: "d777-10",
      competency: "Determines Data Structure Impact",
      topic: "Stacks and Queues",
      prompt: "Why is a deque preferable to a standard Python list when repeatedly removing from the front?",
      choices: ["It automatically sorts values", "It provides efficient operations at both ends", "It prevents duplicates", "It uses binary search"],
      answer: 1,
      explanation: "A deque supports efficient insertion and removal at both ends; removing from the front of a list shifts the remaining elements."
    },
    {
      id: "d777-11",
      competency: "Explains Algorithms",
      topic: "Hash Tables",
      prompt: "What happens when an existing key is inserted into a map?",
      choices: ["A duplicate key is stored", "The existing key's value is updated", "The map is always resized", "The insertion is always rejected"],
      answer: 1,
      explanation: "A map associates one value with each distinct key, so reinserting a key updates its value."
    },
    {
      id: "d777-12",
      competency: "Explains Algorithms",
      topic: "Hash Tables",
      prompt: "A hash collision occurs when:",
      choices: ["A key is inserted twice", "Two keys map to the same table index", "The load factor reaches zero", "A value is larger than its key"],
      answer: 1,
      explanation: "A collision occurs when different keys produce the same table location."
    },
    {
      id: "d777-13",
      competency: "Applies Algorithms",
      topic: "Hash Tables",
      prompt: "Which collision method is especially associated with primary clustering?",
      choices: ["Chaining", "Linear probing", "Double hashing", "Direct hashing"],
      answer: 1,
      explanation: "Linear probing checks consecutive positions, allowing runs of occupied cells called primary clusters to form."
    },
    {
      id: "d777-14",
      competency: "Determines Data Structure Impact",
      topic: "Hash Tables",
      prompt: "Why does resizing a hash table usually improve its performance?",
      choices: ["It lowers the load factor", "It changes values into keys", "It sorts all entries", "It guarantees O(1) worst-case lookup"],
      answer: 0,
      explanation: "Increasing capacity lowers the load factor and generally shortens chains or probe sequences."
    },
    {
      id: "d777-15",
      competency: "Applies Algorithms",
      topic: "Sets",
      prompt: "Which set operation returns only values present in both sets?",
      choices: ["Union", "Difference", "Intersection", "Append"],
      answer: 2,
      explanation: "Intersection returns elements shared by both sets."
    },
    {
      id: "d777-16",
      competency: "Applies Algorithms",
      topic: "Trees",
      prompt: "Which traversal visits a binary search tree's keys in sorted order?",
      choices: ["Preorder", "Inorder", "Postorder", "Level order"],
      answer: 1,
      explanation: "Inorder traversal visits the left subtree, node, and right subtree, producing sorted BST keys."
    },
    {
      id: "d777-17",
      competency: "Determines Data Structure Impact",
      topic: "Trees",
      prompt: "What primarily determines the cost of search, insertion, and removal in a BST?",
      choices: ["The number of leaves only", "The root key", "The tree height", "The most recent traversal"],
      answer: 2,
      explanation: "BST operations follow a root-to-node path, so their cost depends on tree height."
    },
    {
      id: "d777-18",
      competency: "Applies Algorithms",
      topic: "Trees",
      prompt: "Which structure is especially useful for prefix lookup and autocomplete?",
      choices: ["Trie", "Heap", "Stack", "Bitmap"],
      answer: 0,
      explanation: "A trie stores strings along character paths, making prefix retrieval efficient."
    },
    {
      id: "d777-19",
      competency: "Applies Algorithms",
      topic: "Balanced Trees",
      prompt: "An AVL node's balance factor is calculated as:",
      choices: ["Right height minus left height", "Left height minus right height", "Number of children minus one", "Depth plus height"],
      answer: 1,
      explanation: "The AVL balance factor is left subtree height minus right subtree height."
    },
    {
      id: "d777-20",
      competency: "Applies Algorithms",
      topic: "Balanced Trees",
      prompt: "Which correction is used for a right-right AVL imbalance?",
      choices: ["Single right rotation", "Single left rotation", "Left rotation on the child, then right rotation", "Right rotation on the child, then left rotation"],
      answer: 1,
      explanation: "A right-right imbalance is corrected with a single left rotation."
    },
    {
      id: "d777-21",
      competency: "Explains Algorithms",
      topic: "Balanced Trees",
      prompt: "Which statement is a red-black tree property?",
      choices: ["Every red node has a red child", "The root and null leaves are black", "Every balance factor is zero", "All paths contain the same total number of nodes"],
      answer: 1,
      explanation: "The root and null leaves are black, red nodes cannot have red children, and all paths to descendant null leaves have equal black height."
    },
    {
      id: "d777-22",
      competency: "Determines Data Structure Impact",
      topic: "Balanced Trees",
      prompt: "What is a typical difference between AVL and red-black trees?",
      choices: ["AVL trees are not BSTs", "Red-black trees permit linear height", "AVL trees maintain stricter height balance", "Red-black trees cannot rotate"],
      answer: 2,
      explanation: "AVL trees keep stricter height balance and may rotate more often during updates."
    },
    {
      id: "d777-23",
      competency: "Explains Algorithms",
      topic: "Heaps",
      prompt: "Where is the largest item located in a max-heap?",
      choices: ["The leftmost leaf", "The last array position", "The root", "Its location is unknown"],
      answer: 2,
      explanation: "The max-heap property guarantees that a maximum value is at the root."
    },
    {
      id: "d777-24",
      competency: "Determines Data Structure Impact",
      topic: "Heaps",
      prompt: "What is the complexity of peeking at a heap's root?",
      choices: ["O(1)", "O(log n)", "O(n)", "O(n log n)"],
      answer: 0,
      explanation: "The root is directly accessible, so peeking takes constant time."
    },
    {
      id: "d777-25",
      competency: "Applies Algorithms",
      topic: "Heaps",
      prompt: "In a zero-based heap array, what is the left-child index of a node at index i?",
      choices: ["i + 1", "2i", "2i + 1", "2i + 2"],
      answer: 2,
      explanation: "The left child is at 2i + 1 and the right child is at 2i + 2."
    },
    {
      id: "d777-26",
      competency: "Explains Algorithms",
      topic: "Heaps",
      prompt: "A treap combines:",
      choices: ["Queue and stack ordering", "BST key ordering and heap priority ordering", "B-tree ordering and hash probing", "Set uniqueness and linked-list traversal"],
      answer: 1,
      explanation: "A treap follows BST ordering by key and heap ordering by priority."
    },
    {
      id: "d777-27",
      competency: "Determines Data Structure Impact",
      topic: "Graphs",
      prompt: "Which representation is generally best for a sparse graph?",
      choices: ["Adjacency list", "Adjacency matrix", "Complete binary tree", "Two-dimensional heap"],
      answer: 0,
      explanation: "An adjacency list uses O(V + E) space and stores only existing edges."
    },
    {
      id: "d777-28",
      competency: "Determines Data Structure Impact",
      topic: "Graphs",
      prompt: "What is a principal advantage of an adjacency matrix?",
      choices: ["O(V + E) storage for every graph", "O(1) edge-existence checks", "Automatic shortest paths", "It prevents cycles"],
      answer: 1,
      explanation: "The matrix cell for a vertex pair can be checked directly in constant time."
    },
    {
      id: "d777-29",
      competency: "Applies Algorithms",
      topic: "Graphs",
      prompt: "Which shortest-path algorithm handles negative edge weights and can detect negative cycles?",
      choices: ["Dijkstra", "Bellman-Ford", "BFS", "Kruskal"],
      answer: 1,
      explanation: "Bellman-Ford repeatedly relaxes edges, supports negative weights, and can detect reachable negative cycles."
    },
    {
      id: "d777-30",
      competency: "Applies Algorithms",
      topic: "Graphs",
      prompt: "Which algorithm produces an ordering only for a directed acyclic graph?",
      choices: ["Topological sort", "Floyd-Warshall", "Heapsort", "Binary search"],
      answer: 0,
      explanation: "A topological ordering exists only for a directed acyclic graph."
    },
    {
      id: "d777-31",
      competency: "Applies Algorithms",
      topic: "Graphs",
      prompt: "Kruskal's algorithm commonly uses sorted edges together with:",
      choices: ["A trie", "Disjoint sets", "A call stack only", "A Bloom filter"],
      answer: 1,
      explanation: "Disjoint sets efficiently determine whether adding an edge would create a cycle."
    },
    {
      id: "d777-32",
      competency: "Explains Algorithms",
      topic: "Graphs",
      prompt: "What is the typical time complexity of BFS or DFS using an adjacency list?",
      choices: ["O(1)", "O(log V)", "O(V + E)", "O(V³)"],
      answer: 2,
      explanation: "Each vertex and edge is processed a constant number of times."
    },
    {
      id: "d777-33",
      competency: "Applies Algorithms",
      topic: "B-Trees",
      prompt: "What is the maximum number of keys in a B-tree node of order K?",
      choices: ["K + 1", "K", "K - 1", "2K"],
      answer: 2,
      explanation: "An order-K B-tree node can have at most K children and K - 1 keys."
    },
    {
      id: "d777-34",
      competency: "Determines Data Structure Impact",
      topic: "B-Trees",
      prompt: "Why are B-tree variants widely used for storage indexes?",
      choices: ["High branching reduces height and page accesses", "Every key is stored at the root", "They never require updates", "Every node has only one key"],
      answer: 0,
      explanation: "Their high branching factor keeps the tree shallow and reduces expensive storage-page accesses."
    },
    {
      id: "d777-35",
      competency: "Applies Algorithms",
      topic: "B-Trees",
      prompt: "What happens when a full B-tree node is split?",
      choices: ["All keys are deleted", "A middle key is promoted to the parent", "The node becomes a linked list", "Every child becomes a root"],
      answer: 1,
      explanation: "A middle key is promoted, while the remaining keys are divided between separate nodes."
    },
    {
      id: "d777-36",
      competency: "Applies Algorithms",
      topic: "Searching and Sorting",
      prompt: "What requirement must be satisfied before binary search can be used?",
      choices: ["The collection must be sorted", "It must be a linked list", "Values must be unique", "Its size must be a power of two"],
      answer: 0,
      explanation: "Sorted order lets the middle comparison eliminate half of the remaining search space."
    },
    {
      id: "d777-37",
      competency: "Explains Algorithms",
      topic: "Searching and Sorting",
      prompt: "Which sorting algorithm averages O(n log n) but has a worst case of O(n²)?",
      choices: ["Merge sort", "Quicksort", "Selection sort", "Radix sort"],
      answer: 1,
      explanation: "Quicksort averages O(n log n), but consistently poor pivots can produce O(n²) behavior."
    },
    {
      id: "d777-38",
      competency: "Determines Data Structure Impact",
      topic: "Searching and Sorting",
      prompt: "Which simple sorting algorithm often performs well on nearly sorted data?",
      choices: ["Insertion sort", "Selection sort", "Floyd-Warshall", "Heapsort"],
      answer: 0,
      explanation: "Insertion sort performs little movement on nearly sorted input and can approach O(n)."
    },
    {
      id: "d777-39",
      competency: "Determines Data Structure Impact",
      topic: "Databases",
      prompt: "Which structure can quickly prove that a database key is absent, while a positive result may be a false positive?",
      choices: ["Merkle tree", "Bloom filter", "B+ tree", "LSM tree"],
      answer: 1,
      explanation: "A Bloom filter has no false negatives, but a positive membership result may be false."
    },
    {
      id: "d777-40",
      competency: "Determines Data Structure Impact",
      topic: "Databases",
      prompt: "Which structure is optimized for write-heavy storage using memory buffers and sorted disk runs?",
      choices: ["Trie", "LSM tree", "Stack", "Adjacency matrix"],
      answer: 1,
      explanation: "An LSM tree buffers writes in memory and later merges them into sorted disk structures."
    }
  ];
})();
