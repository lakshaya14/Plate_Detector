# main.py
from controller.camera_controller import start_camera
from service.detection_setup import ocr, plate_cascade

if __name__ == "__main__":
        
    start_camera(ocr, plate_cascade)
