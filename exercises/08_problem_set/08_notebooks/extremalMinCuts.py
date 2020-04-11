import matplotlib.pyplot as plt
import networkx as nx
import random


def toygraph ():
    G = nx.DiGraph()
    G.add_nodes_from(["F", "G", "C", "s", "t"])
    vertex_pos = {"F": (0, .5), "G": (1, 1), "C": (1, 0), "s": (-1, 0.5), "t": (2, .5)}
    edges = [
        ("s", "F", {"capacity": 5}),
        ("C", "t", {"capacity": 2}),
        ("G", "t", {"capacity": 3}),
        ("F", "G", {"capacity": 3}),
        ("F", "C", {"capacity": 2}),
        ("G", "C", {"capacity": 5})
    ]
    G.add_edges_from(edges)

    # Draw the graph
    nx.draw(G, vertex_pos, with_labels=True, font_size=15, arrowsize=20, node_color="yellow")
    nx.draw_networkx_edge_labels(G, pos=vertex_pos, label_pos=0.5, edge_labels={(u, v): d["capacity"] for u, v, d in edges}, font_size=15)
    plt.show()
    return G

def random_graph (n):
    import math
    
    # Generate random graph    
    G = nx.generators.erdos_renyi_graph(n, 1.2*math.log(n)/n, directed = True)
    # Set random edge lengths
    nx.set_edge_attributes(G, dict([[e, random.randint(1,3)] for e in G.edges]), "capacity")
    
    # Relabel graph
    relabel = {0: "s", n-1: "t"}
    G = nx.relabel.relabel_nodes(G, relabel)

    # Fix positions of nodes
    node_pos = nx.circular_layout(G)

    # Draw the graph
    nx.draw(G, with_labels=True, pos=node_pos, node_color='lightblue')
    nx.draw_networkx_edge_labels(G, pos=node_pos, label_pos=0.5, edge_labels={(u, v): G[u][v]["capacity"] for u, v in G.edges}, font_size=15)

    plt.show()
    
    return G

def draw_cut(G,cut,node_pos=None):
    if (node_pos == None):
        node_pos = nx.circular_layout(G)
    nx.draw(G, with_labels=True, pos=node_pos, node_color='lightblue')
    nx.draw_networkx_edge_labels(G, pos=node_pos, label_pos=0.5, edge_labels={(u, v): G[u][v]["capacity"] for u, v in G.edges}, font_size=15)
    nx.draw_networkx_nodes(G,node_pos,
                       nodelist=cut,
                       node_color='r')
