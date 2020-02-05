from pyKey import pressKey, releaseKey, press, sendSequence, showKeys

import time
import os
import re
import json
import keyboard
import playsound

import mido
## 


def key(s):
    if s == 1:
        return "1"
    elif s == 2:
        return "!"
    elif s == 3:
        return "2"
    elif s == 4:
        return "@"
    elif s == 5:
        return "3"
    elif s == 6:
        return "4"
    elif s == 7:
        return "$"
    elif s == 8:
        return "5"
    elif s == 9:
        return "%"
    elif s == 10:
        return "6"
    elif s == 11:
        return "^"
    elif s == 12:
        return "7"
    elif s == 13:
        return "8"
    elif s == 15:
        return "9"
    elif s == 16:
        return "("
    elif s == 17:
        return "0"
    elif s == 18:
        return "q"
    elif s == 19:
        return "Q"
    elif s == 20:
        return "w"
    elif s == 21:
        return "Q"
    elif s == 22:
        return "e"
    elif s == 23:
        return "E"
    elif s == 24:
        return "r"
    elif s == 25:
        return "t"
    elif s == 26:
        return "T"
    elif s == 27:
        return "y"
    elif s == 28:
        return "Y"
    elif s == 29:
        return "u"
    elif s == 30:
        return "i"
    elif s == 31:
        return "I"
    elif s == 32:
        return "o"
    elif s == 33:
        return "O"
    elif s == 34:
        return "p"
    elif s == 35:
        return "P"
    elif s == 36:
        return "a"
    elif s == 37:
        return "s"
    elif s == 38:
        return "S"
    elif s == 39:
        return "d"
    elif s == 40:
        return "D"
    elif s == 41:
        return "f"
    elif s == 42:
        return "g"
    elif s == 43:
        return "G"
    elif s == 44:
        return "h"
    elif s == 45:
        return "H"
    elif s == 46:
        return "j"
    elif s == 47:
        return "J"
    elif s == 48:
        return "k"
    elif s == 49:
        return "l"
    elif s == 50:
        return "L"
    elif s == 51:
        return "z"
    elif s == 52:
        return "Z"
    elif s == 53:
        return "x"
    elif s == 54:
        return "c"
    elif s == 55:
        return "C"
    elif s == 56:
        return "v"
    elif s == 57:
        return "V"
    elif s == 58:
        return "b"
    elif s == 59:
        return "B"
    elif s == 60:
        return "n"
    elif s == 61:
        return "m"
def beep():
    playsound.playsound('beep.mp3', True)

def boop():
    playsound.playsound('boop.mp3', True)

##

_scenarios = [x for x in os.listdir(os.path.dirname(os.path.abspath(__file__)) + "/scenarios/") if x.endswith(".scen") or x.endswith(".mid")]
scenarios = []

for scene in _scenarios:
    scenarios.append(os.path.dirname(os.path.abspath(__file__)) + "/scenarios/" + scene)

scene = 0

for i in range(len(scenarios)):
    print("{}: {}".format(i, scenarios[i]))

def prev():
    global scene
    if scene == 0:
        boop()
        return
    scene = scene - 1
    print("Current: {}".format(scenarios[scene]))
    beep()

    
def next():
    global scene
    if scene + 1 < len(scenarios):
        scene = scene + 1
        print("Current: {}".format(scenarios[scene]))
        beep()
    else:
        boop()

##



def readScenario():
    global tempo
    isOnce, speed = False, 0.2
    
    name = scenarios[scene]
    
    if ".scen" in name:
        f = open(name, 'r')
        text = f.read().replace(" ", "").replace("\n", "").replace("\r", "")
        for character in text:
            if character == "]":
                isOnce = False
                continue
            if character == "[":
                isOnce = True
                continue    
            if isOnce:
                press(character, 0.1)
            else:
                press(character, 0.1)
                time.sleep(speed)
        f.close()        
    if ".mid" in name:
        mid = mido.MidiFile(name)
        for track in mid.tracks:
            for msg in track:
                if msg.type == "note_on":
                    note = key(msg.note - 35)
                    if note:
                        press(note, 0.005)
                        time.sleep(0.01)
##


keyboard.add_hotkey("alt", readScenario)

keyboard.add_hotkey("left", prev)
keyboard.add_hotkey("right", next)

print("Press ESC to stop.")
keyboard.wait('esc')