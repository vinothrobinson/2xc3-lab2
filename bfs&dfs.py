from collections import deque
import graph


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
                if node == node2:
                    L = [node]
                    temp_node = node
                    while temp_node != tracking.get(node1):
                        temp_node = tracking.get(temp_node)
                        L = [temp_node] + L
                    L = [node1] + L
                    return L
                S.append(node)
    return []


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
