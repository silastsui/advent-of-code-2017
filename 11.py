from collections import Counter

def clean_path(filename):
    """
    Args:
        filename (str): filename
    """
    with open(filename) as f:
        return f.readlines()[0].strip().split(',')


def dec11a(steps):
    """
    Args:
        lengths (list): list of integers
    """
    x, y = 0, 0
    for i in data:
        if i == 'n':
            y += 1
        elif i == 's':
            y -= 1
        elif i == 'nw':
            x -= 1
            y += 0.5
        elif i == 'ne':
            x += 1
            y += 0.5
        elif i == 'sw':
            x -= 1
            y -= 0.5
        elif i == 'se':
            x += 1
            y -= 0.5

    return abs(x/2 + y)

def dec11a(steps):
    """
    Args:
        lengths (list): list of integers
    """
    x, y = 0, 0
    max_dist = 0
    for i in data:
        if i == 'n':
            y += 1
        elif i == 's':
            y -= 1
        elif i == 'nw':
            x -= 1
            y += 0.5
        elif i == 'ne':
            x += 1
            y += 0.5
        elif i == 'sw':
            x -= 1
            y -= 0.5
        elif i == 'se':
            x += 1
            y -= 0.5
        if abs(x/2 + y) > max_dist:
            max_dist = abs(x/2 + y)

    return max_dist
