import captcha
import unittest

class CapTest(unittest.TestCase):
    def test_input_store(self):
        """store input"""
        print ( "id: " + self .id())
        self.assertIsInstance(captcha.input(), str)
    def test_output_return(self):
        """output should be int"""
        print ( "id: " + self .id())
        self.assertIsInstance(captcha.output(), int)
    def test_striped_return(self):
        """strip return should be list"""
        print ( "id: " + self .id())
        self.assertIsInstance(captcha.striped(123), list)    
    def test_case(self):
        """correctly work with input"""
        print ( "id: " + self .id())
        self.assertEqual(captcha.work('111'), 1)

    def test_case2(self):
        """correctly work with input"""
        print ( "id: " + self .id())
        self.assertEqual(captcha.work('1122'), 3)

    def test_filtered(self):
        """retirn sum as intered"""
        print ( "id: " + self .id())
        self.assertIsInstance(captcha.filter(), int)

if __name__ == '__main__' :
    unittest.main()
