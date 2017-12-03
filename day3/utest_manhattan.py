import manhattan
import unittest

class CapTest(unittest.TestCase):
    def test_find_way_up(self):
        """find max value from list"""
        print ( "id: " + self.id())
        self.assertEqual(checksum.findway(23), 2)
    def test_find_way_left(self):
        """find max value from list"""
        print ( "id: " + self.id())
        self.assertEqual(checksum.findway(11), 2)
    def test_find_way_common(self):
        """find max value from list"""
        print ( "id: " + self.id())
        self.assertEqual(checksum.findway(1024), 31)

if __name__ == '__main__' :
    unittest.main()
