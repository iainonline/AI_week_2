import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

node_list = [('SITE2', 'SITE1', 636),
     ('SITE6', 'SITE1', 526),
     ('SITE7', 'SITE1', 668),
     ('SITE8', 'SITE1', 437),
     ('SITE2', 'SITE5', 1),
     ('SITE1', 'SITE6', 673),
     ('SITE2', 'SITE6', 319),
     ('SITE7', 'SITE6', 298),
     ('SITE8', 'SITE6', 252),
     ('SITE1', 'SITE7', 786),
     ('SITE2', 'SITE7', 301),
     ('SITE5', 'SITE8', 46),
     ('SITE6', 'SITE8', 359),
     ('SITE7', 'SITE8', 787)]

def create_tree(node_list):
    df = pd.DataFrame(node_list, columns=['site1', 'site2', 'cost'])
    G = nx.from_pandas_edgelist(df, 'site1', 'site2', edge_attr='cost')
    return G  # a graph object from the networkx library

G = create_tree(node_list)

G = nx.Graph(G)
pos = nx.spring_layout(G)
labels = nx.get_edge_attributes(G, 'cost')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
nx.draw(G, pos, with_labels=True)
plt.axis('off')
plt.show()