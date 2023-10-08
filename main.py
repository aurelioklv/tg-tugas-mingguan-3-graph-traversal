from collections import deque

import matplotlib.pyplot as plt
import networkx as nx
import util

G1 = nx.Graph()
G2 = nx.Graph()
util.init_edges_from_file(G1, "edge_list_1.txt")
util.init_edges_from_file(G2, "edge_list_2.txt")

# print(G1.edges(data=True))
# print(G2.edges(data=True))

print("-" * 25 + "1" + "-" * 25)
odd_vertices_1 = util.get_odd_vertices(G1)
print(odd_vertices_1)

if nx.is_eulerian(G1):
    print("Graph 1 is Eulerian")
elif nx.is_semieulerian(G1):
    print("Graph 1 is Semi-Eulerian")

path = [u for u, v in nx.eulerian_path(G1)]

dd = deque(nx.eulerian_path(G1), maxlen=1)
last_element = dd.pop()

path.append(last_element[1])
formatted_path = " - ".join(path)
print(f"{formatted_path}")

edge_labels_1 = {(u, v): d["weight"] for u, v, d in G1.edges(data=True)}
edge_labels_2 = {(u, v): d["weight"] for u, v, d in G2.edges(data=True)}

pos_1 = {
    "u": (0, 3),
    "y": (0, 1),
    "z": (0, -1),
    "v": (0, -3),
    "x": (-2, 0),
    "w": (2, 0),
}

pos_2 = {
    "u": (0.5, 3),
    "y": (0.5, -3),
    "z": (2, -1),
    "v": (-2, -1.5),
    "x": (-2, 1.5),
    "w": (2, 1),
}

nx.draw(
    G1,
    pos_1,
    with_labels=True,
    node_color="skyblue",
    node_size=500,
    font_size=10,
    font_color="black",
    font_weight="bold",
    edge_color="gray",
    width=2,
)
nx.draw_networkx_edge_labels(G1, pos_1, edge_labels=edge_labels_1, font_size=10)
plt.show()

tsp_solution = nx.approximation.traveling_salesman_problem(G2, cycle=True)
tsp_distance = sum(G2[u][v]["weight"] for u, v in zip(tsp_solution, tsp_solution[1:]))

nx.draw(
    G2,
    pos_2,
    with_labels=True,
    node_color="skyblue",
    node_size=500,
    font_size=10,
    font_color="black",
    font_weight="bold",
    edge_color="gray",
    width=2,
)

print("-" * 25 + "2" + "-" * 25)
nx.draw_networkx_edge_labels(G2, pos_2, edge_labels=edge_labels_2, font_size=10)
nx.draw_networkx_edges(
    G2,
    pos_2,
    edgelist=[
        (u, v) for u, v in zip(tsp_solution, tsp_solution[1:] + [tsp_solution[0]])
    ],
    edge_color="red",
    width=2,
)
print("The route of the traveller is:", tsp_solution)
print("The total distance is:", tsp_distance)
plt.show()
