import graph
from collections import deque


def BFS3(G, start):
    Q = deque([start])
    marked = {}
    for node in G.adj:
        marked[node] = False
    marked[start] = True
    edgeTo = {}

    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if not marked[node]:
                Q.append(node)
                marked[node] = True
                edgeTo[node] = current_node
    return edgeTo


g = graph.Graph(7)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 4)
g.add_edge(3, 5)
g.add_edge(4, 5)
g.add_edge(4, 6)
print(BFS3(g, 1))
