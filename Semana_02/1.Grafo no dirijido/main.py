import networkx  as nx
from solve import *
import matplotlib.pyplot as plt

graph = build_graph();

print("Number of nodes: " + str(graph.number_of_nodes()))
print("Nodes: ", graph.nodes())
print("Number of edges: " + str(graph.number_of_edges()))
print("Edges: ", graph.edges())

# Paso 3 (Opcional): En PyCharm añade aqui el código necesario
#        para mostrar gráficamente el grafo.
# ...


G = nx.petersen_graph()
G.add_node(1)
subax1 = plt.subplot(121)
nx.draw(G, with_labels=True, font_weight='bold')
subax2 = plt.subplot(122)
nx.draw_shell(G, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')