import turtle

class Disk(object):
    def __init__(self, name="", xpos=0, ypos=0, height=20, width=40):
        self.dname = name
        self.dxpos = xpos
        self.dypos = ypos
        self.dheight = height
        self.dwidth = width

    def showdisk(self):
        turtle.goto(self.dxpos, self.dypos)
        turtle.setheading(0)  
        turtle.pendown()
        turtle.forward(self.dwidth)
        turtle.left(90)
        turtle.forward(self.dheight)
        turtle.left(90)
        turtle.forward(self.dwidth)
        turtle.left(90)
        turtle.forward(self.dheight)
        turtle.left(90)
        turtle.penup()

    def newpos(self, xpos, ypos):
        self.dxpos = xpos
        self.dypos = ypos

    def cleardisk(self):
        turtle.goto(self.dxpos, self.dypos)
        turtle.setheading(0)  

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
        turtle.goto(self.pxpos, self.pypos)
        turtle.setheading(0)  # East
        turtle.pendown()
        turtle.forward(self.pthick)
        turtle.left(90)
        turtle.forward(self.plength)
        turtle.left(90)
        turtle.forward(self.pthick)
        turtle.left(90)
        turtle.forward(self.plength)
        turtle.left(90)
        turtle.penup()

    def pushdisk(self, disk):
        disk.newpos(self.pxpos, self.toppos)
        self.stack.append(disk)
        self.toppos += disk.dheight
        disk.showdisk()

    def popdisk(self):
        if self.stack:
            disk = self.stack.pop()
            self.toppos -= disk.dheight
            return disk
        return None

class Hanoi(object):
    def __init__(self, n=3, start="A", workspace="B", destination="C"):
        self.start = Pole(start, 0, 0)
        self.workspace = Pole(workspace, 150, 0)
        self.destination = Pole(destination, 300, 0)
        self.start.showpole()
        self.workspace.showpole()
        self.destination.showpole()

        for i in range(n):
            self.start.pushdisk(Disk("d" + str(i), 0, i * 20, 20, (n - i) * 30))

    def movedisk(self, start, destination):
        disk = start.popdisk()
        destination.pushdisk(disk)

    def movetower(self, n, s, d, w):
        if n == 1:
            self.movedisk(s, d)
        else:
            self.movetower(n-1, s, w, d)
            self.movedisk(s, d)
            self.movetower(n-1, w, d, s)

    def solve(self):
        self.movetower(3, self.start, self.destination, self.workspace)

turtle.speed(7) 
h = Hanoi()
h.solve()
turtle.done()
