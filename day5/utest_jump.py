import jump
import unittest

class CapTest(unittest.TestCase):
    def test_input_store(self):
        """store input"""
        print ( "id: " + self .id())
        self.assertIsInstance(jump.input(), list)
    def test_case(self):
        """correctly work with input"""
        print ( "id: " + self .id())
        self.assertEqual(jump.change([5,0,0,1]), [6,0,0,1])

if __name__ == '__main__' :
    unittest.main()

