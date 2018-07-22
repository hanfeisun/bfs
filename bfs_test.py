import unittest
from bfs import bfs, NetworkHasCircleException, parse_network


class BFSTestCase(unittest.TestCase):
    def test_empty_graph(self):
        self.assertEqual(None, bfs("A", "C", {}))

    def test_no_path(self):
        self.assertEqual(None, bfs("A", "C", {"A": "B", "B": "D", "F": "C"}))

    def test_simplist_path(self):
        self.assertEqual({'A,C'}, bfs("A", "C", {"A": "C"}))

    def test_two_paths(self):
        self.assertEqual({'A,D,F,C', "A,B,C"}, bfs("A", "C", parse_network("./network.txt")))

    def test_circle(self):
        self.assertRaises(NetworkHasCircleException, bfs, "A", "C", {"A": "B", "B": "A"})


if __name__ == '__main__':
    unittest.main()
