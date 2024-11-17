import matplotlib.pyplot as plt
from itertools import product
import networkx as nx


def graph_visualization(days_of_week, times_of_day, weathers):
    """
    Function to visualize the graph of the observations
    """
    
    observations_graph = list(product(days_of_week, times_of_day, weathers))
    G = nx.Graph()

    for combination in observations_graph:
        G.add_node(combination, type="combination")
        for item in combination:
            G.add_node(item, type="item")
            G.add_edge(item, combination)

    node_colors = []
    node_sizes = []
    for node in G.nodes:
        if isinstance(node, tuple):
            node_colors.append("lightblue")
            node_sizes.append(800)
        elif node in days_of_week:
            node_colors.append("red")
            node_sizes.append(300)
        elif node in times_of_day:
            node_colors.append("green")
            node_sizes.append(300)
        elif node in weathers:
            node_colors.append("orange")
            node_sizes.append(300)

    plt.figure(figsize=(16, 10))
    pos = nx.kamada_kawai_layout(G)
    edges = nx.draw_networkx_edges(G, pos, alpha=0.3)
    nodes = nx.draw_networkx_nodes(
        G, pos, node_size=node_sizes, node_color=node_colors, alpha=0.9
    )
    labels = nx.draw_networkx_labels(G, pos, font_size=8)

    legend_elements = [
        plt.Line2D([0], [0], marker="o", color="w", label="Combination", markerfacecolor="lightblue", markersize=10),
        plt.Line2D([0], [0], marker="o", color="w", label="Day of Week", markerfacecolor="red", markersize=10),
        plt.Line2D([0], [0], marker="o", color="w", label="Time of Day", markerfacecolor="green", markersize=10),
        plt.Line2D([0], [0], marker="o", color="w", label="Weather", markerfacecolor="orange", markersize=10),
    ]
    plt.legend(handles=legend_elements, loc="upper left", fontsize=10)

    plt.title("Observation Network Graph and originating items", fontsize=14)
    plt.axis("off")
    plt.show()