import graph


def has_cycle(G):
    on_stack = [False for _ in range(G.number_of_nodes())]
    marked = [False for _ in range(G.number_of_nodes())]

    for i in range(G.number_of_nodes()):
        stack = [i]
        on_stack[i] = True
        if marked[i] == False:
            while len(stack) != 0:
                current_node = stack.pop()
                on_stack[current_node] = False
                if not marked[current_node]:
                    marked[current_node] = True
                    for node in G.adjacent_nodes(current_node):
                        if on_stack[node]:
                            return True
                        stack.append(node)
                        on_stack[node] = True
    return False