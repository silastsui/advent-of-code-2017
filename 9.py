def clean_stream(filename):
    """
    Args:
        filename (str): filename
    """
    with open(filename) as f:
        return f.readlines()[0].strip()

def dec9a(stream):
    """
    Args:
        stream (str): stream of characters
    """
    groups = []
    garbage = False
    skip = False
    score = 0
    for x in data:
        if skip:
            skip = False
            continue
        if x == '!':
            skip = True
            continue
        if garbage:
            if x == '>':
                garbage = False
            continue
        if x == "{":
            groups.append('{')
        if x == "}":
            score += len(groups)
            groups.pop()
        if x == '<':
            garbage = True
    return score

def dec9b(stream):
    """
    Args:
        stream (str): stream of characters
    """
    garbage = False
    skip = False
    score = 0
    for x in data:
        if skip:
            skip = False
            continue
        if x == '!':
            skip = True
            continue
        if garbage:
            if x == '>':
                garbage = False
            else:
                score += 1
            continue
        if x == '<':
            garbage = True

    return score
