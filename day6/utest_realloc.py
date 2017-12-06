import realloc
import unittest

class CapTest(unittest.TestCase):
    def test_input_store(self):
        """store input"""
        print ( "id: " + self.id())
        self.assertIsInstance(realloc.indata(), list)
    def test_case_max(self):
        """correctly find max index"""
        print ( "id: " + self.id())
        self.assertEqual(realloc.maxfind([0,2,7,7]), (7,2)) 
    def test_case_final(self):
        """correctly work with input"""
        print ( "id: " + self.id())
        self.assertEqual(realloc.main([0,2,7,0]), 5)

if __name__ == '__main__' :
    unittest.main()

