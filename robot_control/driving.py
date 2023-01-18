def turn_left(facing, arduino=None):
    if arduino is not None:
        arduino.write(bytes("l", 'utf-8'))
    if facing == 'up':
        return 'left'
    elif facing == 'right':
        return 'up'
    elif facing == 'down':
        return 'right'
    elif facing == 'left':
        return 'down'


def turn_right(facing, arduino=None):
    if arduino is not None:
        arduino.write(bytes("l", 'utf-8'))
    
    if facing == 'up':
        return 'right'
    elif facing == 'right':
        return 'down'
    elif facing == 'down':
        return 'left'
    elif facing == 'left':
        return 'up'


def drive_forward(pos, facing, arduino=None):
    if arduino is not None:
        arduino.write(bytes("f", 'utf-8'))
    new_pos = pos.copy()
    
    if facing == 'up':
        new_pos[0] -= 1
    elif facing == 'right':
        new_pos[1] += 1
    elif facing == 'down':
        new_pos[0] += 1
    elif facing == 'left':
        new_pos[1] -= 1
    return new_pos


def drive_backward(pos, facing, arduino=None):
    if arduino is not None:
        arduino.write(bytes("b", 'utf-8'))
    new_pos = pos.copy()
    
    if facing == 'up':
        new_pos[0] += 1
    elif facing == 'right':
        new_pos[1] -= 1
    elif facing == 'down':
        new_pos[0] -= 1
    elif facing == 'left':
        new_pos[1] += 1
    return new_pos