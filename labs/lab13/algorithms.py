from graphics import *

def read_data(filename):
    file = open(filename, 'r')
    line_list = list(file.readlines())
    count = 0
    output = []

    while count < len(line_list):
        nums = line_list[count].split()
        i = 0
        while i < len(nums):
            output.append(int(nums[i]))
            i += 1
        count += 1

    file.close()
    return output

def is_in_linear(search_val, values):
    answer = search_val in values
    return answer

def is_in_binary(search_val, values):
    low = 0
    high = len(values) - 1

    while low <= high:

        mid = (high + low) // 2

        if values[mid] < search_val:
            low = mid + 1
        elif values[mid] > search_val:
            high = mid - 1
        else:
            return True

    return False

def selection_sort(values):

    for i in range(len(values)):
        min = i

        for j in range(i+1, len(values)):

            if values[min] > values[j]:
                min = j

        values[i], values[min] = values[min], values[i]

def calc_area(rect):
    p1x, p1y = rect.getP1().getX(), rect.getP1().getY()
    p2x, p2y = rect.getP2().getX(), rect.getP2().getY()

    len = p2y - p1y
    wid = p2x - p1x

    area = len * wid

    return area

def rect_sort(rectangles):

    for i in range(len(rectangles)):
        min = i

        for j in range(i+1, len(rectangles)):

            if calc_area(rectangles[min]) > calc_area(rectangles[j]):
                min = j

        rectangles[i], rectangles[min] = rectangles[min], rectangles[i]
