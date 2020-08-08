import curses
from pynput.keyboard import Key


from .utils import (
    clamp,
    BALL,
    RACKET_CHUNK,
    C_YELLOW_BLACK,
    C_WHITE_BLACK,
    around,
)


from .controler import Key_Hell


class Game:
    def __init__(self):
        # log
        self.log_file = open("log.txt", 'a')
        # Screen
        self.screen = curses.initscr()
        self.X_MAX, self.Y_MAX = self.screen.getmaxyx()
        self.screen.nodelay(True)
        curses.noecho()
        curses.curs_set(0)
        self.win = 0

        # Control
        self.keys = Key_Hell()

        # Colors
        curses.start_color()
        curses.init_pair(
            C_YELLOW_BLACK,
            curses.COLOR_YELLOW,
            curses.COLOR_BLACK
        )

        # Ball x vertical y horizontal
        self.bpos_x = self.X_MAX // 2
        self.bpos_y = 10
        self.bspeed_x = 2
        self.bspeed_y = 4

        # Player height
        self.player1 = self.X_MAX // 2
        self.player2 = self.X_MAX // 2
        self.bar_height = self.X_MAX // 3

    def run(self):
        # Ball
        self.bpos_x += self.bspeed_x
        self.bpos_y += self.bspeed_y

        # Racket
        if self.keys.map[Key.up]:
            self.player2 -= 1
        elif self.keys.map[Key.down]:
            self.player2 += 1
        if self.keys.map['a']:
            self.player1 -= 1
        elif self.keys.map['q']:
            self.player1 += 1

        self.hit()

    def hit(self):
        self.player1 = clamp(
            0 + self.bar_height // 2 + 1,
            self.player1,
            self.X_MAX - self.bar_height // 2 - 1
        )
        self.player2 = clamp(
            0 + self.bar_height // 2 + 1,
            self.player2,
            self.X_MAX - self.bar_height // 2 - 1
        )

        if self.bpos_x not in range(1, self.X_MAX - 1):
            self.bpos_x = clamp(1, self.bpos_x, self.X_MAX - 1)
            self.bspeed_x *= -1
        if self.bpos_y < 1:
            if self.bpos_x in around(self.player1, self.bar_height):
                self.bpos_y = 1
                self.bspeed_y *= -1
            else:
                self.win = 2
        elif self.bpos_y > self.Y_MAX - 2:
            if self.bpos_x in around(self.player2, self.bar_height):
                self.bpos_y = self.Y_MAX - 2
                self.bspeed_y *= -1
            else:
                self.win = 1

    def draw(self):
        self.screen.clear()
        self.draw_ball()
        self.draw_bars()
        self.screen.refresh()

    def draw_ball(self):
        self.screen.addch(
            self.bpos_x,
            self.bpos_y,
            BALL,
            curses.color_pair(C_WHITE_BLACK)
        )

    def draw_bars(self):
        range1 = around(self.player1, self.bar_height)
        range2 = around(self.player2, self.bar_height)
        for i in range(1, self.X_MAX):
            if i in range1:
                self.screen.addch(i, 0, RACKET_CHUNK)
            if i in range2:
                self.screen.addch(i, self.Y_MAX - 1, RACKET_CHUNK)

    def exit(self):
        self.log_file.close()
        curses.endwin()
        print("------End--------")
