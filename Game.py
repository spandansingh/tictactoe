import numpy as np
from abc import ABC, abstractmethod

class TicTacToe(ABC):

	board = None
	n = 3
	moveCount = 0
	default_char = None

	def __init__(self):
		self.board = np.full(self.n ** 2, self.default_char)

	def move(self, sign, pos):
		
		self.moveCount += 1 

		#Check if the position has occupied
		if self.isOccupied(pos):
			return (False, 'Occupied')

		self.board[pos] = sign

		#Check if anybody has won
		if(self.isWon(sign, pos)):
			return (True, 'Won')

		#Check if the board is full
		if self.isFull():
			return (True, 'Tie')

		return (True, 'Continue')

	@abstractmethod
	def isWon(self, sign, pos):
		pass

	def isOccupied(self, pos):
		return self.board[pos] != self.default_char

	def isFull(self):
		return self.moveCount == self.n ** 2



class SimpleTicTacToe(TicTacToe):

	default_char = "N"

	def isWon(self, sign, pos):

		board = np.reshape(self.board, (self.n, self.n))

		#Check for all rows and columns
		for i in range(0, self.n):
			if np.all(board[i,:] == sign) or np.all(board[:,i] == sign):
				return True
		
		#Check for diagonals 
		if np.all(board.diagonal() == sign): 
			return True

		#Check for antidiagonals
		if np.all(np.fliplr(board).diagonal() == sign):
			return True

		return False


class NumericTicTacToe(TicTacToe):

	default_char = 0
	sum_to_win = 15

	def isWon(self, sign, pos):

		board = np.reshape(self.board, (self.n, self.n))

		#Check for all rows and columns
		for i in range(0, self.n):
			if np.sum(board[i,:]) == self.sum_to_win or np.sum(board[:,i]) == self.sum_to_win:
				return True
		
		#Check for diagonals 
		if np.sum(board.diagonal()) == self.sum_to_win: 
			return True

		#Check for antidiagonals
		if np.sum(np.fliplr(board).diagonal()) == self.sum_to_win:
			return True

		return False



