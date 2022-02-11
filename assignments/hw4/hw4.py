"""
Name: <Joey Del Guercio>
<ProgramName>.py

Problem: <Creating some graphics and creating a sequence>

Certification of Authenticity:
I certify that this assignment is entirely my own work.

"""

from graphics import *
import math

def squares():
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Clicks", width, height)

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to draw a square")
    instructions.draw(win)

    # builds a circle
    shape = Rectangle(Point(50, 50),Point(100,100))
    shape.setOutline("green")
    shape.setFill("green")
    shape.draw(win)

    # allows the user to click multiple times to move the circle
    for _ in range(num_clicks):
        click = win.getMouse()
        center = shape.getCenter()  # center of circle
        # move amount is distance from center of circle to the
        # point where the user clicked
        change_x = click.getX() - center.getX()
        change_y = click.getY() - center.getY()
        newshape = shape.clone()
        newshape.move(change_x, change_y)
        newshape.draw(win)

    inst_pt2 = Point(200,200)
    instructions2 = Text(inst_pt2, "Click again to close")
    instructions2.draw(win)
    win.getMouse()
    win.close()


def rectangle():
    width = 400
    height = 400
    win = GraphWin("Clicks", width, height)

    p1 = win.getMouse()
    p4 = win.getMouse()
    p1x, p1y = p1.getX(), p1.getY()
    p4x, p4y = p4.getX(), p4.getY()
    rec = Rectangle(p1,p4)
    rec.draw(win)
    length = abs(p1x) + abs(p4x)
    width = abs(p1y) + abs(p4y)
    perimeter, area = 2*length + 2*width, length*width
    comp_string = "Perimeter: {} & Area: {}".format(perimeter, area)
    compslocation = Point(width / 2, height - 10)
    comp = Text(compslocation, comp_string)
    comp.draw(win)

    inst_pt = Point(200, 200)
    instructions = Text(inst_pt, "Click again to close")
    instructions.draw(win)
    win.getMouse()
    win.close()



def circle():
    width = 400
    height = 400
    win = GraphWin("Clicks", width, height)

    center = win.getMouse()
    edge = win.getMouse()
    center_x, center_y = center.getX(), center.getY()
    edge_x, edge_y = edge.getX(), edge.getY()
    radius = math.sqrt((edge_x - center_x)**2 + (edge_y - center_y)**2)

    shape = Circle(center, radius)
    shape.setOutline("green")
    shape.setFill("green")
    shape.draw(win)

    rad_string = "Radius: {}".format(radius)
    rad_location = Point(width / 2, height - 10)
    rad_text = Text(rad_location, rad_string)
    rad_text.draw(win)

    inst_pt = Point(200, 200)
    instructions = Text(inst_pt, "Click again to close")
    instructions.draw(win)
    win.getMouse()
    win.close()

def pi2():
    num = 4
    denom = 1
    pi_sum = 0

    terms = eval(input("enter the number of terms to sum:"))
    for i in range(terms):
        pi_sum += (num / denom)
        num *= -1
        denom += 2

    accuracy = abs(math.pi - pi_sum)
    print("pi approximation:", pi_sum)
    print("accuracy:", accuracy)




if __name__ == '__main__':
    pass
