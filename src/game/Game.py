from tkinter import Tk, Canvas


class Game :

    def __init__(self):
        self.frame = Tk()
        self.canvas = Canvas(self.frame, background="black")

    def createPlayer(self):
        while 1:
            player = self.canvas.create_rectangle((200,200), (50,50), fill='blue')
            self.canvas.move(player, 10, 10)

            self.canvas.move(player, 150, 150)