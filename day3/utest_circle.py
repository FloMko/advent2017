import circle
import unittest

class CapTest(unittest.TestCase):
    def test_find_neighbors(self):
        """find max value from list"""
        print ( "id: " + self.id())
        self.assertEqual(circle.neighbors([[7, 0, 0], [0, 0, 0], [0, 0, 1]]), 8)


if __name__ == '__main__' :
    unittest.main()
