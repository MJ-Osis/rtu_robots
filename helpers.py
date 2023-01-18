def end_condition(visited, start_pos, grid):
    # Create a queue and add the current position to it
    queue = [tuple(start_pos)]
    # Keep track of visited squares
    reachable = set(visited)
    # While the queue is not empty
    while queue:
        curr_pos = queue.pop(0)
        # Mark the current position as visited
        reachable.add(curr_pos)
        # Check the squares in all four directions
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_pos = (curr_pos[0] + dx, curr_pos[1] + dy)
            if (0 <= new_pos[0] < len(grid)) and (0 <= new_pos[1] < len(grid[0])) and (grid[new_pos[0]][new_pos[1]] == 0) and (new_pos not in visited):
                queue.append(new_pos)
                reachable.add(new_pos)
    return reachable == visited


def check_if_ahead_inside_grid(pos, grid_shape, facing):
    if facing == 'up':
        return pos[0] > 0
    elif facing == 'right':
        return pos[1] < grid_shape[1] - 1
    elif facing == 'down':
        return pos[0] < grid_shape[0] - 1
    elif facing == 'left':
        return pos[1] > 0


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
    
    if facing == 'up':
        pos[0] -= 1
    elif facing == 'right':
        pos[1] += 1
    elif facing == 'down':
        pos[0] += 1
    elif facing == 'left':
        pos[1] -= 1
    return pos


def drive_backward(pos, facing, arduino=None):
    if arduino is not None:
        arduino.write(bytes("b", 'utf-8'))
    
    if facing == 'up':
        pos[0] += 1
    elif facing == 'right':
        pos[1] -= 1
    elif facing == 'down':
        pos[0] -= 1
    elif facing == 'left':
        pos[1] += 1
    return pos
