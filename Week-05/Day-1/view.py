from tkinter import *
from map import Map

root = Tk()

canvas = Canvas(root, width='720', height='720')
canvas.pack()

class View(object):
    def __init__(self):
        self.floor = PhotoImage(file="floor.png")
        self.wall = PhotoImage(file="wall.png")


    def draw_map(self, canvas):
        x = 0
        y = 0
        for row in range(len(self.tilemap)):
            for column in range(len(self.tilemap[0])):
                if self.tilemap[row][column] == 1:
                    canvas.create_image(x, y, anchor=NW, image=self.wall)
                else:
                    canvas.create_image(x, y, anchor=NW, image=self.floor)
                x += 72
            x = 0
            y += 72

    def display():
        pass

    def hub():
        pass


view1 = View()
view1.draw_map(canvas)
view1.draw_entity(0,0)

# Tell the canvas that we prepared a function that can deal with the key press events
root.bind("<KeyPress>", on_key_press)
canvas.pack()

# Select the canvas to be in focused so it actually recieves the key hittings
canvas.focus_set()

root.mainloop()