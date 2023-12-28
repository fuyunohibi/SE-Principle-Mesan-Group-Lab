import turtle as t

class Disk(object):
    def __init__(self, name="", xpos=-40, ypos=0, height=20, width=100):
        self.dname = name
        self.dxpos = xpos
        self.dypos = ypos
        self.dheight = height
        self.dwidth = width

    def showdisk(self):
        t.penup()
        t.goto(self.dxpos, self.dypos)
        t.pendown()
        t.setheading(0)  
        t.begin_fill()
        for _ in range(2):
            t.forward(self.dwidth)
            t.left(90)
            t.forward(self.dheight)
            t.left(90)
        t.end_fill()
        t.setheading(0) 

    def newpos(self, xpos, ypos):
        self.cleardisk()
        self.dxpos = xpos
        self.dypos = ypos
        self.showdisk()  

    def cleardisk(self):
        t.penup()
        t.goto(self.dxpos, self.dypos)
        t.setheading(0) 
        t.pendown()
        t.color("white") 
        t.begin_fill()
        for _ in range(2):
            t.forward(self.dwidth)
            t.left(90)
            t.forward(self.dheight)
            t.left(90)
        t.end_fill()
        t.color("black") 
        t.setheading(0) 
        

class Pole(object):
    def __init__(self, name="", xpos=0, ypos=0, thick=10, length=100):
        self.pname = name
        self.stack = []
        self.toppos = 0
        self.pxpos = xpos
        self.pypos = ypos
        self.pthick = thick
        self.plength = length

    def showpole(self):
        t.penup()
        t.goto(self.pxpos, self.pypos)
        t.pendown()
        t.forward(self.pthick)
        t.left(90)
        t.forward(self.plength)
        t.left(90)
        t.forward(self.pthick)
        t.left(90)
        t.forward(self.plength)
        t.left(90)
        t.goto(self.pxpos,self.pypos)
        t.penup()

    def pushdisk(self, disk):
        self.stack.append(disk)
        disk.showdisk()

    def popdisk(self):
        topDisk = self.stack[-1]
        topDisk.cleardisk()
        topDisk.dypos = self.plength + topDisk.dheight
        topDisk.showdisk() 

if __name__ == "__main__":
    p = Pole()
    p.showpole()
    d = Disk()
    p.pushdisk(d)
    p.popdisk()
    t.done()
    # p.pushdisk(d)
