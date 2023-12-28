import turtle

class Disk(object):
    def __init__(self, name="", xpos=0, ypos=0, height=20, width=40):
        self.dname = name
        self.dxpos = xpos
        self.dypos = ypos
        self.dheight = height
        self.dwidth = width

    def showdisk(self):
        turtle.penup()
        turtle.goto(self.dxpos, self.dypos)
        turtle.pendown()
        turtle.setheading(0)  
        turtle.begin_fill()
        for _ in range(2):
            turtle.forward(self.dwidth)
            turtle.left(90)
            turtle.forward(self.dheight)
            turtle.left(90)
        turtle.end_fill()
        turtle.setheading(0) 

    def newpos(self, xpos, ypos):
        self.cleardisk()
        self.dxpos = xpos
        self.dypos = ypos
        self.showdisk()  

    def cleardisk(self):
        turtle.penup()
        turtle.goto(self.dxpos, self.dypos)
        turtle.setheading(0) 
        turtle.pendown()
        turtle.color("white") 
        turtle.begin_fill()
        for _ in range(2):
            turtle.forward(self.dwidth)
            turtle.left(90)
            turtle.forward(self.dheight)
            turtle.left(90)
        turtle.end_fill()
        turtle.color("black") 
        turtle.setheading(0) 
        

if __name__ == "__main__":
    d1 = Disk("d1", 0, 0)
    d1.showdisk()
    d1.newpos(0, 100)
    d1.cleardisk()
    d1.newpos(0, 0)
    d2 = Disk("d2", 0, 0, 10, 50)
    d2.showdisk()
    d3 = Disk("d3", 0, 0, 5, 30)
    d3.showdisk()
    turtle.mainloop()
