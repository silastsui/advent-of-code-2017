def clean_banks(filename):
    """
    Args:
        filename (str): filename
    """
    with open(filename) as f:
        return [int(x) for x in f.readlines()[0].strip().split()]

def dec6a(instr):
    """
    Args:
        instr (list): list of integers
    """
    known_states = []
    count = 0
    while data not in known_states:
        known_states.append(data.copy())
        count += 1
        redist = max(data)
        idx = data.index(redist)
        data[idx] = 0
        for i in range(1, redist+1):
            n = (i+idx) % len(data)
            data[n] += 1

    return count

def dec6b(instr):
    """
    Args:
        instr (list): list of integers
    """
    known_states = []
    count = 0
    while data not in known_states:
        known_states.append(data.copy())
        count += 1
        redist = max(data)
        idx = data.index(redist)
        data[idx] = 0
        for i in range(1, redist+1):
            n = (i+idx) % len(data)
            data[n] += 1

    return count - known_states.index(data)
