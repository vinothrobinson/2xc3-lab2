import timeit
import graph
import timeit


def experiment(node_num, trial_num):
    average_times = []
    max_edge_num = graph.triangle(node_num - 1)
    for edge_num in range(max_edge_num):
        times = 0
        for _ in trial_num:
            G = graph.create_random_graph(node_num, edge_num)

            start = timeit.default_timer()
            # Run Experiment
            end = timeit.default_timer()
            times += end - start
        average_times.append(times / trial_num)
    return average_times

for i in range(20):
    print(f"Triangle {i}: {triangle(i)}")