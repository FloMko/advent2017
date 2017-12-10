import register
import unittest


class CapTest(unittest.TestCase):
    def test_input_store(self):
        """store input"""
        print ("id: " + self.id())
        self.assertIsInstance(register.indata(), list)

    def test_indata_chunk(self):
        """analyze leaf"""
        print ("id: " + self.id())
        self.assertEqual(register.collect(
            'b inc 5 if a > 1',
            'a inc 1 if b < 5',
            'c dec -10 if a >= 1',
            'c inc -20 if c == 10',
        ), {'a': 0, 'b': 0, 'c': 0})


if __name__ == '__main__':
    unittest.main()
