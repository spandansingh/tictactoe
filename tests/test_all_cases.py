import unittest 

import sys 
sys.path.append('..')

from Game import TicTacToe

class TestAllCases(unittest.TestCase): 

	# Returns True or False.
	def testWon(self): 
		Game = TicTacToe()

		r = Game.move("X", 0)
		self.assertTrue(r[0])
		self.assertEqual(r[1], 'Continue')

		r = Game.move("O", 4)
		self.assertTrue(r[0])
		self.assertEqual(r[1], 'Continue')

		r = Game.move("X", 1)
		self.assertTrue(r[0])
		self.assertEqual(r[1], 'Continue')

		r = Game.move("O", 3)
		self.assertTrue(r[0])
		self.assertEqual(r[1], 'Continue')

		r = Game.move("X", 2)
		self.assertTrue(r[0])
		self.assertEqual(r[1], 'Won')

	def testTie(self):
		Game = TicTacToe()

		r = Game.move("X", 0)
		self.assertTrue(r[0])
		self.assertEqual(r[1], 'Continue')

		r = Game.move("O", 4)
		self.assertTrue(r[0])
		self.assertEqual(r[1], 'Continue')

		r = Game.move("X", 6)
		self.assertTrue(r[0])
		self.assertEqual(r[1], 'Continue')

		r = Game.move("O", 3)
		self.assertTrue(r[0])
		self.assertEqual(r[1], 'Continue')

		r = Game.move("X", 5)
		self.assertTrue(r[0])
		self.assertEqual(r[1], 'Continue')

		r = Game.move("O", 7)
		self.assertTrue(r[0])
		self.assertEqual(r[1], 'Continue')

		r = Game.move("X",8)
		self.assertTrue(r[0])
		self.assertEqual(r[1], 'Continue')

		r = Game.move("O", 2)
		self.assertTrue(r[0])
		self.assertEqual(r[1], 'Continue')

		r = Game.move("O", 1)
		self.assertTrue(r[0])
		self.assertEqual(r[1], 'Tie')

	def testOccupied(self):
		Game = TicTacToe()

		r = Game.move("X", 0)
		self.assertTrue(r[0])
		self.assertEqual(r[1], 'Continue')

		r = Game.move("O", 4)
		self.assertTrue(r[0])
		self.assertEqual(r[1], 'Continue')

		r = Game.move("X", 6)
		self.assertTrue(r[0])
		self.assertEqual(r[1], 'Continue')

		r = Game.move("O", 0)
		self.assertFalse(r[0])
		self.assertEqual(r[1], 'Occupied')

	def testDiagonal(self):
		Game = TicTacToe()

		r = Game.move("X", 0)
		self.assertTrue(r[0])
		self.assertEqual(r[1], 'Continue')

		r = Game.move("O", 3)
		self.assertTrue(r[0])
		self.assertEqual(r[1], 'Continue')

		r = Game.move("X", 8)
		self.assertTrue(r[0])
		self.assertEqual(r[1], 'Continue')

		r = Game.move("O", 6)
		self.assertTrue(r[0])
		self.assertEqual(r[1], 'Continue')

		r = Game.move("X", 4)
		self.assertTrue(r[0])
		self.assertEqual(r[1], 'Won')

	def testAntiDiagonal(self):
		Game = TicTacToe()

		r = Game.move("X", 2)
		self.assertTrue(r[0])
		self.assertEqual(r[1], 'Continue')

		r = Game.move("O", 1)
		self.assertTrue(r[0])
		self.assertEqual(r[1], 'Continue')

		r = Game.move("X", 6)
		self.assertTrue(r[0])
		self.assertEqual(r[1], 'Continue')

		r = Game.move("O", 5)
		self.assertTrue(r[0])
		self.assertEqual(r[1], 'Continue')

		r = Game.move("X", 4)
		self.assertTrue(r[0])
		self.assertEqual(r[1], 'Won')

if __name__ == '__main__': 
	unittest.main()