"""
Name: <Joey Del Guercio>
<ProgramName>.py

Problem: <math accumulators and displays>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""
import math


def sum_of_threes(): #done
    upper = eval(input("What is your upper bound?"))
    threes = list(filter(lambda x: x % 3 == 0, range(upper + 1)))
    threes_sum = sum(threes)
    print("sum of threes is ", threes_sum)



def multiplication_table(): #done
    rows = 10
    columns = 10
    for i in range(1, rows+1):
        print('\n')
        for j in range(1, columns+1):
            prod = i * j
            print(prod, end='\t')

def triangle_area(): #done
    side_a = eval(input("side a length?"))
    side_b = eval(input("side b length?"))
    side_c = eval(input("side c length?"))
    surfarea = (side_a + side_b + side_c) / 2
    area = math.sqrt(surfarea * (surfarea-side_a) * (surfarea-side_b) * (surfarea-side_c))
    print("your area is ", area)

def sum_squares(): #done
    lower = eval(input("lower bound?"))
    upper = eval(input("upper bound?"))
    thesum = 0
    for i in range(lower, upper + 1):
        thesum = thesum + (i * i)
    print(thesum)





def power(): #done
    base = eval(input("Base?"))
    exponent = eval(input("Exponent?"))
    answer = 1
    for _ in range(exponent):
        answer *= base
    print(base, "^", exponent, "=", answer)

if __name__ == '__main__':
    pass
