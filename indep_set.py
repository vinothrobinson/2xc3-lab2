import graph

def is_indep_set(G, S):
    for node1 in S:
        for node2 in G.adj[node1]:
            if node2 in S:
                return False
    return True


def MIS(G):
    nodes = [i for i in range(G.number_of_nodes())]
    subsets = graph.power_set(nodes)
    S = []
    for subset in subsets:
        if is_indep_set(G, subset):
            if len(subset) > len(S):
                S = subset
    return S
