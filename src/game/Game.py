from tkinter import Tk, Canvas

from src.game.Player import Player

PLAYER_X_START = 200
PLAYER_Y_START = 200


class Game :

    def __init__(self):
        self.frame = Tk()
        self.canvas = Canvas(self.frame, width=1000, height=1000, background="black")
        self.rectangle = self.createPlayer()
        self.player = Player(PLAYER_X_START, PLAYER_Y_START)
        self.key_pressed = {}
        self.set_bindings()
        self.animate()
        self.canvas.pack()
        self.frame.mainloop()

    def animate(self):
        print(self.key_pressed)
        if self.key_pressed['z']: self.up()
        if self.key_pressed['q']: self.left()
        if self.key_pressed['s']: self.down()
        if self.key_pressed['d']: self.right()
        self.frame.after(10, self.animate)

    def createPlayer(self):
        return self.canvas.create_rectangle((PLAYER_X_START, PLAYER_Y_START), (50, 50), fill='blue')

    def set_bindings(self):
        self.frame.bind('<KeyPress-x>', self.pressed)
        for char in ['z', 'q', 's', 'd']:
            print("coucou %s" % char)
            self.frame.bind('<KeyPress-%s>' % char, self.pressed)
            self.frame.bind('<KeyRelease-%s>' % char, self.released)
            self.key_pressed[char] = False

    def pressed(self, event):
        self.key_pressed[event.char] = True

    def released(self, event):
        self.key_pressed[event.char] = False

    def left(self):
        self.player.posX -= 10
        self.canvas.move(self.rectangle, -10, 0)

    def right(self):
        self.player.posY += 10
        self.canvas.move(self.rectangle, 10, 0)

    def up(self):
        self.player.posY -= 10
        self.canvas.move(self.rectangle, 0, -10)

    def down(self):
        self.player.posX += 10
        self.canvas.move(self.rectangle, 0, 10)


Game()