from time import sleep

def kek1(x):
    print('kek1 ... ', end='')
    sleep(2)
    print('done')
    return x > 3


def kek2(y):
    print('kek2 ... ', end='')
    sleep(4)
    print('done')
    return y == 3


def kek3(z):
    print('kek3 ... ', end='')
    sleep(6)
    print('done')
    return z < 3


if kek1(2) and kek2(4) and kek3(0) or kek3(4) or kek2(3):
    print('1')
else:
    print('2')
