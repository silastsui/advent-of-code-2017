def clean_path(filename):
    """
    Args:
        filename (str): filename
    """
    with open(filename) as f:
        return [x.strip().split() for x in f.readlines()]

def dec18a(data):
    last_played = ''
    idx = 0
    sounds = {}
    while True:
        x = data[idx]
        if x[1] not in sounds.keys():
            sounds[x[1]] = 0
        if x[0] == 'set':
            if x[2] in sounds.keys():
                sounds[x[1]] = sounds[x[2]]
            else:
                sounds[x[1]] = int(x[2])
        elif x[0] == 'add':
            sounds[x[1]] += int(x[2])
        elif x[0] == 'mul':
            if x[2] in sounds.keys():
                sounds[x[1]] *= sounds[x[2]]
            else:
                sounds[x[1]] *= int(x[2])
        elif x[0] == 'mod':
            if x[2] in sounds.keys():
                sounds[x[1]] = sounds[x[1]] % sounds[x[2]]
            else:
                sounds[x[1]] = sounds[x[1]] % int(x[2])
        elif x[0] == 'rcv':
            if sounds[x[1]] != 0:
                return last_played
        elif x[0] == 'snd':
            last_played = sounds[x[1]]
        elif x[0] == 'jgz':
            if sounds[x[1]] > 0:
                if x[2] in sounds.keys():
                    idx += sounds[x[2]]
                else:
                    idx += int(x[2])
            else:
                idx += 1
        if x[0] != 'jgz':
            idx += 1
