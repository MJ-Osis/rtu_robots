import numpy as np
import serial
import robot_control as rc


GRID_SHAPE = (8, 8)
START_POS = [7, 0]
FACING = 'up'

SIZE_OF_SQUARE = 1
RUN_ARDUINO = False
OBSTACLE_PROB = 0.2

pos = START_POS
facing = FACING

grid = None
arduino = None
if RUN_ARDUINO:
    arduino = serial.Serial('COM3', baudrate=9600)
else:
    grid = np.where(np.random.rand(*GRID_SHAPE) < OBSTACLE_PROB, 1, 0)



visited = set()
# While there are still unvisited squares
while True:
    
    has_where_to_go = False
    
    forward_obstacle = rc.get_distance('forward', facing, pos, grid=grid, arduino=arduino, size_of_square=SIZE_OF_SQUARE)
    if not forward_obstacle and rc.check_if_ahead_inside_grid(pos, GRID_SHAPE, facing):
        visited.add(tuple(pos))
        pos = rc.drive_forward(pos, facing, arduino)
        continue
    
    left_obstacle = rc.get_distance('left', facing, pos, grid=grid, arduino=arduino, size_of_square=SIZE_OF_SQUARE)
    if not left_obstacle:
        facing = rc.turn_left(facing)
        continue
    
    right_obstacle = rc.get_distance('right', facing, pos, grid=grid, arduino=arduino, size_of_square=SIZE_OF_SQUARE)
    if not right_obstacle:
        facing = rc.turn_right(facing)
    
    # check if all reachable squares have been visited
    if len(visited) == (len(grid) * len(grid[0]) - sum(sum(row) for row in grid)):
        break
