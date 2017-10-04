from tkinter import *
import random

class Entity(object):

    def __init__(self):
        self.x = x
        self.y = y

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

    def draw_entity(self, x, y):
        self.hero = self.canvas.create_image(x, y, anchor=NW, image = self.hero_down)
        
    def update_entity(self, img):
        self.img = img
        self.canvas.itemconfigure(self.hero, image = self.img)

    def move(self, dx, dy):
        self.canvas.move(self.hero, dx, dy)
        self.x += dx
        self.y += dy

# class Skeleton(Entity):

#     def __init__(self, canvas):
#         self.skeleton = None
#         self.x = 0
#         self.y = 0
#         self.skeleton = PhotoImage(file="skeleton.png")
#         self.canvas = canvas

#     def draw_skeleton(self):
#         self.skeleton1 = self.draw_entity(self.skeleton, )

#     def move_skeleton(self, dx, dy):
#         self.canvas.move(self.skeleton, dx, dy)    