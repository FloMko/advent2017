import captcha
import unittest

class CapTest(unittest.TestCase):
    def test_output_return(self):
        """output should be int"""
        print ( "id: " + self .id())
        self.assertIsInstance(captcha.output(), int)
    
    def test_case(self):
        """correctly work with input"""
        print ( "id: " + self .id())
        self.assertEqual(captcha.work('11'), 1)


if __name__ == '__main__' :
    unittest.main()
