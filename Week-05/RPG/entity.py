from tkinter import *
import random
from mymap import Map

class Entity(object):


    def __init__(self, canvas):
        self.canvas = canvas
        

class Hero(Entity):
    
    def __init__(self, canvas):
        self.hero = None
        self.x = 0
        self.y = 0
        self.hero_down = PhotoImage(file="hero-down.png")
        self.hero_up = PhotoImage(file="hero-up.png")
        self.hero_left = PhotoImage(file="hero-left.png")
        self.hero_right = PhotoImage(file="hero-right.png")
        self.canvas = canvas


    def draw_hero(self, x, y):
        self.hero = self.canvas.create_image(x, y, anchor=NW, image = self.hero_down)

        
    def update_entity(self, img):
        self.img = img
        self.canvas.itemconfigure(self.hero, image = self.img)


    def move(self, dx, dy):
        self.canvas.move(self.hero, dx, dy)
        self.x += dx
        self.y += dy


class Skeleton(Entity):


    def __init__(self, canvas):
        self.skeleton_image = None
        # self.x = 0
        # self.y = 0
        self.skeleton_file = PhotoImage(file="skeleton.png")
        self.canvas = canvas

        
    def draw_skeleton(self, coordinates):
        for i in range(len(coordinates)):
            self.skeleton = self.canvas.create_image(coordinates[i][0], coordinates[i][1], anchor=NW, image=self.skeleton_file)


class Boss(Entity):


    def __init__(self, canvas):
        self.boss_image = None
        self.boss_file = PhotoImage(file = "boss.png")
        self.canvas = canvas


    def draw_boss(self, coordinates):
        self.boss = self.canvas.create_image(coordinates[0], coordinates[1], anchor=NW, image=self.boss_file)
   