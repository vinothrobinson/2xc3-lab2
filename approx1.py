import graph
# Aprrox1 Function
# Highest Degree = vertex with the longest adjacency list
def approx1(G):
    C = set()
    G2 = graph.graph_copy(G)
    while graph.is_vertex_cover(G, C) == False:
        list_length = {}
        for node in G2.adj:
            list_length[node] = len(G2.adj[node])
        max_len = max(list_length.values())
        for node in G2.adj:
            if len(G2.adj[node]) == max_len and node not in C:
                highest_degree = node
        C.add(highest_degree)
        remove_node(G2, highest_degree)
    return C

def remove_node(G, n):
    G.adj.pop(n)
    for node in G.adj.keys():
        if n in G.adj[node]:
            G.adj[node].remove(n)

g = graph.Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(0, 3)
g.add_edge(3, 4)
print(approx1(g))