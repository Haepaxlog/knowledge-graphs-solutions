import argparse

class Graph:
    def __init__(self, file_path):
        with open(file_path, "r") as f:
            line = f.readline()
            meta = [int(line.strip("\n")) for line in line.split("\t")]
            self.n = meta[0]
            self.m = meta[1]

            self.vertices = {}
            for line in f:
                v_line = [line for line in line.split("\t")]
                v_line.pop()
                v_line = [int(v) for v in v_line]

                vertex = v_line[0]
                if self.vertices.get(vertex) == None:
                    self.vertices[vertex] = []

                self.vertices[vertex] = v_line[1:]


    def get_pointing_vertices(self, vertex):
        return self.vertices[vertex]

'''
v1->v2: all n vertices need to be considered
v2->v3: go through at worst n-1 vertices
v3->vx: linearly go through n vertices

filtering is also O(n), but needs to be done at worst n times so O(n^2)

get_pointing_vertices is O(1), because of hashmap

=> O(n^3 + n^2)
'''
def count_triangles(graph, debug):
    count = 0
    for vertex in graph.vertices:
        # v1 -> v2
        pointing_vertices = graph.get_pointing_vertices(vertex)
        if debug:
            print("v1->v2", vertex, pointing_vertices)
        for pointing_vertex in pointing_vertices:
            # v2 -> v3
            pointed_vertices = graph.get_pointing_vertices(pointing_vertex)
            pointed_vertices = [v for v in pointed_vertices if v != vertex]
            if debug:
                print("v2->v3", pointing_vertex, pointed_vertices)
            for pointed_vertex in pointed_vertices:
                # v3 -> vx
                target_vertices = graph.get_pointing_vertices(pointed_vertex)
                if debug:
                    print("v3->vx", pointed_vertex, target_vertices)
                if vertex in target_vertices:
                    print("(", vertex, pointing_vertex, pointed_vertex, ")")
                    count += 1

    return count
    
def main(args):
    graph = Graph(args.filepath)
    print("number of triangles:", count_triangles(graph, args.debug))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filepath")
    parser.add_argument("--debug", action="store_true")

    args = parser.parse_args()
    main(args)
