from concurrent.futures import BrokenExecutor


def calc(a, b):
    c = a+b
    return c


print(calc(10, 20))
