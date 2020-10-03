import unittest
from quadratic_equation import Quad

class TestQuad(unittest.TestCase):
	def testQuad(self):
		roots = [-1.0] # D==0
		self.assertEqual(Quad.Quad(2,4,2), roots, "Should be [-1.0]")

		roots = [-1.0, -3.0] # D>0
		self.assertEqual(Quad.Quad(1,4,3), roots, "Should be [-1.0, -3.0]")

		roots = [] # D<0
		self.assertEqual(Quad.Quad(1,2,3), roots, "Should be []")

