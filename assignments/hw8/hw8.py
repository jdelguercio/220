"""
Name: <your name goes here – first and last>
<ProgramName>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""
import math
from graphics import *

def add_ten(nums):
    for i in range(len(nums)):
        nums[i] += 10


def square_each(nums):
    for i in range(len(nums)):
        nums[i] *= nums[i]


def sum_list(nums):
    nums_sum = 0
    for i in range(len(nums)):
        nums_sum += nums[i]
    return nums_sum


def to_numbers(nums):
    for i in range(len(nums)):
        nums[i] = eval(nums[i])


def sum_of_squares(nums):
    nums_out = []
    for i in nums:
        num_list = i.split(',')
        to_numbers(num_list)
        square_each(num_list)
        num_sum = sum_list(num_list)
        nums_out.append(num_sum)
    return nums_out

def starter(weight, wins):
    if 150 <= weight < 160 and wins >= 5:
        return True
    elif weight > 199 or wins > 20:
        return True
    else:
        return False

def leap_year(year):
    if ((year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0)):
        return True
    else:
        return False

def circle_overlap():
    width_px = 700
    height_px = 700
    win = GraphWin("Circle", width_px, height_px)
    width = 10
    height = 10
    win.setCoords(0, 0, width, height)

    center = win.getMouse()
    circumference_point = win.getMouse()
    radius = math.sqrt(
        (center.getX() - circumference_point.getX()) ** 2 + (center.getY() - circumference_point.getY()) ** 2)
    circle_one = Circle(center, radius)
    circle_one.setFill("light blue")
    circle_one.draw(win)

    center2 = win.getMouse()
    circumference_point2 = win.getMouse()
    radius2 = math.sqrt(
        (center2.getX() - circumference_point2.getX()) ** 2 + (center2.getY() - circumference_point2.getY()) ** 2)
    circle_two = Circle(center2, radius2)
    circle_two.setFill("light pink")
    circle_two.draw(win)


def did_overlap(circle_one, circle_two):

    width_px = 700
    height_px = 700
    win = GraphWin("Circle", width_px, height_px)

    center = win.getMouse()
    circumference_point = win.getMouse()
    radius = math.sqrt(
        (center.getX() - circumference_point.getX()) ** 2 + (center.getY() - circumference_point.getY()) ** 2)
    circle_one = Circle(center, radius)
    circle_one.setFill("light blue")
    circle_one.draw(win)

    center2 = win.getMouse()
    circumference_point2 = win.getMouse()
    radius2 = math.sqrt(
        (center2.getX() - circumference_point2.getX()) ** 2 + (center2.getY() - circumference_point2.getY()) ** 2)
    circle_two = Circle(center2, radius2)
    circle_two.setFill("light pink")
    circle_two.draw(win)

    eud_dist_cent = math.sqrt(
        (center2.getX() - center.getX()) ** 2 + (center2.getY() - center.getY()) ** 2)
    overlap_txt = 'The circles overlap'
    nolap_txt = 'The circles do not overlap'
    if (radius + radius2) >= eud_dist_cent:
        overlap_text = Text(Point(350, 360), overlap_txt)
        overlap_text.draw(win)
        click_txt = 'Click anywhere to close window'
        click_text = Text(Point(250, 450), click_txt)
        click_text.draw(win)
        win.getMouse()
        win.close()
        return True

    else:
        nolap_text = Text(Point(350, 360), nolap_txt)
        nolap_text.draw(win)
        click_txt = 'Click anywhere to close window'
        click_text = Text(Point(250, 450), click_txt)
        click_text.draw(win)
        win.getMouse()
        win.close()
        return False

if __name__ == '__main__':
    pass
