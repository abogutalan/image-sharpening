from PIL import Image, ImageEnhance

im = Image.open("images/gnu_sharpen.png")

enhancer = ImageEnhance.Sharpness(im)

# original image
factor = 1
im_s_1 = enhancer.enhance(factor)
im_s_1.show('original-img.png')

# sharpened image
factor = 4
im_s_1 = enhancer.enhance(factor)
im_s_1.show('sharpened-img.png')
