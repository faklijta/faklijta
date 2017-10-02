from tkinter import *
from mymap import Map
from entity import Hero


class Game(object):

    def __init__(self):
        root = Tk()
        canvas_height = 720
        canvas_width = 720
        canvas = Canvas(root, width=canvas_width, height=canvas_height)
        self.map = Map()
        self.map.draw_map(canvas)
        self.hero = Hero(canvas)
        self.hero.draw_entity(0, 0)
        root.bind("<KeyPress>", self.on_key_press)
        canvas.pack()
        root.mainloop()


    def on_key_press(self, e):
        if ( e.keysym == 'Up' ):
            self.hero.move(0,-72)
        elif( e.keysym == 'Down' ):
            self.hero.move(0,72)
        elif( e.keysym == 'Right' ):
            self.hero.move(72,0)
        elif( e.keysym == 'Left' ):
            self.hero.move(-72,0)

game = Game()