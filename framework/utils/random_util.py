import random
import string


def get_random_password_and_email():
    lower_alphabet = list(string.ascii_lowercase)
    upper_alphabet = list(string.ascii_uppercase)
    cyrillic_alphabet = 'АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя'
    password = ''
    password += upper_alphabet[random.randint(0, len(upper_alphabet) - 1)]

    for i in range(5):
        password += lower_alphabet[random.randint(0, len(lower_alphabet) - 1)]
        password += str(random.randint(0, 9))
    password += cyrillic_alphabet[random.randint(0, len(cyrillic_alphabet) - 1)]

    email = '' + password[1]
    domain = ''
    for i in range(5):
        email += lower_alphabet[random.randint(0, len(lower_alphabet) - 1)]
        domain += lower_alphabet[random.randint(0, len(lower_alphabet) - 1)]

    return password, email, domain


def random_list_element(given_list, count):
    result_list = []
    working_list = given_list
    for i in range(count):
        idx = random.randint(0, len(working_list) - 1)
        result_list.append(working_list[idx])
        working_list.remove(working_list[idx])
    return result_list


def generate_random_list(size):
    random_list = list()
    for i in range(size):
        random_list.append(random.randint(0, 2))
    return random_list
