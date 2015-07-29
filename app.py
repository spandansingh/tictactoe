from Game import TicTacToe

if __name__ == '__main__':

	player1Sign = "X"
	player2Sign = "O"

	Game = TicTacToe(player1Sign, player2Sign)
	
	Game.play1(0)
	Game.play2(4)
	
	Game.play1(6)
	Game.play2(3)
	
	Game.play1(5)
	Game.play2(7)

	Game.play1(8)
	Game.play2(1)
	
	Game.play1(2)