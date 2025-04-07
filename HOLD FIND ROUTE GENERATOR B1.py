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

im = PIL.Image.open(r"C:\Users\Maggie\Pictures\Woody pictures\B1.png")
enhancer = PIL.ImageEnhance.Sharpness(im)
enhanced_im = enhancer.enhance(1.5)
enhanced_im.save(r"C:\Users\Maggie\Pictures\Woody pictures\sharp1.png")
sized=3
def openImage(path):
    # Open Image
    file_path = path
    img = cv2.imread(file_path,1)

    # Image can be resized to a standard size to speed up processing.
    c = sized*1000/img.shape[0]
    x = int(img.shape[0] * c)
    y = int(img.shape[1] * c)
    img = cv2.resize(img, (y,x))

    return img

# Let's load a simple image with 3 black squares 
image1 = openImage(r"C:\Users\Maggie\Pictures\Woody pictures\sharp1.png") 
image2 = openImage(r"C:\Users\Maggie\Pictures\Woody pictures\sharp1.png") 
image3 = openImage(r"C:\Users\Maggie\Pictures\Woody pictures\sharp1.png")
image4 = openImage(r"C:\Users\Maggie\Pictures\Woody pictures\sharp1.png")
image5 = openImage(r"C:\Users\Maggie\Pictures\Woody pictures\B1.png")


image1 = cv2.GaussianBlur(image1, (3, 3), 0)

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
    
    holdlocations = []
    holdradius = []
    holdhull =[]
    for cnt in hull:
        (x,y),radius = cv2.minEnclosingCircle(cnt)
        center = (int(x),int(y))
        radius = int(radius)
        holdlocations.append(center)
        holdradius.append(radius)
        
    holds =[holdlocations,holdradius,hull]

#cv2.imshow("Keypoints", drawing)

cv2.imwrite(r"C:\Users\Maggie\Pictures\Woody pictures\tryout blob.png", image2)

'''def holddraw(img,img1, n):
    
    j=0
    while j<n:
        #bluring
        img = cv2.GaussianBlur(img, (1,1), 0)
    
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
    return img1, holds'''



#imageX, holds = holddraw(image2,image3,1)

print(holds)
print(len(holds[0]))

print(len(holds[1]))


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

holdf = holdsizefilter(holds, 4,90)

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
		1.3, (255, 0, 55), 2)
        #return the image with the contour number drawn on it
    
    return image 
  
imageN = numberholds(image4,holdf)

cv2.imwrite(r"C:\Users\Maggie\Pictures\Woody pictures\tryout numbering.png", imageN)

#X AND Y AND TEH STARTING HOLDS

#this can be improved later. maybe split theta into 3 areas on the board. for now just do one theta until you get random route generation work.ing. Then theta can be improved. 

distanceholds30and43=82
h30 = holdf[0][29]
h43= holdf[0][42]
d3043=(((h30[0]-h43[0])**2) + (((h30[1]-h43[1])**np.cos(0.523599))**2))**(1./2.)
theta1=d3043/82
print(theta1)
distanceholds12and30=101
h12=holdf[0][11]
h30 =holdf[0][29]
d1330=((h30[0]-h12[0])**2 + ((h30[1]-h12[1])*np.cos(0.523599))**2)**(1./2.)
theta2=d1330/101
print(theta2)
maxarmspan= 180
maxarmlength = 84

def distanceratio(holds,h1,h2,d):
    ha = holds[0][h1-1]
    hb = holds[0][h2-1]
    dab=(((ha[0]-hb[0])**2) + (((ha[1]-hb[1])**np.cos(0.523599))**2))**(1./2.)
    theta=dab/d
    return theta

xxx= distanceratio(holdf,12,40,170)
print(xxx)

def Mindistancetoholds(point,holds):
    distance=[]
    holdno=[]
    for i in range(len(holds[0])):
        x=holds[0][i][0]
        y=holds[0][i][1]
        d=(((point[0]-x)**2) + ((point[1]-y)**2))**(1./2.)
        distance.append(d)
        holdno.append(i)
    holddist=[distance,holdno]
    minholdno = holddist[0].index(min(holddist[0]))
    
    return minholdno

def Routemake(holds,image,starthold,armlength):
    
    start=holds[0][starthold-1]
    
    X= start[0]
    Y= start[1]
    
    Xlist= [X]
    Ylist= [Y]
    'the list containing the co ordinates of different holds'
    R= [Xlist,Ylist]
    dmax=int(sized*1.58*armlength)
    
    while Y>97:
        
        X = X + random.randint(int(-1.6*dmax) ,int(1.6*dmax))
        Y = Y - random.randint(int(1.2*dmax) ,int(1.9*dmax))
        
        print(Y)
        z=[X,Y]
        holdchoice=Mindistancetoholds(z,holds)
                
        R[0] = R[0] + [holds[0][holdchoice][0]]
        R[1] = R[1] + [holds[0][holdchoice][1]]
    
    
    return R

a = np.array(Routemake(holdf,image5,160,84))
print(a[0])
print(a[1])
print(a[0][2])
for i in range(len(a[0])):
    cv2.circle(image5, (a[0][i],a[1][i]), 15, (255, 0, 0), 5)

cv2.imwrite(r"C:\Users\Maggie\Pictures\Woody pictures\routemadeB1.png", image5)


