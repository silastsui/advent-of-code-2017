import math

def clean_path(filename):
    """
    Args:
        filename (str): filename
    """
    with open(filename) as f:
        data = [x.strip().split(", ") for x in f.readlines()]
    for line in data:
        for i in range(len(line)):
            line[i] = [int(k) for k in line[i][3:-1].split(',')]


    return data

def add_vec(a, b):
    return [a[0] + b[0], a[1] + b[1], a[2] + b[2]]

def get_norm(a):
    return int(math.sqrt(a[0] **2 + a[1]**2 + a[2]**2))

def dec20a(data):
    for t in range(500):
        for i in data:
            i[1] = add_vec(i[1], i[2])
            i[0] = add_vec(i[0], i[1])

    norms = []
    idx = 0
    for i in range(len(data)):
        norms.append(get_norm(data[i][0]))
    return norms.index(min(norms))

def dec20b(data):
    for t in range(500):
    temp = {}
    for i in data:
        i[1] = add_vec(i[1], i[2])
        i[0] = add_vec(i[0], i[1])

        if str(i[0]) not in temp.keys():
            temp[str(i[0])] = [i]
        else:
            temp[str(i[0])].append(i)

    for i in temp.keys():
        if len(temp[i]) > 1:
            for x in temp[i]:
                data.remove(x)

    return len(data)
