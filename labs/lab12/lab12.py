import algorithms
from random import randint

def find_and_remove(list, value):
    count = 0
    while count < len(list):

        if list[count] == value:
            list[count] = 'Joey'
            count = len(list)
        else:
            count += 1

def good_input():
    x = 0
    while x not in range(1, 10):

        x = eval(input('please enter a number between 1-10'))

        if x in range(1, 10):
            print(x)
        else:
            print('previous input not between 1-10, try again')

def num_digits():
    x = 69


    while x > 0:
        x = eval(input('enter a number'))

        div_count = 0
        num = x

        while num > 0:
            num = num // 10
            div_count += 1
        if x > 0:
            print(div_count)
        else:
            pass
        if x <= 0:
            break




def hi_lo_game():
    rand = randint(1, 100)
    guesses = 0

    if guesses == 7:
        print('Sorry, you lose. The number was {}'.format(rand))

    while guesses < 7:

        guess = eval(input('guess a number between 1-100'))

        if guess == rand:
            guesses += 1
            print('correct')
            print('You win in {} guesses'.format(guesses))
            break

        elif guess < rand:
            guesses += 1
            print('too low')

        elif guess > rand:
            guesses += 1
            print('too high')

        elif guesses == 7:
            print('Sorry, you lose. The number was {}'.format(rand))
            break


def main():
    test_list = [1, 2, 3, 4, 5, 6, 7, 8, 6, 10]
    test_val = 6

    print('list functions:')
    print('pre-function:', test_list)
    find_and_remove(test_list, test_val)
    print('post-function: ', test_list)

    print('linear search:')
    values = algorithms.read_data('data_sorted.txt')
    print('not in list check:')
    print(algorithms.is_in_linear(72, values))
    print('in list check:')
    print(algorithms.is_in_linear(75, values))

    good_input()

    num_digits()

    hi_lo_game()


main()
