# from pylab import *
import skimage
from skimage import data, io, filters, exposure, feature, measure
from skimage.filters import rank, threshold_otsu
# from skimage.util.dtype import convert
from skimage import img_as_float, img_as_ubyte
# from skimage.io import Image
from skimage.color import rgb2hsv, hsv2rgb, rgb2gray
# from skimage.filters.edges import convolve
from matplotlib import pylab as plt  
import numpy as np
from numpy import array
from os import walk
import os


def main():

    files = []
    for file in os.listdir('images'):
        # print('{}'.format(os.path.join(os.getcwd(), 'images', file)))
        files.append('{}'.format(os.path.join(os.getcwd(), 'images', file)))

    for (f, i) in zip(files, range(20)):
        
        im = img_as_float(io.imread(f))
        gray = rgb2gray(im)

        # thresh = threshold_otsu(gray)
        # thresholded_img = gray > thresh
        # median = filters.rank.median(gray, np.ones([3,3],dtype=np.uint8))
        # img_filled = np.zeros_like(gray, dtype=)
        # rr, cc = skimage.draw.polygon(gray[:, 0], gray[:, 1], im.shape)
        # img_filled[rr, cc] = 1
        # label = skimage.measure.label(img_filled)
        # rprops = skimage.measure.regionprops(label)

        # print (rprops[0].centroid / np.asarray([400, 400]))
        contours = measure.find_contours(gray, 0.33)
        # contours = sorted(contours, key=lambda x: len(x))[-1]

        
        # Display the image and plot all contours found
        fig, ax = plt.subplots()
        ax.imshow(im, interpolation='nearest', cmap=plt.cm.gray)

        for n, c in enumerate(contours):
            ax.plot(c[:, 1], c[:, 0], linewidth=2)

        ax.axis('image')
        ax.set_xticks([])
        ax.set_yticks([])
        plt.show()


if __name__ == '__main__':
    main()