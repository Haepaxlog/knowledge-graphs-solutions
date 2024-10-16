import sys
import argparse

from enum import IntEnum

class Count(IntEnum):
    OUT = 0
    IN = 1

class MinMax(IntEnum):
    MAX = 0
    MIN = 1

def count_node_edges(edges, count_method):
    nodes = {}
    for edge in edges:
        if nodes.get(edge[count_method]) != None:
            nodes[edge[count_method]] += 1
        else:
            nodes[edge[count_method]] = 1

    return nodes

def count_min_max(nodes, count_method):
    v = 0

    if count_method == MinMax.MAX:
        v = max(nodes.values())

    if count_method == MinMax.MIN:
        v = min(nodes.values())

    fitting_nodes = []
    for node, i in nodes.items():
        if i == v:
            fitting_nodes.append(node)

    return fitting_nodes

def process_graph_from_lines(lines, count_method):
    n = lines[0][0]

    edges = lines[1:]
    nodes = count_node_edges(edges, count_method)

    return (n, nodes)

def read_graph_lines(file_path):
    lines = []
    with open(file_path, "r") as f:
        lines = [line.strip().split(" ") for line in f]

    return lines

def main(args):
    file_path = args.filepath
    lines = read_graph_lines(file_path)

    try:
        (n, nodes_out) = process_graph_from_lines(lines, Count.OUT)
        (_, nodes_in) = process_graph_from_lines(lines, Count.IN)
        if nodes_out and nodes_in:
            max_nodes_out = count_min_max(nodes_out, Count.OUT)
            print(f"Nodes with maximal out degree: {max_nodes_out}")

            min_nodes_in = count_min_max(nodes_in, Count.IN)
            print(f"Nodes with minimal in degree: {min_nodes_in}")
        else:
            print("No connected nodes in graph")
    except:
        print("File is misformatted!", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filepath")

    args = parser.parse_args()
    main(args)
