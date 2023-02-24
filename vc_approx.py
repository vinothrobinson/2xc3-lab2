import graph
import random

# --------------------- Remove Node Function -------------------------
def remove_node(G, n):
    G.adj.pop(n)
    for node in G.adj.keys():
        if n in G.adj[node]:
            G.adj[node].remove(n)

# --------------------- Approx() Function Variations -------------------------
# Approx1 Function
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
    
# Aprrox2 Function
def approx2(G):
    C = set()
    G2 = graph.graph_copy(G)
    while graph.is_vertex_cover(G, C) == False:
        random_node = random.choice(list(G2.adj.keys()))
        C.add(random_node)
    return C

# Aprrox3 Function
def approx3(G):
    Gp = graph.graph_copy(G)
    Cover = set()
    while not graph.is_vertex_cover(G, Cover):
        n1 = random.choice(list(Gp.adj.keys()))
        while len(Gp.adj[n1]) == 0:
            n1 = random.choice(list(Gp.adj.keys()))
        n2 = random.choice(Gp.adj[n1])

        Cover.add(n1)
        Cover.add(n2)
        remove_node(Gp, n1)
        remove_node(Gp, n2)
    return Cover