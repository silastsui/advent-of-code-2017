def clean_sheet(filename):
    """
    Args:
        filename (str): filename
    """
    with open(filename) as f:
        return [[int(x) for x in line.strip().split()] for line in f.readlines()]


def dec2a(sheet):
    """
    Args:
        sheet (list): parsed spreadsheet
    """
    total = 0
    for line in data:
        total += (max(line) - min(line))

    return total

def dec2b(sheet):
    """
    Args:
        sheet (list): parsed spreadsheet
    """
    total = 0
    for line in data:
        for x in range(len(line)):
            for y in range(x+1, len(line)):
                if line[y] != 0 and line[x]%line[y] == 0:
                    total += line[x]//line[y]
                elif line[x] != 0 and line[y]%line[x] == 0:
                    total += line[y]//line[x]

    return total
