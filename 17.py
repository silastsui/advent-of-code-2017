def dec17a(steps):
    """
    Args:
        steps (int): number of steps
    """
    values = [0]
    k = 337
    i = 0
    for x in range(1, 2018):
        i = (i+k)%len(values) + 1
        values.insert(i, x)

    idx = values.index(2017)

    return values[idx+1]

def dec17b(steps):
    """
    Args:
        steps (int): number of steps
    """
    k = steps
    i = 0
    value = 0
    for x in range(1, 50000001):
        i = (i+k)%x + 1
        if i == 1:
            value = x

    return value
