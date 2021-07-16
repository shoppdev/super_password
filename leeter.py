import random
import pass_creator

def bookend(word):
    word = pass_creator.random_symbol() + word
    word = pass_creator.random_number() + word
    word = pass_creator.random_letter() + word
    return word


if __name__ == '__main__':
    