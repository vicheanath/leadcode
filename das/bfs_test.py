import unittest

from das.bfs import BFS

class TestBFS(unittest.TestCase):
    def setUp(self):
        self.graph = {
            'A': ['B', 'C'],
            'B': ['A', 'D', 'E'],
            'C': ['A', 'F'],
            'D': ['B'],
            'E': ['B', 'F'],
            'F': ['C', 'E']
        }
        self.bfs = BFS(self.graph, 'A')

    def test_bfs(self):
        self.assertEqual(self.bfs.visited, ['A', 'B', 'C', 'D', 'E', 'F'])
        self.assertEqual(self.bfs.parent, {
            'A': None,
            'B': 'A',
            'C': 'A',
            'D': 'B',
            'E': 'B',
            'F': 'C'
        })
        self.assertEqual(self.bfs.level, {
            'A': 0,
            'B': 1,
            'C': 1,
            'D': 2,
            'E': 2,
            'F': 2
        })

    def test_get_path(self):
        self.assertEqual(self.bfs.get_path('F'), ['A', 'C', 'F'])

    def test_get_level(self):
        self.assertEqual(self.bfs.get_level('F'), 2)


if __name__ == '__main__':
    unittest.main()