# -*- coding: utf-8 -*-
"""
Thursday 25 Feb 2021
Python 3.7.1
Sam E. Wiegand

Purpose:
Produce images of concentric shapes (circle, square, equilateral triangle)
in grayscale where the intensity at some 'radius' from the center is based
on a given sinusoid and contrast %.

Note that x and y are used as coordinates, where positive x is 'down' and
positive y is 'right' in the produced image.

"""

import numpy as np
import png

#
# FUNCTION DEFINITIONS
#

# Returns radius of (x,y) from image center for concentric circles
def circleRadius(x, y, width):
    center = width/2
    return (((center) - (x+1))**2 + ((center) - (y+1))**2)**(0.5)


# Defines 'radius' of (x,y) from image center for concentric squares
def squareRadius(x, y, width):
    center = width/2

    if (abs(y+1 - center) > abs(x+1 - center)):
        # left/right side of the square
        return abs(y+1 - center)
    else:
        # top/bottom side of the square
        return abs(x+1 - center)


# Defines 'radius' of (x,y) from image center for concentric triangles
# This is an equilateral triangle oriented with one side parallel
#   with the bottom of the image. The angles between sides are all 60°
def triangleRadius(x, y, width):
    center = width/2

    # Check if on the bottom side of the triangle
    if ((x+1) > center):
        if (np.tan(np.pi/3) >= abs((y+1) - center) / ((x+1) - center)):
           return (-center + (x+1))

    # Else, define vector v as the direction perpendicular to
    #   the left/right sides of the concentric triangles.
    vx = np.tan(np.pi/6)
    vy = 1

    # Use vector projection to determine the 'radius'
    # The projection of a onto b is:
    #   proj = (a • b) / |b|
    dot_product = (center - (x+1))*vx + abs((y+1) - center)*vy
    return dot_product / (vx**2 + vy**2)**(0.5)


# Draws the picture at full contrast
def drawImage(width, shape):

    # Initialize image as an empty numpy array
    im = np.empty((width, width), dtype='float')

    # Calculate all pixel values based on radii definitions
    for i in range(width):
        for j in range(width):
            if (shape == 'circle'):
                radius = circleRadius(i, j, width)
            elif (shape == 'square'):
                radius = squareRadius(i, j, width)
            else:
                radius = triangleRadius(i, j, width)
            im[i][j] = sinusoid(radius)
    return im


# Normalizes the image to the specified contrast % and average intensity
def normalizeImage(im, bits, contrast, contrast_offset):

    # Define max intensity according to bit size and contrast
    abs_max = (2**bits - 1)
    scaled_max = abs_max * contrast

    # Normalize image intensities accordingly
    im -= im.min()
    im /= im.max()
    im *= scaled_max

    # Center around specified intensity offset
    im += (abs_max * contrast_offset) - (scaled_max * contrast_offset)
    return im


# Saves image to folder or filepath specified
def saveImage(im, filepath, bits):
    # Convert from float to uint
    if (bits == 8):
        im = im.astype(np.uint8)
    elif (bits == 16):
        im = im.astype(np.uint16)
    elif (bits == 32):
        im = im.astype(np.uint32)
    else:
        print("jank warning")

    # Save image
    tool = png.Writer(width=width, height=width, bitdepth=bits, greyscale=True)
    tool.write(open(filepath, 'wb'), im)


#
# MAIN PROGRAM
#

if __name__=="__main__":

    # Basic variables
    width = 1000 # im side length in pixels
    shape = 'square' # options: ['circle', 'square', 'triangle']
    contrast = 1.0 # 1.0 = full contrast
    contrast_offset = 0.5 # average intensity level
    bits = 16 # 8-bit, 16-bit, etc. final image

    # Sinusoidal parameters
    # (can be changed to any formula as desired)
    def sinusoid(radius):
        return np.sin(.05 * radius) + np.sin(.15 * radius)

    # Filepath and file name to save to
    filepath = 'concentric_ims\\test.png' # use double \ in filepath

    # Draw and save image
    im = drawImage(width, shape)
    im = normalizeImage(im, bits, contrast, contrast_offset)
    saveImage(im, filepath, bits)
