from collections import deque
import graph

def BFS2(G, node1, node2):
    path_dict = {}
    Q = deque([node1])
    marked = {node1 : True}
    for node in G.adj:
        if node != node1:
            marked[node] = False
    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            #if node == node2:
                #return True
            if not marked[node]:
                path_dict[node] = []
                for i in G.adj[node]:
                    if not marked[i]:
                        path_dict[node].append(i)
                Q.append(node)
                marked[node] = True

    final_list = deque([])
    found_path = False
    while found_path == False:
        for list in path_dict.values():
            if node2 in list:
                final_list.appendleft(node2)
                key = findKey(path_dict, node2)
            else:
                found_path = True
    return []

def findKey(path_dict, node):
    pass

'''
t = ("hi","ho")
print(t[1])
'''