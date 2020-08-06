import time
import curses


from .game import Game


print("Preparing to initialize screen...")
game = Game()
start = time.time()
while not game.win:
    game.draw()
    game.run()
    curses.napms(60)
game.exit()
print(f"Player {game.win} win!")
