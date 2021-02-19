import cv2
import numpy as np

# Load input image
original_image = cv2.imread('images/gnu_sharpen.png',0)

# Cross-shaped Kernel
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5)) 

# erosion
erosion = cv2.erode(original_image, kernel, iterations=1)
# dilation
dilation = cv2.dilate(original_image,kernel,iterations=1)
# opening = another name of erosion followed by dilation for removing noise
opening = cv2.morphologyEx(original_image, cv2.MORPH_OPEN, kernel)
# closing = reverse of opening, dilation followed by erosion to close black points on the object
closing = cv2.morphologyEx(original_image, cv2.MORPH_CLOSE, kernel)
# Morphological Gradient = dilation - erosion ==> outline of the object
gradient = cv2.morphologyEx(original_image, cv2.MORPH_GRADIENT, kernel)
# Top Hat = Original Image - Opening
tophat = cv2.morphologyEx(original_image, cv2.MORPH_TOPHAT, kernel)
# Black Hat = Closing - Original Image
blackhat = cv2.morphologyEx(original_image, cv2.MORPH_BLACKHAT, kernel)

# display images
cv2.imshow('Original Image',original_image)
cv2.imshow('Erosion',erosion)
cv2.imshow('Dilation',dilation)
cv2.imshow('Opening',opening)
cv2.imshow('Closing',closing)
cv2.imshow('Gradient',gradient)
cv2.imshow('Tophat',tophat)
cv2.imshow('Blackhat',blackhat)

cv2.waitKey(0)
cv2.destroyAllWindows()