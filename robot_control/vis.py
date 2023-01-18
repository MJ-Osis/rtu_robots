import cv2 as cv
import numpy as np


def visualize_grid(grid, pix_per_square=100):
    shape = grid.shape
    canvas = np.zeros((shape[0] * pix_per_square, shape[1] * pix_per_square, 3), dtype=np.uint8)
    
    # Draw gridlines
    for i in range(shape[0]):
        cv.line(canvas, (0, i * pix_per_square), (canvas.shape[1], i * pix_per_square), (255, 255, 255))
    for i in range(shape[1]):
        cv.line(canvas, (i * pix_per_square, 0), (i * pix_per_square, canvas.shape[0]), (255, 255, 255))
        
    # Draw obstacles
    for i in range(shape[0]):
        for j in range(shape[1]):
            if grid[i, j] == 1:
                cv.rectangle(canvas, (j * pix_per_square, i * pix_per_square), ((j + 1) * pix_per_square, (i + 1) * pix_per_square), (0, 0, 255), -1)
                
    return canvas


def draw_robot(canvas, pos, facing, pix_per_square=100):
    # Draw robot as circle
    cv.circle(canvas, (pos[1] * pix_per_square + pix_per_square // 2, pos[0] * pix_per_square + pix_per_square // 2), pix_per_square // 2, (0, 255, 0), -1)
    
    # Draw small square in facing direction
    if facing == 'up':
        square_pos = (pos[1] * pix_per_square + int(pix_per_square * (0.5 - 0.125)), pos[0] * pix_per_square)
    elif facing == 'down':
        square_pos = (pos[1] * pix_per_square  + int(pix_per_square * (0.5 - 0.125)), (pos[0] + 1) * pix_per_square - pix_per_square // 4)
    elif facing == 'left':
        square_pos = (pos[1] * pix_per_square, pos[0] * pix_per_square + int(pix_per_square * (0.5 - 0.125)))
    else:
        square_pos = ((pos[1] + 1) * pix_per_square - pix_per_square // 4, pos[0] * pix_per_square + int(pix_per_square * (0.5 - 0.125)))
        
    cv.rectangle(canvas, square_pos, (square_pos[0] + pix_per_square // 4, square_pos[1] + pix_per_square // 4), (255, 255, 0), -1)
    
