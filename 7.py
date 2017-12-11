from collections import Counter

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
        discs = {}
        for line in f.readlines():
            line = line.strip().split()
            children = ("".join(line[3:])).split(",")
            discs[line[0]] = Disc(line[0], int(line[1][1:-1]), children)
        return discs

def dec7a(discs):
    """
    Args:
        discs (list): list of disc objects
    """
    parents = {}
    for disc in data:
        for child in disc.children:
            if child not in parents.keys():
                parents[child] = disc.name

    parent = data[0].name
    while parent in parents.keys():
        parent = parents[parent]

    return parent

def get_total_weight(head):
    if data[head].children == ['']:
        return data[head].weight
    return data[head].weight + sum([get_total_weight(x) for x in data[head].children])

def find_unbalanced(head):
    if head in unbalanced:
        unbalanced.remove(head)
    for x in data[head].children:
        if x in unbalanced:
            return find_unbalanced(x)
    return head

def dec7b(discs):
    """
    Args:
        discs (list): list of disc objects
    """
    total_weights = {}
    for x in data.keys():
        total_weights[x] = get_total_weight(x)

    parents = {}
    for disc in data:
        parents[disc] = [total_weights[x] for x in data[disc].children if x != ""]

    unbalanced = set()
    for x in children_weights.keys():
        if children_weights[x] == []:
            continue
        value = children_weights[x][0]
        for y in children_weights[x]:
            if y != value:
                unbalanced.add(x)

    head = "eugwuhl" #from previous part

    unbalanced = find_unbalanced(head)
    unbalanced_children = [total_weights[x] for x in data[unbalanced].children]

    counter = Counter(unbalanced_children)
    val = min(counter, key=counter.get)
    target_val = max(counter, key=counter.get)

    unbalanced = [x for x in data[unbalanaced].children if total_weights[x] == val][0]

    return data[unbalanced].weight + (target_val - val)
