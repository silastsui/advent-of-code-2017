def clean_path(filename):
    """
    Args:
        filename (str): filename
    """
    with open(filename) as f:
        data = [x.strip().split('/') for x in f.readlines()]

    for x in range(len(data)):
        data[x] = [int(data[x][0]), int(data[x][1])]

    return data


def find_strongest_pipe(data, start, pipe):

    if len(data[start]) == 0:
        if len(pipe) > 0:
            valid_pipes.append(2*sum(pipe) - pipe[-1])
            return 2*sum(pipe) - pipe[-1]

    for x in data[start]:
        new_data = data.copy()
        new_pipe = pipe.copy()
        new_start = x

        temp = new_data[start].copy()
        temp.remove(x)
        new_data[start] = temp

        temp = new_data[x].copy()
        temp.remove(start)
        new_data[x] = temp


        new_pipe.append(x)

        find_strongest_pipe(new_data, new_start, new_pipe)

def dec24a(data):
    pipes = {}
    for x in data:
        if x[0] not in pipes:
            pipes[x[0]] = [x[1]]
        else:
            pipes[x[0]].append(x[1])

        if x[1] not in pipes:
            pipes[x[1]] = [x[0]]
        else:
            pipes[x[1]].append(x[0])

    start = 0
    pipe = []
    valid_pipes = []
    find_strongest_pipe(pipes, start, pipe)

    return max(valid_pipes)

def find_strongest_longest_pipe(data, start, pipe):

    if len(data[start]) == 0:
        if len(pipe) > 0:
            valid_pipes.append([len(pipe), 2*sum(pipe) - pipe[-1]])
            return

    for x in data[start]:
        new_data = data.copy()
        new_pipe = pipe.copy()
        new_start = x

        temp = new_data[start].copy()
        temp.remove(x)
        new_data[start] = temp

        temp = new_data[x].copy()
        temp.remove(start)
        new_data[x] = temp


        new_pipe.append(x)

        find_strongest_pipe(new_data, new_start, new_pipe)


def dec24a(data):
    pipes = {}
    for x in data:
        if x[0] not in pipes:
            pipes[x[0]] = [x[1]]
        else:
            pipes[x[0]].append(x[1])

        if x[1] not in pipes:
            pipes[x[1]] = [x[0]]
        else:
            pipes[x[1]].append(x[0])

    start = 0
    pipe = []
    valid_pipes = []
    find_strongest_pipe(pipes, start, pipe)

    return sorted(valid_pipes)[-1]
