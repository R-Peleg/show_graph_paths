import networkx as nx
import re
import pickle
import argparse
from collections import Counter


def load_graph(path):
    """Load a DiGraph from a file."""
    try:
        return nx.read_gpickle(path)
    except AttributeError:
        with open(path, 'rb') as f:
            return pickle.load(f)


def filter_nodes_by_regex(graph, pattern):
    """Filter nodes in the graph by a regex pattern."""
    regex = re.compile(pattern)
    return {node for node in graph.nodes if regex.match(node)}


def find_nodes(graph, from_nodes, to_nodes):
    """Find all paths from any node in from_nodes to any node in to_nodes."""
    paths = []
    for source in from_nodes:
        for dest in to_nodes:
            try:
                paths.append(nx.shortest_path(graph, source, dest))
            except nx.NetworkXAlgorithmError:
                pass
    c = Counter()
    for p in paths:
        c.update(p)
    return c


def display_graph_graphvis(G):
    """Display the graph plot with plotly"""
    import gravis as gv
    gv.d3(G, node_size_data_source='count', show_node_label=False).display()


def display_subgraph(subgraph):
    """Display the subgraph using matplotlib."""
    import matplotlib.pyplot as plt
    pos = nx.spring_layout(subgraph)
    nx.draw(subgraph, pos, with_labels=True,
            node_color='lightblue', edge_color='gray',
            node_size=500, font_size=10)
    plt.show()

def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('graph_path', type=str, help='Path to the saved nx DiGraph')
    parser.add_argument('from_pattern', type=str, help='Regex for from_nodes')
    parser.add_argument('to_pattern', type=str, help='Regex for to_nodes')

    args = parser.parse_args()

    # Load the graph
    graph = load_graph(args.graph_path)
    
    # Filter nodes using regex
    from_nodes = filter_nodes_by_regex(graph, args.from_pattern)
    to_nodes = filter_nodes_by_regex(graph, args.to_pattern)
    
    # Find all nodes with paths from from_nodes to to_nodes
    nodes = find_nodes(graph, from_nodes, to_nodes)
    
    # Create subgraph from paths
    subgraph = graph.subgraph(nodes.keys())
    nx.set_node_attributes(subgraph, nodes, 'count')
    print(f'Created graph with {len(subgraph.nodes)} nodes')
    
    # Display the subgraph
    display_graph_graphvis(subgraph)


if __name__ == "__main__":
    main()
