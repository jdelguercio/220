from graphics import *
import math


def triangle(): #done
    width = 500
    height = 500
    win = GraphWin("Clicks", width, height)

    p1 = win.getMouse()
    p2 = win.getMouse()
    p3 = win.getMouse()

    p1x, p1y = p1.getX(), p1.getY()
    p2x, p2y = p2.getX(), p2.getY()
    p3x, p3y = p3.getX(), p3.getY()

    tri = Polygon(p1, p2, p3)
    tri.draw(win)

    l1 = math.sqrt((p2x - p1x) ** 2 + (p2y - p1y) ** 2)
    l2 = math.sqrt((p3x - p2x) ** 2 + (p3y - p2y) ** 2)
    l3 = math.sqrt((p1x - p3x) ** 2 + (p1y - p3y) ** 2)

    perimeter = l1 + l2 + l3
    svar = (l1 + l2 + l3) / 2
    area = math.sqrt(svar * (svar - l1) * (svar - l2) * (svar - l3))

    comp_string = "Perimeter: {} & Area: {}".format(perimeter, area)
    compslocation = Point(width / 2, height - 10)
    comp = Text(compslocation, comp_string)
    comp.draw(win)

    input()


def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")

    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    red_textEntry = Entry(Point(red_text_pt.getX() + 45, red_text_pt.getY()), 3)
    red_textEntry.draw(win)

    green_textEntry = Entry(Point(green_text_pt.getX() + 45, green_text_pt.getY()), 3)
    green_textEntry.draw(win)

    blue_textEntry = Entry(Point(blue_text_pt.getX() + 45, blue_text_pt.getY()), 3)
    blue_textEntry.draw(win)



    for i in range(5):

        win.getMouse()

        red = red_textEntry.getText()
        red_int = int(red)

        green = green_textEntry.getText()
        green_int = int(green)

        blue = blue_textEntry.getText()
        blue_int = int(blue)


        shape.setFill(color_rgb(red_int, green_int, blue_int))
    win.getMouse()
    win.close()




def process_string(): #done
    sentence = input('enter a sentence: ')
    sentence_list = list(sentence)
    print(sentence_list[0])
    print(sentence_list[-1])
    print(sentence_list[2:6])
    print(sentence_list[0], sentence_list[-1], sep='')
    print(sentence_list[0:3]*10)
    for i in sentence_list:
        print(i, end='\n')
    print(len(sentence))

def process_list(): #done
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]

    x = values[1]+values[3]
    print(x)
    x = values[0]+values[2]
    print(x)
    x = values[1]*5
    print(x)
    x = list(values[2:5])
    print(x)
    x = [values[2], values[3], values[0]]
    print(x)
    x = [values[2], values[0], eval(values[5])]
    print(x)
    x = values[0]+values[2]+eval(values[5])
    print(x)
    x = len(values)
    print(x)

def another_series(): #done
    terms = eval(input('how many terms would you like? '))
    my_list = [2, 4, 6] * 10000
    print(my_list[0:terms], sep='')
    my_sum = sum(my_list[0:terms])
    print('sum = {}'.format(my_sum))

def target(): #done
    width = 500
    height = 500
    win = GraphWin("Clicks", width, height)

    center = Point(250,250)
    white_circle = Circle(center, 250)
    black_circle = Circle(center, 200)
    blue_circle = Circle(center, 150)
    red_circle = Circle(center, 100)
    yellow_center = Circle(center, 50)


    white_circle.setFill('white')

    black_circle.setFill('black')

    blue_circle.setFill('blue')

    red_circle.setFill('red')

    yellow_center.setFill('yellow')

    white_circle.draw(win)
    black_circle.draw(win)
    blue_circle.draw(win)
    red_circle.draw(win)
    yellow_center.draw(win)

    input()