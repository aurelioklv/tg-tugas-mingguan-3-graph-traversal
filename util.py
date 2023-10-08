import networkx as nx


def init_edges_from_file(G: nx.Graph, filename="edge_list.txt"):
    with open(filename, "r") as file:
        lines = file.readlines()

    for line in lines:
        components = line.strip().split()

        if len(components) == 2:
            node1, node2 = components
            G.add_edge(node1, node2)

        elif len(components) == 3:
            node1, node2, weight = components
            G.add_edge(node1, node2, weight=float(weight))
        else:
            print(f"Invalid edge: {line}")


def get_odd_vertices(G: nx.Graph):
    odd_degree_vertices = [v for v in G.nodes() if G.degree[v] % 2 != 0]

    return odd_degree_vertices
