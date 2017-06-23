#!/usr/bin/python
# -*- coding: utf-8 -*-
#copyRight by Nicolas P. Rougier https://github.com/rougier/numpy-tutorial

import numpy as np  
import matplotlib.pyplot as plt  
import matplotlib.animation as animation 

def iterate_1(Z):
    # Count neighbours
    N = np.zeros(Z.shape, int)
    N[1:-1,1:-1] += (Z[0:-2,0:-2] + Z[0:-2,1:-1] + Z[0:-2,2:] +
                     Z[1:-1,0:-2]                + Z[1:-1,2:] +
                     Z[2:  ,0:-2] + Z[2:  ,1:-1] + Z[2:  ,2:])
    N_ = N.ravel()
    Z_ = Z.ravel()

    # Apply rules
    R1 = np.argwhere( (Z_==1) & (N_ < 2) )
    R2 = np.argwhere( (Z_==1) & (N_ > 3) )
    R3 = np.argwhere( (Z_==1) & ((N_==2) | (N_==3)) )
    R4 = np.argwhere( (Z_==0) & (N_==3) )

    # Set new values
    Z_[R1] = 0
    Z_[R2] = 0
    Z_[R3] = Z_[R3]
    Z_[R4] = 1

    # Make sure borders stay null
    Z[0,:] = Z[-1,:] = Z[:,0] = Z[:,-1] = 0


def iterate_2(Z):
    # Count neighbours
    N = (Z[0:-2,0:-2] + Z[0:-2,1:-1] + Z[0:-2,2:] +
         Z[1:-1,0:-2]                + Z[1:-1,2:] +
         Z[2:  ,0:-2] + Z[2:  ,1:-1] + Z[2:  ,2:])

    # Apply rules
    birth = (N==3) & (Z[1:-1,1:-1]==0)
    survive = ((N==2) | (N==3)) & (Z[1:-1,1:-1]==1)
    Z[...] = 0
    Z[1:-1,1:-1][birth | survive] = 1
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
    M[0:10,0:10]=Z

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
            iterate_2(t)
            yield t  
      
    ani = animation.FuncAnimation(fig, update, data_gen, interval=10)  
    plt.show()


if __name__=='__main__':
    am_test()