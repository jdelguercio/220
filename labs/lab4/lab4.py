from graphics import *
import time


def greetingcard():
    width = 500
    height = 400
    win = GraphWin("Clicks", width, height)

    background = Rectangle(Point(0,0), Point(500,400))
    background.setFill("Pink")
    background.setOutline("Pink")
    background.draw(win)

    heart = Polygon(Point(250,150), Point(275,125), Point(320,150), Point(290, 200), Point(265, 250), Point(250, 275), Point(235, 250), Point(210, 200), Point(180, 150), Point(225, 125))
    heart.setFill("Red")
    heart.setOutline("Black")
    heart.draw(win)

    arrowbody = Rectangle(Point(30,200), Point(95,198))
    arrowbody.setFill("Black")
    arrowbody.setOutline("Black")
    arrowbody.draw(win)

    arrowhead = Polygon(Point(95, 202), Point(95, 196), Point(102, 199))
    arrowhead.setFill("Black")
    arrowhead.setOutline("Black")
    arrowhead.draw(win)

    greetingloc = Point(250, 100)
    greeting = Text(greetingloc, "Happy Valentines Day!")
    greeting.draw(win)

    for i in range(37):
        arrowbody.move(3,0)
        arrowhead.move(3,0)
        time.sleep(.04)

    inst_pt = Point(250, 380)
    instructions = Text(inst_pt, "Click to close.")
    instructions.draw(win)
    win.getMouse()
    win.close()

