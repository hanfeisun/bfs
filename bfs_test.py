import unittest
from bfs import bfs, NetworkHasCircleException, parse_network, check_circle


class BFSTestCase(unittest.TestCase):
    def test_empty_graph(self):
        self.assertEqual(None, bfs("A", "C", {}))

    def test_no_path(self):
        self.assertEqual(None, bfs("A", "C", {"A": ["B"], "B": ["D"], "F": ["C"]}))

    def test_simplist_path(self):
        self.assertEqual({'A,C'}, bfs("A", "C", {"A": ["C"]}))

    def test_two_paths(self):
        self.assertEqual({'A,D,F,C', "A,B,C"}, bfs("A", "C", parse_network("./network.txt")))

    def test_circle(self):
        self.assertEqual(None, bfs("A", "C", {"A": ["B"], "B": ["A"]}))

    def test_path_with_circles(self):
        self.assertEqual({"A,B,C"}, bfs("A", "C", {"A": ["B"], "B": ["A", "C"]}))

    def test_check_circle_with_self_circle(self):
        self.assertEqual({"A": ["B"], "B": ["C"]}, check_circle("A",  {"A": ["A", "B"], "B": ["A", "C"]}))


    def test_path_with_self_circle(self):
        self.assertEqual({"A,B,C"}, bfs("A", "C", {"A": ["B", "A"], "B": ["A", "C"]}))

if __name__ == '__main__':
    unittest.main()
