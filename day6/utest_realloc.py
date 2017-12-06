import realloc
import unittest

class CapTest(unittest.TestCase):
    def test_input_store(self):
        """store input"""
        print ( "id: " + self.id())
        self.assertIsInstance(realloc.indata(), list)
    def test_case(self):
        """correctly work with input"""
        print ( "id: " + self.id())
        self.assertEqual(realloc.turn([0,2,7,0]), 5)

if __name__ == '__main__' :
    unittest.main()

