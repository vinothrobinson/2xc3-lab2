import graph
import random
# Aprrox1 Function
# Highest Degree = vertex with the longest adjacency list
def approx1(G):
    C = set()
    G2 = graph.graph_copy(G)
    while graph.is_vertex_cover(G, C) == False:
        random_node = random.choice(list(G2.adj.keys()))
        C.add(random_node)
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
#print(g.number_of_nodes())
print(approx1(g))