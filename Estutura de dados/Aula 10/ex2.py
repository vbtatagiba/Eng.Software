import networkx as nx
import matplotlib.pyplot as plt

# criando o grafo
G = nx.Graph()

# adicionando os nós
G.add_nodes_from(['casa1', 'casa2', 'casa3', 'agua', 'gas', 'luz'])

# adicionando as arestas
G.add_edges_from([('casa1', 'agua'), ('casa1', 'gas'), ('casa1', 'luz'),
                  ('casa2', 'agua'), ('casa2', 'gas'), ('casa2', 'luz'),
                  ('casa3', 'agua'), ('casa3', 'gas'), ('casa3', 'luz')])

# colorindo os vértices
colors = nx.greedy_color(G, strategy='largest_first')

# definindo as posições dos nós
pos = {
    'casa1': (1, 2),
    'casa2': (2, 2),
    'casa3': (3, 2),
    'agua': (2, 1),
    'gas': (2, 0),
    'luz': (2, 3)
}

# desenhando o grafo
nx.draw(G, pos, with_labels=True, node_color=[colors[node] for node in G.nodes()], edge_color='black')

# mostrando o grafo
plt.show()
