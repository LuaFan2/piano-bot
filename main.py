from pyKey import pressKey, releaseKey, press, sendSequence, showKeys

import time
import os
import re
import json
import keyboard
import playsound

## 

def beep():
    playsound.playsound('beep.mp3', True)

def boop():
    playsound.playsound('boop.mp3', True)

##

_scenarios = [x for x in os.listdir(os.path.dirname(os.path.abspath(__file__)) + "/scenarios/") if x.endswith(".scen")]
scenarios = []

for scene in _scenarios:
    scenarios.append(os.path.dirname(os.path.abspath(__file__)) + "/scenarios/" + scene)

scene = 0

def prev():
    global scene
    if scene == 0:
        boop()
        return
    scene = scene - 1
    beep()

def next():
    global scene
    if scene + 1 < len(scenarios):
        scene = scene + 1
        beep()
    else:
        boop()
##

def readScenario():
    with open(scenarios[scene],'r') as f:
        speed = 0.2
        for line in f:
            if re.match("{(.*?)}", line):
                speed = float(line.replace("{", "").replace("}", "").replace("\n", ""))
                continue
            for word in line.split():
                if re.match("\[(.*?)\]", word):
                    time.sleep(speed)
                    sendSequence(word.replace("[", "").replace("]", ""))
                else:
                    for c in word:
                        time.sleep(speed)
                        press(c, 0.1)

##

keyboard.add_hotkey("alt", readScenario)

keyboard.add_hotkey("left", prev)
keyboard.add_hotkey("right", next)

print("Press ESC to stop.")
keyboard.wait('esc')