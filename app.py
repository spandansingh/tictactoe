from Game import TicTacToe

if __name__ == '__main__':

	# Game = TicTacToe("Simple") # Simple or Numeric

	# #Whichever sign moves first will automatically becomes player 1 sign

	# print(Game.move("X",0))
	# print(Game.move("O",4))

	# print(Game.move("X",6))
	# print(Game.move("O",3))

	# print(Game.move("X",5))
	# print(Game.move("O",7))

	# print(Game.move("X",8))
	# print(Game.move("O",1))

	Game = TicTacToe("Numeric")

	print(Game.move(3, 0))
	print(Game.move(4, 1))
	print(Game.move(9, 6))
	print(Game.move(6, 5))
	print(Game.move(5, 3))
	print(Game.move(8, 2))