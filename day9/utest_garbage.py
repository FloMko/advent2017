import garbage
import unittest


class CapTest(unittest.TestCase):
    def test_input_store(self):
        """store input"""
        print ("id: " + self.id())
        self.assertIsInstance(garbage.indata(), str)

    def test_rewrite_input(self):
        """chain input to store"""
        print ("id: " + self.id())
        self.assertEqual(garbage.rewrite('<!>{}{{{}!>>'), '<>')

    def test_count_score(self):
        """lets count"""
        print ("id: " + self.id())
        self.assertEqual(garbage.score('{{{}}}'), 6)


if __name__ == '__main__':
    unittest.main()
