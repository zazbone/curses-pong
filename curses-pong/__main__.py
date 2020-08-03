import time
import curses


from .game import Game


print("Preparing to initialize screen...")
game = Game()
start = time.time()
while time.time() - start < 10:
    try:
        game.draw()
        game.run()
        curses.napms(30)
        if game.crashed:
            break
    except Exception:
        game.crashed = True
        game.where = "Main loop"
game.exit()
