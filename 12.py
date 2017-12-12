def clean_path(filename):
    """
    Args:
        filename (str): filename
    """
    with open(filename) as f:
        items = {}
        for x in f.readlines():
            x = x.split()
            items[int(x[0])] = [int(x) for x in "".join(x[2:]).split(',')]

        return items


def dec12a(data):
    """
    Args:
        lengths (list): list of integers
    """
    included = set()
    queue = [0]
    while queue:
        for x in data[queue[0]]:
            if x not in included:
                queue.append(x)
                included.add(x)
        queue.pop(0)

    return len(included)


def dec12b(data):
    """
    Args:
        lengths (list): list of integers
    """
    count = 0
    while len(data) > 0:
        included = set()
        queue = [list(data.keys())[0]]
        while queue:
            for x in data[queue[0]]:
                if x not in included:
                    queue.append(x)
                included.add(x)
            queue.pop(0)

        for y in included:
            del data[y]
        count += 1


    return count
