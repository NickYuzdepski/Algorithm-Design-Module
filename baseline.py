from collections import deque

# adj[u] consists of all vertices adjacent to u
adj = [[3], [4], [5], [0, 4, 6], [1, 3, 5, 7], [2, 4], [3, 7], [4, 6, 8], [7]]


def bfs_distances(adj: list[list[int]], s: int):
    """Calculate the shortest-path distances from the start vertex to every 
    other vertex.

    Args:
        adj: The adjacency list representation of a graph.
        s: The start vertex.

    Returns:
        A list of distances where each distance corresponds to the vertex u in
        the provided adjacency list.
    """
    visited = []
    distances = []

    # Initialize visited and distances lists
    for u in adj:
        visited.append(False)
        distances.append(float('inf'))

    # Mark the start vertex as visited and set its distance to 0
    visited[s] = True
    distances[s] = 0

    # Create a new empty queue and enqueue the start vertex
    d = deque()
    d.append(s)

    # While the queue is not empty
    while d:
        # Dequeue a vertex from the queue
        u = d.popleft()

        for v in adj[u]:
            # If the vertex has not been visited yet, mark it as visited, set
            # its distance, and enqueue it
            if not visited[v]:
                visited[v] = True
                distances[v] = distances[u] + 1
                d.append(v)

    return distances


def copy_adj(adj: list[list[int]]):
    """Create a deep copy of the provided adjacency list.

    Args:
        adj: The adjacency list representation of a graph.

    Returns:
        A copy of the adjacency list.
    """
    new_adj = []
    for u in adj:
        new_adj.append(u[:])
    return new_adj


def count_edges(adj: list[list[int]]):
    """Count the number of edges in the provided adjacency list.

    Args:
        adj: The adjacency list representation of a graph.

    Returns:
        The number of edges in the graph.
    """
    count = 0
    for u in adj:
        count += len(u)
    # Each edge is counted twice in an undirected graph
    return count // 2


def refine_maze(adj: list[list[int]]):
    """Refine a maze M represented by the provided adjacency list.

    Args:
        adj: The adjacency list representation of a graph.

    Returns:
        A refined maze R represented by an adjacency list with the minimum
        number of edges such that for every pair of vertices u and v, the
        distance from u to v in R is at most two units longer than the
        distance from u to v in M.
    """
    # Create copies of the adjacency list to work with
    current_adj = copy_adj(adj)
    best_adj = copy_adj(adj)

    # Count the number of edges in the original adjacency list and initialize
    # the best edge count to this value
    initial_edges = count_edges(adj)
    best_edge_count = initial_edges

    # Calculate the distances in the original maze for all pairs of vertices
    orig_all_distances = []
    for u in range(len(adj)):
        orig_all_distances.append(bfs_distances(adj, u))

    # Create a list of edges from the original adjacency list
    edges = []
    for u, neighbors in enumerate(adj):
        for v in neighbors:
            if u < v:
                edges.append((u, v))

    def is_valid() -> bool:
        """Check if the distance constraint is satisfied for all pairs of
        vertices.

        Returns:
            True if the distance constraint is satisfied, False otherwise.
        """
        for u in range(len(adj)):
            new_distances = bfs_distances(current_adj, u)
            for v in range(len(adj)):
                if new_distances[v] > orig_all_distances[u][v] + 2:
                    return False
        return True

    def backtrack(idx: int, current_edge_count: int):
        """Backtrack through the edges to find a refined maze with the minimum
        number of edges.

        Args:
            idx: The current index in the edges list.
            current_edge_count: The current number of edges in the new
            adjacency list.
        """
        nonlocal best_edge_count, best_adj

        # If we have considered all edges, update the best edge count and
        # adjacency list if necessary
        if idx == len(edges):
            if current_edge_count < best_edge_count:
                best_edge_count = current_edge_count
                best_adj = copy_adj(current_adj)
            return

        u, v = edges[idx]

        # Try removing the edge (u, v) from the new adjacency list
        current_adj[u].remove(v)
        current_adj[v].remove(u)

        # Check if the distance constraint is satisfied after removing the edge
        if is_valid():
            backtrack(idx + 1, current_edge_count - 1)

        # Restore the edge (u, v) in the new adjacency list
        current_adj[u].append(v)
        current_adj[v].append(u)

        # Try keeping the edge (u, v) in the new adjacency list
        backtrack(idx + 1, current_edge_count)

    # Start the backtracking process with the initial edge count
    backtrack(0, initial_edges)

    return best_adj
