from tkinter import *
from PIL import Image, ImageTk

root = Tk()
canvas = Canvas(root, width='600', height= '600')


# class Map(object):
#     def __init__(self, x, y, size):
#         self.rect = canvas.create_rectangle(x, y, x+size, y+size)

#     def is_wall():
#         pass

    # def get_tile(self, x, y):
filename = PhotoImage(file="floor.png")
image = canvas.create_image(0, 0, anchor=NW, image=filename)

    # def get_cell():
    #     pass

canvas.pack()

root.mainloop()