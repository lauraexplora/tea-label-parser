import time

class Countdown:
    def __init__(self, t) -> None:
        self._countdown = t
        self._start_time = 0

    def start(self):
        self._start_time = round(time.time() * 1000)
    
    def get_remaining(self):
        current_time = round(time.time() * 1000)
        remaining = self._countdown - (current_time - self._start_time)
        if (remaining < 0):
            return 0
        return remaining
