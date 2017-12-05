import jump
import unittest

class CapTest(unittest.TestCase):
    def test_input_store(self):
        """store input"""
        print ( "id: " + self.id())
        self.assertIsInstance(jump.indata(), list)
    def test_case(self):
        """correctly work with input"""
        print ( "id: " + self.id())
        self.assertEqual(jump.change([4,0,0,1]), ([5,0,0,1], 5))
    def test_case_negative(self):
        """correctly work with input"""
        print ( "id: " + self.id())
        self.assertEqual(jump.change([4,0,-1,1], 2), ([4,0,0,1], -1))

if __name__ == '__main__' :
    unittest.main()

