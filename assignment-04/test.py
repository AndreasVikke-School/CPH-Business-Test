
import os
import sys
import random as rnd
from tkinter import *
from tkinter.ttk import * 
  
class GFG:
    def __init__(self, master = None):
        self.master = master
          
        # to take care movement in x direction
        self.x = 0
        # to take care movement in y direction
        self.y = 0
  
        # canvas object to create shape
        self.width = 600
        self.height = 400
        self.canvas = Canvas(master, width=self.width, height=self.height)
        # creating rectangle
        self.playerSize = 20
        self.rectangle = self.canvas.create_rectangle(
                         0, 0, 0+self.playerSize, 0+self.playerSize, fill = "black")
        self.food = self.canvas.create_oval(
                         20, 20, 20+self.playerSize, 20+self.playerSize, fill = "red")
                         
        self.canvas.pack()
        self.speed = 500
        self.tail = []
        # calling class's movement method to 
        # move the rectangle
        self.grid()
        self.movement()


    def grid(self):
        for i in range(0, self.width, 20):
            self.canvas.create_line([(i, 0), (i, self.height)], tag='grid_line')
        for i in range(0, self.height, 20):
            self.canvas.create_line([(0, i), (self.width, i)], tag='grid_line')

    def spawn(self):
        coordsPlayer = self.canvas.coords(self.rectangle)
        coordsFood = self.canvas.coords(self.food)
        print(coordsPlayer)
        print(coordsFood)
        if(coordsPlayer[0] == coordsFood[0] and coordsPlayer[3] == coordsFood[3]):
            self.tail.append(self.canvas.create_rectangle(coordsPlayer[0], coordsPlayer[1], coordsPlayer[2], coordsPlayer[3], fill='black'))
            self.speed = round(self.speed * 0.9)
            self.canvas.delete(self.food)
            rndX = rnd.randrange(0, self.width-self.playerSize, self.playerSize)
            rndY = rnd.randrange(0, self.height-self.playerSize, self.playerSize)
            while(True):
                if( rndX == coordsPlayer[0] and rndY == coordsPlayer[2]):
                    rndX = rnd.randrange(0, self.width-self.playerSize, self.playerSize)
                    rndY = rnd.randrange(0, self.height-self.playerSize, self.playerSize)
                else:
                    break
            self.food = self.canvas.create_oval(
                         rndX, rndY, rndX+self.playerSize, rndY+self.playerSize, fill = "red")
        else:
            self.kill(coordsPlayer)
        
    def movement(self):
        # This is where the move() method is called
        # This moves the rectangle to x, y coordinates
        coords = self.canvas.coords(self.rectangle)
        if(coords[0] < 0):
            self.canvas.move(self.rectangle, self.width-self.playerSize, self.y)
        elif(coords[2] > self.width):
            self.canvas.move(self.rectangle, -self.width+self.playerSize, self.y)
        elif(coords[1] < 0):
            self.canvas.move(self.rectangle, self.x, self.height-self.playerSize)
        elif(coords[3] > self.height):
            self.canvas.move(self.rectangle, self.x, -self.height+self.playerSize)
        else:
            self.canvas.move(self.rectangle, self.x, self.y)
        self.spawn()
        self.moveTail(coords)
        self.canvas.after(self.speed, self.movement)

    def moveTail(self, coords):
        prev = coords
        for i in range(0, len(self.tail)):
            cTail = self.canvas.coords(self.tail[i])
            self.canvas.delete(self.tail[i])
            self.tail[i] = self.canvas.create_rectangle(prev[0], prev[1], prev[2], prev[3], fill = "black")
            prev = cTail

    def kill(self, coords):
        for t in self.tail:
            tCoords = self.canvas.coords(t)
            if(coords[0] == tCoords[0] and coords[3] == tCoords[3]):
                python = sys.executable
                os.execl(python, python, * sys.argv)



    # for motion in negative x direction
    def left(self, event):
        print(event.keysym)
        if(self.x == 0):
            self.x = -self.playerSize
            self.y = 0
      
    # for motion in positive x direction
    def right(self, event):
        print(event.keysym)
        if(self.x == 0):
            self.x = self.playerSize
            self.y = 0
      
    # for motion in positive y direction
    def up(self, event):
        print(event.keysym)
        if(self.y == 0):
            self.x = 0
            self.y = -self.playerSize
        
    # for motion in negative y direction
    def down(self, event):
        print(event.keysym)
        if(self.y == 0):
            self.x = 0
            self.y = self.playerSize

    #setSpeed
    def setSpeed(self, event):
        print(self.speed)
        self.speed = 500 if self.speed < 500 else 100
  
if __name__ == "__main__":
  
    # object of class Tk, resposible for creating
    # a tkinter toplevel window
    master = Tk()
    gfg = GFG(master)
  
    # This will bind arrow keys to the tkinter
    # toplevel which will navigate the image or drawing
    master.bind("<KeyPress-Left>", lambda e: gfg.left(e))
    master.bind("<KeyPress-Right>", lambda e: gfg.right(e))
    master.bind("<KeyPress-Up>", lambda e: gfg.up(e))
    master.bind("<KeyPress-Down>", lambda e: gfg.down(e))
    master.bind("<KeyPress-a>", lambda e: gfg.setSpeed(e))
      
    # Infnite loop breaks only by interrupt
    mainloop()