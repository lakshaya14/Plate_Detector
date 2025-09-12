from utils.clean_plate import remove_space_and_special_char as filter_valid_plates
 
def read_plate_text(img_roi, ocr):
    """
    Runs OCR on the plate image and processes the detected text.
    Returns the plate text and accuracy if detected, else None.
    """
    output = ocr.ocr(img_roi)
 
    # Make sure OCR returned at least one result
    if output and len(output) > 0:
        rec_texts = output[0].get('rec_texts', [])
        rec_scores = output[0].get('rec_scores', [])
 
        if rec_texts and rec_scores:
            num_plate = rec_texts[0]
            accuracy = rec_scores[0]
            # Filter plate text if needed
            filter_valid_plates(num_plate, accuracy)
            return num_plate, accuracy
 
    # If OCR detected nothing, return None
    return None, None