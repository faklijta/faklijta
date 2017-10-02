from tkinter import *
from PIL import Image, ImageTk

root = Tk()
canvas = Canvas(root, width='720', height= '720')
# tilemap = [[0,0,0,0,0,0,0,0,0,0]]


# class Map(object):
#     def __init__(self, x, y, size):
#         self.rect = canvas.create_rectangle(x, y, x+size, y+size)

#     def is_wall():
#         pass


# image = canvas.create_image(0, 0, anchor=NW, image=filename)
# def get_tile(x, y):
filename = PhotoImage(file="floor.png")
x = 0
y = 0
for row in range(10):
    for column in range(10):
        canvas.create_image(x, y, anchor=NW, image=filename)
        x += 72
    x = 0
    y += 72


    # def get_cell():
    #     pass
# map1= Map()
# map1.get_tile(0,0)
# get_tile(0,0)
canvas.pack()

root.mainloop()