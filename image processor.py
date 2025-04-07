# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 17:23:49 2020

@author: Maggie
"""

import cv2 
import numpy as np 
import PIL
from PIL import ImageEnhance
import random


# Let's load a simple image with 3 black squares 

cv2.waitKey(0) 

im = PIL.Image.open(r"C:\Users\Maggie\Pictures\Woody pictures\mw5.png")
enhancer = PIL.ImageEnhance.Sharpness(im)
enhanced_im = enhancer.enhance(9.5)
enhanced_im.save(r"C:\Users\Maggie\Pictures\Woody pictures\sharp1.png")

def openImage(path):
    # Open Image
    file_path = path
    img = cv2.imread(file_path,1)

    # Image can be resized to a standard size to speed up processing.
    c = 1000.0/img.shape[0]
    x = int(img.shape[0] * c)
    y = int(img.shape[1] * c)
    img = cv2.resize(img, (y,x))

    return img

# Let's load a simple image with 3 black squares 
image1 = openImage(r"C:\Users\Maggie\Pictures\Woody pictures\sharp1.png") 
image2 = openImage(r"C:\Users\Maggie\Pictures\Woody pictures\sharp1.png") 
image3 = openImage(r"C:\Users\Maggie\Pictures\Woody pictures\sharp1.png")
image4 = openImage(r"C:\Users\Maggie\Pictures\Woody pictures\sharp1.png")
image5 = openImage(r"C:\Users\Maggie\Pictures\Woody pictures\mw5.png")


image1 = cv2.GaussianBlur(image1, (5, 5), 0)

image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY) 

# Find Canny edges 
edged = cv2.Canny(image1, 30, 200) 
cv2.waitKey(0) 
  
# Finding Contours 
# Use a copy of the image e.g. edged.copy() 
# since findContours alters the image 
contours, hierarchy = cv2.findContours(edged,  
    cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 
  
#cv2.imshow('Canny Edges After Contouring', edged) 
cv2.waitKey(0) 

# create hull array for convex hull points
hull = []

# calculate points for each contour
for i in range(len(contours)):

    # creating convex hull object for each contour
    hull.append(cv2.convexHull(contours[i], False))



# Draws contours onto a blank canvas
drawing = np.zeros((image1.shape[0], image1.shape[1], 3), np.uint8)

for i in range(len(contours)):

    color_contours = (0, 255, 0) # green - color for contours

    color = (255, 0, 0) # blue - color for convex hull

    # draw ith contour

    #cv2.drawContours(drawing, contours, i, color_contours, 5, 5, hierarchy)

    # draw ith convex hull object

    cv2.drawContours(image2, hull, i, color, 3, 3)

#cv2.imshow("Keypoints", drawing)

cv2.imwrite(r"C:\Users\Maggie\Pictures\Woody pictures\tryout blob.png", image2)

def holddraw(img,img1, n):
    
    j=0
    while j<n:
        #bluring
        img = cv2.GaussianBlur(img, (7,7), 0)
    
        #greyscale
        #img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    
        #find edges
        edged = cv2.Canny(img, 30, 200) 
    
        cv2.waitKey(0) 
    
        contours, hierarchy = cv2.findContours(edged,  
                                               cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    
        # create hull array for convex hull points
        hull = []
    
        for i in range(len(contours)):

            # creating convex hull object for each contour
            hull.append(cv2.convexHull(contours[i], False))
        
        for i in range(len(contours)):

            color_contours = (0, 255, 0) # green - color for contours

            color = (255, 0, 0) # blue - color for convex hull

            # draw ith contour

            #cv2.drawContours(drawing, contours, i, color_contours, 5, 5, hierarchy)

            # draw ith convex hull object
            img = img1
            cv2.drawContours(img, hull, i, color, 3, 3)
        
        j = j+1
        
    for i in range(len(contours)):
        cv2.drawContours(img1, hull, i ,color, 3, 3)
    
    #make a hold filter
    print(hull)
    
    holdlocations = []
    holdradius = []
    holdhull =[]
    for cnt in hull:
        (x,y),radius = cv2.minEnclosingCircle(cnt)
        center = (int(x),int(y))
        radius = int(radius)
        holdlocations.append(center)
        holdradius.append(radius)
        
        print('Contour: centre {},{}, radius {}'.format(x,y,radius))
    
    holds =[holdlocations, holdradius,hull]
    return img1, holds



imageX, holds = holddraw(image2,image3,1)

print(holds)
print(len(holds[0]))

print(len(holds[1]))

print(len(holds[2]))

def holdsizefilter(holds,rmin,rmax):
    centerf = []
    radiusf = []
    hullf= []
    for i in range(len(holds[0])):
        if holds[1][i]>rmin and holds[1][i]<rmax:
            centerf.append(holds[0][i])
            radiusf.append(holds[1][i])
            hullf.append(holds[2][i])       
        i = i+1
    holdf=[centerf,radiusf,hullf]
    return holdf

holdf = holdsizefilter(holds, 13,62)

print(holdf[1])

for i in range(len(holdf[2])):

    color_contours = (0, 25, 0) # green - color for contours
    color = (25, 0, 0) # blue - color for convex hull
        

    # draw ith convex hull object

    cv2.drawContours(image4, holdf[2], i, color, 3, 3)
        
  
    

cv2.imwrite(r"C:\Users\Maggie\Pictures\Woody pictures\tryout redrawing2.png", image4)


def numberholds (image, holdf):
	# draw the countour number on the image
    for i in range(len(holdf[2])):
        cv2.putText(image, "#{}".format(i + 1), holdf[0][i], cv2.FONT_HERSHEY_SIMPLEX,
		1.0, (255, 255, 255), 2)
        #return the image with the contour number drawn on it
    
    return image 
  
imageN = numberholds(image4,holdf)

cv2.imwrite(r"C:\Users\Maggie\Pictures\Woody pictures\tryout numbering.png", imageN)



