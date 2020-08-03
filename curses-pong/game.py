import curses


from .utils import clamp


class Game:
    def __init__(self):
        # Crash dump
        self.crashed = False
        self.where = "nowhere"

        # Screen
        self.screen = curses.initscr()
        self.X_MAX, self.Y_MAX = self.screen.getmaxyx()

        # Ball /!\ Warning in curse x, y pos in inverted
        self.bpos_x = 10
        self.bpos_y = 10
        self.bspeed_x = 1
        self.bspeed_y = 2

    def run(self):
        self.bpos_x += self.bspeed_x
        self.bpos_y += self.bspeed_y
        self.hit()

    def draw(self):
        try:
            self.screen.clear()
            self.screen.addch(self.bpos_x, self.bpos_y, "■")
            self.screen.refresh()
        except Exception:
            self.crashed = True
            self.where = "draw"

    def hit(self):
        if self.bpos_x not in range(1, self.X_MAX):
            self.bpos_x = clamp(0, self.bpos_x, self.X_MAX - 1)
            self.bspeed_x *= -1
        if self.bpos_y not in range(1, self.Y_MAX):
            self.bpos_y = clamp(0, self.bpos_y, self.Y_MAX - 1)
            self.bspeed_y *= -1

    def exit(self):
        curses.endwin()
        print("------End--------")
        if self.crashed:
            print("Curse crashed in {}".format(self.where))
        else:
            print("Window ended.")
