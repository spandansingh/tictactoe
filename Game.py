
class TicTacToe():

	board = []
	sign1 = "",
	sign2 = ""
	boardDesign = [
		[0, 1, 2],
		[3, 4, 5],
		[6, 7, 8]
	]
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
	currentMove = -1
	currentPos = None
	currentSign = None
	moveCount = -1
	winningPattern = None

	def __init__(self, sign1, sign2):
		self.board = ["N"]*9
		self.sign1 = sign1
		self.sign2 = sign2


	def play1(self, pos):

		if self.currentMove == -1 or self.currentMove == 2:
			self.currentMove = 1
			self.play(self.sign1, pos)
		else:
			print("Invalid move by Player One, Now is player Two chance to move")
			exit()

	def play2(self, pos):
		if self.currentMove == -1 or self.currentMove == 1:
			self.currentMove = 2
			self.play(self.sign2, pos)
		else:
			print("Invalid Move by Player Two, Now is player One chance to move")
			exit()

	def play(self, sign, pos):
		
		self.currentPos = pos
		self.currentSign = sign

		if(self.board[pos] != "N"):
			print("Invalid move by Player "+ self.getPlayer() +" at position:", pos)
			exit()

		self.board[pos] = sign
		print("Player "+ self.getPlayer() + " puts " + sign + " at position " + str(pos))
		self.move()

	def move(self):
		
		self.moveCount += 1 

		if self.isResult():
			self.showResult()
			self.printBoard()

		elif self.isFull():
			print("\nGame Result : Its a Tie")
			self.printBoard()

	def isResult(self):
		
		i = -1
		for patterns in self.winning_patterns:
			i+=1

			if self.currentPos not in patterns:
				continue

			s = self.board[patterns[0]]
			
			if s != self.currentSign:
				continue

			flag = True
			for p in patterns[1:]:
				if self.board[p] == "N" or self.board[p] != s:
					flag = False
					break
			if(flag):
				self.winningPattern = patterns
				return True

		return False
			

	def showResult(self):
		print(
			"\nGame Result : \nPlayer "+ self.getPlayer() + 
			" wins by pattern -> " + str(self.winningPattern) + 
			" on move number " + str(self.moveCount)
		)

	def getPlayer(self):
		return self.currentSign == self.sign1 and "One" or "Two"  
		

	def isFull(self):
		return self.moveCount == 8

	def printBoard(self):
		print("\nBoard :\n")
		for pattern in self.boardDesign:
			for p in pattern:
				print(self.board[p]+" ", end = '')
			print("\n")
		self.exit()

	def exit(self):
		exit()

