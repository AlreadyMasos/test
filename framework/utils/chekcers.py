def check_if_json(response):
    try:
        response.json()
        return True
    except ValueError:
        return False


def check_sorted_by(response, param_name):
    list_of_elems = [x[param_name] for x in response.json()]
    return list_of_elems == sorted(list_of_elems)


def empty_check(resp):
    return len(resp.json()) == 0


def check_post(real_post, current_post):
    return real_post == current_post