import skimage
from skimage import data, io, filters, exposure, feature, measure, morphology
from skimage.filters import rank, threshold_otsu
from skimage import img_as_float, img_as_ubyte
from skimage.color import rgb2hsv, hsv2rgb, rgb2gray, rgb2hed
from matplotlib import pylab as plt 
import numpy as np
from numpy import array
from PIL import Image
import cv2
from os import walk
import os

def main():

    files = []
    for file in os.listdir('images'):
        # print('{}'.format(os.path.join(os.getcwd(), 'images', file)))
        files.append('{}'.format(os.path.join(os.getcwd(), 'images', file)))

    fig, axs = plt.subplots(2, 3)

    black = Image.new('RGB', (400, 400), 'black')

    for (f, i, ax) in zip(files, range(6), axs.ravel()):
        
        # Read image
        im = io.imread(f)

        # Resize image
        im = skimage.transform.resize(im, (400, 400), anti_aliasing=True)

        # Color conversion
        im_hed = rgb2hed(im)

        # Rescale colors to (0..1) and stack it to list
        h = exposure.rescale_intensity(im_hed[:, :, 0], out_range=(0, 1))
        d = exposure.rescale_intensity(im_hed[:, :, 2], out_range=(0, 1))
        zdh = np.dstack((np.zeros_like(h), d, h))

        # To grayscale
        gray = rgb2gray(zdh)
        # plt.imshow(gray)

        # Get factor of brightness threshold
        thresh = threshold_otsu(gray)

        # Transform to binary image 
        im_bin = gray > thresh

        # Apply dilatation
        im_bin = morphology.dilation(im_bin, morphology.square(5))
        
        # Remove small objects 
        im_bin = morphology.remove_small_objects(im_bin)

        # Find contours
        contour = measure.find_contours(im_bin, 0.8)
        
        # Plot all contours found and add circle in the centre
        for n, c in enumerate(contour):
            if(len(c) > 100):
                ax.plot(c[:, 1], c[:, 0], linewidth=1, color='white')

        ax.imshow(black, interpolation='nearest', cmap=plt.cm.gray)

        ax.axis('image')
        ax.set_xticks([])
        ax.set_yticks([])

    plt.show()

if __name__ == '__main__':
    main()