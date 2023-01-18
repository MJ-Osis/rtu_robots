def get_obstacles(pos, grid):
    y, x = pos # This is fake news
    obstacles = [False] * 4
    if x - 1 < 0 or grid[y, x-1] == 1: # Left
        obstacles[0] = True
    if x + 1 > grid.shape[1]-1 or grid[y, x+1] == 1: # Right
        obstacles[1] = True
    if y - 1 < 0 or grid[y-1,x] == 1: # Up
        obstacles[2] = True
    if y + 1 > grid.shape[0]-1 or grid[y+1, x] == 1: # Down
        obstacles[3] = True
    return obstacles # [left, right, up, down]


def check_obstacle(pos, grid, facing, direction):
    obstacles = get_obstacles(pos, grid) # [left, right, up, down]
    if facing == "up":
        if direction == "forward":
            return obstacles[2]
        elif direction == "left":
            return obstacles[0]
        elif direction == "right":
            return obstacles[1]
    elif facing == "down":
        if direction == "forward":
            return obstacles[3]
        elif direction == "left":
            return obstacles[1]
        elif direction == "right":
            return obstacles[0]
    elif facing == "left":
        if direction == "forward":
            return obstacles[0]
        elif direction == "left":
            return obstacles[3]
        elif direction == "right":
            return obstacles[2]
    elif facing == "right":
        if direction == "forward":
            return obstacles[1]
        elif direction == "left":
            return obstacles[2]
        elif direction == "right":
            return obstacles[3]



def get_distance(dir, facing=None, pos=None, grid=None, arduino=None, size_of_square=None):
    if arduino is not None:
        if dir == 'forward':
            arduino.write(bytes("8", 'utf-8'))
        elif dir == 'left':
            arduino.write(bytes("4", 'utf-8'))
        else:
            arduino.write(bytes("6", 'utf-8'))
        arduino.write(bytes("d", 'utf-8'))
        dist = arduino.read()
        return dist < size_of_square
    else:
        return check_obstacle(pos, grid, facing, dir)