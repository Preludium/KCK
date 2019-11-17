import numpy as np
from pyzbar import pyzbar
import cv2

cap = cv2.VideoCapture(0)

cap.set(3, 1280)
cap.set(4, 720)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # print(str(len(frame)) + " x " +str(len(frame[0])))
    # Our operations on the frame come here
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    barcodes = pyzbar.decode(frame)
    barcodeData = ""
    for barcode in barcodes:
	    # extract the bounding box location of the barcode and draw the
	    # bounding box surrounding the barcode on the image
	    (x, y, w, h) = barcode.rect
	    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
    
	    # the barcode data is a bytes object so if we want to draw it on
	    # our output image we need to convert it to a string first
	    barcodeData = barcode.data.decode("utf-8")
	    barcodeType = barcode.type
    
	    # draw the barcode data and barcode type on the image
	    text = "{} ({})".format(barcodeData, barcodeType)
	    cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
	    	0.5, (0, 0, 255), 2)
 
	    # print the barcode type and data to the terminal
	    print("[INFO] Found {} barcode: {}".format(barcodeType, barcodeData))


    # show the output image
    cv2.imshow("Image", frame)
    # if barcodeData != "":
        # cap.grab()
        # while(True):
        #     if cv2.waitKey(2) & cv2.waitKey(1):
        #         break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()