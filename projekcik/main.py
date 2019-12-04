import barcode_detection
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

	cv2.imshow("Image", frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()