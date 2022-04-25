
from algorithms import *

rectangle1 = Rectangle(Point(100, 200), Point(300, 300))
rectangle2 = Rectangle(Point(200, 200), Point(370, 310))
rectangle3 = Rectangle(Point(400, 100), Point(450, 300))
rectangles = [rectangle1, rectangle2, rectangle3]

def trade_alert(filename):
    file = open(filename, 'r')
    for line in file:
        trades = line.split()
    trades = list(map(int, trades))

    sec = 0
    for trade in trades:
        sec += 1
        if trade > 830:
            print('WARNING: trading volume in excess of 830. {} trades at {} seconds'.format(trade, sec))
        elif trade == 500:
            print('WARNING: trading volume equals 500. {} trades at {} seconds'.format(trade, sec))
        else:
            print('Note: {} trades at {} seconds'.format(trade, sec))

def main():
    print('rect_sort() check:')
    print('pre-sort: {}'.format(rectangles))
    rect_sort(rectangles)
    print('post-sort: {}'.format(rectangles))

    trade_alert('trades.txt')

main()

