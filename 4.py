import collections

def clean_passphrase(filename):
    """
    Args:
        filename (str): filename
    """
    with open(filename) as f:
        return [[x for x in line.strip().split()] for line in f.readlines()]


def dec4a(passphrase):
    """
    Args:
        passphrase (list): list of strings used in passphrase
    """
    count = len(data)
    for passphrase in data:
        words = set()
        for word in passphrase:
            if word not in words:
                words.add(word)
            else:
                count -= 1
                break

    return count

def dec4b(passphrase):
    """
    Args:
        passphrase (list): list of strings used in passphrase
    """
    count = len(data)
    for passphrase in data:
        words = []
        for word in passphrase:
            letters = collections.Counter(word)
            if letters not in words:
                words.append(letters)
            else:
                count -= 1
                break

    return count
