# Project Deliverable
> https://drive.google.com/file/d/19jnVzQhDyPJ_KYiSoOk746e7H9lXSPgh/view?usp=sharing

# How to run the program:

- Full package Download (contains both main modules and contrib/extra modules): 
> pip install opencv-contrib-python 

- Download and update skimage library for Unsharp Masking
> pip install scikit-image
> pip install --upgrade scikit-image

- Download Wand
> pip install wand
> brew install freetype imagemagick

- Instead of manually downloading libraries use the terminal commands below
> chmod 755 download_libraries.sh 
> ./download_libraries.sh

- Use terminal commands below to run all python scripts
> chmod 755 run_all.sh 
> ./run_all.sh

- Run python scripts:
python custom_filter.py
python fuzzy_morphological_filtering.py
python laplacian_filter.py
python sharpener.py
python sharpness_PIL.py
python unsharp_masking.py
python wand_sharpen.py

### Resources


###### How to Sharpen Image using Python OpenCV ?

- https://www.youtube.com/watch?v=MGDOrCpQwO4

- http://datahacker.rs/004-how-to-smooth-and-sharpen-an-image-in-opencv/#sharpen-an-image

- https://subscription.packtpub.com/book/application_development/9781785283932/2/ch02lvl1sec22/sharpening

##### Unsharp masking 

- https://scikit-image.org/docs/dev/auto_examples/filters/plot_unsharp_mask.html
- https://www.youtube.com/watch?v=_p_36DIJMIw

Unsharp masking works in two steps:

- Get the Laplacian (second derivative) of your image.
- Take away the Laplacian (or a fraction of it) from the original image.

Pseudocode:
> sharp_image = image - a * Laplacian(image)

##### Python Pillow – Adjust Image Sharpness
- https://pythonexamples.org/python-pillow-adjust-image-sharpness/

##### Python – sharpen() function in Wand
- https://www.geeksforgeeks.org/python-sharpen-function-in-wand/
