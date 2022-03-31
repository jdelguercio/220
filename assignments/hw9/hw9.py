import random as rd
from graphics import *

def get_words(file_name):
    file = open(file_name, 'r')
    word_list = []
    for line in file:
        # line = line.strip()
        word_list.append(line)
    return word_list

def get_random_word(words):
    randnum = rd.randint(0, len(words)-1)
    random_word = words[randnum]
    random_word = random_word.strip()
    return random_word


def letter_in_secret_word(letter, secret_word):
    if letter in secret_word:
        return True
    else:
        return False


def already_guessed(letter, guesses):
    if letter in guesses:
        return True
    else:
        return False


def make_hidden_secret(secret_word, guesses):
    hidden_secret_word = secret_word
    for letter in secret_word:
        if letter in guesses:
            pass
        else:
            hidden_secret_word = hidden_secret_word.replace(letter, '_')
    hidden_secret_word = " ".join(hidden_secret_word)
    return hidden_secret_word



def won(guessed):
    if '_' in guessed:
        return False
    else:
        return True


def play_graphics(secret_word):
    width = 750
    height = 750
    win = GraphWin("hangman", width, height)

    gallow1 = Line(Point(375, 400), Point(375, 175))
    gallow1.draw(win)
    gallow2 = Line(Point(410, 400), Point(260, 400))
    gallow2.draw(win)
    gallow3 = Line(Point(260, 175), Point(375, 175))
    gallow3.draw(win)
    gallow4 = Line(Point(260, 175), Point(260, 230))
    gallow4.draw(win)

    guesses = []
    guesses_left = 6
    hidden_secret_word = make_hidden_secret(secret_word, guesses)

    hidden_text = Text(Point(375, 500), hidden_secret_word)
    hidden_text.draw(win)

    guesses_text = Text(Point(375, 475), "guesses: {}".format(guesses))
    guesses_text.draw(win)

    guess_txt = Text(Point(305, 530), "guess a letter: ")
    guess_txt.draw(win)

    guess_entry = Entry(Point(375, 530), 3)
    guess_entry.draw(win)

    click_txt = Text(Point(375, 700), 'click to enter letter')
    click_txt.draw(win)

    head = Circle(Point(260, 250), 20)
    torso = Line(Point(260, 270), Point(260, 300))
    arm_l = Line(Point(260, 275), Point(245, 280))
    arm_r = Line(Point(260, 275), Point(275, 280))
    leg_l = Line(Point(260, 300), Point(250, 310))
    leg_r = Line(Point(260, 300), Point(270, 310))

    while not won(hidden_secret_word) and guesses_left > 0:
        win.getMouse()
        letter = guess_entry.getText()

        if not already_guessed(letter, guesses) and letter in secret_word:
            guesses.append(letter)
            hidden_secret_word = make_hidden_secret(secret_word, guesses)
            guesses_text.undraw()
            guesses_text = Text(Point(375, 475), "guesses: {}".format(guesses))
            guesses_text.draw(win)
            hidden_text.undraw()
            hidden_text = Text(Point(375, 500), hidden_secret_word)
            hidden_text.draw(win)
        elif not already_guessed(letter, guesses) and letter not in secret_word:
            guesses.append(letter)
            guesses_left += -1
            hidden_secret_word = make_hidden_secret(secret_word, guesses)
            guesses_text.undraw()
            guesses_text = Text(Point(375, 475), "guesses: {}".format(guesses))
            guesses_text.draw(win)
            hidden_text.undraw()
            hidden_text = Text(Point(375, 500), hidden_secret_word)
            hidden_text.draw(win)

            if guesses_left == 5:
                head.draw(win)
            elif guesses_left == 4:
                torso.draw(win)
            elif guesses_left == 3:
                arm_l.draw(win)
            elif guesses_left == 2:
                arm_r.draw(win)
            elif guesses_left == 1:
                leg_l.draw(win)
            elif guesses_left == 0:
                leg_r.draw(win)
            else:
                pass

        else:
            pass

    if won(hidden_secret_word):
        win_txt = Text(Point(650, 530),"winner!")
        win_txt.draw(win)
        win.getMouse()
        win.close()
    elif guesses_left == 0:
        loser_txt = Text(Point(650, 530), "you've lost!")
        secret_word_txt = Text(Point(650, 350), secret_word)
        loser_txt.draw(win)
        secret_word_txt.draw(win)
        win.getMouse()
        win.close()
    else:
        pass







def play_command_line(secret_word):
    guesses = []
    guesses_left = 6
    hidden_secret_word = make_hidden_secret(secret_word, guesses)

    print('already guessed: {}'.format(guesses))
    print('guesses remaining: {}'.format(guesses_left))
    print(hidden_secret_word)

    while not won(hidden_secret_word) and guesses_left > 0:

        letter = input('guess a letter:')

        if not already_guessed(letter, guesses) and letter in secret_word:
            guesses.append(letter)
            hidden_secret_word = make_hidden_secret(secret_word, guesses)
            print('already guessed: {}'.format(guesses))
            print('guesses remaining: {}'.format(guesses_left))
            print(hidden_secret_word)
        elif not already_guessed(letter, guesses) and letter not in secret_word:
            guesses.append(letter)
            guesses_left += -1
            hidden_secret_word = make_hidden_secret(secret_word, guesses)
            print('already guessed: {}'.format(guesses))
            print('guesses remaining: {}'.format(guesses_left))
            print(hidden_secret_word)
        else:
            print('invalid move')
            print('already guessed: {}'.format(guesses))
            print('guesses remaining: {}'.format(guesses_left))
            # print(hidden_secret_word)

    if won(hidden_secret_word):
        # print('winner!', secret_word, sep='\n')
        print('winner!')
    elif guesses_left == 0:
        print("sorry you've lost. The word was {}".format(secret_word))
    else:
        pass








if __name__ == '__main__':
    pass
    # play_command_line(secret_word)
    # play_graphics(secret_word)

