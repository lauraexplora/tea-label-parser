import cv2
import numpy as np
import pytesseract
from pytesseract import Output
import re

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

def read_label():
    # Capture frame-by-frame
    # for _ in range(50):  # Read 10 frames to allow the camera to stabilize
    success, frame = cap.read()
    if (not success):
        print('FAIL')
        return None
    t = pytesseract.image_to_string(thresholding(get_grayscale(frame)), lang='deu', output_type=Output.DICT)

    print(t)
    
    s = re.search(r"[0-9]+(\s*-\s*)*[0-9]*([,.]+[0-9]+)*(?=\sMin)", t['text'])
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
    l.replace(',','.')

    m = float(l)
    return int(m * 60000)

while True:
    label = read_label()
    if label:
        print('MATCH')
        print(label_to_ms(label))
        break
    
 
# When everything done, release the capture
cap.release()