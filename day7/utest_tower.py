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
                ,('ehsqyyb', True, ['xtcdt', 'tujcuy', 'wiqohmb', 'cxdwmu'], 174))

    def test_aknowleg(self):
        """add leaf in set of child leaf"""
        print ( "id: " + self.id())
        self.assertEqual(tower.aknowleg(['kdsf','dfs','asd']), {'kdsf', 'dfs', 'asd'})

    def test_aknowleg_prog(self):
        """add prog in set of parent prog"""
        print ( "id: " + self.id())
        self.assertEqual(tower.aknowleg_prog('kdsf'), {'kdsf'})

    def test_find_root(self):
        """correct find root"""
        print ( "id: " + self.id())
        self.assertEqual(tower.root(), 'mkxke')

    def test_correct_sum(self):
        """detect unbalance parent and it's child"""
        print ( "id: " + self.id())
        self.assertEqual(tower.balance(
                {'zzzcrp':(100, True, ['dsmuem', 'xlpgtmn', 'rdcew']),
                    'dsmuem':(31, False, None),
                    'xlpgtmn':(31, False, None),
                    'rdcew':(31, False, None),
                })
                , 'zzcrp', True)

if __name__ == '__main__' :
    unittest.main()


