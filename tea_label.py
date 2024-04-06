import cv2
import pytesseract
from pytesseract import Output
import re

def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

def read_label(frame):
    t = pytesseract.image_to_string(thresholding(get_grayscale(frame)), lang='deu', output_type=Output.DICT)
    return t['text']
    
def get_minutes(ocr):
    # TODO: account for 'Mın'?
    # TODO: account for 'Mindestens'
    s = re.search(r"[0-9]+(\s*-\s*)*[0-9]*([,.]+[0-9]+)*(?=\s*Min)", ocr)
    if (s is not None):
        return s.group()
    return s

def label_to_ms(label):
    # Remove whitespace
    l = label.replace(' ', '')
    # Use the minimum brewing time
    if ('-' in l):
        l = l.split('-')[0]
    # Ensure decimals are in non-EU format
    l = l.replace(',','.')

    m = float(l)

    return int(m * 60000)