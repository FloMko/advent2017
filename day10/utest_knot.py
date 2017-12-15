import knot
import unittest
from collections import deque


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
        self.assertEqual(knot.reverse(deque([0, 1, 2, 3, 4]), 0, 3), deque([2,1,0,3,4]))
    
    def test_reverse_section_out_of_list(self):
        """
        get circular list, position in list and lenght of reverse
        return modified list
        """
        print ("id: " + self.id())
        self.assertEqual(knot.reverse(deque([2,1,0,3,4]), 3, 4), deque([4,3,0,1,2]))

    def test_xor(self):
        """
        get sparse hash, return xored sparse hash
        """
        print ("id: " + self.id())
        self.assertEqual(knot.xor([65,27,9,1,4,3,40,50,91,7,6,0,2,5,68,22]), 64)


if __name__ == '__main__':
    unittest.main()

