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

    for (f, i) in zip(files, range(20)):
        
        im = cv2.imread(f)
        im = cv2.medianBlur(im,5)

        # th2 = cv2.adaptiveThreshold(im,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2)
        # th3 = cv2.adaptiveThreshold(im,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

        # gray scale
        sigma = 2

        # find canny edges | for static sigma
        edged = cv2.Canny(gray, 500, 200) 

        # compute the median of the single channel pixel intensities
        v = np.median(gray)

        # apply automatic Canny edge detection using the computed median
        lower = int(max(0, (1.0 - sigma) * v))
        upper = int(min(255, (1.0 + sigma) * v))
        edged = cv2.Canny(gray, lower, upper)

        # find contours | use copy of the canny edges couse find contours alters image 
        contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # draw contours on black foreground
        cv2.imshow('Canny Edges After Contouring', edged) 
        # px, py = 400*(i%4), 400*int(i/5)
        # cvs.paste(edged, (px, py))#, px + 400, py + 400))

        # draw color contours on original image
        cv2.drawContours(im, contours, -1, (0, 255, 0), 3)   
        cv2.imshow('{}'.format(f[-13:]), im) 

        if cv2.waitKey(0): 
            cv2.destroyAllWindows() 
        elif cv2.waitKey(9):
            exit(0)


def resize(image):
    print(image)
    im = Image.open(image)
    imResize = im.resize((400,400), Image.ANTIALIAS)
    imResize.save(image + ' resized.jpg', 'JPEG', quality=90)


if __name__ == '__main__':
    main()