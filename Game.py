
class TicTacToe():

	board = []
	winning_patterns = [
		[0, 1, 2],
		[3, 4, 5],
		[6, 7, 8],
		[0, 3, 6],
		[1, 4, 7],
		[2, 5, 8],
		[0, 4, 8],
		[2, 4, 6]
	]

	moveCount = 0

	def __init__(self):
		self.board = ["N"]*9

	def move(self, sign, pos):
		
		self.moveCount += 1 

		#Check if the position has occupied
		if(self.isOccupied(pos)):
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
		
		for pattern in self.winning_patterns:

			if pos not in pattern:
				continue

			t = filter(lambda x: self.board[x] != sign, pattern)
		
			if not list(t):
				return True

		return False

	def isOccupied(self, pos):
		return self.board[pos] != "N"

	def isFull(self):
		return self.moveCount == 9

