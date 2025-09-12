import cv2
# from detection_setup import ocr, plate_cascade
import config
from service.text_reader import read_plate_text
 
def detect_plate(img, ocr, plate_cascade):
 
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    plates = plate_cascade.detectMultiScale(img_gray, 1.1, 4)
 
    for (x, y, w, h) in plates:
        area = w * h
        if area > config.MIN_PLATE_AREA:
            cv2.rectangle(img, (x,y), (x+w+10, y+h+10), (0,255,0), 2)
            img_roi = img[y:y + h + 10, x:x + w + 10]
            read_plate_text(img_roi, ocr)
            cv2.imshow("Detected Plate", img_roi)