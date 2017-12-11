import knot
import unittest


class CapTest(unittest.TestCase):
    def test_input_store(self):
        """store input"""
        print ("id: " + self.id())
        self.assertIsInstance(knot.indata(), list)

    def test_reverse_section(self):
        """
        get circular list, position in list and lenght of reverse
        return modified list
        """
        print ("id: " + self.id())
        self.assertEqual(knot.reverse([0, 1, 2, 3, 4], 0, 3), [2,1,0,3,4])



if __name__ == '__main__':
    unittest.main()

