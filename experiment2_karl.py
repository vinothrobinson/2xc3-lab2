import graph
import is_connected
import matplotlib.pyplot as plot

def experiment2(n):
    total_list = []
    tri_num = graph.triangle(n-1)
    trial_num = 100
    for num_of_edges in range(tri_num+1):
        list = []
        true_num = 0
        for i in range(trial_num):
            g = graph.create_random_graph(n, num_of_edges)
            list.append(is_connected.is_connected(g))
        for bool in list:
            if bool:
                true_num += 1
        total_list.append(true_num/trial_num*100)
    plot.plot(total_list)
    plot.title("Number of Edges vs Connectedness")
    plot.xlabel("Number of Edges")
    plot.ylabel("Connectedness (%)")
    plot.show()