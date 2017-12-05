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
        self.assertEqual(jump.turn([4,0,0,1]), 1)
    def test_case_negative(self):
        """correctly work with input"""
        print ( "id: " + self.id())
        self.assertEqual(jump.turn([2,0,-1,1]), 7)
    def test_case_turn(self):
        """correctly work with turn"""
        print ( "id: " + self.id())
        self.assertEqual(jump.turn([-1,0,0,0]), 10)
    def test_case_turn(self):
        """correctly work with turn"""
        print ( "id: " + self.id())
        self.assertEqual(jump.turn2([2,3,2,3,-1]), 10)

if __name__ == '__main__' :
    unittest.main()

