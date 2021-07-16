import random
import pass_creator


def convert_to_ascii(letter):
    return int(ord(letter))


def letter_converter(letter):
    letter_list = ['a', 'e', 'o', 's']
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
            elif letter.lower() == 'o':
                letter = '0'
    return letter


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
    return leeted


def bookend(word):
    end = ''
    end = pass_creator.random_symbol() + end
    end = pass_creator.random_number() + end
    end = pass_creator.random_letter() + end
    return end + word # + end[::-1]


if __name__ == '__main__':
    print(bookend(leet_it('ashton1')))