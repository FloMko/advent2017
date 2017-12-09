import realloc
import unittest


class CapTest(unittest.TestCase):
    def test_input_store(self):
        """store input"""
        print ("id: " + self.id())
        self.assertIsInstance(realloc.indata(), list)

    def test_case_max(self):
        """correctly find max index"""
        print ("id: " + self.id())
        self.assertEqual(realloc.maxfind([0, 2, 7, 7]), (7, 2))

    def test_case_equal(self):
        """detect loop"""
        print ("id: " + self.id())
        self.assertEqual(realloc.detect(
            [0, 2, 7, 7], [[0, 2, 7, 6], [0, 2, 7, 7]]), False)

    def test_case_equal2(self):
        """detect loop"""
        print ("id: " + self.id())
        self.assertEqual(realloc.detect(
            [0, 2, 7, 7], [[0, 2, 7, 6], [0, 2, 7, 3]]), True)

    def test_case_distribute(self):
        """realloc memory"""
        print ("id: " + self.id())
        self.assertEqual(realloc.distribute([0, 2, 7, 0]), [2, 4, 1, 2])

    def test_case_aknowleged(self):
        """detect loop"""
        print ("id: " + self.id())
        self.assertEqual(realloc.aknowleg([2, 3, 0, 0],[[]]), [[],[2, 3, 0, 0]])

    def test_case_aknowleged2(self):
        """detect loop"""
        print ("id: " + self.id())
        self.assertEqual(realloc.aknowleg([2, 4, 1, 1], [[],[2, 3, 0, 0]]), [
                         [],[2, 3, 0, 0], [2, 4, 1, 1]])

    def test_case_final(self):
        """correctly work with input"""
        print ("id: " + self.id())
        self.assertEqual(realloc.stepcount([0, 2, 7, 0]), 5)


if __name__ == '__main__':
    unittest.main()
