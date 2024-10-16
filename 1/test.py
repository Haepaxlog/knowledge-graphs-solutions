import unittest
from main import process_graph_from_lines, count_min_max, read_graph_lines, Count

class Tests(unittest.TestCase):
    def test_graph_data_1(self):
        lines = read_graph_lines("simple-graphs/01-triangle.txt")

        (n, nodes_out) = process_graph_from_lines(lines, Count.OUT)
        self.assertEqual(n, "3")

        max_nodes_out = count_min_max(nodes_out, Count.OUT)
        self.assertEqual(max_nodes_out, ["0","1","2"])

        (_, nodes_in) = process_graph_from_lines(lines, Count.IN)
        min_nodes_in = count_min_max(nodes_in, Count.IN)
        self.assertEqual(min_nodes_in, ["1", "2", "0"])

    def test_graph_data_2(self):
        lines = read_graph_lines("simple-graphs/02-empty.txt")
        (n, nodes_out) = process_graph_from_lines(lines, Count.OUT)
        self.assertEqual(n, "3")
        self.assertEqual(nodes_out, {})

    def test_graph_data_3(self):
        lines = read_graph_lines("simple-graphs/03-k5.txt")
        (n, nodes_out) = process_graph_from_lines(lines, Count.OUT)
        self.assertEqual(n, "5")

        max_nodes_out = count_min_max(nodes_out, Count.OUT)
        self.assertEqual(max_nodes_out, ["0","1","2","3","4"])

        (_, nodes_in) = process_graph_from_lines(lines, Count.IN)
        min_nodes_in = count_min_max(nodes_in, Count.IN)
        self.assertEqual(min_nodes_in, ["1", "2", "3", "4", "0"])

    def test_graph_data_4(self):
        lines = read_graph_lines("simple-graphs/04-s5.txt")
        (n, nodes_out) = process_graph_from_lines(lines, Count.OUT)
        self.assertEqual(n, "5")

        max_nodes_out = count_min_max(nodes_out, Count.OUT)
        self.assertEqual(max_nodes_out, ["0"])

        (_, nodes_in) = process_graph_from_lines(lines, Count.IN)
        min_nodes_in = count_min_max(nodes_in, Count.IN)
        self.assertEqual(min_nodes_in, ["1", "2", "3", "4"])

if __name__ == "__main__":
    unittest.main()
