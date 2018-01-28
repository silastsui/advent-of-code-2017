def clean_path(filename):
    """
    Args:
        filename (str): filename
    """
    with open(filename) as f:
        return [list(x)[:-1] for x in f.readlines()]

def dec19(data):
    for x in range(len(data[0])):
    if data[0][x] == '|':
        start_index = x

    direction = 'd'
    answer = ''
    x0 = start_index
    y0 = 0
    count = 0

    while is_valid_cell(x0, y0):
        count += 1
        if data[y0][x0] not in ['-', '+', '|']:
            print(data[y0][x0])
        if data[y0][x0] == ' ':
            count -= 1
            break
        x1, y1 = get_next_block(x0, y0, direction)

        # continue moving in same direction
        if direction in ['u', 'd']:


            # continue moving in same direction
            if data[y1][x1] == '|':
                x0, y0 = x1, y1

            # skip next block and continue in same direction
            elif data[y1][x1] == '-':
                count += 1
                x2, y2 = get_next_block(x1, y1, direction)
                if data[y2][x2] not in ['-', '|', '+']:
                        answer += data[y2][x2]
                x0, y0 = x2, y2

            # move left or right of the corner
            elif data[y1][x1] == '+':
                count += 1
                if data[y1][x1-1] == ' ':
                    if data[y1][x1+1] not in ['-', '|', '+']:
                        answer += data[y1][x1+1]
                    x0, y0 = x1+1, y1
                    direction = 'r'
                else:
                    if data[y1][x1-1] not in ['-', '|', '+']:
                        answer += data[y1][x1+1]
                    x0, y0 = x1-1, y1
                    direction = 'l'

            else:
                count += 1
                answer += data[y1][x1]
                x0, y0 = get_next_block(x1, y1, direction)

        else: # direction in ['l', 'r']

            # continue moving in same direction
            if data[y1][x1] == '-':
                x0, y0 = x1, y1

            # skip next block and continue in same direction
            elif data[y1][x1] == '|':
                count += 1
                x2, y2 = get_next_block(x1, y1, direction)
                if data[y2][x2] not in ['-', '|', '+']:
                        answer += data[y2][x2]
                x0, y0 = x2, y2

            # move up or down of the corner
            elif data[y1][x1] == '+':
                count += 1
                if data[y1-1][x1] == ' ':
                    if data[y1+1][x1] not in ['-', '|', '+']:
                        answer += data[y1+1][x1]
                    x0, y0 = x1, y1+1
                    direction = 'd'
                else:
                    if data[y1-1][x1] not in ['-', '|', '+']:
                        answer += data[y1-1][x1]
                    x0, y0 = x1, y1-1
                    direction = 'u'

            else:
                count += 1
                answer += data[y1][x1]
                x0, y0 = get_next_block(x1, y1, direction)

    return answer, count
