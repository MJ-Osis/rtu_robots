import serial
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
import time
import numpy as np
import cv2 as cv

from griesanas_funkcijas import up, down, left, right, turning_enum

matrix = np.ones((6, 6), dtype=np.int32)

matrix[2, 1] = 0
matrix[2, 2] = 0
matrix[3, 2] = 0
matrix[4, 4] = 0

cv.imshow('matrix', matrix.astype(np.uint8)*255)
cv.waitKey(0)

exit()

grid = Grid(matrix=matrix)

start = grid.node(2, 5)
end = grid.node(3, 1)

finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
path, runs = finder.find_path(start, end, grid)

print('operations:', runs, 'path length:', len(path))
print(grid.grid_str(path=path, start=start, end=end))
print(path)

arduino = serial.Serial('COM3', baudrate=9600) # Same baudrate, as in Arduino program
print('Established serial connection to Arduino')

movement_str = ''
state = 'u'

for idx, p in enumerate(path[1:]):
    loc_change = (p[0] - path[idx][0], p[1] - path[idx][1])
    state, mov = turning_enum[loc_change](state)
    movement_str += mov + 'f'

print(movement_str)

time.sleep(2)

arduino.write(bytes("w", 'utf-8'))

for m in movement_str:
  arduino.write(bytes(m, 'utf-8'))  
  time.sleep(1)

arduino.write(bytes("v", 'utf-8'))
