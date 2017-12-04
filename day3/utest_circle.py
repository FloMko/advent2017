import circle
import unittest

class CapTest(unittest.TestCase):
    def test_find_neighbors(self):
        """find max value from list"""
        print ( "id: " + self.id())
        self.assertEqual(circle.neighbors([[7, 0, 0], [0, 0, 0], [0, 0, 1]]), 1)
    def test_find_neighbors2(self):
        """find max value from list"""
        print ( "id: " + self.id())
        self.assertEqual(circle.neighbors([[0, 7, 0], [0, 0, 0], [0, 0, 1]]), 8)
    def test_set_num(self):
        """find max value from list"""
        print ( "id: " + self.id())
        self.assertEqual(circle.set_node([[0, 7, 0], [0, 0, 0], [0, 0, 1]]), [[1, 0, 0], [0, 0, 0], [0, 0, 1]])

if __name__ == '__main__' :
    unittest.main()
