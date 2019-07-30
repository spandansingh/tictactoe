import numpy as np

class TicTacToe():

	board = []
	n = 3
	moveCount = 0

	def __init__(self):
		self.board = np.full(self.n ** 2, "N")

	def move(self, sign, pos):
		
		self.moveCount += 1 

		#Check if the position has occupied
		if self.isOccupied(pos):
			return (False, 'Occupied')

		self.board[pos] = sign
		
		#Check if the board is full
		if self.isFull():
			return (True, 'Tie')

		#Check if anybody has won
		if(self.isWon(sign, pos)):
			return (True, 'Won')

		return (True, 'Continue')

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

	def isOccupied(self, pos):
		return self.board[pos] != "N"

	def isFull(self):
		return self.moveCount == 9

