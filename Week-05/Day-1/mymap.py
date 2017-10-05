from tkinter import *
from random import *

class Map(object):

    def __init__(self):
        self.floor = PhotoImage(file = "floor.png")
        self.wall = PhotoImage(file = "wall.png")
        self.tile_size = 72
        self.x = 0
        self.y = 0
        self.tilemap = [[0,0,0,1,0,1,0,0,0,0],
                        [0,0,0,1,0,1,0,1,1,0],
                        [0,1,1,1,0,1,0,1,1,0],
                        [0,0,0,0,0,1,0,0,0,0],
                        [1,1,1,1,0,1,1,1,1,0],
                        [0,1,0,1,0,0,0,0,1,0],
                        [0,1,0,1,0,0,0,0,1,0],
                        [0,0,0,0,0,0,0,0,1,0],
                        [0,1,1,1,0,0,0,0,1,0]]


    def draw_map(self, canvas):
        for row in range(len(self.tilemap)):
            for column in range(len(self.tilemap[0])):
                if self.tilemap[row][column] == 1:
                    canvas.create_image(self.x, self.y, anchor=NW, image=self.wall)
                    self.x += self.tile_size
                else:
                    canvas.create_image(self.x, self.y, anchor=NW, image=self.floor)
                    self.x += self.tile_size
            self.x = 0
            self.y += self.tile_size

    
    def is_wall(self, x, y):
        cell_x = x//self.tile_size 
        cell_y = y//self.tile_size 
        if cell_x >= 0 and cell_x < len(self.tilemap[0]) and cell_y >= 0 and cell_y < len(self.tilemap):
            return self.tilemap[cell_y][cell_x] == 1
        else:
            return True

    
    def get_cell(self, x, y):
        x = int(x/72)
        y = int(y/72)
        return self.tilemap[y][x]


    def create_random_coordinates(self, skel_num):
        coordinates = []
        while len(coordinates) != skel_num:
            x = randint(0, len(self.tilemap[0]) - 1)
            y = randint(0, len(self.tilemap) - 1)
            if self.tilemap [y][x] == 0 and [x, y] not in coordinates and [x, y] != [0, 0]:
                coordinates.append([x * self.tile_size, y * self.tile_size])
        return coordinates

    
class Hud(object):

    def __init__(self):
        self.x = 0
        self.y = 0
    

    def draw_hud(self, canvas, x, y):
        canvas.create_text(x, y, font=(12), anchor=NW, text=" Hero " + "(Level 1) " + "HP: 10/10 " + "|" + " DP: 8" + "|" + " SP: 6" )