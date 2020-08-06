from pynput import keyboard
from pynput.keyboard import Key


class Key_Hell:
    def __init__(self):
        self.map = {
            Key.up: False,
            Key.down: False,
            'a': False,
            'q': False
        }
        listener = keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release)
        listener.start()

    def on_press(self, key):
        if key in self.map.keys():
            self.map[key] = True
        elif key.char in self.map.keys():
            self.map[key.char] = True

    def on_release(self, key):
        if key in self.map.keys():
            self.map[key] = False
        elif key.char in self.map.keys():
            self.map[key.char] = False
