import tower
import unittest

class CapTest(unittest.TestCase):
    def test_input_store(self):
        """store input"""
        print ( "id: " + self.id())
        self.assertIsInstance(tower.indata(), list)

    def test_indata_chunk(self):
        """analyze leaf"""
        print ( "id: " + self.id())
        self.assertEqual(tower.chunk('ehsqyyb (174) -> xtcdt, tujcuy, wiqohmb, cxdwmu')
                ,('ehsqyyb', True, ['xtcdt', 'tujcuy', 'wiqohmb', 'cxdwmu']))

    def test_aknowleg(self):
        """add leaf in set of child leaf"""
        print ( "id: " + self.id())
        self.assertEqual(tower.aknowleg(['kdsf','dfs','asd']), {'kdsf', 'dfs', 'asd'})

    def test_aknowleg_prog(self):
        """add prog in set of parent prog"""
        print ( "id: " + self.id())
        self.assertEqual(tower.aknowleg_prog('kdsf'), {'kdsf'})

    def test_aknowleg_prog(self):
        """add prog in set of parent prog"""
        print ( "id: " + self.id())
        self.assertEqual(tower.aknowleg_prog('kdsf'), {'kdsf'})


if __name__ == '__main__' :
    unittest.main()


