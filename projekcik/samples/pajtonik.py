import cv2
import argparse
from pyzbar import pyzbar
from matplotlib import pyplot as plt
from skimage import data, io, filters, exposure, feature, measure, morphology

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to input image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

barcodes = pyzbar.decode(image)

for barcode in barcodes:
	# extract the bounding box location of the barcode and draw the
	# bounding box surrounding the barcode on the image
	(x, y, w, h) = barcode.rect
	cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
 
	# the barcode data is a bytes object so if we want to draw it on
	# our output image we need to convert it to a string first
	barcodeData = barcode.data.decode("utf-8")
	barcodeType = barcode.type
 
	# draw the barcode data and barcode type on the image
	text = "{} ({})".format(barcodeData, barcodeType)
	cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
		0.5, (0, 0, 255), 2)
 
	# print the barcode type and data to the terminal
	print("[INFO] Found {} barcode: {}".format(barcodeType, barcodeData))
 
# show the output image
cv2.imshow("Image", image)
cv2.waitKey(0)

# fig, ax = plt.subplot()

# for c in barcodes:
#     ax.plot(c[:, 1], c[:, 0], linewidth=1)



# ax.imshow(image, interpolation='nearest', cmap=plt.cm.gray)
# ax.axis('image')
# ax.set_xticks([])
# ax.set_yticks([])
# plt.show()
