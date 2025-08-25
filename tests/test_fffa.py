import unittest
from fffa import fff
import numpy as np
from fffa.utils import read_tsp

class TestFFFA(unittest.TestCase):
    def test_small_matrix(self):
        graph = [
            [0, 2, 9, 10],
            [1, 0, 6, 4],
            [15, 7, 0, 8],
            [6, 3, 12, 0]
        ]
        best_cost, best_path = fff(graph, num_foxes=10, G=100)
        #print(best_cost, best_path)
        #print(type(best_path))
        # Just check return types for now
        self.assertIsInstance(best_path, np.ndarray)
        self.assertIsInstance(best_cost, (int, float))
        self.assertLess(best_cost, 100, f"Best cost {best_cost} is not less than 100")
        self.assertGreaterEqual(len(best_path), 2)

    def test_gr48(self):
        graph=read_tsp("data/gr48.tsp")
        best_cost, best_path = fff(graph, num_foxes=150, G=500)
        #print(best_cost, best_path)
        #print(type(best_path))
        # Just check return types for now
        self.assertIsInstance(best_path, np.ndarray)
        self.assertIsInstance(best_cost, (int, float))
        self.assertGreater(best_cost, 0, f"Best cost {best_cost} is not greater than 0")
        self.assertLess(best_cost, 9000, f"Best cost {best_cost} is not less than 9000")
        #self.assertGreaterEqual(len(best_path), 2)

    def test_gr666(self):
        graph=read_tsp("data/gr666.tsp")
        best_cost, best_path = fff(graph, num_foxes=150, G=500)
        #print(best_cost, best_path)
        #print(type(best_path))
        # Just check return types for now
        self.assertIsInstance(best_path, np.ndarray)
        self.assertIsInstance(best_cost, (int, float))
        self.assertGreater(best_cost, 0, f"Best cost {best_cost} is not greater than 0")
        self.assertLess(best_cost, 30000, f"Best cost {best_cost} is not less than 30,000")
        #self.assertGreaterEqual(len(best_path), 2)

    def test_hk48(self):
        graph=read_tsp("data/hk48.tsp")
        best_cost, best_path = fff(graph, num_foxes=150, G=500)
        #print(best_cost, best_path)
        #print(type(best_path))
        # Just check return types for now
        self.assertIsInstance(best_path, np.ndarray)
        self.assertIsInstance(best_cost, (int, float))
        self.assertGreater(best_cost, 0, f"Best cost {best_cost} is not greater than 0")
        self.assertLess(best_cost, 30000, f"Best cost {best_cost} is not less than 30000")
        #self.assertGreaterEqual(len(best_path), 2)

if __name__ == "__main__":
    unittest.main()
