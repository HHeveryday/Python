from multiprocessing.spawn import _main
from threading import main_thread
from pip import main


def add(a, b):
    return a+b


if __name__ == '__main__':  # NOTE 只有运行calc才会执行下面的代码
    print(add(10, 20))
