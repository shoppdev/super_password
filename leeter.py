import random
import pwnd_check
import sys

import pass_creator


def convert_to_ascii(letter):
    return int(ord(letter))


def make_longer():
    pass


def length_checker(word):
    if len(word) < 8:
        print('!! Your password is less than the recommended min length. !!')


def letter_converter(letter):
    letter_list = ['a', 'e', 'h', 'o', 's', 'x']
    # chance to upper or lower
    if random.randint(0, 1) == 1:
        letter = letter.upper()
    else:
        letter = letter.lower()
    # chance to leet it
    if letter.lower() in letter_list:
        if random.randint(0, 1):
            if letter.lower() == 'a':
                letter = '@'
            elif letter.lower() == 'e':
                letter = '3'
            elif letter.lower() == 's':
                letter = '$'
            elif letter.lower() == 'x':
                letter = '+'
            elif letter.lower() == 'h':
                letter = '4'
        if letter.lower() == 'o':
            letter = '0'
    return letter


def number_converter(letter):
    pass


def leet_it(word):
    leeted = ''
    for letter in word:
        ascii_letter = convert_to_ascii(letter)
        if 65 <= ascii_letter <= 90:
            leeted = leeted + letter_converter(letter)
        elif 95 <= ascii_letter <= 122:
            leeted = leeted + letter_converter(letter)
        elif 48 <= ascii_letter <= 57:
            leeted = leeted + letter
        else:
            leeted = leeted + letter
    return leeted


# might change to make usable gibberish
def bookend(word):
    end = ''
    end = pass_creator.random_symbol() + end
    end = pass_creator.random_number() + end
    end = pass_creator.random_letter() + end
    return end[0] + word  # + end[1:3]


if __name__ == '__main__':

    user_input = sys.argv[1]
    length_checker(user_input)
    word = leet_it(user_input)
    b_word = bookend(word)

    print(f'New pass = {user_input} found {pwnd_check.check_password(user_input)}')
    print(f'New pass = {word} found {pwnd_check.check_password(word)}')
    print(f'With ends = {b_word} found {pwnd_check.check_password(b_word)}')
