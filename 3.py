import math

def get_sum(x, y):
    neighbours = [(x-1, y-1),
                  (x-1, y),
                  (x-1, y+1),
                  (x, y-1),
                  (x, y+1),
                  (x+1, y-1),
                  (x+1, y),
                  (x+1, y+1)]
    total = 0
    for square in neighbours:
        if square in grid.keys():
            total += grid[square]

    return total

def dec3a(num):
    """
    Args:
        num (int): input number
    """

    layer = math.floor((math.sqrt(num)+1)/2)
    side_length = 2*layer
    remainder = (2*layer+1)**2 - num

    x, y = layer, -layer

    if remainder > side_length: #bottom right corner to bottom left corner
        remainder -= side_length
        x -= side_length
    else:
        x -= remainder
        return abs(x) + abs(y)

    if remainder > side_length: #bottom left corner to upper left corner
        remainder -= side_length
        y += side_length
    else:
        y += remainder
        return abs(x) + abs(y)

    if remainder > side_length: #upper left corner to upper right corner
        remainder -= side_length
        x += side_length
    else:
        x += remainder
        return abs(x) + abs(y)

    if remainder > side_length: #upper right corner to bottom right corner
        remainder -= side_length
        y -= side_length
    else:
        y -= remainder
        return abs(x) + abs(y)

def dec3b(num):
    """
    Args:
        num (int): input number
    """
    grid = {(0, 0): 1}

    x, y = 0, 0
    x_dir, y_dir = True, True
    length = 1
    val = 1
    while val < puzzle_input:
        if x_dir and y_dir: #moving right
            for i in range(length):
                x += 1
                grid[(x, y)] = get_sum(x, y)
            x_dir = False
        if not x_dir and y_dir: #moving up
            for i in range(length):
                y += 1
                grid[(x, y)] = get_sum(x, y)
            y_dir = False
            length += 1
        if not x_dir and not y_dir: #moving left
            for i in range(length):
                x -= 1
                grid[(x, y)] = get_sum(x, y)
            x_dir = True
        if x_dir and not y_dir: #moving down
            for i in range(length):
                y -= 1
                grid[(x, y)] = get_sum(x, y)
            y_dir = True
            length += 1

    return list(filter(lambda x: x > puzzle_input, sorted(grid.values())))[0]
