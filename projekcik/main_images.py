import sys
import barcode_detection
from pyzbar import pyzbar
import cv2


if len(sys.argv) != 2:
    print("Add image path to command")
    exit(0)

path = str(sys.argv[1])

im = cv2.imread(path)
# im = cv2.resize(im, (1280, 720))
im = cv2.resize(im, (1920, 1080))

# call barcode detection function
barcodeBox = barcode_detection.detect(im)

if barcodeBox is not None:
	cv2.drawContours(im, [barcodeBox], -1, (0, 255, 0), 2)
	barcodes = pyzbar.decode(barcodeBox)
	for barcode in barcodes:
		# (x, y, w, h) = barcode.rect # extracting and drawing barcode bounds frame
		# cv2.rectangle(im, (x, y), (x + w, y + h), (0, 0, 255), 2)
   
    	# barcode conversion (get type and data)
		barcodeType = barcode.type
		barcodeData = barcode.data.decode("utf-8")
   
    	# drawing barcode data and barcode type
		# text = "{} ({})".format(barcodeData, barcodeType)
		# cv2.putText(im, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    	# print the barcode type and data
		print("Found {} barcode: {}".format(barcodeType, barcodeData))

cv2.imshow("Image", im)

cv2.waitKey(0)