import cv2
import rainbowhat

from tea_label import read_label, label_to_ms, get_minutes
from clock_display import display_clock, display_message
from countdown import Countdown
from yourewelcome import midi

class Goober:
    def __init__(self) -> None:
        self._timer = Countdown(0)
        self._cap = cv2.VideoCapture(0)
        self._cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
    
    def __del__(self):
        self._cap.release()
        rainbowhat.rainbow.clear()


    def scan_packet(self):
        while True:
            rainbowhat.rainbow.set_all(127, 127, 127)
            rainbowhat.rainbow.show()
            _, frame = self._cap.read()
            label = read_label(frame)
            if label != '':
                display_message('WAIT')
                minutes = get_minutes(label)
                if (minutes):
                    ms = label_to_ms(minutes)
                    # TODO: If longer than makes sense, reject?
                    rainbowhat.rainbow.clear()
                    break
            else:
                display_message('SCAN')

        return ms
    
g = Goober()
ms = g.scan_packet()
display_clock(ms)

# while 1:
#     midi()
#     # GPIO.cleanup()