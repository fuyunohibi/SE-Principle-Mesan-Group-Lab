import turtle

class Disk:
    def __init__(self, name, xpos, ypos, height, width):
        self.name = name
        self.xpos = xpos
        self.ypos = ypos
        self.height = height
        self.width = width

    def showdisk(self):
        turtle.penup()
        turtle.goto(self.xpos - self.width/2, self.ypos)
        turtle.pendown()
        for _ in range(2):
            turtle.forward(self.width)
            turtle.left(90)
            turtle.forward(self.height)
            turtle.left(90)
        turtle.penup()

    def newpos(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos

    def cleardisk(self):
        turtle.penup()
        turtle.goto(self.xpos - self.width/2, self.ypos)
        turtle.pendown()
        turtle.color("white")
        for _ in range(2):
            turtle.forward(self.width)
            turtle.left(90)
            turtle.forward(self.height)
            turtle.left(90)
        turtle.color("black")
        turtle.penup()

class Pole:
    def __init__(self, name, xpos, ypos, thick, length):
        self.name = name
        self.stack = []
        self.toppos = ypos
        self.xpos = xpos
        self.ypos = ypos
        self.thick = thick
        self.length = length

    def showpole(self):
        turtle.penup()
        turtle.goto(self.xpos - self.thick/2, self.ypos)
        turtle.pendown()
        turtle.forward(self.thick)
        turtle.left(90)
        turtle.forward(self.length)
        turtle.left(90)
        turtle.forward(self.thick)
        turtle.left(90)
        turtle.forward(self.length)
        turtle.left(90)
        turtle.penup()

    def pushdisk(self, disk):
        disk.newpos(self.xpos, self.toppos)
        self.stack.append(disk)
        self.toppos += disk.height
        disk.showdisk()

    def popdisk(self):
        if self.stack:
            disk = self.stack.pop()
            disk.cleardisk()
            self.toppos -= disk.height
            return disk
        return None

class Hanoi:
    def __init__(self, n=3, start="A", workspace="B", destination="C"):
        self.start = Pole(start, 0, -100, 20, 300)
        self.workspace = Pole(workspace, 150, -100, 20, 300)
        self.destination = Pole(destination, 300, -100, 20, 300)
        self.start.showpole()
        self.workspace.showpole()
        self.destination.showpole()

        for i in range(n):
            disk = Disk("d" + str(i), 0, -100 + i * 20, 20, 40 + (n-i-1) * 20)
            self.start.pushdisk(disk)

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
turtle.bgcolor("white")
turtle.hideturtle()

h = Hanoi(3)
h.solve()

turtle.done()
