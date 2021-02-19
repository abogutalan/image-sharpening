import cv2
import numpy as np

# Load input image
original_image = cv2.imread('images/gnu_sharpen.png')

# Create a sharpening kernel
sharpening_filter = np.array([
    [-1,-1,-1],
    [-1,9,-1],
    [-1,-1,-1]
])

# Applying kernel(s) to the input image to get the sharpened image
sharpened_image = cv2.filter2D(original_image, -1, sharpening_filter)

cv2.imshow('Original Image', original_image)
cv2.imshow('Sharpened Image', sharpened_image)

cv2.waitKey(0)
cv2.destroyAllWindows()