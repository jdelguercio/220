
from graphics import *
from lab10.door import Door
from lab10.button import Button
from random import randint

def main():

    width_px = 700
    height_px = 600
    win = GraphWin("3 Doors", width_px, height_px)

    d_shape1 = Rectangle(Point(25, 200), Point(225, 575))
    d_text1 = 'Door 1'
    door1 = Door(d_shape1, d_text1)
    door1.color_door('pink')
    door1.draw(win)

    d_shape2 = Rectangle(Point(250, 200), Point(450, 575))
    d_text2 = 'Door 2'
    door2 = Door(d_shape2, d_text2)
    door2.color_door('pink')
    door2.draw(win)

    d_shape3 = Rectangle(Point(475, 200), Point(675, 575))
    d_text3 = 'Door 3'
    door3 = Door(d_shape3, d_text3)
    door3.color_door('pink')
    door3.draw(win)

    eb_shape = Rectangle(Point(475, 25), Point(675, 75))
    eb_text = 'Exit'
    ebutton = Button(eb_shape, eb_text)
    ebutton.draw(win)

    wb_shape = Rectangle(Point(25, 25), Point(125, 75))
    wb_text = 0
    wbutton = Button(wb_shape, wb_text)
    wbutton.draw(win)

    lb_shape = Rectangle(Point(125, 25), Point(225, 75))
    lb_text = 0
    lbutton = Button(lb_shape, lb_text)
    lbutton.draw(win)

    wins_text, losses_text = Text(Point(75, 15), 'wins'), Text(Point(175, 15), 'losses')
    wins_text.draw(win)
    losses_text.draw(win)

    click_text, playagain_text = Text(Point(350, 125), 'Click to guess which is the secret door!'), Text(Point(350, 160), 'Click anywhere to play again')
    click_text.draw(win)

    doors = [door1, door2, door3]

    while True:

        point = win.getMouse()

        if ebutton.is_clicked(point):
            exit()

        rando = randint(0, 2)
        secret_door = doors[rando]
        secret_door.set_secret(True)
        bad_doors = []

        for door in doors:
            if door.is_secret():
                pass
            else:
                bad_doors.append(door)

        print(len(bad_doors))
        bad_door1, bad_door2 = bad_doors[0], bad_doors[1]

        if secret_door.is_clicked(point):
            secret_door.open('green', 'Correct')
            wb_text += 1
            wbutton.set_label(wb_text)

        elif bad_door1.is_clicked(point):
            bad_door1.open('red', 'Wrong')
            lb_text += 1
            lbutton.set_label(lb_text)

        elif bad_door2.is_clicked(point):
            bad_door2.open('red', 'Wrong')
            lb_text += 1
            lbutton.set_label(lb_text)

        playagain_text.draw(win)
        win.getMouse()
        secret_door.set_secret(False)
        door1.close('pink', 'Door 1')
        door2.close('pink', 'Door 2')
        door3.close('pink', 'Door 3')
        playagain_text.undraw()

main()
