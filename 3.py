import math
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
