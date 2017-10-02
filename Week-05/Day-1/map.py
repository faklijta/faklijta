from tkinter import *

root = Tk()
canvas = Canvas(root, width='720', height= '720')
tilemap = [[0,0,0,1,0,1,0,0,0,0],
           [0,0,0,1,0,1,0,1,1,0],
           [0,1,1,1,0,1,0,1,1,0],
           [0,0,0,0,0,1,0,0,0,0],
           [1,1,1,1,0,1,1,1,1,0],
           [0,1,0,1,0,0,0,0,1,0],
           [0,1,0,1,0,0,0,0,1,0],
           [0,0,0,0,0,0,0,0,1,0],
           [0,1,1,1,0,0,0,0,1,0],
           [0,0,0,1,0,0,1,0,0,0]]


# class Map(object):
#     def __init__(self, x, y, size):
#         self.rect = canvas.create_rectangle(x, y, x+size, y+size)

#def is_wall():
#pass

# image = canvas.create_image(0, 0, anchor=NW, image=filename)
# def get_tile(x, y):
floor = PhotoImage(file="floor.png")
wall = PhotoImage(file="wall.png")

x = 0
y = 0
for row in range(len(tilemap)):
    for column in range(len(tilemap[0])):
        if tilemap[row][column] == 1:
            canvas.create_image(x, y, anchor=NW, image=wall)
        else:
            canvas.create_image(x, y, anchor=NW, image=floor)
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