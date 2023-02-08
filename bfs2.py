from collections import deque
import graph

def BFS2(G, node1, node2):
    if node1 == node2:
        return []
    if node2 in G.adj[node1]:
        return [node1, node2]

    path_dict = {}
    Q = deque([node1])
    marked = {node1 : True}
    for node in G.adj:
        if node != node1:
            marked[node] = False
    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if not marked[node]:
                path_dict[node] = []
                for i in G.adj[node]:
                    if not marked[i]:
                        path_dict[node].append(i)
                Q.append(node)
                marked[node] = True

    final_list = deque([])
    current_node = node2
    b = False
    while True:
        for key in path_dict.keys():
            if current_node in path_dict[key]:
                final_list.appendleft(current_node)
                current_node = key
                b = True
                if current_node in G.adj[node1]:
                    final_list.appendleft(current_node)
                    final_list.appendleft(node1)
                    return final_list
        if not b:
            return []

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
print(g.adj)
print(BFS2(g, 2, 11))