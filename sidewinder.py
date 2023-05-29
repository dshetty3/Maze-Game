# generates a square maze (size*size) with the sidewinder technique

import numpy as np
import random as rd


class SideWinder:

    def __init__(self):
        pass

    def carve_maze(self, grid:np.ndarray, size:int) -> np.ndarray:
        output_grid = np.empty([size*3, size*3],dtype=str)
        output_grid[:] = 0
        
        i = 0
        j = 0
        
        
        while i < size:
            previous_l = []
            w = i*3 + 1
            while j < size:
                k = j*3 + 1
                toss = grid[i,j]
                output_grid[w,k] = 1
                if toss == 0 and k+2 < size*3:
                    output_grid[w,k+1] = 1
                    output_grid[w,k+2] = 1
                    previous_l.append(j)
                if toss == 1:
                    # it's impossible to carve outside after preprocessing
                    # look back, choose a random cell
                    if grid[i,j-1] == 0:
                        # reaching from 0
                        # mandatory to be sure that previous_l has at least one element
                        # if we are coming from a list of previous cells, choose one and...
                        r = rd.choice(previous_l)
                        k = r * 3 + 1
                    
                    # ...just carve north
                    # this just carve north if this is the first element of the row (1 element loop)
                    output_grid[w-1,k] = 1
                    output_grid[w-2,k] = 1
                    previous_l = []
                
                j += 1
                
            i += 1
            j = 0
            
        return output_grid

    def preprocess_grid(self, grid, size) :
        # fix first row and last column to avoid digging outside the maze external borders
        first_row = grid[0]
        first_row[first_row == 1] = 0
        grid[0] = first_row
        for i in range(1,size):
            grid[i,size-1] = 1
        return grid



    def generate(self, dims):
        n=1
        p=0.5
        size=dims


        grid = np.random.binomial(n,p, size=(size,size))
        processed_grid = self.preprocess_grid(grid, size)

        maze = self.carve_maze(processed_grid, size)
        maze = maze.tolist()
        for i in range(len(maze)):
            for j in range(len(maze[0])):
                if maze[i][j] == '0':
                    maze[i][j] = 0
                elif maze[i][j] == '1':
                    maze[i][j] = 1
        
        maze = np.array(maze)
                


        return maze

    

