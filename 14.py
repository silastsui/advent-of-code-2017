def clean_ascii_lengths(hash_input):
    """
    Args:
        filename (str): filename
    """

    return [ord(x) for x in hash_input] + [17, 31, 73, 47, 23]

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


def dec14a(input_hash):
    """
    Args:
        input_hash (str): input hash
    """
    count = 0
    for x in range(128):
        data = clean_ascii_lengths('{}}-{}'.format(input_hash, x))
        hash_string = dec10b(data)
        count += bin(int(hash_string, 16))[2:].zfill(128).count('1')

    return count

def clear_region(x, y, grid):
    """Clears all squares in a region"""
    
    grid[y][x] = 0
    if x != 0 and grid[y][x-1] == 1:
        clear_region(x-1, y, grid)
    if x != len(grid)-1 and grid[y][x+1] == 1:
        clear_region(x+1, y, grid)
    if y != 0 and grid[y-1][x] == 1:
        clear_region(x, y-1, grid)
    if y != len(grid)-1 and grid[y+1][x] == 1:
        clear_region(x, y+1, grid)
    return


def dec14b(input_hash):
    """
    Args:
        input_hash (str): input hash
    """
    grid = []
    for x in range(128):
        data = clean_ascii_lengths('{}-{}'.format(input_hash, x))
        hash_string = dec10b(data)
        grid += [[int(x) for x in bin(int(hash_string, 16))[2:].zfill(128)]]

    count = 0
    for y in range(128):
        for x in range(128):
            if total[y][x] == 1:
                count += 1
                clear_region(x, y, total)

    return count
