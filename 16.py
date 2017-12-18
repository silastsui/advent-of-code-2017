def clean_path(filename):
    """
    Args:
        filename (str): filename
    """
    with open(filename) as f:
        data = f.readlines()[0].strip().split(',')
    for x in range(len(data)):
        if data[x][0] == 'x':
            data[x] = ['x'] + [int(i) for i in data[x][1:].split('/')]
        elif data[x][0] == 'p':
            data[x] = ['p'] + data[x][1:].split('/')
        elif data[x][0] == 's':
            data[x] = ['s'] + [int(data[x][1:])]
    return data

def dec16a(instructions):
    """
    Args:
        instructions (list): list of dance moves
    """
    programs = list('abcdefghijklmnop')
    for i in instructions:
        if i[0] == 's':
            programs = programs[-i[1]:] + programs[:-i[1]]
        elif i[0] == 'x':
            programs[i[1]], programs[i[2]] = programs[i[2]], programs[i[1]]
        elif i[0] == 'p':
            idx1 = programs.index(i[1])
            idx2 = programs.index(i[2])
            programs[idx1], programs[idx2] = programs[idx2], programs[idx1]

    return "".join(programs)


def dec16b(instructions):
    """
    Args:
        instructions (list): list of dance moves
    """
    programs = list('abcdefghijklmnop')
    for k in range(1000000000):
        if programs == list('abcdefghijklmnop') and k != 0:
            break
        for i in data:
            if i[0] == 's':
                programs = programs[-i[1]:] + programs[:-i[1]]
            elif i[0] == 'x':
                programs[i[1]], programs[i[2]] = programs[i[2]], programs[i[1]]
            elif i[0] == 'p':
                idx1 = programs.index(i[1])
                idx2 = programs.index(i[2])
                programs[idx1], programs[idx2] = programs[idx2], programs[idx1]

    for _ in range(1000000000%k):
        for i in data:
            if i[0] == 's':
                programs = programs[-i[1]:] + programs[:-i[1]]
            elif i[0] == 'x':
                programs[i[1]], programs[i[2]] = programs[i[2]], programs[i[1]]
            elif i[0] == 'p':
                idx1 = programs.index(i[1])
                idx2 = programs.index(i[2])
                programs[idx1], programs[idx2] = programs[idx2], programs[idx1]

    return programs
