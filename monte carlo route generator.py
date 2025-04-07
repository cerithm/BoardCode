# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 16:56:41 2020

@author: Maggie
"""

import random
import matplotlib.pyplot as plt

# vertical movement
a = random.randint(0,3) 
d = random.randint(2,4) 

'Horizontal movement'
b = random.randint(-3,3)
c = random.randint(-5,5) 
'Holds_per_row'
hpr=[2,5,1,4,5,8,5]

print(c)

'x and y is the position of the starting hold'
'''def Routemake(x,y):
    
    
    X= [x]
    Y= [y]
    'the list containing the co ordinates of different holds'
    R= [[x],[y]]
    
    
    while y<7:
        
        #x = x + random.randint(-5 ,5)
        y = y +  random.randint(random.randint(0,1),3)
        if y>7:
            y = 7
        print(y)
        z= hpr[y-1]
        
        x = random.randint(1, z)
        
        
        R[0] = R[0] +[x] 
        R[1] = R[1] +[y]
        
    return R

'random start holds'
rst=[0,0]
rst[1]= random.randint(1,3)
rst[0]= random.randint(1,hpr[rst[1]-1])


r1= Routemake(rst[0],rst[1])

print(r1) 
plt.plot(r1[0],r1[1])'''

    
