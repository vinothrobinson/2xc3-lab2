from collections import deque
import graph
# ------ DFS2 -----------------
def DFS2(G, node1, node2):
    if node1 == node2: # Edge Case, node1 is not connected to itself
        return []
    if node2 in G.adj[node1]: # Edge Case, node 1 is directly connected to node 2
        return [node1, node2]
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
                tracking[node] = current_node #Sets the value as parent, and the parent as value 
                print(tracking)
                if node == node2:
                    L = [node]
                    temp_node = node
                    while temp_node != tracking.get(node1):
                        print(tracking.get(temp_node))
                        temp_node = tracking.get(temp_node)
                        L = [temp_node] + L
                    L = [node1] + L
                    return L
                S.append(node)
    return []
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
print(DFS2(g, 2, 1))
"""