import networkx as nx
import random
import matplotlib.pyplot as plt


def toy_example():
    # Generate sample graph
    G = nx.DiGraph()
    G.add_nodes_from(["s",1,2,3,4,"t"])
    G.add_weighted_edges_from([("s",1,5),(1,2,3),(1,3,2),(1,4,6),(2,4,2),(3,4,3),(4,"t",1)], "length")
    
    # Return the graph
    return G   


def random_graph(n):
    import math
    
    # Generate random graph    
    G = nx.generators.erdos_renyi_graph(n, 1.2*math.log(n)/n, directed = True)
    # Set random edge lengths
    nx.set_edge_attributes(G, dict([[e, random.randint(1,9)] for e in G.edges]), "length")
    
    # Return relabeled graph
    relabel = {0: "s", n-1: "t"}
    return nx.relabel.relabel_nodes(G, relabel)


def draw(G):
    import networkx.algorithms.isomorphism as iso
    
    if nx.is_isomorphic(G, toy_example()):
        # If G is the toy example, we'd like to use fixed vertex positions
        vertex_pos = {"s": (-1.5, .5), 1: (0, .5), 2: (1, 1), 3: (1, 0), 4: (2, .5), "t": (3.5, .5)}
        nx.draw(G, vertex_pos, with_labels = True, font_size = 15, arrowsize = 20, node_color = 'y')
        nx.draw_networkx_edge_labels(G, pos = vertex_pos, label_pos = 0.5, edge_labels = nx.get_edge_attributes(G, "length"), font_size = 15)
    else:
        # Else, we go for a circular layout
        node_pos =  nx.circular_layout(G)
        nx.draw(G, with_labels = True, pos = node_pos, node_color = 'lightblue')
        nx.draw_networkx_edge_labels(G, pos = node_pos, label_pos = 0.5, edge_labels = nx.get_edge_attributes(G, "length"), font_size = 15)
    
    plt.show()


def check(algorithm, graph):
    # Check if there is a path at all
    if nx.has_path(graph,'s','t'):
        # Compute values
        alg = algorithm(graph)
        opt = nx.shortest_path_length(graph,'s','t','length')
        
        # Print values
        print(f"Your algorithm computes an s-t distance of {alg}.")
        print(f"The actual s-t distance is {opt}.\n")
        
        # Feedback
        if alg == opt:
            print("Congratulations! Your implementation is correct on the given instance.")
        else:
            print("There seems to be an issue. Try to revise your implementation!")
    else:
        # No s-t path exists
        print("The input graph does not have an s-t path at all.")