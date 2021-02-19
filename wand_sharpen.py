# import Image from wand.image module 
from wand.image import Image 
  
# Read image using Image function 
with Image(filename ="images/gnu_sharpen.png") as img: 
  
    # generating sharp image using sharpen() function. 
    img.sharpen(radius = 16, sigma = 8) 
    img.save(filename ="wandImage.jpeg")
    print("Shapened Image is created in the root drectory")
 