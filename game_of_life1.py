#!/usr/bin/python
# -*- coding: utf-8 -*-
#copyRight by Nicolas P. Rougier https://github.com/rougier/numpy-tutorial

import numpy as np  
import matplotlib.pyplot as plt  
import matplotlib.animation as animation 

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

 

Z1 = [[0,0,0,0,0,0],
     [0,0,0,1,0,0],
     [0,1,0,1,0,0],
     [0,0,1,1,0,0],
     [0,0,0,0,0,0],
     [0,0,0,0,0,0]] 
     
def am_test():
    N=50
    M = np.zeros((N,N))
    M[0:6,0:6]=Z1
    
    Z = np.random.randint(0,2,(10,10))
    #M[0:10,0:10]=Z

    fig = plt.figure()  
    axes1 = fig.add_subplot(111)  
    line = axes1.imshow(M,interpolation='nearest', cmap=plt.cm.gray_r)
      
    def update(data):  
        line.set_data(data)  
        return line
    # 生成器提供参数  
    def data_gen():
        t=M 
        while True:  
            iterate(t)
            yield t  
      
    ani = animation.FuncAnimation(fig, update, data_gen, interval=10)  
    plt.show()


if __name__=='__main__':
    am_test()