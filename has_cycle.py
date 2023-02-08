import graph


def has_cycle(G):
    on_stack = [False for _ in range(G.number_of_nodes())]
    marked = [False for _ in range(G.number_of_nodes())]

    stack = [0]
    on_stack[0] = True

    while len(stack) != 0:
        current_node = stack.pop()
        if not marked[current_node]:
            marked[current_node] = True
            for node in G.adjacent_nodes(current_node):
                if on_stack[node]:
                    return False
                stack.append(node)
    return True

G = graph.create_random_graph(10, 5)
for i in range(G.number_of_nodes()):
    print(f"Node {i}: {G.adjacent_nodes(i)}")

print(f"Has cycle: {has_cycle(G)}")