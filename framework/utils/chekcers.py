def check_if_json(response):
    try:
        response.json()
        return True
    except ValueError:
        return False


def empty_check(resp):
    return len(resp.json()) == 0

