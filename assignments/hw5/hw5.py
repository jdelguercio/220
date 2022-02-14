"""
Name: <Joey Del Guercio>
<ProgramName>.py

Problem: <learning basic string uses>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.

"""


def name_reverse():
    name =  input('enter your name (first last):')
    first, last = name.split(' ')
    reversed_name = "{}, {}".format(last, first)
    print(reversed_name)



def company_name():
    domain = input('enter a domain:')
    _, company, _ = domain.split('.')
    print(company)


def initials():
    n_students = eval(input('how many students are in your class?'))
    for students in range(1, n_students+1):
        q_string = "what is the name of student {}?".format(students)
        student_name = (input(q_string))
        first, last = student_name.split(' ')
        first_initial, last_initial = first[0], last[0]
        student_initials = "{}{}".format(first_initial,last_initial)
        print(student_initials)


def names():
    names_input = input('enter a comma-separated list of names:')
    names_list = names_input.split(',')
    print(names_list)
    for name in names_list:
        first, last = name.split(' ')
        first_initial, last_initial = first[0], last[0]
        name_initials = "{}{}".format(first_initial, last_initial)
        print(name_initials)




def thirds():
    pass


def word_average():
    pass


def pig_latin():
    pass


if __name__ == '__main__':
    # name_reverse()
    # company_name()
    # initials()
    # names()
    # thirds()
    # word_average()
    # pig_latin()
    pass
