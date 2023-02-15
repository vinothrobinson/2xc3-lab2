import matplotlib.pyplot as plot
import graph
import has_cycle


def experiment1(node_num, trial_num):
    cycle_percentage = []
    max_edge_num = graph.triangle(node_num - 1)
    for edge_num in range(max_edge_num+1):
        cycle_count = 0
        for _ in range(trial_num):
            G = graph.create_random_graph(node_num, edge_num)

            # Run Experiment
            if has_cycle.has_cycle(G):
                cycle_count += 1
        cycle_percentage.append(cycle_count / trial_num)
    plot.plot(cycle_percentage)
    plot.title(f"Cycle Detection: Number of Edges vs Cycle Percentage (|V| = {node_num})")
    plot.xlabel("Number of Nodes")
    plot.ylabel("Cycle Percentage")
    plot.show()


experiment1(5, 100)
experiment1(10, 100)
experiment1(15, 100)
experiment1(20, 100)
experiment1(30, 100)