def clean_path(filename):
    """
    Args:
        filename (str): filename
    """
    with open(filename) as f:
        depth = {}
        for x in f.readlines():
            x = x.strip().split(": ")
            depth[int(x[0])] = int(x[1])

        return depth

def get_scanner_loc(depth, time):
    """Gets location of a scanner at any given time"""
    time = time%(2*(depth-1))

    if time < depth:
        return time
    return 2*(depth-1) - time


def dec12a(data):
    """
    Args:
        lengths (list): list of integers
    """
    severity = 0
    for layer in range(max(data.keys())+1):
        if layer not in data.keys():
            continue
        if get_scanner_loc(data[layer], layer) == 0:
            severity += data[layer] * layer

    return severity


def dec12b(data):
    """
    Args:
        lengths (list): list of integers
    """
    caught = True
    delay = 0
    while caught:
        caught = False
        for layer in range(delay, 100 + delay):
            if layer-delay not in data.keys():
                continue
            if get_scanner_loc(data[layer-delay], layer) == 0:
                caught = True
                break
        delay += 1

    return delay - 1
