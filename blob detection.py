# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 12:58:40 2020

@author: Maggie
"""

'''# Setup SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params()

# Change thresholds
params.minThreshold = 10
params.maxThreshold = 200


# Filter by Area.
params.filterByArea = True
params.minArea = 1500

# Filter by Circularity
params.filterByCircularity = True
params.minCircularity = 0.1

# Filter by Convexity
params.filterByConvexity = True
params.minConvexity = 0.87

# Filter by Inertia
params.filterByInertia = True
params.minInertiaRatio = 0.01

# Create a detector with the parameters
detector = cv2.SimpleBlobDetector(params)


# Detect blobs.
keypoints = detector.detect(edged)

# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures
# the size of the circle corresponds to the size of blob

im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Show blobs
cv2.imshow("Keypoints", im_with_keypoints)
cv2.waitKey(0)

cv2.imwrite(r"C:\Users\Maggie\Pictures\Woody pictures\out222.png", edged)'''

print("Number of Contours found = " + str(len(hull)))
for cnt in hull:
   (x,y),radius = cv2.minEnclosingCircle(cnt)
   center = (int(x),int(y))
   radius = int(radius)
   print('Contour: centre {},{}, radius {}'.format(x,y,radius))