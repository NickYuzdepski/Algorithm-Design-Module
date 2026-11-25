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
    # Create a copy of the adjacency list to work with
    new_adj = copy_adj(adj)
    candidate_adj = new_adj

    # Count the number of edges in the original adjacency list and initialize
    # the best edge count to this value
    edge_count = count_edges(adj)
    best_edge_count = edge_count

    for u, neighbors in enumerate(adj):
        for v in neighbors[:]:
            # Remove the edge (u, v) from the new adjacency list if it exists
            if v in new_adj[u]:
                new_adj[u].remove(v)
            if u in new_adj[v]:
                new_adj[v].remove(u)
            current_edge_count = edge_count - 1

            # Calculate the distances from u to all other vertices in both the
            # original and new adjacency lists
            old_distances = bfs_distances(adj, u)
            new_distances = bfs_distances(new_adj, u)

            # Check if the distance constraint is satisfied for all vertices
            constraint_satisfied = True
            for d in old_distances:
                if new_distances[d] > old_distances[d] + 2:
                    # If the distance constraint is violated, restore the edge
                    # (u, v) and break out of the loop
                    constraint_satisfied = False
                    new_adj[u].append(v)
                    new_adj[v].append(u)
                    current_edge_count += 1
                    break

            # If the distance constraint is satisfied and the current edge
            # count is less than the best edge count, update the best edge
            # count and the candidate adjacency list
            if constraint_satisfied and current_edge_count < best_edge_count:
                best_edge_count = current_edge_count
                candidate_adj = new_adj

    return candidate_adj
