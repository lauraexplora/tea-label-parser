import rainbowhat

def display_message(message):
    rainbowhat.display.print_str(message)
    rainbowhat.display.show()

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

def display_clock(ms):
    clock_str = ms_to_clock(ms)
    display_message(clock_str)