import networkx as nx
import util

G1 = nx.Graph()
G2 = nx.Graph()
util.init_edges_from_file(G1, "edge_list_1.txt")
util.init_edges_from_file(G2, "edge_list_2.txt")

print(G1.edges(data=True))
print(G2.edges(data=True))

# 1
odd_vertices_1 = util.get_odd_vertices(G1)
print(odd_vertices_1)

print(nx.is_eulerian(G1))
print(nx.is_semieulerian(G1))

path = [u for u, v in nx.eulerian_path(G1)]
formatted_path = " - ".join(path)
print(formatted_path)
