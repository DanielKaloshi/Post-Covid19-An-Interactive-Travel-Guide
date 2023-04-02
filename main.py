""" A runner file to output our Interactive User Module"""


def runner() -> None:
    """ Runner to run file user_interactions.py"""
    with open("user_interactions.py") as f:
        exec(f.read())


if __name__ == '__main__':
    user_in
