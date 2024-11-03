import argparse

class Pair:
    def __init__(self, source, target):
        self.source = int(source)
        self.target = int(target)


def read_graph_lines(file_path):
    lines = []
    with open(file_path, "r") as f:
        lines = [line.strip().split(" ") for line in f]

    return lines

def read_simple_format(file_path):
    lines = read_graph_lines(file_path)

    n = lines[0][0]
    lines.pop(0)
    pairs = [Pair(line[0], line[1]) for line in lines]

    return (n, pairs)

def get_node_neighbours(node, pairs):
    neighbours = []
    for pair in pairs:
        if pair.source == node and pair.target not in neighbours:
            neighbours.append(pair.target)

    return neighbours

def get_nodes(pairs):
    nodes = []
    for pair in pairs:
        if not pair.source in nodes:
            nodes.append(pair.source)
        if not pair.target in nodes:
            nodes.append(pair.target)

    return nodes

def main(args):
    (n, pairs) = read_simple_format(args.filepath)
    m = len(pairs)

    vertices = sorted(get_nodes(pairs))
    with open("./out", "w") as f:
        f.write(f"{n}\t{m}\n")
        for vertex in vertices:
            f.write(f"{vertex}\t")
            neighbours = sorted(get_node_neighbours(vertex, pairs))
            for neighbour in neighbours:
                f.write(f"{neighbour}\t")
            f.write("\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filepath")

    args = parser.parse_args()
    main(args)
