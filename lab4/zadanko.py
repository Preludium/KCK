from pylab import *
import skimage
from skimage import data, io, filters, exposure, feature
from skimage.filters import rank
from skimage.util.dtype import convert
from skimage import img_as_float, img_as_ubyte
from skimage.io import Image
from skimage.color import rgb2hsv, hsv2rgb, rgb2gray
from skimage.filters.edges import convolve
from matplotlib import pylab as plt  
import numpy as np
from numpy import array

img = img_as_float(data.imread('img/noisy.png'))
#img = im
figure(figsize=(20,20))
subplot(1,3,1)
io.imshow(img**0.5)
subplot(1,3,2)
io.imshow(filters.sobel(img)**0.5)
subplot(1,3,3)
io.imshow(skimage.feature.canny(img, sigma=3))