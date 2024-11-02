import networkx as nx
import matplotlib.pyplot as plt

# Graph of some roads Ukraine
G = nx.Graph()
G.add_nodes_from(["Kyiv", "Kharkiv", "Odessa", "Dnipro", "Donetsk"])
G.add_edges_from(
    [
        ("Kyiv", "Kharkiv"),
        ("Kyiv", "Odessa"),
        ("Kyiv", "Dnipro"),
        ("Kyiv", "Donetsk"),
        ("Kharkiv", "Odessa"),
        ("Kharkiv", "Dnipro"),
        ("Odessa", "Dnipro"),
        ("Dnipro", "Donetsk"),
        ("Donetsk", "Kharkiv"),
    ]
)

G["Kyiv"]["Kharkiv"]["weight"] = 469
G["Kyiv"]["Odessa"]["weight"] = 475
G["Kyiv"]["Dnipro"]["weight"] = 487
G["Kyiv"]["Donetsk"]["weight"] = 688
G["Kharkiv"]["Odessa"]["weight"] = 716
G["Kharkiv"]["Dnipro"]["weight"] = 217
G["Odessa"]["Dnipro"]["weight"] = 452
G["Dnipro"]["Donetsk"]["weight"] = 248
G["Donetsk"]["Kharkiv"]["weight"] = 304

# Print the number of nodes and edges in the graph
print(f"Number of nodes: {G.number_of_nodes()}, number of edges: {G.number_of_edges()}")

# Print degree centrality, closeness centrality, and betweenness centrality
print(f"Degree Centrality: {nx.degree_centrality(G)}")
print(f"Closeness Centrality: {nx.closeness_centrality(G)}")
print(f"Betweenness Centrality: {nx.betweenness_centrality(G)}")

# Plot the graph with edge labels
plt.figure(figsize=(12, 6))
labels = nx.get_edge_attributes(G, "weight")
pos = nx.circular_layout(G)
nx.draw(G, pos, with_labels=True, font_size=11, node_size=2000, node_color="yellow")
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()
