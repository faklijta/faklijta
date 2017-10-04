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
        self.hero.update_entity(self.hero.hero_down)
        root.bind("<KeyPress>", self.on_key_press)
        canvas.pack()
        root.mainloop()


    def on_key_press(self, e):
        if ( e.keysym == 'Up' ):
            self.hero.update_entity(self.hero.hero_up)
            if self.map.is_wall(self.hero.x, self.hero.y - self.map.tile_size) == False:
                self.hero.move(0,- self.map.tile_size)
        elif( e.keysym == 'Down' ):
            self.hero.update_entity(self.hero.hero_down)
            if self.map.is_wall(self.hero.x, self.hero.y + self.map.tile_size) == False:
                self.hero.move(0, + self.map.tile_size)
        elif( e.keysym == 'Right' ):
            self.hero.update_entity(self.hero.hero_right)
            if self.map.is_wall(self.hero.x + self.map.tile_size, self.hero.y) == False:
                self.hero.move(+ self.map.tile_size, 0)
        elif( e.keysym == 'Left' ):
            self.hero.update_entity(self.hero.hero_left)
            if self.map.is_wall(self.hero.x - self.map.tile_size, self.hero.y) == False:
                self.hero.move(- self.map.tile_size, 0)
            

game = Game()