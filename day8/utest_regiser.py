import register
import unittest

class CapTest(unittest.TestCase):
    def test_input_store(self):
        """store input"""
        print ( "id: " + self.id())
        self.assertIsInstance(register.indata(), list)

if __name__ == '__main__' :
    unittest.main()
