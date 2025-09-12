
# import cv2
# from service.number_plate_detector import detect_plate
# import config

# def start_camera(ocr, plate_cascade):
#     cap = cv2.VideoCapture(0)
#     cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
#     cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)

#     while True:
#         success, img = cap.read()
#         if not success:
#             break

#         detect_plate(img, ocr, plate_cascade)

#         cv2.imshow("Camera Output", img)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#     stop_camera()

# def stop_camera():
#     global cap
#     if cap is not None:
#         cap.release()
#         cv2.destroyAllWindows()


# import cv2
# from service.number_plate_detector import detect_plate
# import config

# def start_camera(ocr, plate_cascade):
#     cap = cv2.VideoCapture(0)
#     cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
#     cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)

#     while True:
#         success, img = cap.read()
#         if not success:
#             break

#         detect_plate(img, ocr, plate_cascade)

#         cv2.imshow("Camera Output", img)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     cap.release()
#     cv2.destroyAllWindows()
# controller/camera_controller.py
import cv2
from PIL import Image, ImageTk
from service.number_plate_detector import detect_plate

cap = None  

def start_camera(ocr, plate_cascade, label_widget):
    global cap
    if cap is None:
        cap = cv2.VideoCapture(0)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)

    def update_frame():
        global cap
        if cap is not None:
            success, frame = cap.read()
            if success:

                detect_plate(frame, ocr, plate_cascade)

                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(frame_rgb)
                imgtk = ImageTk.PhotoImage(image=img)

                label_widget.imgtk = imgtk  

                label_widget.config(image=imgtk)


            label_widget.after(30, update_frame)

    update_frame()

def stop_camera(label_widget=None):
    global cap
    if cap is not None:
        cap.release()
        cap = None
        if label_widget is not None:
            from PIL import Image, ImageTk
            img = Image.open("C:/Users/admin/Desktop/detector.png")
            img = img.resize((900, 500)) 
            
            img_tk = ImageTk.PhotoImage(img)
            label_widget.config(image=img_tk)
            label_widget.image = img_tk


            

            
