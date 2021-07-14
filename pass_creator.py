import random


# get length of password

# for each digit of the pw randomly choose a letter (upper/lower), a number, or a symbol


def random_letter():
    letter = random.randint(65, 90)
    i = random.randint(0, 1)
    if i == 0:
        return chr(letter)
    else :
        return chr(letter).lower()


def random_number():
    return chr(random.randint(48, 57))


def random_symbol():
    return chr(random.randint(33, 46))


def what_to_choose(pw):
    if pw == '':
        return random_letter()
    else:
        choice = random.randint(1, 3)
        if choice == 1:
            return  random_letter()
        elif choice == 2:
            return random_number()
        else:
            return random_symbol()


def make_password(pw_len):
    new_pass = ''

    for letter in range(pw_len):
        digit = what_to_choose(new_pass)
        new_pass = new_pass + digit

    return new_pass

