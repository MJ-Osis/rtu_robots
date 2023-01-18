import numpy as np
import serial
import robot_control as rc
import cv2 as cv

GRID_SHAPE = (8, 8)
START_POS = [7, 0]
FACING = 'up'

SIZE_OF_SQUARE = 1
RUN_ARDUINO = False
OBSTACLE_PROB = 0.2

VISUALIZE = True

pos = START_POS
facing = FACING

grid = None
arduino = None
if RUN_ARDUINO:
    arduino = serial.Serial('COM3', baudrate=9600)
else:
    grid = np.where(np.random.rand(*GRID_SHAPE) < OBSTACLE_PROB, 1, 0)
    grid[START_POS[0], START_POS[1]] = 0
    

visited = {}
for i in range(grid.shape[0]):
    for j in range(grid.shape[1]):
        if grid[i, j] == 0:
            visited[(i, j)] = False
            
last_visited = pos
visited_circle = []

# While there are still unvisited squares
while not all(list(visited.values())):
    
    grid_canvas = rc.visualize_grid(grid)
    rc.draw_robot(grid_canvas, pos, facing)

    win = cv.namedWindow('grid', cv.WINDOW_NORMAL)
    cv.imshow('grid', grid_canvas)
    cv.waitKey(0)
    
    print("Current pos:", pos)
    
    options = []
    
    left_obstacle = rc.get_distance('left', facing, pos, grid=grid, arduino=arduino, size_of_square=SIZE_OF_SQUARE)
    if not left_obstacle:
        options.append('left')
        
    forward_obstacle = rc.get_distance('forward', facing, pos, grid=grid, arduino=arduino, size_of_square=SIZE_OF_SQUARE)
    if not forward_obstacle:
        options.append('forward')
        
    right_obstacle = rc.get_distance('right', facing, pos, grid=grid, arduino=arduino, size_of_square=SIZE_OF_SQUARE)
    if not right_obstacle:
        options.append('right')
        
    if not options:
        facing = rc.turn_left(facing, arduino)
        facing = rc.turn_left(facing, arduino)
        continue
        
    if 'left' in options:
        if not visited[tuple(rc.drive_forward(pos, rc.turn_left(facing, None), None))]:
            facing = rc.turn_left(facing, arduino)
            pos = rc.drive_forward(pos, facing, arduino)
            print("Left", pos)
            continue
        
    if 'forward' in options:
        if not visited[tuple(rc.drive_forward(pos, facing, None))]:
            pos = rc.drive_forward(pos, facing, arduino)
            print("Forward", pos)
            continue
        
    if 'right' in options:
        if not visited[tuple(rc.drive_forward(pos, rc.turn_right(facing, None), None))]:
            facing = rc.turn_right(facing, arduino)
            pos = rc.drive_forward(pos, rc.turn_right(facing, None), None)
            print("Right", pos)
            continue
        
    if 'left' in options:
        facing = rc.turn_left(facing, arduino)
        pos = rc.drive_forward(pos, rc.turn_left(facing, None), None)
        continue 
    
    if 'forward' in options:
        pos = rc.drive_forward(pos, facing, None)
        continue
     
    if 'right' in options:
        facing = rc.turn_right(facing, arduino)
        pos = rc.drive_forward(pos, rc.turn_right(facing, None), None)
        continue
        