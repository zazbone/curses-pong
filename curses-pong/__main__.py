import time
import curses


from .game import Game


print("Preparing to initialize screen...")
game = Game()
start = time.time()
while True:
    game.draw()
    game.run()
    if game.win:
        break
    curses.napms(60)
game.exit()
print(f"Player {game.win} win!")
