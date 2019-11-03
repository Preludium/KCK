# from pylab import *
# import skimage
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
from PIL import Image
import cv2
from os import walk
import os


def main():

    files = []
    for file in os.listdir('images'):
        # print('{}'.format(os.path.join(os.getcwd(), 'images', file)))
        files.append('{}'.format(os.path.join(os.getcwd(), 'images', file)))

    # for image in files:
    #     resize(image)
    # exit(0)

    # img = Image.open(files[1])
    # x, y = 0, 0
    # cvs = Image.new('RGB', (4 * 400, 5 * 400))

    for (f, i) in zip(files, range(20)):
        
        im = cv2.imread(f)
        im = cv2.medianBlur(im,5)

        th2 = cv2.adaptiveThreshold(im,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2)

        # th3 = cv2.adaptiveThreshold(im,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)
        # gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        # im = img_as_float(data.imread(f))
        # gray = rgb2gray(im)

        # thresh = threshold_otsu(gray)
        # thresholded_img = gray > thresh
        # median = filters.rank.median(gray, np.ones([3,3],dtype=np.uint8))
        # contours = measure.find_contours(thresholded_img, 0.5)
        # contour = sorted(contours, key=lambda x: len(x))[-1]

        # rr, cc = skimage.draw.polygon(c[:, 0], c[:, 1], shape=img.shape)
        # img_filled[rr, cc] = i
        # Display the image and plot all contours found
        # fig, ax = plt.subplots()
        # ax.imshow(im, cmap=plt.cm.gray)

        # for c in enumerate(contours):
            # if area > 10000:
                # ax.plot(c[:, 1], c[:, 0], linewidth=1)
        plt.imshow(th2)
        # ax.axis('image')
        # ax.set_xticks([])
        # ax.set_yticks([])
        plt.show()

        # gray scale
        # sigma = 2

        # find canny edges | for static sigma
        # edged = cv2.Canny(gray, 500, 200) 

        # compute the median of the single channel pixel intensities
        # v= np.median(gray)

        # apply automatic Canny edge detection using the computed median
        # lower = int(max(0, (1.0 - sigma) * v))
        # upper = int(min(255, (1.0 + sigma) * v))
        # edged = cv2.Canny(gray, lower, upper)
        # io.imshow(skimage.feature.canny(gray, sigma=3))

        # exit(0)
        # find contours | use copy of the canny edges couse find contours alters image 
        # contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # draw contours on black foreground
        # cv2.imshow('Canny Edges After Contouring', edged) 
        # px, py = 400*(i%4), 400*int(i/5)
        # print(px)
        # print(py)
        # cvs.paste(edged, (px, py))#, px + 400, py + 400))

        # draw color contours on original image
        # cv2.drawContours(im, contours, -1, (0, 255, 0), 3)   
        # cv2.imshow('{}'.format(f[-13:]), im) 

        # if cv2.waitKey(0): 
        #     cv2.destroyAllWindows() 
        # elif cv2.waitKey(9):
        #     exit(0)

    # cvs.save('plocik.jpg', format='jpg')


def resize(image):
    print(image)
    im = Image.open(image)
    imResize = im.resize((400,400), Image.ANTIALIAS)
    imResize.save(image + ' resized.jpg', 'JPEG', quality=90)


if __name__ == '__main__':
    main()