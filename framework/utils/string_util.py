from random import choice
from string import ascii_letters


def set_random_string(length):
    random_string = (''.join(choice(ascii_letters) for i in range(length)))
    return random_string


def set_random_email(length):
    return set_random_string(length)+'@gmail.com'
