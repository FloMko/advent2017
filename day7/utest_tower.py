import tower
import unittest

class CapTest(unittest.TestCase):
    def test_input_store(self):
        """store input"""
        print ( "id: " + self.id())
        self.assertIsInstance(tower.indata(), list)
    def test_indata_chunk(self):
        """detect loop"""
        print ( "id: " + self.id())
        self.assertEqual(tower.chunk('ehsqyyb (174) -> xtcdt, tujcuy, wiqohmb, cxdwmu'
            ),[ehsqyyb, 174, True])

if __name__ == '__main__' :
    unittest.main()


