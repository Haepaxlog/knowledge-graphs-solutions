import argparse
import gzip
from enum import Enum

class Colour(Enum):
    RED = 1
    BLUE = 2

class Edge:
    def __init__(self, s, p, o):
        self.sub = s
        self.pred = p
        self.obj = o

    def __str__(self):
        return f"{self.sub} {self.pred} {self.obj} ."

class RDF:
    def __init__(self, file_path):
        self.file_path = file_path
        with gzip.open(self.file_path, 'rt') as f:
            file_content = f.read().split("\n")
            file_content.pop()
            self.file_content = file_content


    def __connections_for_subject(self, subject):
        connections = []
        for content in self.file_content:
            properties = content.split(" ")
            properties.pop()
            edge = Edge(properties[0], properties[1], properties[2])
            if edge.sub == subject:
                connections.append(edge)

        return connections

    def __colour_different(self, colour):
        if colour == Colour.BLUE:
            return Colour.RED
        if colour == Colour.RED:
            return Colour.BLUE

    def __first_subject(self):
        connections = []
        for content in self.file_content:
            properties = content.split(" ")
            properties.pop()
            edge = Edge(properties[0], properties[1], properties[2])
            return edge.sub


    def is_two_colourable(self, debug):
        subject = self.__first_subject()
        connections = self.__connections_for_subject(subject)

        coloured = {}
        colour = Colour.RED
        coloured[subject] = colour

        stack = []
        for connection in connections:
            stack.append(connection.sub)
        while stack != []:
            sub = stack.pop()
            if debug:
                print(sub)

            connections = self.__connections_for_subject(sub)

            diff_colour = self.__colour_different(colour)

            for connection in connections:
                if (coloured.get(connection.pred) == colour or coloured.get(connection.obj) == colour) and (connection.obj != connection.sub):
                    return False

                if coloured.get(connection.pred) == None:
                    coloured[connection.pred] = diff_colour
                    stack.append(connection.pred)

                if coloured.get(connection.obj) == None:
                    coloured[connection.obj] = diff_colour
                    stack.append(connection.obj)

            colour = diff_colour

        return True

def main(args):
    rdf = RDF(args.filepath)

    print(len(rdf.file_content))
    print(f"{args.filepath} is {'two colourable' if rdf.is_two_colourable(args.debug) else 'not two colourable'}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filepath")
    parser.add_argument("--debug", action="store_true")

    args = parser.parse_args()

    main(args)
