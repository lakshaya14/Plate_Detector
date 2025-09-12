import cv2
import config
from paddleocr import PaddleOCR

print("Before")
ocr = PaddleOCR(
    use_doc_orientation_classify=False, 
    use_doc_unwarping=False, 
    use_textline_orientation=False)
print("After")

plate_cascade = cv2.CascadeClassifier(config.HAARCASCADE_PATH)
if plate_cascade.empty():
    print("Error: Haar cascade not loaded!")
    exit(1)


