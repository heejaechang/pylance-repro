import os


def get(id=None):
    return None if os.getenv('something') else int(1)