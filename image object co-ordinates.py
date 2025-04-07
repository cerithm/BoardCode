# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 15:30:04 2020

@author: Maggie
"""

#!/usr/bin/env python3

import numpy as np
import cv2

# Load image
#impath = 'C:\Users\Maggie\Pictures\Woody pictures\my woody 1.png'
im = cv2.imread(r"C:\Users\Maggie\Pictures\Woody pictures\my woody 1.png")

# Convert to grayscale and threshold
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,1,255,0)

# Find contours, draw on image and save
im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(im, contours, -1, (0,255,0), 3)
cv2.imwrite('result.png',im)

# Show user what we found
for cnt in contours:
   (x,y),radius = cv2.minEnclosingCircle(cnt)
   center = (int(x),int(y))
   radius = int(radius)
   print('Contour: centre {},{}, radius {}'.format(x,y,radius))