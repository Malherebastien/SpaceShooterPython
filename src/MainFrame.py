from tkinter import Tk


class MainFrame:

    def __init__(self, couleur):
        self.frame = Tk()
        self.frame.configure(background=couleur)
        self.frame.mainloop()

