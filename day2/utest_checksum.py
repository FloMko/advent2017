import checksum
import unittest

class CapTest(unittest.TestCase):
    def test_indata_store(self):
        """store input"""
        print ( "id: " + self.id())
        self.assertIsInstance(checksum.indata(), list)
    def test_middata_return(self):
        """create list for work with data"""
        print ( "id: " + self.id())
        self.assertIsInstance(checksum.middata(checksum.indata()), list)
    def test_filtered_return(self):
        """output should be int"""
        print ( "id: " + self.id())
        self.assertIsInstance(checksum.main(), int)
    def test_find_max(self):
        """find max value from list"""
        print ( "id: " + self.id())
        self.assertEqual(checksum.maxof([9,3,1,8]), 9)
    def test_find_min(self):
        """find max value from list"""
        print ( "id: " + self.id())
        self.assertEqual(checksum.minof([9,3,1,8]), 1)
    def test_case(self):
        """correctly work with input"""
        print ( "id: " + self.id())
        self.assertEqual(checksum.work([9,3,1,8]), 8)
if __name__ == '__main__' :
    unittest.main()

