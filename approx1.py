import graph
# Aprrox1 Function
# Highest Degree = vertex with the longest adjacency list
def approx1(G):
    C = ()
    list_length = {}
    G2 = graph.graph_copy(G)
    while graph.is_vertex_cover(G, C) == False:
        for node in G2.adj:
            list_length[node] = len(G2.adj(node))
        max_len = max(list_length.values())
        for node in G2.adj:
            if len(G2.adj[node]) == max_len and node not in C:
                highest_degree = node
        C.add(highest_degree)
        for node in G2.adj:
            if highest_degree in G2.adj[node].values():
                G2.adj[node].pop(G2.adj[node].index(highest_degree))
    return C