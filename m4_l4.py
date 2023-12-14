"""Boolean34"""
x, y = input().split()
x = int(x)
y = int(y)


def is_black():
    black = (x % 2 == 1 and y % 2 == 1)
    return black


def is_white():
    white = (x % 2 == y % 3)
