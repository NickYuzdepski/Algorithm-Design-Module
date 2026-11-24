# adj[u] consists of all vertices adjacent to u
adj = [[4], [5], [6], [1, 5, 7], [2, 4, 6, 8], [3, 5], [4, 8], [5, 7, 9], [8]]

def bfs_distances(adj: list[list[int]], s: int):
    """Calculate the distances from the start vertex to every other vertex.

    Args:
        adj: The adjacency list representation of a graph.
        s: The start vertex.

    Returns:
        A list of distances where each distance corresponds to the vertex u in
        the adjacency list.
    """

