def clean_instructions(filename):
    """
    Args:
        filename (str): filename
    """
    with open(filename) as f:
        return [int(line.strip()) for line in f.readlines()]

def dec5a(instr):
    """
    Args:
        instr (list): list of integers
    """
    steps = 0
    idx = 0
    while idx >= 0 and idx < len(data):
        jump = data[idx]
        data[idx] += 1
        idx += jump
        steps += 1

    return steps

def dec5b(instr):
    """
    Args:
        instr (list): list of integers
    """
    steps = 0
    idx = 0
    while idx >= 0 and idx < len(data):
        jump = data[idx]
        if jump >= 3:
            data[idx] -= 1
        else:
            data[idx] += 1
        idx += jump
        steps += 1
