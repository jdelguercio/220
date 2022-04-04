
from graphics import *
from door import Door
from button import Button

def main():

    width_px = 600
    height_px = 600
    win = GraphWin("Test", width_px, height_px)

    d_shape = Rectangle(Point(200, 200), Point(400, 600))
    d_text = 'closed'
    door = Door(d_shape, d_text)
    door.color_door('green')
    door.draw(win)

    b_shape = Rectangle(Point(200, 50), Point(400, 150))
    b_text = 'exit'
    button = Button(b_shape, b_text)
    button.draw(win)



    while True:

        point = win.getMouse()

        if button.is_clicked(point):
            exit()

        if door.is_clicked(point) and d_text == 'closed':

            door.undraw()

            d_text = 'open'
            door = Door(d_shape, d_text)
            door.color_door('pink')
            door.draw(win)

        elif door.is_clicked(point) and d_text == 'open':

            door.undraw()

            d_text = 'closed'
            door = Door(d_shape, d_text)
            door.color_door('green')
            door.draw(win)

if __name__ == '__main__':
    main()
