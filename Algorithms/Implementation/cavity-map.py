#!/bin/python

import sys


n = int(raw_input().strip())
grid = []
grid_i = 0
for grid_i in xrange(n):
    grid_t = list(raw_input().strip())
    grid.append(grid_t)

for i in xrange(1,n-1):
    for j in xrange(1,n-1):
        if (grid[i][j-1] != 'X' and grid[i][j]>grid[i][j-1]) and (grid[i][j+1] != 'X' and grid[i][j]>grid[i][j+1]) and (grid[i-1][j] != 'X' and grid[i][j]>grid[i-1][j]) and (grid[i+1][j] != 'X' and grid[i][j]>grid[i+1][j]):
            grid[i][j] = 'X'

for line in grid:
    print ''.join(line)
