#!/usr/bin/python3.8
#
# This script is used to monitor the battery charge level of your laptop and alert you if it goes below a certain level
# Requirement : gtts
# Add this script as a service 

from gtts import gTTS
import subprocess
import time
import os

def notify(mytext, status):
    language = 'en'
    myobj = gTTS(text=mytext, lang='en', slow=False)
    myobj.save("battery.mp3")
    for i in range(10):
        state = int(subprocess.check_output("cat /sys/class/power_supply/AC/online", shell=True))
        if state == status:
            os.system("mpg321 -q battery.mp3")


def monitor():
    status = int(subprocess.check_output("cat /sys/class/power_supply/AC/online", shell=True))
    battery_level  = int(subprocess.check_output("cat /sys/class/power_supply/BAT0/capacity", shell=True))
    if battery_level < 20 and status == 0:
        notify(mytext = 'Battery Low , Connect Charger', status = 0)

    if battery_level > 95 and status == 1:
        notify(mytext = 'Battery Full , Disconnect Charger', status = 1)

while True:
    monitor()
    time.sleep(300)
