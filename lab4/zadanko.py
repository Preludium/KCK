from pylab import *
# import skimage
# from skimage import data, io, filters, exposure, feature
# from skimage.filters import rank
# from skimage.util.dtype import convert
# from skimage import img_as_float, img_as_ubyte
# from skimage.io import ImageCollection
# from skimage.color import rgb2hsv, hsv2rgb, rgb2gray
# from skimage.filters.edges import convolve
# from matplotlib import pylab as plt  
import numpy as np
from numpy import array
from PIL import Image
import cv2
from os import walk
import os


def main():

    files = []
    for file in os.listdir('images'):
        # print('{}'.format(os.path.join(os.getcwd(), 'images\\', file)))
        files.append('{}'.format(os.path.join(os.getcwd(), 'images\\', file)))

    # img = Image.open(files[1])
    # (x, y) = img.size

    # cvs = Image.new('RGB', (5 * x, 5 * y))

    for (f, i) in zip(files, range(1, 22)):
        # dobry4.jpg do wyjebania
        im = cv2.imread(f)
        # im.resize(x, y)

        # gray scale
        gray = cv2.cvtColor(src = im, code = cv2.COLOR_BGR2GRAY)
        sigma = 0.33

        # find canny edges | for static sigma
        # edged = cv2.Canny(gray, 500, 200) 

        # compute the median of the single channel pixel intensities
        v= np.median(im)

        # apply automatic Canny edge detection using the computed median
        lower = int(max(0, (1.0 - sigma) * v))
        upper = int(min(255, (1.0 + sigma) * v))
        edged = cv2.Canny(im, lower, upper)

        # find contours | use copy of the canny edges couse find contours alters image 
        contours, hierarchy = cv2.findContours(image = edged.copy(), mode = cv2.RETR_EXTERNAL, method = cv2.CHAIN_APPROX_SIMPLE)

        # draw contours on black foreground
        cv2.imshow('Canny Edges After Contouring', edged) 
        # px, py = x*int(i/5), y*(i%5)
        # cvs.paste(edged, (px, py))

        # draw color contours on original image
        cv2.drawContours(im, contours, -1, (0, 255, 0), 3)   
        cv2.imshow('{}'.format(f[-13:]), im) 

        if cv2.waitKey(0): 
            cv2.destroyAllWindows() 
        elif cv2.waitKey(9):
            exit(0)

    # cvs.save('plocik.jpg', format='jpg')


if __name__ == '__main__':
    main()