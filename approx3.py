import graph
import random


def approx3(G):
    Gp = graph.graph_copy(G)
    Cover = []
    while not graph.is_vertex_cover(G, Cover):
        n1 = random.choice(list(Gp.adj.keys()))
        while len(Gp.adj[n1]) == 0:
            n1 = random.choice(list(Gp.adj.keys()))
        n2 = random.choice(Gp.adj[n1])

        Cover.append(n1)
        Cover.append(n2)
        remove_node(Gp, n1)
        remove_node(Gp, n2)
    return Cover


def remove_node(G, n):
    G.adj.pop(n)
    for node in G.adj.keys():
        if n in G.adj[node]:
            G.adj[node].remove(n)


G = graph.Graph(6)

G.add_edge(0, 1)
G.add_edge(1, 3)
G.add_edge(0, 2)
G.add_edge(2, 3)
G.add_edge(2, 4)
G.add_edge(3, 4)
G.add_edge(3, 5)

print(G.adj)
print(approx3(G))