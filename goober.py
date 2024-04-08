import cv2
import rainbowhat
import time

from tea_label import read_label, label_to_ms, get_minutes
from countdown import Countdown
from yourewelcome import midi

def ms_to_clock(ms):
    seconds=int((ms/1000)%60)
    minutes=int((ms/(1000*60))%60)
    if (minutes > 99):
        minutes = 99
        seconds = 99

    seconds_str = str(seconds)
    minutes_str = str(minutes)

    if (len(seconds_str) < 2):
        seconds_str = '0' + seconds_str

    if (len(minutes_str) < 2):
        minutes_str = ' ' + minutes_str

    return minutes_str + seconds_str

class Goober:
    def __init__(self) -> None:
        self._timer = Countdown(0)
        self._cap = cv2.VideoCapture(0)
        self._cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
        self._ms = 0
        self._scan = False
        self._scan_message = 'SCAN'

        self._display_clock()

    def __del__(self):
        self._cap.release()
        self._clear()

    def _display_message(self, message):
        rainbowhat.display.print_str(message)
        rainbowhat.display.show()

    def _display_clock(self):
        clock_str = ms_to_clock(self._ms)
        self._display_message(clock_str)

    def _reset_scan(self):
        self._scan = False
        self._scan_message = 'SCAN'

    def _clock(self):
        rainbowhat.rainbow.clear()
        self._display_clock()

    def toggle_scan(self):
        self._scan = not self._scan

    def scan_packet(self):
        self._display_message(self._scan_message)
        rainbowhat.rainbow.set_all(127, 127, 127)
        rainbowhat.rainbow.show()
        _, frame = self._cap.read()
        label = read_label(frame)
        print(label)
        if label != '':
            self._scan_message = 'WAIT'
            minutes = get_minutes(label)
            if (minutes):
                self._ms = label_to_ms(minutes)
                # TODO: If longer than makes sense, reject?
                self._reset_scan()
                self._clock()
        else:
            self._scan_message = 'SCAN'
    
    def add_minute(self):
        self._ms += 60000
        self._display_clock()

    def add_second(self):
        self._ms += 1000
        self._display_clock()

    def set_time(self, ms):
        self._ms = ms
        self._display_clock()

    def run(self):
        if(self._scan):
            self.scan_packet()
        else:
            self._clock()
    
g = Goober()

@rainbowhat.touch.A.press()
def press_a(channel):
    g.toggle_scan()

while True:
    g.run()
    # time.sleep(0.05)

# while 1:
#     midi()
#     # GPIO.cleanup()