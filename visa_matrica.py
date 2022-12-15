import time
import numpy as np
import serial
from griesanas_funkcijas import up, down, left, right, turning_enum, get_loc

size_of_square = 20
matrix = np.zeros((8, 8), dtype=np.int32)

print(matrix)

start = [0, 7]

visited_squares = start
all_squares = np.mgrid[0:8, 0:8].reshape(16, 2)

arduino = serial.Serial('COM3', baudrate=9600) # Same baudrate, as in Arduino program
print('Established serial connection to Arduino')

state = 'u'
loc = start
scanned_rows = []

while True:
    in_front = get_loc(loc, state, 'u')
    if in_front in all_squares and in_front not in visited_squares:
        arduino.write(bytes("d", 'utf-8'))
        dist = arduino.read()
        if dist < size_of_square:
            loc = in_front
            visited_squares.append(loc)
            continue
    
    to_right = get_loc(loc, state, 'r')
    if to_right in all_squares and to_right not in visited_squares:
        arduino.write(bytes("d", 'utf-8'))
        dist = arduino.read()
        if dist < size_of_square:
            loc_change = (loc[0] - to_right[0], loc[1] - to_right[1])
            arduino.write(bytes("", 'utf-8'))
            
            
            loc = to_right
            visited_squares.append(loc)
            continue
    
        
    
    if dist > si




