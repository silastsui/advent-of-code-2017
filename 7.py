class Disc(object):
    def __init__(self, name, weight, children):
        self.name = name
        self.weight = weight
        self.children = children

def clean_disc(filename):
    """
    Args:
        filename (str): filename
    """
    with open(filename) as f:
        discs = []
        for line in f.readlines():
            line = line.strip().split()
            discs.append(Disc(line[0], int(line[1][1:-1]), line[3:]))
        return discs

def dec7a(discs):
    """
    Args:
        discs (list): list of disc objects
    """
    parents = {}
    for disc in data:
        for child in disc.children:
            child = child.strip(',')
            if child not in parents.keys():
                parents[child] = disc.name

    parent = data[0].name
    while parent in parents.keys():
        parent = parents[parent]

    return parent
