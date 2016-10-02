#!/usr/bin/env python
# -*- encoding:utf-8 -*-


#square lattice, Monte Carlo Mothed, Ising Model


from math import exp 
import random
#import numpy as np
import time

from gl import *

def flip():
    i = random.randint(0,L-1)
    j = random.randint(0,L-1)
    lattice[i][j] = - lattice[i][j]

def getEnergy():
    Energy = 0
    for i in range(L):
        for j in range(1,L-1):
           Energy = Energy + lattice[i][j-1]*lattice[i][j]
    for j in range(L):
        for i in range(1, L-1):
           Energy = Energy + lattice[i-1][j]*lattice[i][j]

    for i in range(L):
        for j in range(L):
            Energy = Energy + J * lattice[i][j]
    return Energy
	
def Update():
    global lattice
    E1=getEnergy()
    latticeCOPY=lattice
    flip()
    E2=getEnergy()
    deltaE=E2-E1

    if(deltaE>0):
        if(random.random() >= exp(-beta*deltaE)):
            lattice = latticeCOPY


def warmup():
    for i in range(warmtime):
        Update()
	   
if __name__ == "__main__":
    start = time.clock()
    print(getEnergy())
    warmup()
    #E = []

    print(getEnergy())
    
    E = 0	
    for i in range(sampleSize):
        Update()
        #E.append(getEnergy())
        E = E + getEnergy()
    #print(np.mean(np.array(E)))
    print(E/sampleSize)
    print(getEnergy())
    for i in range(L):
        print(lattice[i])
    end = time.clock()
    print("time: %f s" %(end-start))
