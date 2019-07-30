import unittest 

import sys 
sys.path.append('..')

from Game import TicTacToe

class TestSimple(unittest.TestCase): 

	# Returns True or False.
	def testWon(self): 
		Game = TicTacToe("Numeric")

		r = Game.move(3, 0)
		self.assertTrue(r[0])
		self.assertEqual(r[1], 'Continue')

		r = Game.move(4, 1)
		self.assertTrue(r[0])
		self.assertEqual(r[1], 'Continue')

		r = Game.move(9, 6)
		self.assertTrue(r[0])
		self.assertEqual(r[1], 'Continue')

		r = Game.move(6, 5)
		self.assertTrue(r[0])
		self.assertEqual(r[1], 'Continue')

		r = Game.move(5, 3)
		self.assertTrue(r[0])
		self.assertEqual(r[1], 'Continue')

		r = Game.move(8, 2)
		self.assertTrue(r[0])
		self.assertEqual(r[1], 'Won')

	def testTie(self):
		Game = TicTacToe("Numeric")

		r = Game.move(2, 0)
		self.assertTrue(r[0])
		self.assertEqual(r[1], 'Continue')

		r = Game.move(3, 4)
		self.assertTrue(r[0])
		self.assertEqual(r[1], 'Continue')

		r = Game.move(4, 5)
		self.assertTrue(r[0])
		self.assertEqual(r[1], 'Continue')

		r = Game.move(7, 2)
		self.assertTrue(r[0])
		self.assertEqual(r[1], 'Continue')

		r = Game.move(6, 3)
		self.assertTrue(r[0])
		self.assertEqual(r[1], 'Continue')

		r = Game.move(9, 1)
		self.assertTrue(r[0])
		self.assertEqual(r[1], 'Continue')

		r = Game.move(8, 8)
		self.assertTrue(r[0])
		self.assertEqual(r[1], 'Continue')

		r = Game.move(1, 7)
		self.assertTrue(r[0])
		self.assertEqual(r[1], 'Continue')

		r = Game.move(10, 6)
		self.assertTrue(r[0])
		self.assertEqual(r[1], 'Tie')

	def testOccupied(self):
		Game = TicTacToe("Numeric")

		r = Game.move(2, 0)
		self.assertTrue(r[0])
		self.assertEqual(r[1], 'Continue')

		r = Game.move(5, 4)
		self.assertTrue(r[0])
		self.assertEqual(r[1], 'Continue')

		r = Game.move(7, 6)
		self.assertTrue(r[0])
		self.assertEqual(r[1], 'Continue')

		r = Game.move(6, 0)
		self.assertFalse(r[0])
		self.assertEqual(r[1], 'Occupied')

	def testDiagonal(self):
		Game = TicTacToe("Numeric")

		r = Game.move(4, 0)
		self.assertTrue(r[0])
		self.assertEqual(r[1], 'Continue')

		r = Game.move(5, 4)
		self.assertTrue(r[0])
		self.assertEqual(r[1], 'Continue')

		r = Game.move(2, 3)
		self.assertTrue(r[0])
		self.assertEqual(r[1], 'Continue')

		r = Game.move(7, 2)
		self.assertTrue(r[0])
		self.assertEqual(r[1], 'Continue')

		r = Game.move(6, 8)
		self.assertTrue(r[0])
		self.assertEqual(r[1], 'Won')

	def testAntiDiagonal(self):
		Game = TicTacToe("Numeric")

		r = Game.move(2, 0)
		self.assertTrue(r[0])
		self.assertEqual(r[1], 'Continue')

		r = Game.move(3, 4)
		self.assertTrue(r[0])
		self.assertEqual(r[1], 'Continue')

		r = Game.move(4, 5)
		self.assertTrue(r[0])
		self.assertEqual(r[1], 'Continue')

		r = Game.move(7, 2)
		self.assertTrue(r[0])
		self.assertEqual(r[1], 'Continue')

		r = Game.move(6, 3)
		self.assertTrue(r[0])
		self.assertEqual(r[1], 'Continue')

		r = Game.move(9, 1)
		self.assertTrue(r[0])
		self.assertEqual(r[1], 'Continue')

		r = Game.move(8, 8)
		self.assertTrue(r[0])
		self.assertEqual(r[1], 'Continue')

		r = Game.move(5, 6)
		self.assertTrue(r[0])
		self.assertEqual(r[1], 'Won')


if __name__ == '__main__': 
	unittest.main()