# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 12:26:58 2020

@author: Maggie
"""

import cv2 
import numpy as np 
import PIL
from PIL import ImageEnhance



# Let's load a simple image with 3 black squares 

cv2.waitKey(0) 

im = PIL.Image.open(r"C:\Users\Maggie\Pictures\Woody pictures\mw4.png")
enhancer = PIL.ImageEnhance.Sharpness(im)
enhanced_im = enhancer.enhance(1.2)
enhanced_im.save(r"C:\Users\Maggie\Pictures\Woody pictures\sharp1.png")


