import barcode_detection
import time
from pyzbar import pyzbar
import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
 
while True:
	ret, frame = cap.read()

	# call barcode detection funtction
	barcodeBox = barcode_detection.detect(frame)
 
	if barcodeBox is not None:
		cv2.drawContours(frame, [barcodeBox], -1, (0, 255, 0), 2)
		barcodes = pyzbar.decode(barcodeBox)

		for barcode in barcodes:
			(x, y, w, h) = barcode.rect # extracting and drawing barcode bounds frame
			# cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
    
	    	# barcode conversion (get type and data)
			barcodeType = barcode.type
			barcodeData = barcode.data.decode("utf-8")
    
	    	# drawing barcode data and barcode type
			# text = "{} ({})".format(barcodeData, barcodeType)
			# cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
 
	    	# print the barcode type and data
			print("[INFO] Found {} barcode: {}".format(barcodeType, barcodeData))


	cv2.imshow("Image", frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()