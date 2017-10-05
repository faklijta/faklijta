from tkinter import *
from mymap import Map, Hud
from entity import Hero, Skeleton, Boss


class Game(object):

    def __init__(self):
        root = Tk()
        canvas_height = 700
        canvas_width = 720
        canvas = Canvas(root, width=canvas_width, height=canvas_height)
        self.map = Map()
        self.map.draw_map(canvas)
        self.hero = Hero(canvas)
        self.hero.draw_hero(0, 0)
        self.hero.update_entity(self.hero.hero_down)
        self.skeleton = Skeleton(canvas)
        self.boss = Boss(canvas)
        self.skel_num = 3
        self.coordinates = self.map.create_random_coordinates(self.skel_num + 1)
        self.skeleton.draw_skeleton(self.coordinates[:-1])
        self.boss.draw_boss(self.coordinates[-1])
        self.hud = Hud()
        self.hud.draw_hud(canvas, 0, 650)
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