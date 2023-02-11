from collections import deque
import graph


# ------ DFS2 -----------------
def DFS3(G, node1):
    if node1 not in G.adj:
        return {}
    S = [node1]
    marked = {}
    for node in G.adj:
        marked[node] = False
    tracking = {}
    while len(S) != 0:
        current_node = S.pop()
        if not marked[current_node]:
            marked[current_node] = True
            for node in G.adj[current_node]:
                if marked[node] ==  False:
                    tracking[node] = current_node #Sets the value as parent, and the parent as value 
                    S.append(node)
    return tracking

"""
g = graph.Graph(13)
g.add_edge(2, 1)
g.add_edge(2, 3)
g.add_edge(2, 4)
g.add_edge(1, 3)
g.add_edge(1, 9)
g.add_edge(1, 10)
g.add_edge(3, 4)
g.add_edge(3, 5)
g.add_edge(4, 5)
g.add_edge(4, 6)
g.add_edge(5, 8)
g.add_edge(6, 7)
g.add_edge(9, 11)
g.add_edge(9, 12)
g.add_edge(10, 13)
g.add_edge(11, 12)
print(DFS3(g, 0))
"""