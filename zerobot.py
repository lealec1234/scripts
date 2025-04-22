import ctypes
import os
import time
import pyautogui
import time
import pyscreeze
import autoit
import ctypes
import os
import time
import cv2 as cv
import numpy as np
from mss import mss
from PIL import Image,ImageEnhance
import threading
import tweepy
import keyboard
import sys
SendInput = ctypes.windll.user32.SendInput

# C struct redefinitions 
PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

# Actuals Functions

def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def on_press(key):
    print('{0} pressed'.format(
        key))

def on_release(key):
    print('{0} release'.format(
        key))
    if key == Key.esc:
        # Stop listener
        return False



# directx scan codes http://www.gamespp.com/directx/directInputKeyboardScanCodes.html
def jumpattack3():
    time.sleep(5)
    PressKey(0x2E)#c
    ReleaseKey(0x2E)
    time.sleep(0.5)
    PressKey(0x2E)#c
    ReleaseKey(0x2E)
    time.sleep(1)
    PressKey(0x10)#q
    ReleaseKey(0x10)
    time.sleep(1)
    PressKey(0x2E)#c
    ReleaseKey(0x2E)
    PressKey(0x2E)#c
    ReleaseKey(0x2E)
    time.sleep(1)
    PressKey(0x10)#q
    ReleaseKey(0x10)
    time.sleep(1)
    PressKey(0x2E)#c
    ReleaseKey(0x2E)
    PressKey(0x2E)#c
    ReleaseKey(0x2E)
    time.sleep(1)
    PressKey(0x10)#q
    ReleaseKey(0x10)
    time.sleep(1)
#def leftorright(hexKeyCode):   
  #  PressKey(hexKeyCode)#left
  #  ReleaseKey(hexKeyCode)
def doublejump():
    PressKey(0x39)#c
    time.sleep(0.1)
    ReleaseKey(0x39)
    time.sleep(0.1)
    PressKey(0x2F)#v
    time.sleep(0.1)
    ReleaseKey(0x2F)

def up():
    PressKey(0xC8)#up
    time.sleep(0.1)
    ReleaseKey(0xC8)


def impaleup():
    PressKey(0xC8)#up

    PressKey(0x23)#h
    ReleaseKey(0x23)   
    time.sleep(0.1)

    time.sleep(0.1)
  
    PressKey(0x20)#D
    ReleaseKey(0x20)
    time.sleep(0.1)
    PressKey(0x20)#D
    ReleaseKey(0x20)
    time.sleep(0.1)
    ReleaseKey(0xC8)
def attacks():
    PressKey(0x10)#q
    ReleaseKey(0x10)
   # PressKey(0x13)#r
    #ReleaseKey(0x13)

def moveright():
    PressKey(0xCD)#right
    time.sleep(0.3)
    ReleaseKey(0xCD)


def moveleft():
    PressKey(0xCB)#left
    time.sleep(0.3)
    ReleaseKey(0xCB)


def jump():
    PressKey(0x2E)#c
    ReleaseKey(0x2E)
def realtotem():
    PressKey(0x04)#3
    ReleaseKey(0x04)
def totem():
    PressKey(0x18)#'o'
    ReleaseKey(0x18)
def featherfloat():
    PressKey(0x1E)#'A'
    ReleaseKey(0x1E)

def spamkey():
    PressKey(0x3D)#'o'
    ReleaseKey(0x3D)    


def sjumpdown():
    PressKey(0xD0)#down
    PressKey(0x39)#space
    ReleaseKey(0x39)
    time.sleep(0.3)
    ReleaseKey(0xD0)#release down

def downzerotele():
    PressKey(0xD0)#down
    shift()#shift
    time.sleep(0.3)
    ReleaseKey(0xD0)#release down

def upzerotele():
    PressKey(0xC8)#up
    shift()#shift
    time.sleep(0.3)
    ReleaseKey(0xC8)#up release

def zeroRcombo():
    PressKey(0x13)#r
    ReleaseKey(0x13)
    time.sleep(0.2)
    PressKey(0x13)#r
    ReleaseKey(0x13)
    time.sleep(0.2)
    PressKey(0x13)#r
    ReleaseKey(0x13)
    time.sleep(0.2)
    PressKey(0x13)#r
    ReleaseKey(0x13)
    time.sleep(0.2)
    PressKey(0x13)#r
    ReleaseKey(0x13)
    time.sleep(0.2)
    PressKey(0x13)#r
    ReleaseKey(0x13)

def zeroQRcombo():
    PressKey(0x10)#q
    ReleaseKey(0x10)
    time.sleep(0.4)
    PressKey(0x10)#q
    ReleaseKey(0x10)
    time.sleep(0.4)
    PressKey(0x10)#q
    ReleaseKey(0x10)

    time.sleep(0.4)

    PressKey(0x13)#r
    ReleaseKey(0x13)
    time.sleep(0.4)
    PressKey(0x13)#r
    ReleaseKey(0x13)
    time.sleep(0.4)
    PressKey(0x13)#r
    ReleaseKey(0x13)

def zeroupdowntornadoloop():
    zeroQRcombo()
    time.sleep(0.4)
    downzerotele()
    time.sleep(2.1)
    zeroFcombo()
    time.sleep(0.4)
    upzerotele()
    time.sleep(0.4)

def bft2lootcycle():
    PressKey(0x11)#w
    ReleaseKey(0x11)
    time.sleep(0.4)
    PressKey(0x11)#w
    ReleaseKey(0x11)

    time.sleep(3)

    PressKey(0xCB)#left
    shift()
    time.sleep(0.1)
    ReleaseKey(0xCB)

    time.sleep(3)

    PressKey(0x11)#w
    ReleaseKey(0x11)
    time.sleep(0.4)
    PressKey(0x11)#w
    ReleaseKey(0x11)

    time.sleep(3)

    PressKey(0xCB)#left
    shift()
    time.sleep(0.1)
    ReleaseKey(0xCB)

    time.sleep(3)

    PressKey(0xCD)#right
    time.sleep(3)
    ReleaseKey(0xCD)

    time.sleep(1)

    PressKey(0x11)#w
    ReleaseKey(0x11)
    time.sleep(0.4)
    PressKey(0x11)#w
    ReleaseKey(0x11)

    time.sleep(3)

    PressKey(0xCD)#right
    shift()
    time.sleep(0.1)
    ReleaseKey(0xCD)

    time.sleep(1)

    PressKey(0xCD)#right
    time.sleep(3)
    ReleaseKey(0xCD)

    time.sleep(1)

    PressKey(0xCB)#left
    time.sleep(0.3)
    ReleaseKey(0xCB)

    time.sleep(1)

    upzerotele()
    time.sleep(0.3)
    PressKey(0x18)#'o'
    ReleaseKey(0x18)

    time.sleep(0.3)




def betweenfrostthunder2():
    count=0
    while(True):
        if(count == 14):
            bft2lootcycle()
            count=0
            time.sleep(1)
        zeroupdowntornadoloop()
        count+=1
        print(count)
        

def zeroFcombo():
    PressKey(0x21)#f
    ReleaseKey(0x21)
    time.sleep(0.3)
    PressKey(0x21)#f
    ReleaseKey(0x21)
    time.sleep(0.3)
    PressKey(0x21)#f
    ReleaseKey(0x21)
    PressKey(0x21)#f
    ReleaseKey(0x21)
    time.sleep(0.3)
    PressKey(0x21)#f
    ReleaseKey(0x21)
    time.sleep(0.3)
    PressKey(0x21)#f
    ReleaseKey(0x21)

def zeroScombo():
    PressKey(0x1F)#s
    ReleaseKey(0x1F)
    time.sleep(0.6)
    PressKey(0x1F)#s
    ReleaseKey(0x1F)
    time.sleep(0.6)
    PressKey(0x1F)#s
    ReleaseKey(0x1F)

def dcup1():
    zeroRcombo()
    time.sleep(0.1)
    downzerotele()
    time.sleep(0.2)
    zeroFcombo()
    time.sleep(0.6)
    downzerotele()

    time.sleep(0.9)

    PressKey(0xCD)#right
    time.sleep(0.1)
    ReleaseKey(0xCD)
    time.sleep(0.1)

    zeroScombo()

    time.sleep(0.1)

    downzerotele()

    time.sleep(0.4)

    zeroRcombo()

    time.sleep(0.4)

    downzerotele()

    time.sleep(0.4)

    PressKey(0xCB)#left
    time.sleep(0.1)
    ReleaseKey(0xCB)
    time.sleep(0.1)
    zeroQRcombo()


def dcuplootcycle():
    PressKey(0x11)#w
    ReleaseKey(0x11)
    time.sleep(0.4)
    PressKey(0x11)#w
    ReleaseKey(0x11)

    time.sleep(0.8)

    PressKey(0xCB)#left
    shift()
    time.sleep(0.1)
    ReleaseKey(0xCB)

    time.sleep(0.8)

    PressKey(0x11)#w
    ReleaseKey(0x11)
    time.sleep(0.4)
    PressKey(0x11)#w
    ReleaseKey(0x11)

    time.sleep(0.8)

    PressKey(0xCB)#left
    shift()
    time.sleep(0.1)
    ReleaseKey(0xCB)

    time.sleep(0.8)

    PressKey(0x11)#w
    ReleaseKey(0x11)
    time.sleep(0.4)
    PressKey(0x11)#w
    ReleaseKey(0x11)

    time.sleep(0.8)

    PressKey(0xCB)#left
    shift()
    time.sleep(0.1)
    ReleaseKey(0xCB)

    time.sleep(1.2)

    downzerotele()

    time.sleep(0.4)

    PressKey(0xCD)#right
    shift()
    time.sleep(0.1)
    ReleaseKey(0xCD)

    time.sleep(0.8)

    PressKey(0x11)#w
    ReleaseKey(0x11)
    time.sleep(0.4)
    PressKey(0x11)#w
    ReleaseKey(0x11)

    time.sleep(0.8)

    PressKey(0xCD)#right
    shift()
    time.sleep(0.1)
    ReleaseKey(0xCD)

    time.sleep(0.8)

    PressKey(0x11)#w
    ReleaseKey(0x11)
    time.sleep(0.4)
    PressKey(0x11)#w
    ReleaseKey(0x11)

    time.sleep(0.8)

    PressKey(0xCD)#right
    shift()
    time.sleep(0.1)
    ReleaseKey(0xCD)

    time.sleep(0.8)

    PressKey(0x11)#w
    ReleaseKey(0x11)
    time.sleep(0.4)
    PressKey(0x11)#w
    ReleaseKey(0x11)

    time.sleep(1.2)

    downzerotele()

    time.sleep(0.8)

    zeroRcombo()

    time.sleep(0.4)

    downzerotele()

    time.sleep(0.2)

    zeroQRcombo()

    time.sleep(0.6)

    downzerotele()

    time.sleep(0.2)

    PressKey(0xCB)#left
    time.sleep(0.1)
    ReleaseKey(0xCB)
    time.sleep(0.1)

    PressKey(0x18)#'o'
    ReleaseKey(0x18)

    time.sleep(0.1)

    PressKey(0x10)#q
    ReleaseKey(0x10)
    time.sleep(0.4)
    PressKey(0x10)#q
    ReleaseKey(0x10)
    time.sleep(0.4)
    PressKey(0x10)#q
    ReleaseKey(0x10)

    time.sleep(0.4)


def dccup1():
    count = 0
    while(True):
        if(count==8):
            dcuplootcycle()
            count=0
        dcup1()
        count+=1
        print(count)

def pressAlt():
    PressKey(0x38)#alt
    time.sleep(0.1)
    ReleaseKey(0x38)

def labysuff5maincombo():
    zeroQRcombo()
    time.sleep(0.1)
    downzerotele()
    time.sleep(0.2)
    zeroFcombo()
    time.sleep(0.6)
    downzerotele()
    time.sleep(0.2)
    zeroScombo()
    time.sleep(0.4)
    downzerotele()
    time.sleep(0.2)
    zeroRcombo()
    time.sleep(0.7)
    pressAlt()
    time.sleep(1)
    upzerotele()
    time.sleep(0.1)

def erdashower():
    PressKey(0xD0)#down
    PressKey(0x1D)#ctrl
    time.sleep(0.1)
    ReleaseKey(0x1D)
    time.sleep(0.1)
    ReleaseKey(0xD0)#release down

def erdashowerlabysuff5():
    zeroQRcombo()
    time.sleep(0.1)
    downzerotele()
    time.sleep(0.2)
    zeroFcombo()
    time.sleep(0.6)
    downzerotele()
    time.sleep(0.2)
    zeroScombo()
    time.sleep(0.4)
    downzerotele()
    time.sleep(0.2)

    zeroRcombo()

    time.sleep(0.5)

    PressKey(0x11)#w
    ReleaseKey(0x11)
    time.sleep(0.4)
    PressKey(0x11)#w
    ReleaseKey(0x11)

    time.sleep(1)

    PressKey(0x12)#e
    ReleaseKey(0x12)
    time.sleep(0.4)
    PressKey(0x12)#e
    ReleaseKey(0x12)

    time.sleep(0.4)

    upzerotele()
    time.sleep(1)

    erdashower()

    time.sleep(0.5)

    PressKey(0x11)#w
    ReleaseKey(0x11)
    time.sleep(0.4)
    PressKey(0x11)#w
    ReleaseKey(0x11)

    time.sleep(1)

    PressKey(0x12)#e
    ReleaseKey(0x12)
    time.sleep(0.2)
    PressKey(0xCD)#right
    time.sleep(0.1)
    PressKey(0x12)#e
    time.sleep(0.1)
    ReleaseKey(0x12)
    ReleaseKey(0xCD)

    time.sleep(2)

    PressKey(0xCB)#left
    time.sleep(0.2)
    ReleaseKey(0xCB)

    time.sleep(0.1)

    up()

    time.sleep(0.3)


def labylootcycle():
    PressKey(0x11)#w
    ReleaseKey(0x11)
    time.sleep(0.5)
    PressKey(0x11)#w
    ReleaseKey(0x11)
    time.sleep(0.1)
    zeroQRcombo()
    time.sleep(0.1)
    downzerotele()
    time.sleep(0.2)
    zeroFcombo()
    time.sleep(0.6)
    downzerotele()
    time.sleep(0.2)
    zeroScombo()
    time.sleep(0.4)
    downzerotele()
    time.sleep(0.2)
    zeroRcombo()
    time.sleep(1)

    PressKey(0x11)#w
    ReleaseKey(0x11)
    time.sleep(0.5)
    PressKey(0x11)#w
    ReleaseKey(0x11)
    time.sleep(0.5)

    PressKey(0x12)#e
    ReleaseKey(0x12)

    time.sleep(2)

    upzerotele()

    time.sleep(0.5)

    PressKey(0x1E)#'A'
    time.sleep(0.1)
    ReleaseKey(0x1E)
    time.sleep(0.1)
    PressKey(0x1E)#'A'
    time.sleep(0.1)
    ReleaseKey(0x1E)
    PressKey(0x1E)#'A'
    time.sleep(0.1)
    ReleaseKey(0x1E)
    time.sleep(0.1)
    PressKey(0x1E)#'A'
    time.sleep(0.1)
    ReleaseKey(0x1E)
    PressKey(0x1E)#'A'
    time.sleep(0.1)
    ReleaseKey(0x1E)
    time.sleep(0.1)
    PressKey(0x1E)#'A'
    time.sleep(0.1)
    ReleaseKey(0x1E)
    PressKey(0x1E)#'A'
    time.sleep(0.1)
    ReleaseKey(0x1E)
    time.sleep(0.1)
    PressKey(0x1E)#'A'
    time.sleep(0.1)
    ReleaseKey(0x1E)

    time.sleep(0.3)

    upzerotele()

    time.sleep(1)

    PressKey(0x04)#z
    ReleaseKey(0x04)

    time.sleep(0.5)

    upzerotele()

    time.sleep(2)

    PressKey(0x11)#w
    ReleaseKey(0x11)
    time.sleep(0.4)
    PressKey(0x11)#w
    ReleaseKey(0x11)

    time.sleep(1)

    PressKey(0x12)#e
    ReleaseKey(0x12)
    time.sleep(1.5)
    PressKey(0xCD)#right
    time.sleep(0.1)
    PressKey(0x12)#e
    time.sleep(0.1)
    ReleaseKey(0x12)
    ReleaseKey(0xCD)

    time.sleep(2)

    PressKey(0x2C)#z
    ReleaseKey(0x2C)

    time.sleep(1)

    PressKey(0xCB)#left
    time.sleep(0.2)
    ReleaseKey(0xCB)

    time.sleep(0.1)

    up()

    time.sleep(0.1)

    PressKey(0x18)#'o'
    ReleaseKey(0x18)

    time.sleep(0.3)




def labysuff5():
    counterda = 0
    counterlootcycle = 0
    while(True):
        if(counterlootcycle==8 and counterda==4):
            labylootcycle()
            time.sleep(0.3)
            erdashowerlabysuff5()
            counterlootcycle = 0
            counterda=0
        if(counterlootcycle==8):
            labylootcycle()
            counterlootcycle = 0
            counterda+=1
        if(counterda==4):
            erdashowerlabysuff5()
            counterda=0
            counterlootcycle +=1
            print("counterlootcycle: " + str(counterlootcycle))

        labysuff5maincombo()
        counterda+=1
        counterlootcycle+=1
        print(counterda)
        print("counterlootcycle: " + str(counterlootcycle))
        if(counterlootcycle==9 or counterlootcycle ==10):
            counterlootcycle=8
        if(counterda==5 or counterda==6):
            counterda=4

def zeroupdownforever():
    while(True):
        zeroupdowntornadoloop()
'''
def otherplayer():
    from mss import mss
    try:
        x1,y1 = pyautogui.locateCenterOnScreen("C:/Users/Alec/Desktop/Maplestoryscript/rune/rune_template/minimap_tl.PNG", confidence=0.8)
        x2,y2 = pyautogui.locateCenterOnScreen("C:/Users/Alec/Desktop/Maplestoryscript/rune/rune_template/minimap_br.PNG", confidence=0.8)

        width = x2 - x1
        height = y2 - y1
        print(x1,y1, width,height)
        mon = {'top': 109, 'left': 25, 'width': 200, 'height': 80}
        print(mon)
        
        with mss() as mss_instance:
            while True:
                onruneX = 0
                onruneY = 0

                screenshot = mss_instance.grab(mon)

                img = Image.frombytes("RGB", screenshot.size, screenshot.bgra, "raw", "BGRX")  # Convert to PIL.Image
                try:
                    otherplayerX,otherplayerY = pyautogui.locateCenterOnScreen("C:/Users/Alec/Desktop/Maplestoryscript/other_player_template.png", confidence=0.8)
                    print("other player on map need to run")
                    PressKey(0x3C)#f2 return to town scroll
                    ReleaseKey(0x3C)
                    time.sleep(0.5)
                    os._exit(0)
                    
                except TypeError:
                    print("no other player")
                    time.sleep(0.1)
                    pass


    except TypeError:
        print("not found")
        pass
'''

def threadings():
    thread1 = threading.Thread(target=labysuff5)
    thread1.daemon = True
    thread1.start()

    thread2 = threading.Thread(target=otherplayer)
    thread2.daemon = True
    thread2.start()

    while(True):
        thread1.join(1)
        thread2.join(1)
        if not thread1.is_alive() and thread2.is_alive():
            os._exit(0)

def firespirits():
    while(True):
        labysuff5maincombo()


def juniper():
    while(True):
        PressKey(0x3D)#f3 herb bag
        ReleaseKey(0x3D)
        time.sleep(0.1)
        PressKey(0x15)#press y
        ReleaseKey(0x15)
        time.sleep(0.1)

def attacklr():
    while(True):
        PressKey(0x11)#'w'
        time.sleep(0.1)
        ReleaseKey(0x11)

        time.sleep(0.3)

        moveleft()

        PressKey(0x11)#'w'
        time.sleep(0.1)
        ReleaseKey(0x11)

        time.sleep(0.3)

        moveright()

def left():
    PressKey(0xCB)#left
    time.sleep(0.1)
    ReleaseKey(0xCB)

def right():
    PressKey(0xCD)#right
    time.sleep(0.1)
    ReleaseKey(0xCD)

def shift():
    PressKey(0x2A)#left shift
    time.sleep(0.1)
    ReleaseKey(0x2A)

   

def setdownbothsummons():
    PressKey(0xD0)#down arrow

    PressKey(0x1E)#A (first summon)
    time.sleep(0.1)
    ReleaseKey(0x1E)
    time.sleep(0.1)
    PressKey(0x1E)#A (first summon)
    time.sleep(0.1)
    ReleaseKey(0x1E)
    time.sleep(0.1)
    PressKey(0x1E)#A (first summon)
    time.sleep(0.1)
    ReleaseKey(0x1E)

    time.sleep(0.5)

    PressKey(0x1F)#S (second summon)
    time.sleep(0.1)
    ReleaseKey(0x1F)
    time.sleep(0.1)
    PressKey(0x1F)#S (second summon)
    time.sleep(0.1)
    ReleaseKey(0x1F)
    time.sleep(0.1)
    PressKey(0x1F)#S (second summon)
    time.sleep(0.1)
    ReleaseKey(0x1F)

    time.sleep(0.1)
    ReleaseKey(0xD0)

def seterdashower():

    PressKey(0x1F)#S (second summon)
    time.sleep(0.1)
    ReleaseKey(0x1F)
    time.sleep(0.1)
    PressKey(0x1F)#S (second summon)
    time.sleep(0.1)
    ReleaseKey(0x1F)
    time.sleep(0.1)
    PressKey(0x1F)#S (second summon)
    time.sleep(0.1)
    ReleaseKey(0x1F)


def setfountain():

    PressKey(0x1E)#A (first summon)
    time.sleep(0.1)
    ReleaseKey(0x1E)
    time.sleep(0.1)
    PressKey(0x1E)#A (first summon)
    time.sleep(0.1)
    ReleaseKey(0x1E)
    time.sleep(0.1)
    PressKey(0x1E)#A (first summon)
    time.sleep(0.1)
    ReleaseKey(0x1E)
  


def yumyum():
    count = 0
    while(True):
        print(count)
        if(count == 14):
            attackteleright()
            time.sleep(0.3)
            attackteleright()
            time.sleep(0.3)
            attackteleright()
            time.sleep(0.3)
            attackteleright()
            time.sleep(0.3)
            attackteleright()
            time.sleep(0.8)

            setdownbothsummons()
            time.sleep(0.5)

            attackteleleft()
            time.sleep(0.3)
            attackteleleft()
            time.sleep(0.3)
            attackteleleft()
            time.sleep(0.3)
            attackteleleft()
            time.sleep(0.3)
            attackteleleft()
            time.sleep(0.3)

            count = 0




        attackteleright()
        time.sleep(0.3)
        attackteleright()
        time.sleep(0.3)
        attackteleright()
        time.sleep(0.3)
        attackteleleft()
        time.sleep(0.3)
        attackteleleft()
        time.sleep(0.3)
        attackteleleft()
        time.sleep(0.3)

        count = count + 1



def lachlach():
    count = 0
    while(True):
        print(count)
        if(count == 14):
            attackteleleft()
            time.sleep(0.3)
            attackteleleft()
            time.sleep(0.3)
            attackteleleft()
            time.sleep(0.3)
            attackteleleft()
            time.sleep(0.3)
            attackteleleft()
            time.sleep(0.8)

            setdownbothsummons()
            time.sleep(0.5)

            attackteleright()
            time.sleep(0.3)
            attackteleright()
            time.sleep(0.3)
            attackteleright()
            time.sleep(0.3)
            attackteleright()
            time.sleep(0.3)
            attackteleright()
            time.sleep(0.3)

            count = 0



        attackteleleft()
        time.sleep(0.3)
        attackteleleft()
        time.sleep(0.3)
        attackteleleft()
        time.sleep(0.3)
        attackteleright()
        time.sleep(0.3)
        attackteleright()
        time.sleep(0.3)
        attackteleright()
        time.sleep(0.5)

        count = count + 1

def downtp():
    PressKey(0xD0)#down arrow
    time.sleep(0.1)

    PressKey(0x2A)#left shift
    time.sleep(0.1)
    ReleaseKey(0x2A)

    time.sleep(0.1)
    ReleaseKey(0xD0)

def uptp():
    PressKey(0xC8)#down arrow
    time.sleep(0.1)

    PressKey(0x2A)#left shift
    time.sleep(0.1)
    ReleaseKey(0x2A)

    time.sleep(0.1)
    ReleaseKey(0xC8)


def attackdowntp():
    PressKey(0x11)#'w'
    time.sleep(0.1)
    ReleaseKey(0x11)

    time.sleep(0.1)
    
    PressKey(0xD0)#down arrow
    time.sleep(0.1)

    PressKey(0x2A)#left shift
    time.sleep(0.1)
    ReleaseKey(0x2A)

 #   time.sleep(0.1)
    ReleaseKey(0xD0)

def attackuptp():
    PressKey(0x11)#'w'
    time.sleep(0.1)
    ReleaseKey(0x11)

    time.sleep(0.1)

    PressKey(0xC8)#down arrow
    time.sleep(0.1)

    PressKey(0x2A)#left shift
    time.sleep(0.1)
    ReleaseKey(0x2A)

 #   time.sleep(0.1)
    ReleaseKey(0xC8)

def attackteleleft():
    PressKey(0x11)#'w'
    time.sleep(0.1)
    ReleaseKey(0x11)

    time.sleep(0.1)

    PressKey(0xCB)#left
    time.sleep(0.1)

    PressKey(0x2A)#left shift
    time.sleep(0.1)
    ReleaseKey(0x2A)

  #  time.sleep(0.1)
    ReleaseKey(0xCB)

def attackteleright():
    PressKey(0x11)#'w'
    time.sleep(0.1)
    ReleaseKey(0x11)

    time.sleep(0.1)
    
    PressKey(0xCD)#right
    time.sleep(0.1)

    PressKey(0x2A)#left shift
    time.sleep(0.1)
    ReleaseKey(0x2A)

 #   time.sleep(0.1)
    ReleaseKey(0xCD) 



def arcana():
    count = 0
    while(True):
        print(count)
        if(count == 6):
            downtp()

            time.sleep(0.5)
            setdownbothsummons()
            time.sleep(0.5)

            attackteleleft()
            time.sleep(0.3)
            attackteleleft()
            time.sleep(0.3)
            attackteleleft()
            time.sleep(0.3)
            attackteleleft()
            time.sleep(0.3)
            attackteleleft()
            time.sleep(0.3)
            attackteleleft()
            time.sleep(0.3)
            attackteleleft()
            time.sleep(0.3)

            attackteleright()
            time.sleep(0.3)
            attackteleright()
            time.sleep(0.3)
            attackteleright()
            time.sleep(0.3)
            attackteleright()
            time.sleep(0.3)
            attackteleright()
            time.sleep(0.3)
            attackteleright()
            time.sleep(0.3)
            attackteleright()
            time.sleep(0.5)


            uptp()

            time.sleep(0.5)

            count = 0



        attackteleleft()
        time.sleep(0.3)
        attackteleleft()
        time.sleep(0.3)
        attackteleleft()
        time.sleep(0.3)
        attackteleleft()
        time.sleep(0.3)
        attackteleleft()
        time.sleep(0.3)
        attackteleleft()
        time.sleep(0.3)

        attackteleright()
        time.sleep(0.3)
        attackteleright()
        time.sleep(0.3)
        attackteleright()
        time.sleep(0.3)
        attackteleright()
        time.sleep(0.3)
        attackteleright()
        time.sleep(0.3)
        attackteleright()
        time.sleep(0.5)

        count = count + 1


def sellas_pd4():
    count = 0
    #2nd ledges from bottom on far right teleport up to start
    while(True):
        print(count)
        if(count == 6):
            attackteleleft()
            time.sleep(0.3)
            attackteleleft()
            
            time.sleep(0.5)
            setdownbothsummons()
            time.sleep(0.5)

            attackuptp()

            time.sleep(0.3)

            PressKey(0x11)#'w'
            time.sleep(0.1)
            ReleaseKey(0x11)

            time.sleep(1)

            attackteleleft()
            time.sleep(0.3)
            attackteleleft()
            time.sleep(0.3)

            PressKey(0x11)#'w'
            time.sleep(0.1)
            ReleaseKey(0x11)

            time.sleep(0.5)


            attackdowntp()
            time.sleep(0.3)

            attackdowntp()

            time.sleep(0.3)

            attackdowntp()

            time.sleep(0.3)

            attackteleright()
            time.sleep(0.3)
            attackteleright()
            time.sleep(0.3)
            attackteleright()
            time.sleep(0.3)

            attackuptp()

            time.sleep(0.3)

            attackteleright()
            time.sleep(0.3)

            attackteleright()
            time.sleep(0.3)

            attackuptp()

            time.sleep(0.3)

            count = 0

        attackteleleft()
        time.sleep(0.3)
        attackteleleft()
        time.sleep(0.3)
        attackteleleft()
        time.sleep(0.3)
        attackteleleft()
        time.sleep(0.3)

        attackdowntp()

        time.sleep(0.3)
        attackteleright()
        time.sleep(0.3)
        attackteleright()
        time.sleep(0.3)
        attackteleright()
        time.sleep(0.3)
        attackteleright()
        time.sleep(0.3)

        attackuptp()

        time.sleep(0.3)

        count = count + 1


def spamy():
    while(True):
        PressKey(0x15)#space jump
        time.sleep(0.1)
        ReleaseKey(0x15)
        time.sleep(0.1)


def generaljumptpL():
    PressKey(0x39)#space jump
    time.sleep(0.1)
    ReleaseKey(0x39)

    time.sleep(0.1)

    PressKey(0x11)#'w'
    time.sleep(0.1)
    ReleaseKey(0x11)

    time.sleep(0.1)

 #   PressKey(0xCB)#left

    time.sleep(0.1)

    PressKey(0x2A)#left shift
    time.sleep(0.1)
    ReleaseKey(0x2A)

    PressKey(0x2A)#left shift
    time.sleep(0.1)
    ReleaseKey(0x2A)


 #   ReleaseKey(0xCB)
    

    time.sleep(0.1)


def jumpupattackupTP():
    PressKey(0xC8)#up

    PressKey(0x39)#space jump
    time.sleep(0.1)
    ReleaseKey(0x39)

    time.sleep(0.1)

    PressKey(0x11)#'w'
    time.sleep(0.1)
    ReleaseKey(0x11)

    time.sleep(0.1)

    PressKey(0x2A)#left shift
    time.sleep(0.1)
    ReleaseKey(0x2A)

    PressKey(0x2A)#left shift
    time.sleep(0.1)
    ReleaseKey(0x2A)
    
    ReleaseKey(0xC8)


def jumpupattackdownTP():
    PressKey(0xD0)#down

    PressKey(0x39)#space jump
    time.sleep(0.1)
    ReleaseKey(0x39)

    time.sleep(0.1)

    PressKey(0x11)#'w'
    time.sleep(0.1)
    ReleaseKey(0x11)

    time.sleep(0.1)

    PressKey(0x2A)#left shift
    time.sleep(0.1)
    ReleaseKey(0x2A)

    PressKey(0x2A)#left shift
    time.sleep(0.1)
    ReleaseKey(0x2A)
    
    ReleaseKey(0xD0)


def generaljumptpR():
    PressKey(0x39)#space jump
    time.sleep(0.1)
    ReleaseKey(0x39)

    time.sleep(0.1)

    PressKey(0x11)#'w'
    time.sleep(0.1)
    ReleaseKey(0x11)

    time.sleep(0.3)

    PressKey(0x2A)#left shift
    ReleaseKey(0x2A)

    PressKey(0x2A)#left shift
    ReleaseKey(0x2A)

    time.sleep(0.3)




def peacemaker():
    PressKey(0x13)#R peacemaker
    time.sleep(0.1)
    ReleaseKey(0x13)
    time.sleep(0.1)
    PressKey(0x13)#R
    time.sleep(0.1)
    ReleaseKey(0x13)

def labysuff6():
    count = 0
    while(True):
        print(count)
        if(count == 3):
            attackteleright()
            time.sleep(0.3)
            attackteleright()
            time.sleep(0.3)
            attackteleright()
            time.sleep(0.3)
            attackteleright()
            time.sleep(0.3)
            attackteleright()
            time.sleep(0.3)
            attackteleright()
            time.sleep(0.3)

            peacemaker()

            time.sleep(0.3)

            attackdowntp()
            time.sleep(0.3)

            attackteleright()
            time.sleep(0.3)

            PressKey(0xCB)#left
            for y in range(6):
                generaljumptpL()
            ReleaseKey(0xCB)
            
            attackteleleft()
            time.sleep(0.3)
            attackteleleft()
            time.sleep(0.3)

            '''
            attackteleleft()
            time.sleep(0.3)
            attackteleleft()
            time.sleep(0.3)
            attackteleleft()
            time.sleep(0.3)
            attackteleleft()
            time.sleep(0.3)
            attackteleleft()
            time.sleep(0.3)
            attackteleleft()
            time.sleep(0.3)
            attackteleleft()
            time.sleep(0.5)
            '''

            attackteleright()
            time.sleep(0.3)
            attackteleright()
            time.sleep(0.5)

            PressKey(0xC8)#Up for portal
            time.sleep(0.1)
            ReleaseKey(0xC8)

            time.sleep(0.3)

            attackteleleft()
            time.sleep(0.3)
            attackteleleft()
            time.sleep(0.3)
            attackteleleft()
            time.sleep(0.3)

            seterdashower()

            time.sleep(0.3)

            attackuptp()

            time.sleep(0.3)

            attackteleleft()
            time.sleep(0.3)

            attackdowntp()
            time.sleep(0.3)

            attackteleleft()
            time.sleep(0.3)
            attackteleleft()
            time.sleep(0.3)

            setfountain()

            attackteleleft()
            time.sleep(0.3)

            attackdowntp()
            time.sleep(0.5)

            count = 0

        attackteleright()
        time.sleep(0.3)
        attackteleright()
        time.sleep(0.3)
        attackteleright()
        time.sleep(0.3)
        attackteleright()
        time.sleep(0.3)
        attackteleright()
        time.sleep(0.3)
        attackteleright()
        time.sleep(0.3)
        attackteleright()
        time.sleep(0.3)

        peacemaker()

        time.sleep(0.3)

        attackteleleft()
        time.sleep(0.3)
        attackteleleft()
        time.sleep(0.3)
        attackteleleft()
        time.sleep(0.3)
        attackteleleft()
        time.sleep(0.3)
        attackteleleft()
        time.sleep(0.3)
        attackteleleft()
        time.sleep(0.3)
        attackteleleft()
        time.sleep(0.3)

        count = count + 1

def rocky1():
    count = 0
    while(True):
        if(count == 5):
            attackteleleft()
            time.sleep(0.3)
            PressKey(0x11)#'w'
            time.sleep(0.1)
            ReleaseKey(0x11)
            time.sleep(0.5)
            attackteleright()
            time.sleep(0.3)

            attackdowntp()
            time.sleep(0.3)
            attackdowntp()
            time.sleep(0.3)

            seterdashower()

            time.sleep(0.5)

            attackteleleft()
            time.sleep(0.3)


            attackdowntp()
            time.sleep(0.3)
            attackdowntp()
            time.sleep(0.3)


            attackteleleft()
            time.sleep(0.3)
            attackteleleft()
            time.sleep(0.3)
            attackteleleft()
            time.sleep(0.5)

            attackteleright()
            time.sleep(0.3)
            attackteleright()
            time.sleep(0.3)
            attackteleright()
            time.sleep(0.3)
            attackteleright()
            time.sleep(0.3)
            attackteleright()
            time.sleep(0.3)

            attackuptp()
            time.sleep(0.3)
            attackuptp()
            time.sleep(0.3)
            attackuptp()
            time.sleep(0.5)

            PressKey(0xC8)#Up for portal
            time.sleep(0.1)
            ReleaseKey(0xC8)

            time.sleep(0.3)

            attackteleright()

            time.sleep(0.3)

            setfountain()

            time.sleep(0.3)

            attackdowntp()
            time.sleep(0.3)

            attackteleright()
            time.sleep(0.3)

            attackuptp()
            time.sleep(0.3)

            attackteleleft()
            time.sleep(0.3)

            attackuptp()
            time.sleep(0.3)

            PressKey(0x11)#'w'
            time.sleep(0.1)
            ReleaseKey(0x11)
            time.sleep(0.5)

            attackteleleft()
            time.sleep(0.5)

            attackdowntp()
            time.sleep(0.2)
            PressKey(0x3D)#left
            time.sleep(0.1)
            ReleaseKey(0x3D)
            time.sleep(0.3)

            PressKey(0xC8)#Up for portal
            time.sleep(0.1)
            ReleaseKey(0xC8)

            time.sleep(0.3)

            attackteleleft()

            time.sleep(0.3)

            attackuptp()

            time.sleep(0.3)

            count = 0
           



        attackdowntp()
        time.sleep(0.3)
        attackdowntp()
        time.sleep(0.3)
        attackdowntp()
        time.sleep(0.3)
        attackdowntp()
        time.sleep(0.3)


        PressKey(0x02)#1 infinity
        time.sleep(0.1)
        ReleaseKey(0x02)

        PressKey(0x13)#R peacemaker
        time.sleep(0.1)
        ReleaseKey(0x13)

        PressKey(0x21)#F door
        time.sleep(0.1)
        ReleaseKey(0x21)

        PressKey(0x05)#4 bene
        time.sleep(0.1)
        ReleaseKey(0x05)

        PressKey(0x06)#5 angel
        time.sleep(0.1)
        ReleaseKey(0x06)

        PressKey(0x07)#6 ab link
        time.sleep(0.1)
        ReleaseKey(0x07)

        PressKey(0x09)#8 will
        time.sleep(0.1)
        ReleaseKey(0x09)

        time.sleep(0.3)

        attackuptp()
        time.sleep(0.3)
        attackuptp()
        time.sleep(0.3)
        attackuptp()
        time.sleep(0.3)
        attackuptp()
        time.sleep(0.3)

        count = count + 1

'''
def burningcerniumwestern1():
    count = 0
    sixthjobcounter = 0
    while(True):
        if(count == 3):
            time.sleep(0.2)
            setfountain()
            time.sleep(0.5)

            attackuptp()
            time.sleep(0.3)

            attackteleleft()
            time.sleep(0.3)

            attackteleleft()
            time.sleep(0.3)

            attackteleleft()
            time.sleep(0.3)

            attackteleleft()
            time.sleep(0.3)

            PressKey(0xCD)#left
            time.sleep(0.3)
            ReleaseKey(0xCD)

            time.sleep(0.3)

            attackdowntp()
            time.sleep(0.3)

            seterdashower()
            time.sleep(0.5)

            attackteleleft()
            time.sleep(0.3)
            attackteleleft()
            time.sleep(0.3)
            attackteleleft()
            time.sleep(0.3)
            attackteleleft()
            time.sleep(0.3)

            attackteleleft()
            time.sleep(0.3)

            attackdowntp()
            time.sleep(0.3)

            attackdowntp()
            time.sleep(0.3)

            attackteleright()
            time.sleep(0.3)
            attackteleright()
            time.sleep(0.3)
            attackteleright()
            time.sleep(0.3)
            attackteleright()
            time.sleep(0.3)

            if(sixthjobcounter == 7):
                PressKey(0x29)#'`' grave symbol
                time.sleep(0.1)
                ReleaseKey(0x29)
                time.sleep(5)
                sixthjobcounter = 0


            attackteleright()
            time.sleep(0.3)
            attackteleright()
            time.sleep(0.3)
            attackteleright()
            time.sleep(0.3)

            attackuptp()
            time.sleep(0.3)

            attackuptp()
            time.sleep(0.3)

            PressKey(0x3D)#f3
            time.sleep(0.1)
            ReleaseKey(0x3D)
            PressKey(0x3D)#f3
            time.sleep(0.1)
            ReleaseKey(0x3D)
            PressKey(0x3D)#f3
            time.sleep(0.1)
            ReleaseKey(0x3D)
            time.sleep(0.1)


            sixthjobcounter = sixthjobcounter + 1
            count = 0





        attackteleleft()
        time.sleep(0.3)
        attackteleleft()
        time.sleep(0.3)
        attackteleleft()
        time.sleep(0.3)
        attackteleleft()
        time.sleep(0.3)
        attackteleleft()
        time.sleep(0.3)
        attackteleleft()
        time.sleep(0.3)

        attackdowntp()
        time.sleep(0.3)

        attackteleright()
        time.sleep(0.3)
        attackteleright()
        time.sleep(0.3)
        attackteleright()
        time.sleep(0.3)
        attackteleright()
        time.sleep(0.3)
        attackteleright()
        time.sleep(0.3)
        attackteleright()
        time.sleep(0.5)

        PressKey(0x02)#1 infinity
        time.sleep(0.1)
        ReleaseKey(0x02)

        PressKey(0x21)#F door
        time.sleep(0.1)
        ReleaseKey(0x21)

        PressKey(0x05)#4 bene
        time.sleep(0.1)
        ReleaseKey(0x05)

        PressKey(0x06)#5 angel
        time.sleep(0.1)
        ReleaseKey(0x06)

        PressKey(0x07)#6 ab link
        time.sleep(0.1)
        ReleaseKey(0x07)

        PressKey(0x09)#8 will
        time.sleep(0.1)
        ReleaseKey(0x09)

        peacemaker()

        time.sleep(0.6)

        attackuptp()
        time.sleep(0.4)

        count = count + 1
'''


def burningcerniumwestern1():
    count = 0
    sixthjobcounter = 0
    while(True):
        if(count == 4):
            attackuptp()
            time.sleep(0.3)

            setfountain()
            time.sleep(0.5)

            attackuptp()
            time.sleep(0.3)

            attackteleleft()
            time.sleep(0.3)

            attackteleleft()
            time.sleep(0.3)


            attackteleleft()
            time.sleep(0.3)

            attackteleleft()
            time.sleep(0.3)

            PressKey(0xCD)#right
            time.sleep(0.3)
            ReleaseKey(0xCD)
           

            time.sleep(0.3)

            attackdowntp()
            time.sleep(0.3)

            seterdashower()
            time.sleep(0.5)

            attackteleleft()
            time.sleep(0.3)

            attackteleleft()
            time.sleep(0.3)
            attackteleleft()
            time.sleep(0.3)
            attackteleleft()
            time.sleep(0.3)

            attackteleleft()
            time.sleep(0.3)

            PressKey(0x11)#'w'
            time.sleep(0.1)
            ReleaseKey(0x11)
            time.sleep(0.5)

            attackdowntp()
            time.sleep(0.3)

            attackdowntp()
            time.sleep(0.3)

            attackteleright()
            time.sleep(0.3)
            attackteleright()
            time.sleep(0.3)
            attackteleright()
            time.sleep(0.3)
            attackteleright()
            time.sleep(0.3)

            if(sixthjobcounter == 7):
                PressKey(0x29)#'`' grave symbol
                time.sleep(0.1)
                ReleaseKey(0x29)
                time.sleep(5)
                sixthjobcounter = 0


            attackteleright()
            time.sleep(0.3)
            attackteleright()
            time.sleep(0.3)
            attackteleright()
            time.sleep(0.3)

            PressKey(0x11)#'w'
            time.sleep(0.1)
            ReleaseKey(0x11)
            time.sleep(0.5)

            attackuptp()
            time.sleep(0.3)

            attackuptp()
            time.sleep(0.3)

            attackdowntp()
            time.sleep(0.3)


            PressKey(0x3D)#f3
            time.sleep(0.1)
            ReleaseKey(0x3D)
            PressKey(0x3D)#f3
            time.sleep(0.1)
            ReleaseKey(0x3D)
            PressKey(0x3D)#f3
            time.sleep(0.1)
            ReleaseKey(0x3D)
            time.sleep(0.1)


            sixthjobcounter = sixthjobcounter + 1
            count = 0





        attackteleleft()
        time.sleep(0.3)
        attackteleleft()
        time.sleep(0.3)
        attackteleleft()
        time.sleep(0.3)
        attackteleleft()
        time.sleep(0.3)
        attackteleleft()
        time.sleep(0.3)
        attackteleleft()
        time.sleep(0.3)

        peacemaker()

        time.sleep(0.5)

        attackteleright()
        time.sleep(0.3)
        attackteleright()
        time.sleep(0.3)
        attackteleright()
        time.sleep(0.3)
        attackteleright()
        time.sleep(0.3)
        attackteleright()
        time.sleep(0.3)
        attackteleright()
        time.sleep(0.3)

        PressKey(0x02)#1 infinity
        time.sleep(0.1)
        ReleaseKey(0x02)

        PressKey(0x21)#F door
        time.sleep(0.1)
        ReleaseKey(0x21)

        PressKey(0x05)#4 bene
        time.sleep(0.1)
        ReleaseKey(0x05)

        PressKey(0x06)#5 angel
        time.sleep(0.1)
        ReleaseKey(0x06)

        PressKey(0x09)#8 will
        time.sleep(0.1)
        ReleaseKey(0x09)

        time.sleep(0.6)

        count = count + 1

def openherbs():
    while(True):
        PressKey(0x58)#f12
        time.sleep(0.1)
        ReleaseKey(0x58)
        time.sleep(0.3)

        PressKey(0x15)#y
        time.sleep(0.1)
        ReleaseKey(0x15)






def outlawwaste2():
    count = 0
    sixthjobcounter = 0
    while(True):
        if(count == 2):
            time.sleep(0.2)
            attackteleleft()
            time.sleep(0.5)
            attackuptp()
            time.sleep(1)
            PressKey(0xC8)#up
            time.sleep(0.1)
            ReleaseKey(0xC8)
            time.sleep(0.5)
            PressKey(0x13)#r
            time.sleep(0.1)
            ReleaseKey(0x13)
            time.sleep(0.3)

            time.sleep(0.5)
            PressKey(0xC8)#up
            time.sleep(0.1)
            ReleaseKey(0xC8)
            time.sleep(0.5)


            attackteleright()
            time.sleep(0.3)
            attackteleright()
            time.sleep(0.3)
            attackteleright()
            time.sleep(0.3)

            setfountain()
            time.sleep(0.5)

            attackuptp()
            time.sleep(0.3)

            attackteleright()
            time.sleep(0.3)

            attackteleright()
            time.sleep(0.3)


            attackdowntp()
            time.sleep(0.3)

            seterdashower()
            time.sleep(0.5)

            attackteleright()
            time.sleep(0.3)
            attackteleright()
            time.sleep(0.3)
            attackteleright()
            time.sleep(0.3)


            attackdowntp()
            time.sleep(0.3)

            PressKey(0x13)#r
            time.sleep(0.1)
            ReleaseKey(0x13)
            time.sleep(0.3)

            attackdowntp()
            time.sleep(0.3)

            attackteleleft()
            time.sleep(0.3)
            attackteleleft()
            time.sleep(0.3)
            attackteleleft()
            time.sleep(0.3)
            attackteleleft()
            time.sleep(0.3)

            if(sixthjobcounter == 7):
                PressKey(0x29)#'`' grave symbol
                time.sleep(0.1)
                ReleaseKey(0x29)
                time.sleep(5)
                sixthjobcounter = 0


            attackteleleft()
            time.sleep(0.3)
            attackteleleft()
            time.sleep(0.3)
            attackteleleft()
            time.sleep(0.5)

            attackuptp()
            time.sleep(0.3)

            attackteleright()
            time.sleep(0.3)
            attackteleright()
            time.sleep(0.3)
            attackteleright()
            time.sleep(0.3)
            attackteleright()
            time.sleep(0.3)
            PressKey(0x13)#r
            time.sleep(0.1)
            ReleaseKey(0x13)
            time.sleep(0.5)

            attackteleright()
            time.sleep(0.3)
            attackteleright()
            time.sleep(0.3)
            attackteleright()
            time.sleep(0.3)

            attackteleleft()
            time.sleep(0.3)
            attackteleleft()
            time.sleep(0.3)
            attackteleleft()
            time.sleep(0.3)
            attackteleleft()
            time.sleep(0.3)
            attackteleleft()
            time.sleep(0.3)
            attackteleleft()
            time.sleep(0.3)
            attackteleleft()
            time.sleep(0.3)
            attackteleleft()
            time.sleep(0.3)

            PressKey(0x3D)#f3
            time.sleep(0.1)
            ReleaseKey(0x3D)
            PressKey(0x3D)#f3
            time.sleep(0.1)
            ReleaseKey(0x3D)
            PressKey(0x3D)#f3
            time.sleep(0.1)
            ReleaseKey(0x3D)
            time.sleep(0.1)

            sixthjobcounter = sixthjobcounter + 1
            count = 0


        attackteleright()
        time.sleep(0.3)
        attackteleright()
        time.sleep(0.3)
        attackteleright()
        time.sleep(0.3)
        attackteleright()
        time.sleep(0.3)
        attackteleright()
        time.sleep(0.3)
        attackteleright()
        time.sleep(0.3)
        attackteleright()
        time.sleep(0.3)


        peacemaker()
        time.sleep(0.3)

        attackteleleft()
        time.sleep(0.3)
        attackteleleft()
        time.sleep(0.3)
        attackteleleft()
        time.sleep(0.3)

        PressKey(0x02)#1 infinity
        time.sleep(0.1)
        ReleaseKey(0x02)

        PressKey(0x21)#F door
        time.sleep(0.1)
        ReleaseKey(0x21)

        PressKey(0x05)#4 bene
        time.sleep(0.1)
        ReleaseKey(0x05)

        PressKey(0x06)#5 angel
        time.sleep(0.1)
        ReleaseKey(0x06)

        PressKey(0x09)#8 will
        time.sleep(0.1)
        ReleaseKey(0x09)

        time.sleep(0.6)




        attackteleleft()
        time.sleep(0.3)
        attackteleleft()
        time.sleep(0.3)
        attackteleleft()
        time.sleep(0.3)
        attackteleleft()
        time.sleep(0.3)

        '''
        PressKey(0x02)#1 infinity
        time.sleep(0.1)
        ReleaseKey(0x02)

        PressKey(0x21)#F door
        time.sleep(0.1)
        ReleaseKey(0x21)

        PressKey(0x05)#4 bene
        time.sleep(0.1)
        ReleaseKey(0x05)

        PressKey(0x06)#5 angel
        time.sleep(0.1)
        ReleaseKey(0x06)

        PressKey(0x09)#8 will
        time.sleep(0.1)
        ReleaseKey(0x09)

        time.sleep(0.6)
        '''
        count = count + 1

'''

def task():
    while True:
        print("Task is running...")
        attacklr()  # Replace this with your actual task

def on_press(key):
    if key == "esc":
        print("Exiting program.")
        sys.exit()

keyboard.on_press_key("esc", lambda _: on_press("esc"))

print("Press 'esc' to exit the program.")
thread = threading.Thread(target=task)
thread.start()

keyboard.wait()  # Wait for any key press to keep the script running
'''


def loopmap():
    while(True):
        PressKey(0xCD)#right
        time.sleep(0.1)
      #  ReleaseKey(0xCD)
        for x in range(12):
            PressKey(0x12)#e
          #  time.sleep(0.1)
            ReleaseKey(0x12)
            time.sleep(0.3)
            

        ReleaseKey(0xCD)

        time.sleep(0.5)

        PressKey(0xCB)#left
        time.sleep(0.1)
      #  ReleaseKey(0xCB)
        for y in range(12):
            PressKey(0x12)#e
          #  time.sleep(0.1)
            ReleaseKey(0x12)
            time.sleep(0.3)
        ReleaseKey(0xCB)

        time.sleep(0.5)
        '''
        PressKey(0x03)#2 POT
        time.sleep(0.1)
        ReleaseKey(0x03)
        '''

def loopmapadele():
    while(True):
        PressKey(0xCD)#right
        time.sleep(0.1)
        for x in range(5):
            doublejump()
            time.sleep(0.1)
            PressKey(0x10)#e
            time.sleep(0.1)
            ReleaseKey(0x10)
            time.sleep(0.55)
        ReleaseKey(0xCD)

        PressKey(0x23)#h
        time.sleep(0.1)
        ReleaseKey(0x23)
        time.sleep(1)

        PressKey(0xCB)#left
        time.sleep(0.1)
        for y in range(5):
            doublejump()
            time.sleep(0.1)
            PressKey(0x10)#e
            time.sleep(0.1)
            ReleaseKey(0x10)
            time.sleep(0.55)
        ReleaseKey(0xCB)

        PressKey(0x13)#r
        time.sleep(0.1)
        ReleaseKey(0x13)
        PressKey(0x13)#r
        time.sleep(0.1)
        PressKey(0x13)#r
        time.sleep(0.1)
        ReleaseKey(0x13)
        PressKey(0x13)#r
        time.sleep(0.1)
        time.sleep(1)

def burningcerniumwestern1_vac():
    count = 0
    sixthjobcounter = 0
    while(True):
        if(count == 128):  #13 for normal, 120 for no moving
            time.sleep(0.5)
            attackdowntp()
            time.sleep(0.3)

            setfountain()

            time.sleep(0.5)

            attackuptp()
            time.sleep(0.3)

            attackteleleft()
            time.sleep(0.3)

            seterdashower()
            time.sleep(0.5)

            attackteleleft()
            time.sleep(0.3)

            attackteleleft()
            time.sleep(0.3)

            attackdowntp()
            time.sleep(0.3)

            PressKey(0x20)#D (sol janus)
            time.sleep(0.1)
            ReleaseKey(0x20)

            time.sleep(0.5)


            if(sixthjobcounter == 7):
                PressKey(0x29)#'`' grave symbol
                time.sleep(0.1)
                ReleaseKey(0x29)
                time.sleep(5)
                sixthjobcounter = 0

            attackteleleft()
            time.sleep(0.3)

            attackteleleft()
            time.sleep(0.3)

            attackteleleft()
            time.sleep(0.3)


            PressKey(0x20)#D (sol janus)
            time.sleep(0.1)
            ReleaseKey(0x20)
            time.sleep(0.5)

            attackteleright()
            time.sleep(0.3)

            attackteleright()
            time.sleep(0.3)

            attackteleright()
            time.sleep(0.3)

            attackteleright()
            time.sleep(0.3)

            attackteleright()
            time.sleep(0.3)

            attackteleright()
            time.sleep(0.3)


            attackuptp()
            time.sleep(0.3)

            PressKey(0x3D)#f3
            time.sleep(0.1)
            ReleaseKey(0x3D)
            PressKey(0x3D)#f3
            time.sleep(0.1)
            ReleaseKey(0x3D)
            PressKey(0x3D)#f3
            time.sleep(0.1)
            ReleaseKey(0x3D)
            time.sleep(0.1)

            sixthjobcounter = sixthjobcounter + 1
            count = 0


        '''
        attackuptp()
        time.sleep(0.3)
        attackdowntp()
        time.sleep(0.3)
        PressKey(0x13)#r
        time.sleep(0.1)
        ReleaseKey(0x13)
        time.sleep(0.7)
        


        PressKey(0x02)#1 infinity
        time.sleep(0.1)
        ReleaseKey(0x02)

        PressKey(0x21)#F door
        time.sleep(0.1)
        ReleaseKey(0x21)

        PressKey(0x05)#4 bene
        time.sleep(0.1)
        ReleaseKey(0x05)

        PressKey(0x06)#5 angel
        time.sleep(0.1)
        ReleaseKey(0x06)

        PressKey(0x09)#8 will
        time.sleep(0.1)
        ReleaseKey(0x09)

        time.sleep(0.6)
        '''


        PressKey(0x11)#w
        time.sleep(0.1)
        ReleaseKey(0x11)
        time.sleep(0.1)

        PressKey(0x02)#1 infinity
        time.sleep(0.1)
        ReleaseKey(0x02)

        count = count + 1


def odium():
    count = 0
    sixthjobcounter = 0
    while(True):    
        if(count == 128):#120 if stand one place , 4 for move
            time.sleep(0.5)
            attackteleright()
            time.sleep(0.3)
            moveleft()
            time.sleep(0.3)

            seterdashower()
            time.sleep(0.5)

            attackteleleft()
            time.sleep(0.3)
            attackteleleft()
            time.sleep(0.3)

            setfountain()
            time.sleep(0.5)

            attackteleleft()
            time.sleep(0.3)
            attackteleleft()
            time.sleep(0.3)

            PressKey(0x20)#D (sol janus)
            time.sleep(0.1)
            ReleaseKey(0x20)
            time.sleep(0.5)

            attackteleleft()
            time.sleep(0.3)


            if(sixthjobcounter == 7):
                PressKey(0x29)#'`' grave symbol
                time.sleep(0.1)
                ReleaseKey(0x29)
                time.sleep(5)
                sixthjobcounter = 0

            attackteleleft()
            time.sleep(0.3)
            attackteleleft()
            time.sleep(0.3)

            PressKey(0x20)#D (sol janus)
            time.sleep(0.1)
            ReleaseKey(0x20)

            time.sleep(0.5)

            attackteleleft()
            time.sleep(0.3)


            attackteleright()
            time.sleep(0.3)
            attackteleright()
            time.sleep(0.3)
            attackteleright()
            time.sleep(0.3)
            attackteleright()
            time.sleep(0.3)
            attackteleright()
            time.sleep(0.3)
            attackteleright()
            time.sleep(0.3)
            attackteleright()
            time.sleep(0.3)
            attackteleright()
            time.sleep(0.3)
            attackteleright()
            time.sleep(0.3)

            PressKey(0x3D)#f3
            time.sleep(0.1)
            ReleaseKey(0x3D)
            PressKey(0x3D)#f3
            time.sleep(0.1)
            ReleaseKey(0x3D)
            PressKey(0x3D)#f3
            time.sleep(0.1)
            ReleaseKey(0x3D)
            time.sleep(0.1)

            moveleft()
            time.sleep(0.3)


            sixthjobcounter = sixthjobcounter + 1
            count = 0

        '''
        attackteleleft()
        time.sleep(0.3)
        attackteleleft()
        time.sleep(0.3)
        attackteleleft()
        time.sleep(0.3)

        attackteleleft()
        time.sleep(0.3)

        attackteleleft()
        time.sleep(0.3)

        attackteleleft()
        time.sleep(0.3)

        PressKey(0x13)#r
        time.sleep(0.1)
        ReleaseKey(0x13)
        time.sleep(0.5)


        attackteleright()
        time.sleep(0.3)
        attackteleright()
        time.sleep(0.3)
        attackteleright()
        time.sleep(0.3)
        attackteleright()
        time.sleep(0.3)
        attackteleright()
        time.sleep(0.3)
        attackteleright()
        time.sleep(0.3)
        '''

        PressKey(0x11)#w
        time.sleep(0.1)
        ReleaseKey(0x11)
        time.sleep(0.1)

        PressKey(0x02)#1 infinity
        time.sleep(0.1)
        ReleaseKey(0x02)
        '''
        PressKey(0x02)#1 infinity
        time.sleep(0.1)
        ReleaseKey(0x02)

        PressKey(0x21)#F door
        time.sleep(0.1)
        ReleaseKey(0x21)

        PressKey(0x05)#4 bene
        time.sleep(0.1)
        ReleaseKey(0x05)

        PressKey(0x06)#5 angel
        time.sleep(0.1)
        ReleaseKey(0x06)

        PressKey(0x09)#8 will
        time.sleep(0.1)
        ReleaseKey(0x09)

        time.sleep(0.6)
        '''
        print(count)
        count = count + 1

def jumpdown():
    PressKey(0xD0)#down
    time.sleep(0.1)
    PressKey(0x39)#space jump
    time.sleep(0.1)
    ReleaseKey(0x39)

    ReleaseKey(0xD0)


def shangri_la_bloomingspring4():
    count = 0
    sixthjobcounter = 0
    infinity_counter = 0
    while(True):
        if(count == 30):
            time.sleep(1)
            if(infinity_counter == 0):
                PressKey(0x02)#1 infinity
                time.sleep(0.1)
                ReleaseKey(0x02)
                time.sleep(1.5)
            if(infinity_counter == 2):
                PressKey(0xD1)#pgdn infinity
                time.sleep(0.1)
                ReleaseKey(0xD1)
                time.sleep(1.5)
                infinity_counter = 0


            jumpupattackupTP()
            time.sleep(0.3)


            jumpupattackdownTP()
            time.sleep(0.3)
            PressKey(0x09)#8 will
            time.sleep(0.1)
            ReleaseKey(0x09)
            time.sleep(0.5)
            attackteleleft()
            time.sleep(0.3)
            attackteleleft()
            time.sleep(0.3)
            attackdowntp()
            time.sleep(0.3)

            PressKey(0xCD)#right
            for y in range(6):
                generaljumptpR()
            ReleaseKey(0xCD)

            time.sleep(0.3)

            #jumpdown()


            time.sleep(1.5)

            PressKey(0x13)#r
            time.sleep(0.1)
            ReleaseKey(0x13)
            time.sleep(0.8)


            PressKey(0xC8)#Up for portal
            time.sleep(0.1)
            ReleaseKey(0xC8)

            time.sleep(0.3)

            attackuptp()
            time.sleep(0.3)
            attackteleleft()
            time.sleep(0.3)
            attackdowntp()
            time.sleep(0.3)

            PressKey(0x20)#D (sol janus)
            time.sleep(0.1)
            ReleaseKey(0x20)
            time.sleep(0.5)

            attackdowntp()
            time.sleep(0.3)

            setfountain()
            time.sleep(0.5)

            attackteleleft()
            time.sleep(0.3)
            attackteleleft()
            time.sleep(0.3)

            attackuptp()
            time.sleep(0.3)
            attackuptp()
            time.sleep(0.3)

            attackteleleft()
            time.sleep(0.3)
            attackteleleft()
            time.sleep(0.3)
            attackdowntp()
            time.sleep(0.3)
            attackteleright()
            time.sleep(0.3)

            PressKey(0x20)#D (sol janus)
            time.sleep(0.1)
            ReleaseKey(0x20)
            time.sleep(0.5)

            attackdowntp()
            time.sleep(0.3)
            seterdashower()
            time.sleep(0.5)

            if(sixthjobcounter == 7):
                PressKey(0x29)#'`' grave symbol
                time.sleep(0.1)
                ReleaseKey(0x29)
                time.sleep(5)
                sixthjobcounter = 0

            attackteleleft()
            time.sleep(0.3)
            attackteleleft()
            time.sleep(0.3)
            attackteleleft()
            time.sleep(0.3)

            PressKey(0x3D)#f3
            time.sleep(0.1)
            ReleaseKey(0x3D)
            PressKey(0x3D)#f3
            time.sleep(0.1)
            ReleaseKey(0x3D)
            PressKey(0x3D)#f3
            time.sleep(0.1)
            ReleaseKey(0x3D)
            time.sleep(0.1)

            
            sixthjobcounter = sixthjobcounter + 1
            infinity_counter = infinity_counter + 1
            count = 0



        PressKey(0x13)#r
        time.sleep(0.1)
        ReleaseKey(0x13)
        time.sleep(0.1)

        PressKey(0x21)#F door
        time.sleep(0.1)
        ReleaseKey(0x21)

        PressKey(0x05)#4 bene
        time.sleep(0.1)
        ReleaseKey(0x05)

        PressKey(0x06)#5 angel
        time.sleep(0.1)
        ReleaseKey(0x06)


        PressKey(0x11)#w
        time.sleep(0.1)
        ReleaseKey(0x11)
        time.sleep(0.1)



        print(count)
        count = count + 1




def shangri_la_bloomingspring4_test():
    count = 0
    sixthjobcounter = 0
    infinity_counter = 0
    while(True):
        if(count == 16):
            time.sleep(1)
            if(infinity_counter == 0):
                PressKey(0x02)#1 infinity
                time.sleep(0.1)
                ReleaseKey(0x02)
                time.sleep(1.5)
            if(infinity_counter == 2):
                PressKey(0xD1)#pgdn infinity
                time.sleep(0.1)
                ReleaseKey(0xD1)
                time.sleep(2)
                infinity_counter = -2


            jumpupattackupTP()
            time.sleep(0.3)


            jumpupattackdownTP()
            time.sleep(0.3)
            PressKey(0x09)#8 will
            time.sleep(0.1)
            ReleaseKey(0x09)
            time.sleep(0.5)
            attackteleleft()
            time.sleep(0.3)
            attackteleleft()
            time.sleep(0.3)
            attackdowntp()
            time.sleep(0.3)

            PressKey(0xCD)#right
            for y in range(6):
                generaljumptpR()
            ReleaseKey(0xCD)

            time.sleep(0.3)

            #jumpdown()
            checkjumpdown()

            #time.sleep(1.5)

            PressKey(0x13)#r
            time.sleep(0.1)
            ReleaseKey(0x13)
            time.sleep(0.8)


            PressKey(0xC8)#Up for portal
            time.sleep(0.1)
            ReleaseKey(0xC8)

            time.sleep(0.3)

            attackuptp()
            time.sleep(0.3)
            attackteleleft()
            time.sleep(0.3)
            attackdowntp()
            time.sleep(0.3)
            
            PressKey(0x20)#D (sol janus)
            time.sleep(0.1)
            ReleaseKey(0x20)
            time.sleep(0.3)

            attackdowntp()
            time.sleep(0.3)
            '''
            setfountain()
            time.sleep(0.5)

            '''

            attackdowntp()
            time.sleep(0.3)

            PressKey(0x20)#D (sol janus)
            time.sleep(0.1)
            ReleaseKey(0x20)
            time.sleep(0.5)


            checkjumpdown()
            #jumpdown()

            #time.sleep(1.5)


            attackdowntp()
            time.sleep(0.3)

            attackteleright()
            time.sleep(0.3)


            PressKey(0x20)#D (sol janus)
            time.sleep(0.1)
            ReleaseKey(0x20)
            time.sleep(0.5)


            attackteleright()
            time.sleep(0.3)
            attackteleright()
            time.sleep(0.3)

            PressKey(0x21)#F door
            time.sleep(0.1)
            ReleaseKey(0x21)
            time.sleep(0.3)


            attackteleright()
            time.sleep(0.3)
            attackteleright()
            time.sleep(0.3)


            seterdashower()
            time.sleep(0.5)

            attackuptp()
            time.sleep(0.3)

            setfountain()
            time.sleep(0.5)
            '''
            PressKey(0x20)#D (sol janus)
            time.sleep(0.1)
            ReleaseKey(0x20)
            time.sleep(0.3)
            '''
            attackteleleft()
            time.sleep(1.5)

            attackuptp()
            time.sleep(0.3)

            attackteleright()
            time.sleep(0.3)
            attackteleright()
            time.sleep(0.3)

            attackdowntp()
            time.sleep(0.3)
            attackdowntp()
            time.sleep(1)

            attackteleleft()
            time.sleep(0.3)

            if(sixthjobcounter == 7):
                PressKey(0x29)#'`' grave symbol
                time.sleep(0.1)
                ReleaseKey(0x29)
                time.sleep(5)
                sixthjobcounter = 0


            attackteleleft()
            time.sleep(0.3)
            attackteleleft()
            time.sleep(0.3)
            attackteleleft()
            time.sleep(0.3)





            PressKey(0x3D)#f3
            time.sleep(0.1)
            ReleaseKey(0x3D)
            PressKey(0x3D)#f3
            time.sleep(0.1)
            ReleaseKey(0x3D)
            PressKey(0x3D)#f3
            time.sleep(0.1)
            ReleaseKey(0x3D)
            time.sleep(0.1)

            
            sixthjobcounter = sixthjobcounter + 1
            infinity_counter = infinity_counter + 1
            count = 0

            movetorune()
   

        PressKey(0x13)#r
        time.sleep(0.1)
        ReleaseKey(0x13)
        time.sleep(0.1)

        PressKey(0x05)#4 bene
        time.sleep(0.1)
        ReleaseKey(0x05)
        time.sleep(0.1)

        PressKey(0x41)#-
        time.sleep(0.1)
        ReleaseKey(0x41)
        time.sleep(0.1)

        PressKey(0x06)#5 angel
        time.sleep(0.1)
        ReleaseKey(0x06)


        PressKey(0x11)#w
        time.sleep(0.1)
        ReleaseKey(0x11)
        time.sleep(0.1)



        print(count)
        count = count + 1



def movetorune():
    from mss import mss
    try:
        x1,y1 = pyautogui.locateCenterOnScreen("C:/Users/Alec/Desktop/Maplestoryscript/positionbot/world.PNG", confidence=0.8)
       # x2,y2 = pyautogui.locateCenterOnScreen("C:/Users/Alec/Desktop/Maplestoryscript/positionbot/minimap_bottomright.PNG", confidence=0.8)

      #  width = x2 - x1
      #  height = y2 - y1
        print(x1,y1)

        #bottom right: x1 +38 , y1 + 190
        #top left: x1 - 247 , y1
        '''
        top = x1 - 247
        left = y1

        width = 247
        height = 190
        '''

        #altered
        top = x1 - 160
        left = y1

        width = 260
        height = 100

        mon = {'top': top, 'left': left, 'width': width, 'height': height}
        print(mon)
        

        with mss() as mss_instance:
            while True:
                onruneX = 0
                onruneY = 0

                screenshot = mss_instance.grab(mon)

                img = Image.frombytes("RGB", screenshot.size, screenshot.bgra, "raw", "BGRX")  # Convert to PIL.Image
                
                try:
                    position_X,position_Y = x1-164, y1+138
                    print("position: ")
                    print(position_X,position_Y)
                    playerX,playerY = pyautogui.locateCenterOnScreen("C:/Users/Alec/Desktop/Maplestoryscript/positionbot/player.PNG", confidence=0.8)
                    print("player: ")
                    print(playerX,playerY)

                    #top y plat: 132
                    #mid y plat: 153
                    #bot y plat: 172

                    #right side of plat : 99, 152
                    #left side of plat : 77, 153



                    if((playerX > (position_X-10)) and (playerX < (position_X+14))):
                        break
                    elif(playerX < position_X):
                        PressKey(0xCD)#right
                        time.sleep(0.3)
                        ReleaseKey(0xCD)
                        attackteleright()
                        time.sleep(0.3)
                    else:
                        PressKey(0xCB)#left
                        time.sleep(0.1)
                        ReleaseKey(0xCB)
                        attackteleleft()
                        time.sleep(0.3)
                    

                except TypeError:
                    print("no runeX")
                    pass
                   # pass
                '''
                if(onruneX == 1):
                    img.show()
                    break
                '''


            #    if(onruneX == 1 and onruneY == 1):
            #        break
              #  img.show()  # Show the image using the default image viewer

                time.sleep(0.1)

            while True:
                onruneX = 0
                onruneY = 0

                screenshot = mss_instance.grab(mon)

                img = Image.frombytes("RGB", screenshot.size, screenshot.bgra, "raw", "BGRX")  # Convert to PIL.Image
                
                       
                try:
                    position_X,position_Y = x1-164, y1+138
                    print("position: ")
                    print(position_X,position_Y)
                    playerX,playerY = pyautogui.locateCenterOnScreen("C:/Users/Alec/Desktop/Maplestoryscript/positionbot/player.PNG", confidence=0.8)
                    print("player: ")
                    print(playerX,playerY)


                    if((playerY > (position_Y-14)) and (playerY < (position_Y+14))):
                        break
                    elif(playerY < position_Y):
                        attackdowntp()
                        time.sleep(0.3)
                    else:
                        attackuptp()
                        time.sleep(0.3)

                except TypeError:
                    print("no runeY")
                    pass

             

    except TypeError:
        print("not found")
        pass


def checkjumpdown():
    from mss import mss
    try:
        x1,y1 = pyautogui.locateCenterOnScreen("C:/Users/Alec/Desktop/Maplestoryscript/positionbot/world.PNG", confidence=0.8)
       # x2,y2 = pyautogui.locateCenterOnScreen("C:/Users/Alec/Desktop/Maplestoryscript/positionbot/minimap_bottomright.PNG", confidence=0.8)

      #  width = x2 - x1
      #  height = y2 - y1
        print(x1,y1)

        #bottom right: x1 +38 , y1 + 190
        #top left: x1 - 247 , y1
        '''
        top = x1 - 247
        left = y1

        width = 247
        height = 190
        '''

        #altered
        top = x1 - 160
        left = y1

        width = 260
        height = 100

        mon = {'top': top, 'left': left, 'width': width, 'height': height}
        print(mon)
        

        with mss() as mss_instance:
            while True:
                onruneX = 0
                onruneY = 0

                screenshot = mss_instance.grab(mon)

                img = Image.frombytes("RGB", screenshot.size, screenshot.bgra, "raw", "BGRX")  # Convert to PIL.Image
                
                while(True):
                    try:
                        position_X,position_Y = x1-164, y1+138
                        print("position: ")
                        print(position_X,position_Y)
                        playerX,playerY = pyautogui.locateCenterOnScreen("C:/Users/Alec/Desktop/Maplestoryscript/positionbot/player.PNG", confidence=0.8)
                        print("player: ")
                        print(playerX,playerY)

                        #top y plat: 132
                        #mid y plat: 153
                        #bot y plat: 172

                        #right side of plat : 99, 152
                        #left side of plat : 77, 153


                        if((playerX == 53) and (playerY ==137)):
                            break
                        else:
                            jumpdown()
                            time.sleep(2)

                    except TypeError:
                        print("did not jump down correctly")
                        pass

                break
            

    except TypeError:
        print("not found")
        pass



def mcoord():
    #! python3
    import pyautogui, sys
    print('Press Ctrl-C to quit.')
    try:
        while True:
            x, y = pyautogui.position()
            positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
            print(positionStr, end='')
            print('\b' * len(positionStr), end='', flush=True)
    except KeyboardInterrupt:
        print('\n')




def otherplayer():
    from mss import mss
    try:

        x1,y1 = pyautogui.locateCenterOnScreen("C:/Users/Alec/Desktop/Maplestoryscript/positionbot/world.PNG", confidence=0.8)
       # x2,y2 = pyautogui.locateCenterOnScreen("C:/Users/Alec/Desktop/Maplestoryscript/positionbot/minimap_bottomright.PNG", confidence=0.8)

      #  width = x2 - x1
      #  height = y2 - y1
        print(x1,y1)

        #bottom right: x1 +38 , y1 + 190
        #top left: x1 - 247 , y1
        '''
        top = x1 - 247
        left = y1

        width = 247
        height = 190
        '''

        #altered
        top = x1 - 160
        left = y1

        width = 260
        height = 100

        mon = {'top': top, 'left': left, 'width': width, 'height': height}
        print(mon)
        
        with mss() as mss_instance:
            while True:

                screenshot = mss_instance.grab(mon)

                img = Image.frombytes("RGB", screenshot.size, screenshot.bgra, "raw", "BGRX")  # Convert to PIL.Image
                try:
                    otherplayerX,otherplayerY = pyautogui.locateCenterOnScreen("C:/Users/Alec/Desktop/Maplestoryscript/positionbot/otherplayer.png", confidence=0.9)
                    print("other player on map need to run")
                    PressKey(0x3C)#f2 return to town scroll
                    time.sleep(0.1)
                    ReleaseKey(0x3C)
                    time.sleep(0.1)
                    PressKey(0x3C)#f2 return to town scroll
                    time.sleep(0.1)
                    ReleaseKey(0x3C)
                    time.sleep(0.1)
                    PressKey(0x3C)#f2 return to town scroll
                    time.sleep(0.1)
                    ReleaseKey(0x3C)
                    time.sleep(0.1)
                    PressKey(0x3C)#f2 return to town scroll
                    time.sleep(0.1)
                    ReleaseKey(0x3C)
                    time.sleep(0.1)
                    PressKey(0x3C)#f2 return to town scroll
                    time.sleep(0.1)
                    ReleaseKey(0x3C)
                    time.sleep(1)
                    os._exit(0)
                except TypeError:
                    print("no other player")
                    pass

                time.sleep(3)


    except TypeError:
        print("not found")
        pass

def shangrila_mapdetect():
    thread1 = threading.Thread(target=shangri_la_bloomingspring4_test)
    thread1.daemon = True
    thread1.start()

    thread2 = threading.Thread(target=otherplayer)
    thread2.daemon = True
    thread2.start()

    while(True):
        thread1.join(1)
        thread2.join(1)
        if not thread1.is_alive() and thread2.is_alive():
            os._exit(0)


def bucc_superjump():
    PressKey(0x13)#R 
    ReleaseKey(0x13)

    PressKey(0x39)#space
    time.sleep(0.1)
    ReleaseKey(0x39)


def bucc_abandonarea2():


    while(True):
        PressKey(0xCD)#right
        time.sleep(0.1)
        ReleaseKey(0xCD)
        time.sleep(0.5)
        bucc_superjump()
        time.sleep(0.1)
        PressKey(0xC8)#up
        PressKey(0x39)#space
        time.sleep(0.1)
        ReleaseKey(0x39)
        ReleaseKey(0xC8)

        time.sleep(0.5)
        PressKey(0x3D)#f3
        time.sleep(0.1)
        ReleaseKey(0x3D)
        time.sleep(0.4)

        bucc_superjump()

        time.sleep(1)
        bucc_superjump()
        time.sleep(1)
        bucc_superjump()
        time.sleep(1)
        bucc_superjump()
            

        ReleaseKey(0xCD)

        time.sleep(1)

        PressKey(0xCB)#left
        time.sleep(0.1)
        ReleaseKey(0xCB)

        time.sleep(0.5)
        bucc_superjump()
        time.sleep(1)
        bucc_superjump()
        time.sleep(1)
        bucc_superjump()
        time.sleep(1)
        bucc_superjump()
        time.sleep(1)
        bucc_superjump()
        time.sleep(1)
        bucc_superjump()


        ReleaseKey(0xCB)

        time.sleep(0.5)

def bucc_worldsorrow3():
    while(True):
        PressKey(0xCD)#right
        time.sleep(0.1)
        ReleaseKey(0xCD)
        time.sleep(0.5)
        bucc_superjump()
        time.sleep(0.1)
        PressKey(0xC8)#up
        PressKey(0x39)#space
        time.sleep(0.1)
        ReleaseKey(0x39)
        ReleaseKey(0xC8)

        time.sleep(0.5)
        PressKey(0x3D)#f3
        time.sleep(0.1)
        ReleaseKey(0x3D)
        time.sleep(0.4)

        bucc_superjump()

        time.sleep(1)
        bucc_superjump()
            

        ReleaseKey(0xCD)

        time.sleep(1)

        PressKey(0xCB)#left
        time.sleep(0.1)
        ReleaseKey(0xCB)

        time.sleep(0.5)
        bucc_superjump()
        time.sleep(1)
        bucc_superjump()
        time.sleep(1)
        bucc_superjump()
        time.sleep(1)
        bucc_superjump()


        ReleaseKey(0xCB)

        time.sleep(0.5)

def greedcache():
    count = 0
    infinity_counter = 0
    while(True):    
        if(count == 17):
            time.sleep(1)
            if(infinity_counter == 0):
                PressKey(0x02)#1 infinity
                time.sleep(0.1)
                ReleaseKey(0x02)
                time.sleep(1.5)
                PressKey(0x3D)#f3
                time.sleep(0.1)
                ReleaseKey(0x3D)
                PressKey(0x3D)#f3
                time.sleep(0.1)
                ReleaseKey(0x3D)
                PressKey(0x3D)#f3
                time.sleep(0.1)
                ReleaseKey(0x3D)
                time.sleep(0.1)
            if(infinity_counter == 2):
                PressKey(0xD1)#pgdn infinity
                time.sleep(0.1)
                ReleaseKey(0xD1)
                time.sleep(2)
                infinity_counter = -2


            infinity_counter = infinity_counter + 1
            count = 0

        attackuptp()
        time.sleep(0.5)
        attackdowntp()
        time.sleep(0.5)
        attackteleleft()
        time.sleep(0.5)
        attackteleright()
        time.sleep(0.5)
        attackteleright()
        time.sleep(0.5)
        attackteleleft()
        time.sleep(0.5)
        PressKey(0x05)#4 bene
        time.sleep(0.1)
        ReleaseKey(0x05)
        PressKey(0x06)#5 angel
        time.sleep(0.1)
        ReleaseKey(0x06)
        time.sleep(0.3)
        count = count + 1
        print(count)


def TOFask():
    while(True):
        while(True):
            try:
                thickX,thickY = pyautogui.locateCenterOnScreen("C:/Users/Alec/Desktop/Maplestoryscript/TOF/ASK.PNG", confidence=0.9)
                print("found ASK")
                autoit.mouse_move(thickX, thickY, 1)
                time.sleep(0.5)
                autoit.mouse_click("left", thickX, thickY, 1)
                time.sleep(0.1)
                autoit.mouse_click("left", thickX, thickY, 1)
                time.sleep(0.1)
                autoit.mouse_click("left", thickX, thickY, 1)
                time.sleep(0.1)
                autoit.mouse_click("left", thickX, thickY, 1)
                time.sleep(1)
                for x in range(20):
                    PressKey(0x15)#y
                    time.sleep(0.1)
                    ReleaseKey(0x15)
                    time.sleep(0.1)
                time.sleep(1)
                break

            except TypeError:
                print("no thread")
                time.sleep(0.1)
                pass

        time.sleep(1860)

        while(True):
            try:
                thickX,thickY = pyautogui.locateCenterOnScreen("C:/Users/Alec/Desktop/Maplestoryscript/TOF/lightbulb.png", confidence=0.9)
                print("found ASK")
                autoit.mouse_move(thickX, thickY, 1)
                time.sleep(0.5)
                autoit.mouse_click("left", thickX, thickY, 1)
                time.sleep(0.1)
                autoit.mouse_click("left", thickX, thickY, 1)
                time.sleep(0.1)
                autoit.mouse_click("left", thickX, thickY, 1)
                time.sleep(0.1)
                autoit.mouse_click("left", thickX, thickY, 1)
                time.sleep(1)
                for x in range(20):
                    PressKey(0x15)#y
                    time.sleep(0.1)
                    ReleaseKey(0x15)
                    time.sleep(0.1)
                time.sleep(1)
                break

            except TypeError:
                print("no thread")
                time.sleep(0.1)
                pass

        time.sleep(10)

def trackplayer():
    from mss import mss
    try:

        x1,y1 = pyautogui.locateCenterOnScreen("C:/Users/Alec/Desktop/Maplestoryscript/positionbot/world.PNG", confidence=0.8)
       # x2,y2 = pyautogui.locateCenterOnScreen("C:/Users/Alec/Desktop/Maplestoryscript/positionbot/minimap_bottomright.PNG", confidence=0.8)

      #  width = x2 - x1
      #  height = y2 - y1
        print(x1,y1)

        #bottom right: x1 +38 , y1 + 190
        #top left: x1 - 247 , y1
        '''
        top = x1 - 247
        left = y1

        width = 247
        height = 190
        '''

        #altered
        top = x1 - 160
        left = y1

        width = 260
        height = 100

        mon = {'top': top, 'left': left, 'width': width, 'height': height}
        print(mon)
        
        with mss() as mss_instance:
            while True:

                screenshot = mss_instance.grab(mon)

                img = Image.frombytes("RGB", screenshot.size, screenshot.bgra, "raw", "BGRX")  # Convert to PIL.Image
                while(True):
                    try:
                        otherplayerX,otherplayerY = pyautogui.locateCenterOnScreen("C:/Users/Alec/Desktop/Maplestoryscript/positionbot/player.png", confidence=0.9)
                        print(otherplayerX,otherplayerY)
                    except TypeError:
                        print("no other player")
                        pass



    except TypeError:
        print("not found")
        pass


def tanjirotboytrain1():
    while(True):
        PressKey(0xCD)#right
        time.sleep(0.1)
      #  ReleaseKey(0xCD)
        for x in range(7):
            PressKey(0x11)#w
            time.sleep(0.1)
            ReleaseKey(0x11)
            time.sleep(0.3)
            
        PressKey(0x13)#r
        time.sleep(0.1)
        ReleaseKey(0x13)


        for x in range(5):
            PressKey(0x11)#w
            time.sleep(0.1)
            ReleaseKey(0x11)
            time.sleep(0.3)

        ReleaseKey(0xCD)

        time.sleep(0.3)

        PressKey(0xCB)#left
        time.sleep(0.1)
      #  ReleaseKey(0xCB)
        for y in range(10):
            PressKey(0x11)#w
            time.sleep(0.1)
            ReleaseKey(0x11)
            time.sleep(0.3)


        ReleaseKey(0xCB)

        time.sleep(0.3)
        '''
        PressKey(0x03)#2 POT
        time.sleep(0.1)
        ReleaseKey(0x03)
        '''



def tanjiro_bittybobforest1():
    while(True):
        PressKey(0xCD)#right
        time.sleep(0.1)
      #  ReleaseKey(0xCD)
        for x in range(11):
            PressKey(0x11)#w
            time.sleep(0.1)
            ReleaseKey(0x11)
            time.sleep(0.3)

        ReleaseKey(0xCD)

        time.sleep(0.1)

        PressKey(0xC8)#up
        PressKey(0xCB)#left
        time.sleep(0.1)

        PressKey(0x12)#e
        time.sleep(0.1)
        ReleaseKey(0x12)
        time.sleep(0.1)
        PressKey(0x12)#e
        time.sleep(0.1)
        ReleaseKey(0x12)
        time.sleep(0.1)
        PressKey(0x12)#e
        time.sleep(0.1)
        ReleaseKey(0x12)
        time.sleep(0.1)
        PressKey(0x12)#e
        time.sleep(0.1)
        ReleaseKey(0x12)
        time.sleep(0.1)
        PressKey(0x12)#e
        time.sleep(0.1)
        ReleaseKey(0x12)
        time.sleep(0.1)
        PressKey(0x12)#e
        time.sleep(0.1)
        ReleaseKey(0x12)
        time.sleep(0.1)

        ReleaseKey(0xC8)#up
        ReleaseKey(0xCB)#left

        PressKey(0xCB)#left
        time.sleep(0.1)
      #  ReleaseKey(0xCB)
        for y in range(8):
            PressKey(0x11)#w
            time.sleep(0.1)
            ReleaseKey(0x11)
            time.sleep(0.3)

        ReleaseKey(0xCB)

        time.sleep(0.3)

        jumpdown()

        time.sleep(1)
        '''
        PressKey(0x03)#2 POT
        time.sleep(0.1)
        ReleaseKey(0x03)
        '''

def tanjiro_yumyum():
    while(True):
        PressKey(0xCD)#right
        time.sleep(0.1)
        ReleaseKey(0xCD)
        for x in range(7):
            PressKey(0x11)#w
            time.sleep(0.1)
            ReleaseKey(0x11)
            time.sleep(0.3)

      #  ReleaseKey(0xCD)


        time.sleep(0.3)

        PressKey(0xCB)#left
        time.sleep(0.1)
        ReleaseKey(0xCB)
        for y in range(7):
            PressKey(0x11)#w
            time.sleep(0.1)
            ReleaseKey(0x11)
            time.sleep(0.3)

      #  ReleaseKey(0xCB)


        time.sleep(0.3)

        '''
        PressKey(0x03)#2 POT
        time.sleep(0.1)
        ReleaseKey(0x03)
        '''


def tanjiro_bft2():
    while(True):
        PressKey(0xCD)#right
        time.sleep(0.1)
        ReleaseKey(0xCD)
        for x in range(11):
            PressKey(0x11)#w
            time.sleep(0.1)
            ReleaseKey(0x11)
            time.sleep(0.3)

      #  ReleaseKey(0xCD)



        time.sleep(0.3)

        PressKey(0xCB)#left
        time.sleep(0.1)
        ReleaseKey(0xCB)
        for y in range(11):
            PressKey(0x11)#w
            time.sleep(0.1)
            ReleaseKey(0x11)
            time.sleep(0.3)

      #  ReleaseKey(0xCB)


        time.sleep(0.3)

        '''
        PressKey(0x03)#2 POT
        time.sleep(0.1)
        ReleaseKey(0x03)
        '''

def shangri_la_bloomingspring4_test():
    count = 0
    sixthjobcounter = 0
    infinity_counter = 0
    while(True):
        if(count == 16):
            time.sleep(1)
            if(infinity_counter == 0):
                PressKey(0x02)#1 infinity
                time.sleep(0.1)
                ReleaseKey(0x02)
                time.sleep(1.5)
            if(infinity_counter == 2):
                PressKey(0xD1)#pgdn infinity
                time.sleep(0.1)
                ReleaseKey(0xD1)
                time.sleep(2)
                infinity_counter = -2


            jumpupattackupTP()
            time.sleep(0.3)


            jumpupattackdownTP()
            time.sleep(0.3)
            PressKey(0x09)#8 will
            time.sleep(0.1)
            ReleaseKey(0x09)
            time.sleep(0.5)
            attackteleleft()
            time.sleep(0.3)
            attackteleleft()
            time.sleep(0.3)
            attackdowntp()
            time.sleep(0.3)

            PressKey(0xCD)#right
            for y in range(6):
                generaljumptpR()
            ReleaseKey(0xCD)

            time.sleep(0.3)

            #jumpdown()
            checkjumpdown()

            #time.sleep(1.5)

            PressKey(0x13)#r
            time.sleep(0.1)
            ReleaseKey(0x13)
            time.sleep(0.8)


            PressKey(0xC8)#Up for portal
            time.sleep(0.1)
            ReleaseKey(0xC8)

            time.sleep(0.3)

            attackuptp()
            time.sleep(0.3)
            attackteleleft()
            time.sleep(0.3)
            attackdowntp()
            time.sleep(0.3)
            
            PressKey(0x20)#D (sol janus)
            time.sleep(0.1)
            ReleaseKey(0x20)
            time.sleep(0.3)

            attackdowntp()
            time.sleep(0.3)
            '''
            setfountain()
            time.sleep(0.5)

            '''

            attackdowntp()
            time.sleep(0.3)

            PressKey(0x20)#D (sol janus)
            time.sleep(0.1)
            ReleaseKey(0x20)
            time.sleep(0.5)


            checkjumpdown()
            #jumpdown()

            #time.sleep(1.5)


            attackdowntp()
            time.sleep(0.3)

            attackteleright()
            time.sleep(0.3)


            PressKey(0x20)#D (sol janus)
            time.sleep(0.1)
            ReleaseKey(0x20)
            time.sleep(0.5)


            attackteleright()
            time.sleep(0.3)
            attackteleright()
            time.sleep(0.3)

            PressKey(0x21)#F door
            time.sleep(0.1)
            ReleaseKey(0x21)
            time.sleep(0.3)


            attackteleright()
            time.sleep(0.3)
            attackteleright()
            time.sleep(0.3)


            seterdashower()
            time.sleep(0.5)

            attackuptp()
            time.sleep(0.3)

            setfountain()
            time.sleep(0.5)
            '''
            PressKey(0x20)#D (sol janus)
            time.sleep(0.1)
            ReleaseKey(0x20)
            time.sleep(0.3)
            '''
            attackteleleft()
            time.sleep(1.5)

            attackuptp()
            time.sleep(0.3)

            attackteleright()
            time.sleep(0.3)
            attackteleright()
            time.sleep(0.3)

            attackdowntp()
            time.sleep(0.3)
            attackdowntp()
            time.sleep(1)

            attackteleleft()
            time.sleep(0.3)

            if(sixthjobcounter == 7):
                PressKey(0x29)#'`' grave symbol
                time.sleep(0.1)
                ReleaseKey(0x29)
                time.sleep(5)
                sixthjobcounter = 0


            attackteleleft()
            time.sleep(0.3)
            attackteleleft()
            time.sleep(0.3)
            attackteleleft()
            time.sleep(0.3)





            PressKey(0x3D)#f3
            time.sleep(0.1)
            ReleaseKey(0x3D)
            PressKey(0x3D)#f3
            time.sleep(0.1)
            ReleaseKey(0x3D)
            PressKey(0x3D)#f3
            time.sleep(0.1)
            ReleaseKey(0x3D)
            time.sleep(0.1)

            
            sixthjobcounter = sixthjobcounter + 1
            infinity_counter = infinity_counter + 1
            count = 0

            movetorune()
   

        PressKey(0x13)#r
        time.sleep(0.1)
        ReleaseKey(0x13)
        time.sleep(0.1)

        PressKey(0x05)#4 bene
        time.sleep(0.1)
        ReleaseKey(0x05)
        time.sleep(0.1)

        PressKey(0x41)#-
        time.sleep(0.1)
        ReleaseKey(0x41)
        time.sleep(0.1)

        PressKey(0x06)#5 angel
        time.sleep(0.1)
        ReleaseKey(0x06)


        PressKey(0x11)#w
        time.sleep(0.1)
        ReleaseKey(0x11)
        time.sleep(0.1)



        print(count)
        count = count + 1


def checkrightplatcarcion():
    '''
    while(True):
        try:
            x1,y1 = pyautogui.locateCenterOnScreen("C:/Users/Alec/Desktop/Maplestoryscript/trackplayer/player.PNG", confidence = 0.9)
            print(x1,y1)

            if(x1 == 220) and (y1 == 148):
                break
            elif(y1 == 169):
                attackteleleft()
                time.sleep(0.3)
                attackuptp()
                time.sleep(0.3)
            else:
                attackteleright()
                time.sleep(0.3)
            #(220 148) right platform
            #(x,169) bottom lane

        except TypeError:
            print('cant see')
            attackteleleft()
            time.sleep(0.3)
            attackuptp()
            time.sleep(0.3)
            pass
    '''
    # Load template once
    template = cv2.imread("C:/Users/Alec/Desktop/Maplestoryscript/trackplayer/player.PNG", cv2.IMREAD_GRAYSCALE)
    w, h = template.shape[::-1]

    with mss.mss() as sct:
        monitor = sct.monitors[1]  # Use monitor 1 (change if multi-monitor)

    while True:
        # Capture screen
        screenshot = sct.grab(monitor)
        img = np.array(screenshot)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Match template
        result = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)

        # Debug info
        print(f"Match confidence: {max_val:.4f}")

        if max_val >= 0.90:
            center_x = max_loc[0] + w // 2
            center_y = max_loc[1] + h // 2
            print(f"Match found at: {center_x}, {center_y}")

            if center_x == 220 and center_y == 148:
                break
            elif center_y == 169:
                attackteleleft()
                time.sleep(0.3)
                attackuptp()
                time.sleep(0.3)
            else:
                attackteleright()
                time.sleep(0.3)

        else:
            print("Can't see player - defaulting to left attack")
            attackteleleft()
            time.sleep(0.3)
            attackuptp()
            time.sleep(0.3)


def sunkenruins4():
    count = 50
    sixthjobcounter = 0
    infinity_counter = 0
    while(True):
        if(count == 50):
            time.sleep(1)
            if(infinity_counter == 0):
                PressKey(0x02)#1 infinity
                time.sleep(0.1)
                ReleaseKey(0x02)
                time.sleep(1.5)
            if(infinity_counter == 2):
                PressKey(0xD1)#pgdn infinity
                time.sleep(0.1)
                ReleaseKey(0xD1)
                time.sleep(2)
                infinity_counter = -2

            PressKey(0x09)#8 will
            time.sleep(0.1)
            ReleaseKey(0x09)
            time.sleep(0.5)

            attackteleright()
            time.sleep(0.3)
            attackteleright()
            time.sleep(0.3)


            attackteleright()
            time.sleep(0.3)

            attackteleright()
            time.sleep(0.3)

            attackteleright()
            time.sleep(0.3)

            attackteleright()
            time.sleep(0.3)

            attackteleright()
            time.sleep(0.3)

            checkrightplatcarcion()

            attackteleleft()
            time.sleep(0.3)

            PressKey(0x20)#D (sol janus)
            time.sleep(0.1)
            ReleaseKey(0x20)
            time.sleep(0.5)

            attackteleleft()
            time.sleep(0.3)

            attackteleleft()
            time.sleep(0.3)

            PressKey(0x20)#D (sol janus)
            time.sleep(0.1)
            ReleaseKey(0x20)
            time.sleep(0.5)

            attackteleleft()
            time.sleep(0.3)

            attackteleleft()
            time.sleep(0.3)

            if(sixthjobcounter == 7):
                PressKey(0x29)#'`' grave symbol
                time.sleep(0.1)
                ReleaseKey(0x29)
                time.sleep(5)
                sixthjobcounter = 0

            PressKey(0x20)#D (sol janus)
            time.sleep(0.1)
            ReleaseKey(0x20)
            time.sleep(0.5)

            attackteleleft()
            time.sleep(0.3)

            attackteleleft()
            time.sleep(0.3)

            setfountain()
            time.sleep(0.5)

            PressKey(0x21)#F door
            time.sleep(0.1)
            ReleaseKey(0x21)
            time.sleep(0.3)

            attackteleleft()
            time.sleep(0.3)

            seterdashower()
            time.sleep(0.5)


            sixthjobcounter = sixthjobcounter + 1
            infinity_counter = infinity_counter + 1
            count = 0



        PressKey(0x05)#4 bene
        time.sleep(0.1)
        ReleaseKey(0x05)
        time.sleep(0.1)

        PressKey(0x41)#-
        time.sleep(0.1)
        ReleaseKey(0x41)
        time.sleep(0.1)

        PressKey(0x06)#5 angel
        time.sleep(0.1)
        ReleaseKey(0x06)
        time.sleep(0.1)

        PressKey(0x11)#w
        time.sleep(0.1)
        ReleaseKey(0x11)
        time.sleep(0.1)



        print(count)
        count = count + 1


    




def artaleposition():
    from mss import mss
    mon = {'top': 50, 'left': 0, 'width': 370, 'height': 200}
    region = (0, 50, 370, 200) #(left, top, width, height)
    print(mon)
    while(True):
        try:
            x1,y1 = pyautogui.locateCenterOnScreen("C:/Users/Alec/Desktop/Maplestoryscript/artale/player.PNG", confidence = 0.6, region=region)
           # x2,y2 = pyautogui.locateCenterOnScreen("C:/Users/Alec/Desktop/Maplestoryscript/positionbot/minimap_bottomright.PNG", confidence=0.8)
            print(x1,y1)
        except TypeError:
            print('cant see')
            pass

def artalehp():
    while(True):
        try:
            x1,y1 = pyautogui.locateCenterOnScreen("C:/Users/Alec/Desktop/Maplestoryscript/artale/hp.PNG", confidence = 0.8)
           # x2,y2 = pyautogui.locateCenterOnScreen("C:/Users/Alec/Desktop/Maplestoryscript/positionbot/minimap_bottomright.PNG", confidence=0.8)

        except TypeError:
            print('cant see')
            PressKey(0x03)#2
            time.sleep(0.1)
            ReleaseKey(0x03)
            time.sleep(0.1)
            pass

def artale():
    from mss import mss
    mon = {'top': 50, 'left': 0, 'width': 370, 'height': 200}
    region = (0, 50, 370, 200) #(left, top, width, height)
    print(mon)
    skillcount=0
        
    with mss() as mss_instance:
        screenshot = mss_instance.grab(mon)
        img = Image.frombytes("RGB", screenshot.size, screenshot.bgra, "raw", "BGRX")  # Convert to PIL.Image
      #  img.show()
    while(True):
        while(True):
            try:
                x1,y1 = pyautogui.locateCenterOnScreen("C:/Users/Alec/Desktop/Maplestoryscript/artale/player.PNG", confidence = 0.6, region=region)
               # x2,y2 = pyautogui.locateCenterOnScreen("C:/Users/Alec/Desktop/Maplestoryscript/positionbot/minimap_bottomright.PNG", confidence=0.8)
                print(x1,y1)
                if(x1>=0) and (x1<=268):
                    PressKey(0xCD)#right
                    time.sleep(0.1)
                    PressKey(0x39)#jump
                    time.sleep(0.1)
                    ReleaseKey(0x39)
                    PressKey(0x10)#q
                    time.sleep(0.1)
                    ReleaseKey(0x10)
                    time.sleep(0.6)
                    ReleaseKey(0xCD)
                    skillcount= skillcount + 1
                    if(skillcount == 6):
                        PressKey(0x05)#4
                        time.sleep(0.1)
                        ReleaseKey(0x05)
                        time.sleep(0.1)
                        skillcount = 0
                else:
                    break



            except TypeError:
                PressKey(0xCD)#right
                time.sleep(0.1)
                PressKey(0x39)#jump
                time.sleep(0.1)
                ReleaseKey(0x39)
                PressKey(0x10)#q
                time.sleep(0.1)
                ReleaseKey(0x10)
                time.sleep(0.6)
                ReleaseKey(0xCD)
                skillcount= skillcount + 1
                if(skillcount == 6):
                    PressKey(0x05)#4
                    time.sleep(0.1)
                    ReleaseKey(0x05)
                    time.sleep(0.1)
                    skillcount = 0
                pass

        time.sleep(0.1)
        PressKey(0xCB)#left
        time.sleep(0.1)
        PressKey(0x39)#jump
        time.sleep(0.1)
        ReleaseKey(0x39)
        PressKey(0x10)#q
        time.sleep(0.1)
        ReleaseKey(0x10)
        time.sleep(0.6)
        ReleaseKey(0xCB)

        print('transition right to rope')
        while(True):
            try:
                x1,y1 = pyautogui.locateCenterOnScreen("C:/Users/Alec/Desktop/Maplestoryscript/artale/player.PNG", confidence = 0.6, region=region)
               # x2,y2 = pyautogui.locateCenterOnScreen("C:/Users/Alec/Desktop/Maplestoryscript/positionbot/minimap_bottomright.PNG", confidence=0.8)
                print(x1,y1)
                if(x1>=259) and (x1<=261):
                    PressKey(0x39)#jump
                    time.sleep(0.1)
                    ReleaseKey(0x39)
                    PressKey(0xC8)#up
                    time.sleep(1)
                    ReleaseKey(0xC8)
                    break
                elif(x1>=262):
                    PressKey(0xCB)#left
                    time.sleep(0.2)
                    ReleaseKey(0xCB)
                    time.sleep(0.1)
                elif(x1<=258):
                    PressKey(0xCD)#right
                    time.sleep(0.2)
                    ReleaseKey(0xCD)
                    time.sleep(0.1)

            except TypeError:
                print('rope error')
                PressKey(0xCB)#left
                time.sleep(0.1)
                ReleaseKey(0xCB)
                time.sleep(0.1)
                pass

        while(True):
            try:
                x1,y1 = pyautogui.locateCenterOnScreen("C:/Users/Alec/Desktop/Maplestoryscript/artale/player.PNG", confidence = 0.6, region=region)
               # x2,y2 = pyautogui.locateCenterOnScreen("C:/Users/Alec/Desktop/Maplestoryscript/positionbot/minimap_bottomright.PNG", confidence=0.8)
                print(x1,y1)
                if(x1>=100) and (x1<=330):
                    PressKey(0xCB)#left
                    time.sleep(0.1)
                    PressKey(0x39)#jump
                    time.sleep(0.1)
                    ReleaseKey(0x39)
                    PressKey(0x10)#q
                    time.sleep(0.1)
                    ReleaseKey(0x10)
                    time.sleep(0.6)
                    ReleaseKey(0xCB)
                    skillcount= skillcount + 1
                    if(skillcount == 6):
                        PressKey(0x05)#4
                        time.sleep(0.1)
                        ReleaseKey(0x05)
                        time.sleep(0.1)
                        skillcount = 0
                else:
                    break



            except TypeError:
                PressKey(0xCB)#left
                time.sleep(0.1)
                PressKey(0x39)#jump
                time.sleep(0.1)
                ReleaseKey(0x39)
                PressKey(0x10)#q
                time.sleep(0.1)
                ReleaseKey(0x10)
                time.sleep(0.6)
                ReleaseKey(0xCB)
                skillcount= skillcount + 1
                if(skillcount == 10):
                    PressKey(0x05)#4
                    time.sleep(0.1)
                    ReleaseKey(0x05)
                    time.sleep(0.1)
                    skillcount = 0
                pass


    #(268,y) right side
    #(142,y) left side



def artale_mage():
    from mss import mss
    mon = {'top': 50, 'left': 0, 'width': 370, 'height': 200}
    region = (0, 50, 370, 200) #(left, top, width, height)
    print(mon)
    skillcount=0
        
    with mss() as mss_instance:
        screenshot = mss_instance.grab(mon)
        img = Image.frombytes("RGB", screenshot.size, screenshot.bgra, "raw", "BGRX")  # Convert to PIL.Image
      #  img.show()
    while(True):
        while(True):
            try:
                x1,y1 = pyautogui.locateCenterOnScreen("C:/Users/Alec/Desktop/Maplestoryscript/artale/player.PNG", confidence = 0.6, region=region)
               # x2,y2 = pyautogui.locateCenterOnScreen("C:/Users/Alec/Desktop/Maplestoryscript/positionbot/minimap_bottomright.PNG", confidence=0.8)
                print(x1,y1)
                if(x1>=0) and (x1<=268):
                    PressKey(0x10)#q
                    time.sleep(0.1)
                    ReleaseKey(0x10)
                    PressKey(0x10)#q
                    time.sleep(0.1)
                    ReleaseKey(0x10)
                    time.sleep(0.6) 
                    PressKey(0xCD)#right
                    time.sleep(0.7)
                    ReleaseKey(0xCD)
                    skillcount= skillcount + 1
                    if(skillcount == 6):
                        PressKey(0x05)#4
                        time.sleep(0.1)
                        ReleaseKey(0x05)
                        skillcount = 0
                else:
                    break



            except TypeError:
                PressKey(0x10)#q
                time.sleep(0.1)
                ReleaseKey(0x10)
                PressKey(0x10)#q
                time.sleep(0.1)
                ReleaseKey(0x10)
                time.sleep(0.6) 
                PressKey(0xCD)#right
                time.sleep(0.7)
                ReleaseKey(0xCD)
                skillcount = skillcount + 1
                if(skillcount == 6):
                    PressKey(0x05)#4
                    time.sleep(0.1)
                    ReleaseKey(0x05)
                    skillcount = 0
                pass

        PressKey(0x10)#q
        time.sleep(0.1)
        ReleaseKey(0x10)
        PressKey(0x10)#q
        time.sleep(0.1)
        ReleaseKey(0x10)
        time.sleep(0.6) 
        PressKey(0xCB)#left
        time.sleep(0.7)
        PressKey(0x10)#q
        time.sleep(0.1)
        ReleaseKey(0x10)
        PressKey(0x10)#q
        time.sleep(0.1)
        ReleaseKey(0x10)


        '''
        PressKey(0xCB)#left
        time.sleep(0.1)
        PressKey(0x10)#q
        time.sleep(0.1)
        ReleaseKey(0x10)
        time.sleep(0.6)
        PressKey(0x39)#jump
        time.sleep(0.1)
        ReleaseKey(0x39)
        time.sleep(0.6)
        time.sleep(0.6)
        ReleaseKey(0xCB)
        '''

        print('transition right to rope')
        while(True):
            try:
                x1,y1 = pyautogui.locateCenterOnScreen("C:/Users/Alec/Desktop/Maplestoryscript/artale/player.PNG", confidence = 0.6, region=region)
               # x2,y2 = pyautogui.locateCenterOnScreen("C:/Users/Alec/Desktop/Maplestoryscript/positionbot/minimap_bottomright.PNG", confidence=0.8)
                print(x1,y1)
                if(x1>=220) and (x1<=262):

                    PressKey(0xC8)#up arrow
                    time.sleep(0.1)

                    PressKey(0x2A)#left shift
                    time.sleep(0.1)
                    ReleaseKey(0x2A)

                    ReleaseKey(0xC8)
                    time.sleep(0.1)

                    PressKey(0xCB)#left
                    time.sleep(0.1)
                    ReleaseKey(0xCB)

                    time.sleep(0.1)

                    PressKey(0x10)#q
                    time.sleep(0.1)
                    ReleaseKey(0x10)
                    PressKey(0x10)#q
                    time.sleep(0.1)
                    ReleaseKey(0x10)
                    time.sleep(0.62)
                    PressKey(0x10)#q
                    time.sleep(0.1)
                    ReleaseKey(0x10)
                    PressKey(0x10)#q
                    time.sleep(0.1)
                    ReleaseKey(0x10)
                    time.sleep(0.6) 
                    break
                elif(x1>=263):
                    PressKey(0xCB)#left
                    time.sleep(0.1)

                    PressKey(0x2A)#left shift
                    time.sleep(0.1)
                    ReleaseKey(0x2A)

                    ReleaseKey(0xCB)
                    time.sleep(0.5)
            except TypeError:
                print('rope error')
                PressKey(0xCB)#left
                time.sleep(0.1)
                ReleaseKey(0xCB)
                time.sleep(0.1)
                pass



        while(True):
            try:
                x1,y1 = pyautogui.locateCenterOnScreen("C:/Users/Alec/Desktop/Maplestoryscript/artale/player.PNG", confidence = 0.6, region=region)
               # x2,y2 = pyautogui.locateCenterOnScreen("C:/Users/Alec/Desktop/Maplestoryscript/positionbot/minimap_bottomright.PNG", confidence=0.8)
                print(x1,y1)
                if(x1>=100) and (x1<=330):
                    PressKey(0x10)#q
                    time.sleep(0.1)
                    ReleaseKey(0x10)
                    PressKey(0x10)#q
                    time.sleep(0.1)
                    ReleaseKey(0x10)
                    time.sleep(0.6) 
                    PressKey(0xCB)#left
                    time.sleep(0.7)
                    ReleaseKey(0xCB) 
                    skillcount = skillcount + 1
                    if(skillcount == 6):
                        PressKey(0x05)#4
                        time.sleep(0.1)
                        ReleaseKey(0x05)
                        skillcount = 0
                else:
                    break



            except TypeError:
                PressKey(0x10)#q
                time.sleep(0.1)
                ReleaseKey(0x10)
                PressKey(0x10)#q
                time.sleep(0.1)
                ReleaseKey(0x10)
                time.sleep(0.6)
                PressKey(0xCB)#left
                time.sleep(0.7)
                ReleaseKey(0xCB) 
                skillcount= skillcount + 1
                if(skillcount == 6):
                    PressKey(0x05)#4
                    time.sleep(0.1)
                    ReleaseKey(0x05)
                    skillcount = 0
                    pass


    #(268,y) right side
    #(142,y) left side

def artale_combined():
    thread1 = threading.Thread(target=artale)
    thread1.daemon = True
    thread1.start()

    thread2 = threading.Thread(target=artalehp)
    thread2.daemon = True
    thread2.start()

    while(True):
        thread1.join(1)
        thread2.join(1)
        if not thread1.is_alive() and thread2.is_alive():
            os._exit(0)

def artale_combined_mage():
    thread1 = threading.Thread(target=artale_mage)
    thread1.daemon = True
    thread1.start()

    thread2 = threading.Thread(target=artalehp)
    thread2.daemon = True
    thread2.start()

    while(True):
        thread1.join(1)
        thread2.join(1)
        if not thread1.is_alive() and thread2.is_alive():
            os._exit(0)




def leftandrightspam():
    while(True):
        PressKey(0xCB)#left
        time.sleep(0.1)
        ReleaseKey(0xCB)
        PressKey(0xCD)#right
        time.sleep(0.1)
        ReleaseKey(0xCD)


def calibrate_map():
    from mss import mss
    mon = {'top': 100, 'left': 30, 'width': 260, 'height': 200}
    region = (30, 100, 260, 200) #(left, top, width, height)
    print(mon)
    skillcount=0
        
    with mss() as mss_instance:
        screenshot = mss_instance.grab(mon)
        img = Image.frombytes("RGB", screenshot.size, screenshot.bgra, "raw", "BGRX")  # Convert to PIL.Image
        img.show()


def artaleposition_lupin():
    region = (30, 100, 260, 200) #(left, top, width, height)
    while(True):
        try:
            x1,y1 = pyautogui.locateCenterOnScreen("C:/Users/Alec/Desktop/Maplestoryscript/artale/player.PNG", confidence = 0.6, region=region)
           # x2,y2 = pyautogui.locateCenterOnScreen("C:/Users/Alec/Desktop/Maplestoryscript/positionbot/minimap_bottomright.PNG", confidence=0.8)
            print(x1,y1)
        except TypeError:
            print('cant see')
            pass


def zombie_lupin():
    from mss import mss
    region = (30, 100, 260, 200) #(left, top, width, height)
    skillcount=0
    previous_position_x = 0
    previous_position_y = 0 
    #top right platform
    for_loop_counter = 0
    while(True):
        while(True):
            try:
                x1, y1 = pyautogui.locateCenterOnScreen("C:/Users/Alec/Desktop/Maplestoryscript/artale/player.PNG", confidence = 0.6, region=region)
                previous_position_x = x1
                previous_position_y = y1
                print(x1,y1)
                if(y1 == 150) and (x1 <= 212):
                    PressKey(0xCD)#right
                    PressKey(0x12)#e
                    time.sleep(0.1)
                    ReleaseKey(0x12)
                    time.sleep(0.6)
                    PressKey(0x39)#space
                    time.sleep(0.1)
                    ReleaseKey(0x39)
                    ReleaseKey(0xCD)
                    for_loop_counter = for_loop_counter + 1
                elif(y1==150) and (x1 > 212) and (x1 <= 234):
                    PressKey(0x12)#e
                    time.sleep(0.1)
                    ReleaseKey(0x12)
                    time.sleep(0.6)
                    for_loop_counter = for_loop_counter + 1
                elif(y1==150) and (x1 > 234):
                    PressKey(0xCB)#left
                    PressKey(0x12)#e
                    time.sleep(0.1)
                    ReleaseKey(0x12)
                    time.sleep(0.6)
                    PressKey(0x39)#space
                    time.sleep(0.1)
                    ReleaseKey(0x39)
                    ReleaseKey(0xCB)
                    for_loop_counter = for_loop_counter + 1
                elif(y1 <=165) and (y1 >= 157):
                    break
                print(for_loop_counter)
                if(for_loop_counter == 10):
                    for_loop_counter = 0
                    break
                print("no more for loop")


            except TypeError:
                print("cant see")
                if(previous_position_y == 150) and (previous_position_x <= 212):
                    PressKey(0xCD)#right
                    PressKey(0x12)#e
                    time.sleep(0.1)
                    ReleaseKey(0x12)
                    time.sleep(0.6)
                    PressKey(0x39)#space
                    time.sleep(0.1)
                    ReleaseKey(0x39)
                    ReleaseKey(0xCD)
                    for_loop_counter = for_loop_counter + 1
                elif(previous_position_y==150) and (previous_position_x > 212) and (previous_position_x <= 234):
                    PressKey(0x12)#e
                    time.sleep(0.1)
                    ReleaseKey(0x12)
                    time.sleep(0.6)
                    for_loop_counter = for_loop_counter + 1
                elif(previous_position_y==150) and (previous_position_x > 234):
                    PressKey(0xCB)#left
                    PressKey(0x12)#e
                    time.sleep(0.1)
                    ReleaseKey(0x12)
                    time.sleep(0.6)
                    PressKey(0x39)#space
                    time.sleep(0.1)
                    ReleaseKey(0x39)
                    ReleaseKey(0xCB)
                    for_loop_counter = for_loop_counter + 1
                elif(y1 <=165) and (y1 >= 157):
                    break
                print(for_loop_counter)
                if(for_loop_counter == 10):
                    for_loop_counter = 0
                    break
                print("no more for loop")
                pass

        print("transition to second platform")
        PressKey(0xCB)#left
        PressKey(0xC8)#up
        time.sleep(0.1)
        while(True):
            try:
                x1, y1 = pyautogui.locateCenterOnScreen("C:/Users/Alec/Desktop/Maplestoryscript/artale/player.PNG", confidence = 0.6, region=region)
                print(x1,y1)
                previous_position_y = y1
                if(y1 < 150) and (x1 == 202):
                    print("on rope jump off")
                    break
                elif(y1 <=165) and (y1 >= 157):
                    break
            except TypeError:
                print("not on rope yet")
                if(y1 < 150) and (x1 == 202):
                    print("on rope jump off")
                    break
                elif(y1 <=165) and (y1 >= 157):
                    break
                pass
        ReleaseKey(0xC8)
        time.sleep(0.1)
        PressKey(0x39)#space
        time.sleep(0.1)
        ReleaseKey(0x39)
        ReleaseKey(0xCB)


        #second platform
        while(True):
            try:
                x1, y1 = pyautogui.locateCenterOnScreen("C:/Users/Alec/Desktop/Maplestoryscript/artale/player.PNG", confidence = 0.6, region=region)
                previous_position_x = x1
                previous_position_y = y1
                print(x1,y1)
                #(x,165) -> (x,157)
                if(y1 <=165) and (y1 >= 157) and (x1 >= 192):
                    PressKey(0xCB)#left
                    PressKey(0x12)#e
                    time.sleep(0.1)
                    ReleaseKey(0x12)
                    time.sleep(0.6)
                    PressKey(0x39)#space
                    time.sleep(0.1)
                    ReleaseKey(0x39)
                    ReleaseKey(0xCB)
                    for_loop_counter = for_loop_counter + 1
                elif(y1 <=165) and (y1 >= 157) and (x1 < 192) and (x1 >= 168):
                    PressKey(0x12)#e
                    time.sleep(0.1)
                    ReleaseKey(0x12)
                    time.sleep(0.6)
                    for_loop_counter = for_loop_counter + 1
                elif(y1 <=165) and (y1 >= 157) and (x1 < 168):
                    PressKey(0xCD)#right
                    PressKey(0x12)#e
                    time.sleep(0.1)
                    ReleaseKey(0x12)
                    time.sleep(0.6)
                    PressKey(0x39)#space
                    time.sleep(0.1)
                    ReleaseKey(0x39)
                    ReleaseKey(0xCD)
                    for_loop_counter = for_loop_counter + 1
                elif(y1 ==179):
                    break
                print(for_loop_counter)
                if(for_loop_counter == 10):
                    for_loop_counter = 0
                    break
                print("no more for loop")


            except TypeError:
                print("cant see")
                            #(x,165) -> (x,157)
                if(previous_position_y <=165) and (previous_position_y >= 157) and (previous_position_x >= 192):
                    PressKey(0xCB)#left
                    PressKey(0x12)#e
                    time.sleep(0.1)
                    ReleaseKey(0x12)
                    time.sleep(0.6)
                    PressKey(0x39)#space
                    time.sleep(0.1)
                    ReleaseKey(0x39)
                    ReleaseKey(0xCB)
                    for_loop_counter = for_loop_counter + 1
                elif(previous_position_y <=165) and (previous_position_y >= 157) and (previous_position_x < 192) and (previous_position_x >= 168):
                    PressKey(0x12)#e
                    time.sleep(0.1)
                    ReleaseKey(0x12)
                    time.sleep(0.6)
                    for_loop_counter = for_loop_counter + 1
                elif(previous_position_y <=165) and (previous_position_y >= 157) and (previous_position_x < 168):
                    PressKey(0xCD)#right
                    PressKey(0x12)#e
                    time.sleep(0.1)
                    ReleaseKey(0x12)
                    time.sleep(0.6)
                    PressKey(0x39)#space
                    time.sleep(0.1)
                    ReleaseKey(0x39)
                    ReleaseKey(0xCD)
                    for_loop_counter = for_loop_counter + 1
                elif(y1 ==179):
                    break
                print(for_loop_counter)
                if(for_loop_counter == 10):
                    for_loop_counter = 0
                    break
                print("no more for loop")
                pass


        print("transition to third platform")
        PressKey(0xCD)#right
        PressKey(0xC8)#up
        time.sleep(0.1)
        while(True):
            try:
                x1, y1 = pyautogui.locateCenterOnScreen("C:/Users/Alec/Desktop/Maplestoryscript/artale/player.PNG", confidence = 0.6, region=region)
                print(x1,y1)
                if(y1 < 165) and (x1 == 202):
                    print("on rope jump off")
                    break
                elif(y1 ==179):
                    break
            except TypeError:
                print("not on rope yet")
                if(y1 < 165) and (x1 == 202):
                    print("on rope jump off")
                    break
                elif(y1 ==179):
                    break
                pass
        ReleaseKey(0xC8)
        time.sleep(0.1)
        PressKey(0x39)#space
        time.sleep(0.1)
        ReleaseKey(0x39)
        ReleaseKey(0xCD)

        #third platform
        while(True):
            try:
                x1, y1 = pyautogui.locateCenterOnScreen("C:/Users/Alec/Desktop/Maplestoryscript/artale/player.PNG", confidence = 0.6, region=region)
                previous_position_x = x1
                previous_position_y = y1
                print(x1,y1)
                if(y1 == 179) and (x1 <= 212):
                    PressKey(0xCD)#right
                    PressKey(0x12)#e
                    time.sleep(0.1)
                    ReleaseKey(0x12)
                    time.sleep(0.6)
                    PressKey(0x39)#space
                    time.sleep(0.1)
                    ReleaseKey(0x39)
                    ReleaseKey(0xCD)
                    for_loop_counter = for_loop_counter + 1
                elif(y1==179) and (x1 > 212) and (x1 <= 234):
                    PressKey(0x12)#e
                    time.sleep(0.1)
                    ReleaseKey(0x12)
                    time.sleep(0.6)
                    for_loop_counter = for_loop_counter + 1
                elif(y1==179) and (x1 > 234):
                    PressKey(0xCB)#left
                    PressKey(0x12)#e
                    time.sleep(0.1)
                    ReleaseKey(0x12)
                    time.sleep(0.6)
                    PressKey(0x39)#space
                    time.sleep(0.1)
                    ReleaseKey(0x39)
                    ReleaseKey(0xCB)
                    for_loop_counter = for_loop_counter + 1
                elif(y1 ==185):
                    break
                print(for_loop_counter)
                if(for_loop_counter == 10):
                    for_loop_counter = 0
                    break
                print("no more for loop")


            except TypeError:
                print("cant see")
                if(previous_position_y == 179) and (previous_position_x <= 212):
                    PressKey(0xCD)#right
                    PressKey(0x12)#e
                    time.sleep(0.1)
                    ReleaseKey(0x12)
                    time.sleep(0.6)
                    PressKey(0x39)#space
                    time.sleep(0.1)
                    ReleaseKey(0x39)
                    ReleaseKey(0xCD)
                    for_loop_counter = for_loop_counter + 1
                elif(previous_position_y==179) and (previous_position_x > 212) and (previous_position_x <= 234):
                    PressKey(0x12)#e
                    time.sleep(0.1)
                    ReleaseKey(0x12)
                    time.sleep(0.6)
                    for_loop_counter = for_loop_counter + 1
                elif(previous_position_y==179) and (previous_position_x > 234):
                    PressKey(0xCB)#left
                    PressKey(0x12)#e
                    time.sleep(0.1)
                    ReleaseKey(0x12)
                    time.sleep(0.6)
                    PressKey(0x39)#space
                    time.sleep(0.1)
                    ReleaseKey(0x39)
                    ReleaseKey(0xCB)
                    for_loop_counter = for_loop_counter + 1
                elif(y1 ==185):
                    break
                print(for_loop_counter)
                if(for_loop_counter == 10):
                    for_loop_counter = 0
                    break
                print("no more for loop")
                pass

        print("transition to fourth platform")
        PressKey(0xCB)#left
        PressKey(0xC8)#up
        time.sleep(0.1)
        while(True):
            try:
                x1, y1 = pyautogui.locateCenterOnScreen("C:/Users/Alec/Desktop/Maplestoryscript/artale/player.PNG", confidence = 0.6, region=region)
                print(x1,y1)
                previous_position_y = y1
                if(y1 < 179) and (x1 == 202):
                    print("on rope jump off")
                    break
                elif(y1 ==185):
                    break
            except TypeError:
                print("not on rope yet")
                if(y1 < 179) and (x1 == 202):
                    print("on rope jump off")
                    break
                elif(y1 ==185):
                    break
                pass
        ReleaseKey(0xC8)
        time.sleep(0.1)
        PressKey(0x39)#space
        time.sleep(0.1)
        ReleaseKey(0x39)
        ReleaseKey(0xCB)

        #fourth platform
        while(True):
            try:
                x1, y1 = pyautogui.locateCenterOnScreen("C:/Users/Alec/Desktop/Maplestoryscript/artale/player.PNG", confidence = 0.6, region=region)
                previous_position_x = x1
                previous_position_y = y1
                print(x1,y1)
                #(x,165) -> (x,157)
                if(y1 == 185) and (x1 >= 192):
                    PressKey(0xCB)#left
                    PressKey(0x12)#e
                    time.sleep(0.1)
                    ReleaseKey(0x12)
                    time.sleep(0.6)
                    PressKey(0x39)#space
                    time.sleep(0.1)
                    ReleaseKey(0x39)
                    ReleaseKey(0xCB)
                    for_loop_counter = for_loop_counter + 1
                elif(y1 == 185) and (x1 < 192) and (x1 >= 168):
                    PressKey(0x12)#e
                    time.sleep(0.1)
                    ReleaseKey(0x12)
                    time.sleep(0.6)
                    for_loop_counter = for_loop_counter + 1
                elif(y1 == 185) and (x1 < 168):
                    PressKey(0xCD)#right
                    PressKey(0x12)#e
                    time.sleep(0.1)
                    ReleaseKey(0x12)
                    time.sleep(0.6)
                    PressKey(0x39)#space
                    time.sleep(0.1)
                    ReleaseKey(0x39)
                    ReleaseKey(0xCD)
                    for_loop_counter = for_loop_counter + 1
                elif(y1 ==200):
                    break
                print(for_loop_counter)
                if(for_loop_counter == 10):
                    for_loop_counter = 0
                    break
                print("no more for loop")


            except TypeError:
                print("cant see")
                            #(x,165) -> (x,157)
                if(previous_position_y == 185) and (previous_position_x >= 192):
                    PressKey(0xCB)#left
                    PressKey(0x12)#e
                    time.sleep(0.1)
                    ReleaseKey(0x12)
                    time.sleep(0.6)
                    PressKey(0x39)#space
                    time.sleep(0.1)
                    ReleaseKey(0x39)
                    ReleaseKey(0xCB)
                    for_loop_counter = for_loop_counter + 1
                elif(previous_position_y == 185) and (previous_position_x < 192) and (previous_position_x >= 168):
                    PressKey(0x12)#e
                    time.sleep(0.1)
                    ReleaseKey(0x12)
                    time.sleep(0.6)
                    for_loop_counter = for_loop_counter + 1
                elif(previous_position_y == 185) and (previous_position_x < 168):
                    PressKey(0xCD)#right
                    PressKey(0x12)#e
                    time.sleep(0.1)
                    ReleaseKey(0x12)
                    time.sleep(0.6)
                    PressKey(0x39)#space
                    time.sleep(0.1)
                    ReleaseKey(0x39)
                    ReleaseKey(0xCD)
                    for_loop_counter = for_loop_counter + 1
                elif(y1 ==200):
                    break
                print(for_loop_counter)
                if(for_loop_counter == 10):
                    for_loop_counter = 0
                    break
                print("no more for loop")
                pass

        print("transition to fifth platform")
        PressKey(0xCD)#right
        time.sleep(0.1)
        while(True):
            try:
                x1, y1 = pyautogui.locateCenterOnScreen("C:/Users/Alec/Desktop/Maplestoryscript/artale/player.PNG", confidence = 0.6, region=region)
                print(x1,y1)
                if(y1 == 200):
                    print("on rope jump off")
                    break
                elif(y1 ==200):
                    break
            except TypeError:
                print("not on rope yet")
                if(y1 == 200):
                    print("on rope jump off")
                    break
                elif(y1 ==200):
                    break
                pass
        time.sleep(0.1)
        ReleaseKey(0xCD)

        #fifth platform
        while(True):
            try:
                x1, y1 = pyautogui.locateCenterOnScreen("C:/Users/Alec/Desktop/Maplestoryscript/artale/player.PNG", confidence = 0.6, region=region)
                previous_position_x = x1
                previous_position_y = y1
                print(x1,y1)
                if(y1 == 200) and (x1 <= 212):
                    PressKey(0xCD)#right
                    PressKey(0x12)#e
                    time.sleep(0.1)
                    ReleaseKey(0x12)
                    time.sleep(0.6)
                    PressKey(0x39)#space
                    time.sleep(0.1)
                    ReleaseKey(0x39)
                    ReleaseKey(0xCD)
                    for_loop_counter = for_loop_counter + 1
                elif(y1==200) and (x1 > 212) and (x1 <= 234):
                    PressKey(0x12)#e
                    time.sleep(0.1)
                    ReleaseKey(0x12)
                    time.sleep(0.6)
                    for_loop_counter = for_loop_counter + 1
                elif(y1==200) and (x1 > 234):
                    PressKey(0xCB)#left
                    PressKey(0x12)#e
                    time.sleep(0.1)
                    ReleaseKey(0x12)
                    time.sleep(0.6)
                    PressKey(0x39)#space
                    time.sleep(0.1)
                    ReleaseKey(0x39)
                    ReleaseKey(0xCB)
                    for_loop_counter = for_loop_counter + 1
                elif(y1 ==229):
                    break
                print(for_loop_counter)
                if(for_loop_counter == 10):
                    for_loop_counter = 0
                    break
                print("no more for loop")


            except TypeError:
                print("cant see")
                if(previous_position_y == 200) and (previous_position_x <= 212):
                    PressKey(0xCD)#right
                    PressKey(0x12)#e
                    time.sleep(0.1)
                    ReleaseKey(0x12)
                    time.sleep(0.6)
                    PressKey(0x39)#space
                    time.sleep(0.1)
                    ReleaseKey(0x39)
                    ReleaseKey(0xCD)
                    for_loop_counter = for_loop_counter + 1
                elif(previous_position_y==200) and (previous_position_x > 212) and (previous_position_x <= 234):
                    PressKey(0x12)#e
                    time.sleep(0.1)
                    ReleaseKey(0x12)
                    time.sleep(0.6)
                    for_loop_counter = for_loop_counter + 1
                elif(previous_position_y==200) and (previous_position_x > 234):
                    PressKey(0xCB)#left
                    PressKey(0x12)#e
                    time.sleep(0.1)
                    ReleaseKey(0x12)
                    time.sleep(0.6)
                    PressKey(0x39)#space
                    time.sleep(0.1)
                    ReleaseKey(0x39)
                    ReleaseKey(0xCB)
                    for_loop_counter = for_loop_counter + 1
                elif(y1 ==229):
                    break
                print(for_loop_counter)
                if(for_loop_counter == 10):
                    for_loop_counter = 0
                    break
                print("no more for loop")
                pass

        print("transition to sixth platform")
        PressKey(0xCB)#left
        time.sleep(0.1)
        while(True):
            try:
                x1, y1 = pyautogui.locateCenterOnScreen("C:/Users/Alec/Desktop/Maplestoryscript/artale/player.PNG", confidence = 0.6, region=region)
                print(x1,y1)
                previous_position_y = y1
                if(y1 == 229):
                    print("on rope jump off")
                    break
                elif(y1 ==229):
                    break
            except TypeError:
                print("not on rope yet")
                if(y1 == 229):
                    print("on rope jump off")
                    break
                elif(y1 ==229):
                    break
                pass
        time.sleep(0.1)
        ReleaseKey(0xCB)

        #sixth platform
        while(True):
            try:
                x1, y1 = pyautogui.locateCenterOnScreen("C:/Users/Alec/Desktop/Maplestoryscript/artale/player.PNG", confidence = 0.6, region=region)
                previous_position_x = x1
                previous_position_y = y1
                print(x1,y1)
                #(x,165) -> (x,157)
                if(y1 == 229) and (x1 >= 192):
                    PressKey(0xCB)#left
                    PressKey(0x12)#e
                    time.sleep(0.1)
                    ReleaseKey(0x12)
                    time.sleep(0.6)
                    PressKey(0x39)#space
                    time.sleep(0.1)
                    ReleaseKey(0x39)
                    ReleaseKey(0xCB)
                    for_loop_counter = for_loop_counter + 1
                elif(y1 == 229) and (x1 < 192) and (x1 >= 168):
                    PressKey(0x12)#e
                    time.sleep(0.1)
                    ReleaseKey(0x12)
                    time.sleep(0.6)
                    for_loop_counter = for_loop_counter + 1
                elif(y1 == 229) and (x1 < 168):
                    PressKey(0xCD)#right
                    PressKey(0x12)#e
                    time.sleep(0.1)
                    ReleaseKey(0x12)
                    time.sleep(0.6)
                    PressKey(0x39)#space
                    time.sleep(0.1)
                    ReleaseKey(0x39)
                    ReleaseKey(0xCD)
                    for_loop_counter = for_loop_counter + 1
                print(for_loop_counter)
                if(for_loop_counter == 10):
                    for_loop_counter = 0
                    break
                print("no more for loop")


            except TypeError:
                print("cant see")
                            #(x,165) -> (x,157)
                if(previous_position_y == 229) and (previous_position_x >= 192):
                    PressKey(0xCB)#left
                    PressKey(0x12)#e
                    time.sleep(0.1)
                    ReleaseKey(0x12)
                    time.sleep(0.6)
                    PressKey(0x39)#space
                    time.sleep(0.1)
                    ReleaseKey(0x39)
                    ReleaseKey(0xCB)
                    for_loop_counter = for_loop_counter + 1
                elif(previous_position_y == 229) and (previous_position_x < 192) and (previous_position_x >= 168):
                    PressKey(0x12)#e
                    time.sleep(0.1)
                    ReleaseKey(0x12)
                    time.sleep(0.6)
                    for_loop_counter = for_loop_counter + 1
                elif(previous_position_y == 229) and (previous_position_x < 168):
                    PressKey(0xCD)#right
                    PressKey(0x12)#e
                    time.sleep(0.1)
                    ReleaseKey(0x12)
                    time.sleep(0.6)
                    PressKey(0x39)#space
                    time.sleep(0.1)
                    ReleaseKey(0x39)
                    ReleaseKey(0xCD)
                    for_loop_counter = for_loop_counter + 1
                print(for_loop_counter)
                if(for_loop_counter == 10):
                    for_loop_counter = 0
                    break
                print("no more for loop")
                pass

        print("transition to rope up")
        PressKey(0xCD)#right
        PressKey(0xC8)#up
        time.sleep(0.1)
        while(True):
            try:
                x1, y1 = pyautogui.locateCenterOnScreen("C:/Users/Alec/Desktop/Maplestoryscript/artale/player.PNG", confidence = 0.6, region=region)
                print(x1,y1)
                if(y1 < 229) and (x1 == 202):
                    print("on rope jump off")
                    break
            except TypeError:
                print("not on rope yet")
                if(y1 < 229) and (x1 == 202):
                    print("on rope jump off")
                    break
                pass
        time.sleep(0.1)
        ReleaseKey(0xC8)
        ReleaseKey(0xCD)
        time.sleep(0.1)

        artale_rope()
        time.sleep(0.1)

        PressKey(0xCD)#right
        time.sleep(0.1)
        PressKey(0x39)#space
        time.sleep(0.1)
        ReleaseKey(0x39)
        ReleaseKey(0xCD)

        time.sleep(0.1)





def artale_rope():
    PressKey(0xC8)#up arrow
    time.sleep(0.1)
    PressKey(0x39)#space
    
    for x in range(20):
        PressKey(0xCB)#left
        time.sleep(0.1)
        ReleaseKey(0xCB)
        PressKey(0xCD)#right
        time.sleep(0.1)
        ReleaseKey(0xCD)

    time.sleep(0.5)
    ReleaseKey(0x39)
    ReleaseKey(0xC8)



#(202,y) = rope position
#(x,150) = top right platform (1)
#(x,165) -> (x,157) = top left platform (2)
#(x,179) = middle right platform (3)
#(x,185) = middle left platform (4)
#(x,200) = bottom right platform (5)
#(x,229) = bottom left platform (6)

#(192,y) and (212,y) too close to rope edge
#(168,y) middle of left platforms

#(234,y) middle of right platforms


def human_delay(min_time=0.1, max_time=0.3):
    time.sleep(random.uniform(min_time, max_time))


#---------------------------------------------------------------------------------------






# set path=C:\Users\Alec\AppData\Local\Programs\Python\Python37-32

# python "C:/Users/Alec/Desktop/Maplestoryscript/zerobot.py"






time.sleep(1)

zombie_lupin()

#artaleposition_lupin()
#calibrate_map()
#artale_combined()
#artale_combined_mage()
#artaleposition()

#artale_rope()
#leftandrightspam()

#tanjirotboytrain1()
#tanjiro_yumyum()
#tanjiro_bft2()


#checkjumpdown()

#trackplayer()


#mcoord()


#movetorune()


#loopmapadele()
#attackteleright()
#yumyum()
#lachlach()
#arcana()
#sellas_pd4()
#labysuff6()
#rocky1()
#burningcerniumwestern1()
#outlawwaste2()
#burningcerniumwestern1_vac()
#odium()


#loopmap()

#greedcache()
#TOFask()

#openherbs()

#shangri_la_bloomingspring4()
#shangri_la_bloomingspring4_test()
#shangrila_mapdetect()

#checkrightplatcarcion()

#sunkenruins4()


#bucc_abandonarea2()
#bucc_worldsorrow3()

#spamy()

#attacklr()
#labysuff5()
#threadings()
#juniper()
#firespirits()

#zeroupdownforever()

#betweenfrostthunder2()

#dccup1()
#loopmap()
