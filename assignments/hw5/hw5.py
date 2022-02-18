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
    stripped_names = []
    for name in names_list:
        stripped_name = name.strip()
        stripped_names.append(stripped_name)
    print(stripped_names)
    for name in stripped_names:
        first, last = name.split(' ')
        first_initial, last_initial = first[0], last[0]
        name_initials = "{}{}".format(first_initial,last_initial)
        print(name_initials, end=' ')







def thirds():
    n_sent = eval(input('enter how many sentences:'))
    thirds_list = []
    thirds_string = ''
    for sentences in range(1, n_sent+1):
        thirds_list.append(thirds_string)
        q_string = "enter sentence {}:?".format(sentences)
        sentence = (input(q_string))
        thirds_string = ''
        for letter in range(0, len(sentence), 3):
            thirds_string += sentence[letter]
    thirds_list.append(thirds_string)
    del thirds_list[0]
    print(*thirds_list, sep = "\n")







def word_average():
    sentence = input('enter a sentence: ')
    sentence_list = sentence.split(' ')
    count_list = []
    for word in sentence_list:
        count = len(word)
        count_list.append(count)
    avg = sum(count_list) / len(count_list)
    print(avg)



# def pig_latin():
#     sentence = input('enter a sentence to convert to pig latin: ')
#     sentence_list = sentence.split(' ')
#     pig_list = []
#     for word in sentence_list:
#         pig = word[1:] + word[0] + "ay"
#         pigl = pig.lower()
#         pig_list.append(pigl)
#     print(*pig_list, sep=' ')

def pig_latin():
    words = str(input('enter a sentence to convert to pig latin:')).split()
    pig_list = []
    for word in words:
        pig = word[1:] + word[0] + "ay"
        pigl = pig.lower()
        pig_list.append(pigl)
    print(*pig_list)
    #this works with everything I test



if __name__ == '__main__':
    # name_reverse()
    # company_name()
    # initials()
    # names()
    # thirds()
    # word_average()
    # pig_latin()
    pass
