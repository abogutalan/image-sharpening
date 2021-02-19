# Laplacian filter is also called Mexican hat.

import cv2
import numpy as np

# Load input image
original_image = cv2.imread('images/gnu_sharpen.png')

# Creating mexican hat filter
mexican_hat_filter = np.array([
    [0, 0, -1, 0, 0], 
    [0, -1, -2, -1, 0],
    [-1, -2, 16, -2, -1], 
    [0, -1, -2, -1, 0], 
    [0, 0, -1, 0, 0]
])

# Applying cv2.filter2D function on our original image
mexican_hat_img = cv2.filter2D(original_image, -1, mexican_hat_filter)

cv2.imshow('Original Image', original_image)
cv2.imshow('Mexican Hat Image', mexican_hat_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
