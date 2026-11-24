from collections import deque

# adj[u] consists of all vertices adjacent to u
adj = [[3], [4], [5], [0, 4, 6], [1, 3, 5, 7], [2, 4], [3, 7], [4, 6, 8], [7]]


def bfs_distances(adj: list[list[int]], s: int):
    """Calculate the distances from the start vertex to every other vertex.

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
    """Create a copy of the provided adjacency list.

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
