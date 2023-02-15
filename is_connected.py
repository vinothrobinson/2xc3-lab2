from collections import deque
import graph

def is_connected(G):
    node1 = 0
    Q = deque([node1])
    marked = {node1: True}
    for node in G.adj:
        if node != node1:
            marked[node] = False
    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if not marked[node]:
                Q.append(node)
                marked[node] = True
    for node in marked:
        if not marked[node]:
            return False
    return True

g = graph.Graph(4)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
print(g.adj)
print(is_connected(g))