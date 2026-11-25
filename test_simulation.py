import unittest
from simulation import simulate
class TestModel(unittest.TestCase):
    def test_bounds(self):
        for r in simulate():
            self.assertGreaterEqual(r["q"],0)
            for k in ("a","d","u","risk"):
                self.assertTrue(0<=r[k]<=1)
    def test_backlog(self):
        self.assertEqual(simulate(g=5,v=100)[-1]["q"],0)
        self.assertGreater(simulate(g=100,v=0)[-1]["q"],0)
    def test_determinism(self):
        self.assertEqual(simulate(),simulate())
    def test_invalid(self):
        with self.assertRaises(ValueError): simulate(g=-1)
if __name__=="__main__": unittest.main()
