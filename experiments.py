import matplotlib.pyplot as plot
import graph
import has_cycle
import is_connected
import indep_set
import vc_approx


def experiment1(node_num, trial_num):
    cycle_percentage = experiment1_data(node_num, trial_num)
    plot.plot(cycle_percentage)
    plot.title(f"Cycle Detection: Number of Edges vs Cycle Percentage (|V| = {node_num})")
    plot.xlabel("Number of Edges")
    plot.ylabel("Cycle Percentage (%)")
    plot.show()


def experiment1_data(node_num, trial_num):
    cycle_percentage = []
    max_edge_num = min(node_num, graph.triangle(node_num - 1))
    for edge_num in range(max_edge_num + 1):
        cycle_count = 0
        for _ in range(trial_num):
            G = graph.create_random_graph(node_num, edge_num)

            # Run Experiment
            if has_cycle.has_cycle(G):
                cycle_count += 1
        cycle_percentage.append(100 * cycle_count / trial_num)
    return cycle_percentage

def experiment1_heatmap(max_node_num, trial_num):
    cycle_matrix = []
    for node_num in range(max_node_num):
        print(f"Running for node_num={node_num}")
        cycle_percentage = experiment1_data(node_num, trial_num) + [100 for _ in range(max_node_num - min(node_num, graph.triangle(node_num - 1)))]
        cycle_matrix.append(cycle_percentage)

    plot.imshow(cycle_matrix, interpolation='gaussian', vmin=0, vmax=100)
    plot.title(f"Cycle Detection: Number of Nodes and Edges vs Cycle Percentage", pad=20)
    plot.xlabel("Number of Edges")
    plot.ylabel("Number of Nodes")
    cbar = plot.colorbar()
    cbar.set_label("Cycle Percentage (%)")
    plot.show()


def experiment2(node_num, trial_num):
    total_list = experiment2_data(node_num, trial_num)
    plot.plot(total_list)
    plot.title("Number of Edges vs Connected Percentage")
    plot.xlabel("Number of Edges")
    plot.ylabel("Connected Percentage (%)")
    plot.show()


def experiment2_data(node_num, trial_num):
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
    return total_list


def experiment2_heatmap(max_node_num, trial_num):
    cycle_matrix = [[100 for i in range(graph.triangle(max_node_num-1)+1)]]
    for node_num in range(1, max_node_num):
        print(f"Running for node_num={node_num}")
        cycle_percentage = experiment2_data(node_num, trial_num) + [100 for _ in range(graph.triangle(max_node_num-1) - graph.triangle(node_num-1))]
        cycle_matrix.append(cycle_percentage)

    plot.imshow(cycle_matrix, interpolation='gaussian', vmin=0, vmax=100)
    plot.title(f"Cycle Detection: Number of Nodes and Edges vs Connected Percentage", pad=10)
    plot.xlabel("Number of Edges")
    plot.ylabel("Number of Nodes", loc='top')
    cbar = plot.colorbar(location='bottom')
    cbar.set_label("Connected Percentage (%)")
    plot.tight_layout()
    plot.show()


def experiment3_data(node_num, trial_num):
    total_lists = [[] for i in range(4)]
    max_edge_num = graph.triangle(node_num - 1)
    for edge_num in range(max_edge_num + 1):
        vc_sizes = [0 for i in range(4)]
        for _ in range(trial_num):
            G = graph.create_random_graph(node_num, edge_num)
            vc_sizes[0] += len(graph.MVC(G))
            vc_sizes[1] += len(vc_approx.approx1(G))
            vc_sizes[2] += len(vc_approx.approx2(G))
            vc_sizes[3] += len(vc_approx.approx3(G))
        for i in range(4):
            total_lists[i].append(vc_sizes[i] / trial_num)
    return total_lists


def experiment3(node_num, trial_num):
    total_lists = experiment3_data(node_num, trial_num)

    plot.plot(total_lists[0], label="MVC Size")
    plot.plot(total_lists[1], label="Approximation 1")
    plot.plot(total_lists[2], label="Approximation 2")
    plot.plot(total_lists[3], label="Approximation 3")
    plot.legend()
    plot.title(f"Number of Edges vs Size of Vertex Cover Approximations (|V| = {node_num}")
    plot.xlabel("Number of Edges")
    plot.ylabel("Size of Vertex Cover Approximations")
    plot.show()



def experiment_last(node_num, trial_num):
    G = graph.create_random_graph(10, 44)
    C = graph.MVC(G)
    I = indep_set.MIS(G)
    print(f"G  : {G.adj}")
    print(f"MVC: {C}")
    print(f"MIS: {I}")


# experiment1(5, 100)
# experiment1(10, 100)
# experiment1(15, 100)
# experiment1(20, 100)
# experiment1(30, 100)
# experiment1_heatmap(30, 500)

# experiment2(10, 100)
#experiment2_heatmap(30, 1)

experiment3(5, 100)
# experiment3(10, 100)
# experiment3(15, 100)
# experiment3(20, 100)
# experiment3(5, 100)

# experiment_last(10, 100)
