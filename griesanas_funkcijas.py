def up(state):
    mov = ''
    if state == 'l':
        mov = 'r'
    elif state == 'r':
        mov = 'l'
    elif state == 'd':
        mov = 'rr'
    return 'u', mov


def down(state):
    mov = ''
    if state == 'l':
        mov = 'l'
    elif state == 'r':
        mov = 'r'
    elif state == 'u':
        mov = 'rr'
    return 'd', mov


def right(state):
    mov = ''
    if state == 'l':
        mov = 'rr'
    elif state == 'u':
        mov = 'r'
    elif state == 'd':
        mov = 'l'
    return 'r', mov


def left(state):
    mov = ''
    if state == 'r':
        mov = 'rr'
    elif state == 'u':
        mov = 'l'
    elif state == 'd':
        mov = 'r'
    return 'l', mov


turning_enum = {
    (1, 0): right, (-1, 0): left, (0, 1): down, (0, -1): up
}


def rotate_right(curr):
    if curr == 'r':
        return 'u'
    if curr == 'd':
        return 'r'
    if curr == 'l':
        return 'd'
    if curr == 'u':
        return 'l'


def get_loc(loc, state, dir):
    dir_offset = 0
    while dir != 'u':
        dir = rotate_right(dir)
        dir_offset += 1
        
    for _ in range(4 - dir_offset):
        state = rotate_right(state)

    e = {
        'u': (-1, 0), 'r': (0, -1), 'd': (1, 0), 'l': (0, 1)} 
    sub = e[state]
    
    loc[0] += sub[0]
    loc[1] += sub[1]
    return [loc[0] + sub[0], loc[1] + sub[1]]


if __name__ == '__main__':
    print(get_loc([1, 2], 'd', 'l'))


