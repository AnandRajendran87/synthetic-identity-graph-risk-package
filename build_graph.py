import networkx as nx
import pandas as pd

def build_identity_graph(edges: pd.DataFrame) -> nx.Graph:
    graph = nx.Graph()
    for _, row in edges.iterrows():
        graph.add_edge(row["source"], row["target"], relationship=row.get("relationship", "linked"))
    return graph

def compute_graph_features(graph: nx.Graph) -> dict:
    centrality = nx.degree_centrality(graph)
    components = list(nx.connected_components(graph))
    return {
        "node_count": graph.number_of_nodes(),
        "edge_count": graph.number_of_edges(),
        "connected_components": len(components),
        "degree_centrality": centrality
    }
