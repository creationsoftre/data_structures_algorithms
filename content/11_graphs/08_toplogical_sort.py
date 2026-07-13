# ============================================================
# Topological Sort - High-Level Notes
# ============================================================
#
# DESCRIPTION
# ------------------------------------------------------------
#
# Topological sort arranges vertices in dependency order.
#
# It is used with a directed graph.
#
# The graph must be:
#
#   Directed
#
#   Acyclic
#
# This type of graph is called a:
#
#   Directed Acyclic Graph
#
# This is commonly shortened to:
#
#   DAG
#
# A topological order makes sure every required step appears
# before the step that depends on it.
#
#
# EXAMPLE - CAR BUILD PROCESS
# ------------------------------------------------------------
#
# A car build contains tasks that must happen in a specific
# order.
#
# Example:
#
#   Order Parts
#        |
#        v
#   Receive Parts
#        |
#        v
#   Install Suspension
#        |
#        v
#   Perform Alignment
#        |
#        v
#   Test Drive
#
# The alignment cannot happen before the suspension is
# installed.
#
# The test drive should not happen before the alignment is
# complete.
#
# A valid topological order is:
#
#   Order Parts
#   Receive Parts
#   Install Suspension
#   Perform Alignment
#   Test Drive
#
#
# DEPENDENCY DIRECTION
# ------------------------------------------------------------
#
# Each directed edge points from a prerequisite to the task
# that depends on it.
#
# Example:
#
#   Install Suspension -> Perform Alignment
#
# This means:
#
#   Install Suspension must happen first.
#
#   Perform Alignment depends on Install Suspension.
#
#
# MULTIPLE DEPENDENCIES
# ------------------------------------------------------------
#
# A task can depend on more than one earlier task.
#
# Example:
#
#   Install Wheels --------\
#                           \
#                            -> Perform Alignment
#                           /
#   Install Suspension ----/
#
# Perform Alignment cannot begin until both tasks are complete.
#
#
# MULTIPLE VALID ORDERS
# ------------------------------------------------------------
#
# A graph may have more than one valid topological order.
#
# Example:
#
#   Install Wheels
#
# and:
#
#   Install Exhaust
#
# may not depend on each other.
#
# Either task could appear first as long as all dependencies
# are respected.
#
#
# IN-DEGREE
# ------------------------------------------------------------
#
# In-degree is the number of edges pointing into a vertex.
#
# In a dependency graph, in-degree represents the number of
# unfinished prerequisites.
#
# Example:
#
#   Install Wheels --------\
#                           \
#                            -> Perform Alignment
#                           /
#   Install Suspension ----/
#
# Perform Alignment has an in-degree of:
#
#   2
#
# It has two prerequisites.
#
#
# KAHN'S ALGORITHM
# ------------------------------------------------------------
#
# This implementation uses Kahn's algorithm.
#
# Kahn's algorithm uses:
#
#   An in-degree dictionary
#
#   A queue
#
# Steps:
#
#   1. Calculate the in-degree of every vertex.
#
#   2. Add every vertex with an in-degree of 0 to the queue.
#
#   3. Remove one vertex from the queue.
#
#   4. Add it to the topological order.
#
#   5. Reduce the in-degree of its neighbors.
#
#   6. Add any neighbor that reaches an in-degree of 0.
#
#   7. Continue until the queue is empty.
#
#
# WHY IN-DEGREE 0?
# ------------------------------------------------------------
#
# A vertex with an in-degree of 0 has no unfinished
# prerequisites.
#
# This means the task is ready to begin.
#
# Example:
#
#   Order Parts
#
# No other task must happen before Order Parts.
#
# Its in-degree is:
#
#   0
#
#
# CYCLE DETECTION
# ------------------------------------------------------------
#
# Topological sort is not possible when the graph contains a
# cycle.
#
# Example:
#
#   Install Wheels -> Perform Alignment
#          ^                 |
#          |                 v
#          +-------- Test Drive
#
# This creates a circular dependency.
#
# Each task waits for another task in the same cycle.
#
# Kahn's algorithm detects a cycle when:
#
#   Number of sorted vertices
#
# is less than:
#
#   Total number of vertices
#
#
# WHEN TO USE TOPOLOGICAL SORT
# ------------------------------------------------------------
#
# Topological sort is useful for:
#
#   Project task scheduling
#
#   Course prerequisites
#
#   Software build dependencies
#
#   Package installation order
#
#   Deployment pipelines
#
#   Manufacturing steps
#
#   Data-processing workflows
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
#   The number of directed edges.
#
# Every vertex is processed once.
#
# Every edge is examined once.
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
#   The adjacency list
#
#   The in-degree dictionary
#
#   The queue
#
#   The final topological order
#
#
# ============================================================
# TOPOLOGICAL SORT IMPLEMENTATION
# ============================================================
from collections import deque
#
#
class DirectedAcyclicGraph:
    def __init__(self):
        # Create an empty adjacency list.
        #
        # Each key represents a task.
        #
        # Each value stores tasks that depend on the key.
        self.graph = {}
#
    def add_vertex(self, vertex):
        # Do not add a duplicate vertex.
        if vertex in self.graph:
            return False
#
        # Add the vertex with no outgoing dependencies.
        self.graph[vertex] = []
#
        # Return True to show that the vertex was added.
        return True
#
    def add_dependency(self, prerequisite, dependent_task):
        # Add the prerequisite when it does not exist.
        if prerequisite not in self.graph:
            self.add_vertex(prerequisite)
#
        # Add the dependent task when it does not exist.
        if dependent_task not in self.graph:
            self.add_vertex(dependent_task)
#
        # Add a directed edge:
        #
        #   prerequisite -> dependent task
        #
        # Do not add the same dependency twice.
        if dependent_task not in self.graph[prerequisite]:
            self.graph[prerequisite].append(dependent_task)
#
    def calculate_in_degrees(self):
        # Give every vertex an initial in-degree of zero.
        in_degrees = {
            vertex: 0
            for vertex in self.graph
        }
#
        # Visit every prerequisite vertex.
        for prerequisite in self.graph:
            # Visit each task that depends on the prerequisite.
            for dependent_task in self.graph[prerequisite]:
                # Increase the dependent task's in-degree.
                in_degrees[dependent_task] += 1
#
        # Return the completed in-degree dictionary.
        return in_degrees
#
    def topological_sort(self, show_steps=False):
        # Calculate every task's number of prerequisites.
        in_degrees = self.calculate_in_degrees()
#
        # Add every task with no prerequisites to the queue.
        #
        # sorted() keeps the output consistent.
        ready_tasks = deque(
            sorted(
                vertex
                for vertex, degree in in_degrees.items()
                if degree == 0
            )
        )
#
        # Store the final dependency order.
        topological_order = []
#
        # Track the current step for readable output.
        step = 1
#
        if show_steps:
            print("=" * 70)
            print("TOPOLOGICAL SORT TRACE")
            print("=" * 70)
            print("Rule: A task enters the queue when all of its")
            print("prerequisites have been completed.")
            print("\nStarting in-degrees:")
#
            for vertex in sorted(in_degrees):
                print(f"  {vertex}: {in_degrees[vertex]}")
#
            print("\nStarting ready queue:", list(ready_tasks))
#
        # Continue while tasks are ready.
        while ready_tasks:
            if show_steps:
                print("\n" + "-" * 70)
                print(f"STEP {step}")
                print("-" * 70)
                print("Ready queue before:", list(ready_tasks))
#
            # Remove the next task with no unfinished
            # prerequisites.
            current_task = ready_tasks.popleft()
#
            # Add the task to the final build order.
            topological_order.append(current_task)
#
            if show_steps:
                print("Completing task:", current_task)
#
            # Track tasks that become ready during this step.
            newly_ready = []
#
            # Visit each task that depends on the completed task.
            for dependent_task in sorted(
                self.graph[current_task]
            ):
                # One prerequisite has now been completed.
                in_degrees[dependent_task] -= 1
#
                if show_steps:
                    print(
                        f"Reduced {dependent_task} in-degree "
                        f"to {in_degrees[dependent_task]}"
                    )
#
                # The task is ready when no prerequisites remain.
                if in_degrees[dependent_task] == 0:
                    ready_tasks.append(dependent_task)
                    newly_ready.append(dependent_task)
#
            # Sort the queue to make the output consistent when
            # multiple tasks become ready at the same time.
            ready_tasks = deque(sorted(ready_tasks))
#
            if show_steps:
                if newly_ready:
                    print("Newly ready tasks:", sorted(newly_ready))
                else:
                    print("Newly ready tasks: None")
#
                print("Ready queue after:", list(ready_tasks))
                print("Build order so far:")
#
                for position, task in enumerate(
                    topological_order,
                    start=1,
                ):
                    print(f"  {position}. {task}")
#
            step += 1
#
        # A complete topological order must contain every
        # vertex.
        if len(topological_order) != len(self.graph):
            if show_steps:
                print("\n" + "=" * 70)
                print("TOPOLOGICAL SORT FAILED")
                print("=" * 70)
                print("The graph contains a cycle.")
                print("Some tasks are waiting on each other.")
#
            return None
#
        if show_steps:
            print("\n" + "=" * 70)
            print("TOPOLOGICAL SORT COMPLETE")
            print("=" * 70)
            print("Valid build order:")
#
            for position, task in enumerate(
                topological_order,
                start=1,
            ):
                print(f"  {position}. {task}")
#
        # Return the valid dependency order.
        return topological_order
#
    def display(self):
        # Display every task and the tasks that depend on it.
        for prerequisite in sorted(self.graph):
            dependent_tasks = sorted(self.graph[prerequisite])
#
            if dependent_tasks:
                print(
                    f"{prerequisite} -> "
                    f"{', '.join(dependent_tasks)}"
                )
            else:
                print(f"{prerequisite} -> None")
#
#
# ============================================================
# CODE EXAMPLE - CAR BUILD DEPENDENCIES
# ============================================================
#
# Create a directed acyclic graph for a project car build.
car_build = DirectedAcyclicGraph()
#
# Parts must be ordered before they can be received.
car_build.add_dependency(
    "Order Parts",
    "Receive Parts",
)
#
# The received parts are required before the installation
# tasks can begin.
car_build.add_dependency(
    "Receive Parts",
    "Install Suspension",
)
car_build.add_dependency(
    "Receive Parts",
    "Install Wheels",
)
car_build.add_dependency(
    "Receive Parts",
    "Install Exhaust",
)
#
# The suspension and wheels must both be installed before the
# alignment can be performed.
car_build.add_dependency(
    "Install Suspension",
    "Perform Alignment",
)
car_build.add_dependency(
    "Install Wheels",
    "Perform Alignment",
)
#
# The alignment and exhaust installation must be complete
# before the car can be inspected.
car_build.add_dependency(
    "Perform Alignment",
    "Final Inspection",
)
car_build.add_dependency(
    "Install Exhaust",
    "Final Inspection",
)
#
# The inspection must pass before the test drive.
car_build.add_dependency(
    "Final Inspection",
    "Test Drive",
)
#
#
# ============================================================
# DISPLAY THE DEPENDENCY GRAPH
# ============================================================
print("=" * 70)
print("CAR BUILD DEPENDENCIES")
print("=" * 70)
car_build.display()
#
#
# ============================================================
# DISPLAY THE INITIAL IN-DEGREES
# ============================================================
#
# The in-degree shows how many prerequisites each task has.
in_degrees = car_build.calculate_in_degrees()
#
print("\n" + "=" * 70)
print("TASK PREREQUISITE COUNTS")
print("=" * 70)
#
for task in sorted(in_degrees):
    prerequisite_count = in_degrees[task]
#
    print(
        f"{task}: "
        f"{prerequisite_count} unfinished prerequisite(s)"
    )
#
#
# ============================================================
# RUN TOPOLOGICAL SORT
# ============================================================
#
# show_steps=True displays the queue, in-degree updates, and
# build order after every completed task.
print("\n")
build_order = car_build.topological_sort(show_steps=True)
#
#
# ============================================================
# DISPLAY THE FINAL RESULT
# ============================================================
print("\n" + "=" * 70)
print("FINAL CAR BUILD ORDER")
print("=" * 70)
#
if build_order is None:
    print("The build contains a circular dependency.")
    print("A valid build order cannot be created.")
else:
    for position, task in enumerate(build_order, start=1):
        print(f"{position}. {task}")
