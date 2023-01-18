import numpy as np

def visited_all(visited, grid):
    reachable_squares = np.count_nonzero(grid == 0)
    return len(visited) == reachable_squares

def check_if_ahead_inside_grid(pos, grid_shape, facing):
    if facing == 'up':
        return pos[0] > 0
    elif facing == 'right':
        return pos[1] < grid_shape[1] - 1
    elif facing == 'down':
        return pos[0] < grid_shape[0] - 1
    elif facing == 'left':
        return pos[1] > 0