# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 17:10:12 2020

@author: Maggie
"""

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread(r"C:\Users\Maggie\Pictures\Woody pictures\2.png",0)
edges = cv.Canny(img,150,200)
plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()