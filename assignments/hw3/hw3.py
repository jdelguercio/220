"""
Name: <Joey Del Guercio>
<ProgramName>.py

Problem:<basic functions using loops, math, and input>

Certification of Authenticity:
I certify that this assignment is entirely my own work.


"""

def average():
    n_grades = eval(input('How many grades would you like to input?'))
    numerator = 0
    for _ in range(1,n_grades + 1):
        grade = eval(input('Enter your grade.'))
        numerator += grade
    the_avg = numerator / n_grades
    print('Your average is: ', the_avg)



def tip_jar():
    tips = 0
    for _ in range (1,6):
        tips += eval(input('What are your tips?'))
    print('total tips: ', tips)



def newton():
    pass


def sequence():
    pass


def pi():
    pass


if __name__ == '__main__':
    pass
