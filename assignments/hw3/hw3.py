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
    num = eval(input('What number do you want to square root? '))
    times = eval(input('How many times should we improve the approximation? '))
    approx = num
    for _ in range(1, times+1):
        approx = (approx + (num / approx)) / 2
    print(approx)


def sequence():
    terms = eval(input('how many terms would you like? '))
    for i in range(1, terms+1):
        output = (i - 1) + (i % 2)
        print(output, end=' ')


def pi():
    n = eval(input('how many terms?'))
    pi_sum = 1
    for i in range(n):
        num = i + (2 - (i % 2))
        denom = i + (1 + (i % 2))
        pi_sum *= (num / denom)
    approx = pi_sum * 2
    print(approx)



if __name__ == '__main__':
    pass
