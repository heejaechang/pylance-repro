def add(a, b):
    return a + b


def new_func(add, d):
    for i in range(10):
        add(i, d)

if __name__ == '__main__':
    d = 5
    new_func(add, d)