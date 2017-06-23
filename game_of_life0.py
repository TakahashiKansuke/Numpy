#!/usr/bin/python
# -*- coding: utf-8 -*-
#copyRight by Nicolas P. Rougier https://github.com/rougier/numpy-tutorial


def compute_neighbours(Z):
    shape = len(Z), len(Z[0])
    N  = [[0,]*(shape[0])  for i in range(shape[1])]
    for x in range(1,shape[0]-1):
        for y in range(1,shape[1]-1):
            N[x][y] = Z[x-1][y-1]+Z[x][y-1]+Z[x+1][y-1] \
                    + Z[x-1][y]            +Z[x+1][y]   \
                    + Z[x-1][y+1]+Z[x][y+1]+Z[x+1][y+1]
    return N

    
def iterate(Z):
    rows,cols = len(Z), len(Z[0])
    N = compute_neighbours(Z)
    for x in range(1,cols-1):
        for y in range(1,rows-1):
            if Z[y][x] == 1 and (N[y][x] < 2 or N[y][x] > 3):
                Z[y][x] = 0
            elif Z[y][x] == 0 and N[y][x] == 3:
                Z[y][x] = 1
    return Z
    
def show(Z):
    for l in Z[1:-1]: print l[1:-1]
    print

 

Z = [[0,0,0,0,0,0],
     [0,0,0,1,0,0],
     [0,1,0,1,0,0],
     [0,0,1,1,0,0],
     [0,0,0,0,0,0],
     [0,0,0,0,0,0]] 
     
for i in range(4): 
    iterate(Z)
    show(Z)