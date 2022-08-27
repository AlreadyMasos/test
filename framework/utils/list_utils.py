from operator import itemgetter


def is_list_sorted(list, key_name, reverse):
    new_list = sorted(list, key=itemgetter(key_name), reverse=reverse)
    return new_list == list


def get_list_with_muliples(count, divider):
    multiples_list = list()
    for i in range(1, count):
        multiples_list.append(i * divider)
    return multiples_list
