import numpy as np

class TicTacToe():

	board = None
	n = 3
	moveCount = 0
	gameType = None

	def __init__(self, gameType):
		self.gameType = gameType

		if self.gameType == "Simple":
			self.board = np.full(self.n ** 2, "N")

		elif self.gameType == "Numeric":
			self.board = np.full(self.n ** 2, 0)
		

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

	def isWon(self, sign, pos):
		
		board = np.reshape(self.board, (self.n, self.n))

		if self.gameType == "Simple":
			return self.isWonSimple(board, sign, pos)

		elif self.gameType == "Numeric":
			return self.isWonNumeric(board, sign, pos)

		return False

	def isWonNumeric(self, board, sign, pos):
		
		sum_to_win = 15

		#Check for all rows and columns
		for i in range(0, self.n):
			if np.sum(board[i,:]) == sum_to_win or np.sum(board[:,i]) == sum_to_win:
				return True
		
		#Check for diagonals 
		if np.sum(board.diagonal()) == sum_to_win: 
			return True

		#Check for antidiagonals
		if np.sum(np.fliplr(board).diagonal()) == sum_to_win:
			return True

		return False

	def isWonSimple(self, board, sign, pos):

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

		if self.gameType == "Simple":
			return self.board[pos] != "N"

		elif self.gameType == "Numeric":
			return self.board[pos] != 0

	def isFull(self):
		return self.moveCount == 9

