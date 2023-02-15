import matplotlib.pyplot as plot
import graph
import has_cycle
import is_connected


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
        cycle_percentage.append(100 * cycle_count / trial_num)
    plot.plot(cycle_percentage)
    plot.title(f"Cycle Detection: Number of Edges vs Cycle Percentage (|V| = {node_num})")
    plot.xlabel("Number of Edges")
    plot.ylabel("Cycle Percentage (%)")
    plot.show()

def experiment2(node_num, trial_num):
    total_list = []
    tri_num = graph.triangle(node_num-1)
    for num_of_edges in range(tri_num+1):
        list = []
        true_num = 0
        for i in range(trial_num):
            g = graph.create_random_graph(node_num, num_of_edges)
            list.append(is_connected.is_connected(g))
        for bool in list:
            if bool:
                true_num += 1
        total_list.append(true_num/trial_num*100)
    plot.plot(total_list)
    plot.title("Number of Edges vs Connected Percentage")
    plot.xlabel("Number of Edges")
    plot.ylabel("Connected Percentage (%)")
    plot.show()

'''experiment1(5, 100)
experiment1(10, 100)
experiment1(15, 100)
experiment1(20, 100)
experiment1(30, 100)'''

experiment2(10, 100)