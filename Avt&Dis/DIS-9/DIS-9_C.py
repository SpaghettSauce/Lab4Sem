import matplotlib.pyplot as plt
import networkx as nx

def visualize_graph(edges, matched_edges):
    G = nx.Graph()
    G.add_edges_from(edges)

    pos = nx.spring_layout(G)
    plt.figure(figsize=(10, 8))

    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='grey', node_size=500, font_size=10)
    
    nx.draw_networkx_edges(G, pos, edgelist=matched_edges, edge_color='r', width=2)

    plt.title('Graph Visualization with Maximum Matching')
    plt.show()

# Example edge list
