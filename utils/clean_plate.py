import re
from service.database_model import DatabaseHandler 

detected_plates = set()
def remove_space_and_special_char(plate_text, accuracy):
    plate_text = plate_text.replace(" ", "") 
    plate_text = re.sub(r'[^a-zA-Z0-9]', '', plate_text) 
    plate_text = plate_text.upper() 
    clean_text = check_match_with_plate_pattern(plate_text)
    if clean_text != None:
        remove_duplicate_plates(clean_text, accuracy)
    return clean_text
def check_match_with_plate_pattern(plate_text):
    plate_pattern = re.compile(r'^[A-Z]{2}\d{2}[A-Z]{1,2}\d{4}$')  
    if plate_pattern.match(plate_text):
        return plate_text 
    else:
        return     
def remove_duplicate_plates(plate_text, accuracy):
    status = "Known"
    direction = "Entry"
    accuracy = round(accuracy, 2)
    if accuracy > 0.8 and 9 < len(plate_text) < 11 and plate_text not in detected_plates:
        print(f"Detected: {plate_text} | Accuracy: {accuracy:.2f}")
        detected_plates.add(status)
        detected_plates.add(plate_text)        
        detected_plates.add(direction)        
        detected_plates.add(accuracy)
        print(detected_plates)
        db = DatabaseHandler()
        db.store_plate(plate_text,accuracy,status,direction)
        db.close()
        
    return detected_plates
