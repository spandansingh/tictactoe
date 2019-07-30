from Game import TicTacToe

if __name__ == '__main__':

	Game = TicTacToe()

	#Whichever sign moves first will automatically becomes player 1 sign

	print(Game.move("X",0))
	print(Game.move("O",4))

	print(Game.move("X",6))
	print(Game.move("O",3))

	print(Game.move("X",5))
	print(Game.move("O",7))

	print(Game.move("X",8))
	print(Game.move("O",1))

	print(Game.move("X",2))