from collections import deque
import graph

# ------ DFS2 -----------------
def DFS2(G, node1, node2):
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
                if node == node2:
                    L = [node]
                    temp_node = node
                    while temp_node != node1:
                        temp_node = tracking.get(temp_node)
                        L = [temp_node] + L
                    return L
                S.append(node)
    return []