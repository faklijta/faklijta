from tkinter import *

class Entity(object):

    def __init__(self):
        self.x = x
        self.y = y

class Hero(object):
    
    def __init__(self, canvas):
        self.hero = None
        self.x = 0
        self.y = 0
        self.hero_down = PhotoImage(file="hero-down.png")
        self.hero_up = PhotoImage(file="hero-up.png")
        self.hero_left = PhotoImage(file="hero-left.png")
        self.hero_right = PhotoImage(file="hero-right.png")
        self.canvas = canvas

    def draw_entity(self, x, y):
        self.hero = self.canvas.create_image(x, y, anchor=NW, image = self.hero_down)
        
    def update_entity(self, img):
        self.img = img
        self.canvas.itemconfigure(self.hero, image = self.img)

    def move(self, dx, dy):
        self.canvas.move(self.hero, dx, dy)
