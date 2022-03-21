from graphics import *
from random import randint
import math


def get_random(move_amount):
    rand_num = randint(-move_amount, move_amount)
    return rand_num


def did_collide(circle, circle2):
    center = Circle.getCenter(circle)
    center2 = Circle.getCenter(circle2)
    radius = Circle.getRadius(circle)
    radius2 = Circle.getRadius(circle2)
    eud_dist_cent = math.sqrt(
        (center2.getX() - center.getX()) ** 2 + (center2.getY() - center.getY()) ** 2)
    if (radius + radius2) >= eud_dist_cent:
        return True
    else:
        return False


def hit_vertical(circle, win):
    center = Circle.getCenter(circle)
    radius = Circle.getRadius(circle)
    if center.getX() + radius >= win.getWidth() or center.getX() - radius <= 0:
        return True
    else:
        return False


def hit_horizontal(circle, win):
    center = Circle.getCenter(circle)
    radius = Circle.getRadius(circle)
    if center.getY() + radius >= win.getHeight() or center.getY() - radius <= 0:
        return True
    else:
        return False

def get_random_color():
    red_int, green_int, blue_int = randint(0, 255), randint(0, 255), randint(0, 255)
    color = color_rgb(red_int, green_int, blue_int)
    return color



def random_balls():
    width_px = 600
    height_px = 600
    win = GraphWin("Circle", width_px, height_px)

    center, center2 = Point(200, 200), Point(400, 400)
    # center, center2 = Point(randint(60, 500), randint(60, 500)), Point(randint(60, 500), randint(60, 500))
    radius, radius2 = 40, 40

    circle = Circle(center, radius)
    circle.setFill("light blue")
    circle.draw(win)

    circle2 = Circle(center2, radius2)
    circle2.setFill("light pink")
    circle2.draw(win)

    move_amount = 50
    randx1, randx2, randy1, randy2 = get_random(move_amount), get_random(move_amount), get_random(
        move_amount), get_random(move_amount)

    while True:
        circle.move(randx1, randy1)
        circle2.move(randx2, randy2)
        time.sleep(.05)

        if hit_vertical(circle, win) == True:
            randx1 *= -1
        if hit_vertical(circle2, win) == True:
            randx2 *= -1
        if hit_horizontal(circle, win) == True:
            randy1 *= -1
        if hit_horizontal(circle2, win) == True:
            randy2 *= -1
        if did_collide(circle, circle2) == True:
            circle.setFill(get_random_color())
            circle2.setFill(get_random_color())
            randx1 *= -1
            randx2 *= -1
            randy1 *= -1
            randy2 *= -1
random_balls()
