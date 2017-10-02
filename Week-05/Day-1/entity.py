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
        self.hero_file = PhotoImage(file="hero-down.png")
        self.canvas = canvas

    def draw_entity(self, x, y):
        self.hero = self.canvas.create_image(x, y, anchor=NW, image = self.hero_file)

    def move(self, dx, dy):
        self.canvas.move(self.hero, dx, dy)
