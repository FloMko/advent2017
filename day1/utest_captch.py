import captcha
import unittest

class CapTest(unittest.TestCase):
    def test_return(self):
        self.assertIsInstance(captcha.output(), int)

if __name__ == '__main__' :
    unittest.main()
