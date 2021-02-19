import cv2
import numpy as np

# Load input image
original_image = cv2.imread('images/gnu_sharpen.png')

# Creating our arbitrary filter
arbitrary_filter = np.array([
    [3, -2, -3], 
    [-4, 8, -6], 
    [5, -1, -0]
])

# Applying kernel/filter to the input image to get the sharpened image
custom_img = cv2.filter2D(original_image,-1,arbitrary_filter)

cv2.imshow('Original Image', original_image)
cv2.imshow('Custom Image', custom_img)

cv2.waitKey(0)
cv2.destroyAllWindows()