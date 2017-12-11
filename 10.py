def clean_lengths(filename):
    """
    Args:
        filename (str): filename
    """
    with open(filename) as f:
        return [int(x) for x in f.readlines()[0].strip().split(',')]

def clean_ascii_lengths(filename):
    """
    Args:
        filename (str): filename
    """
    with open(filename) as f:
        return [ord(x) for x in f.readlines()[0].strip()] + [17, 31, 73, 47, 23]

def dec10a(lengths):
    """
    Args:
        lengths (list): list of integers
    """
    pw = list(range(256))

    skip = 0
    idx = 0
    for length in data:
        start = idx % len(pw)
        end = (idx + length) % len(pw)
        if end < start:
            sublist = (pw[start:] + pw[:end])[::-1]
            pw[start:] = sublist[:(len(pw) - start)]
            pw[:end] = sublist[(len(pw) - start):]
        else:
            pw[start:end] = pw[start:end][::-1]
        idx = (idx + length + skip) % len(pw)
        skip += 1

    return pw[0] * pw[1]

def dec10b(lengths):
    """
    Args:
        lengths (list): list of integers
    """
    pw = list(range(256))

    skip = 0
    idx = 0
    for _ in range(64):
        for length in data:
            start = idx % len(pw)
            end = (idx + length) % len(pw)
            if end < start:
                sublist = (pw[start:] + pw[:end])[::-1]
                pw[start:] = sublist[:(len(pw) - start)]
                pw[:end] = sublist[(len(pw) - start):]
            else:
                pw[start:end] = pw[start:end][::-1]
            idx = (idx + length + skip) % len(pw)
            skip += 1

    dense_hash = []
    for x in range(16):
        temp = pw[16*x: 16*x + 16]
        xor = temp[0]
        for num in temp[1:]:
            xor = xor^num
        dense_hash.append(xor)

    hex_hash = ""
    for x in dense_hash:
        if len(hex(x)[2:]) == 1:
            hex_hash += "0" + hex(x)[2:]
        else:
            hex_hash += hex(x)[2:]

    return hex_hash
