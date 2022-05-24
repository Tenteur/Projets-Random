#import all the necessaries
import os
import random
import time
from multiprocessing.connection import wait

import pyautogui


def FIsMatching():
    matches = False
    while matches == False:
        if pyautogui.pixelMatchesColor(20, 20, (16, 110, 191, 255)):
            pyautogui.moveTo(450, 250)
            matches = True
        else:
            matches = False

def GIsMatching():
    matches = False
    while matches == False:
        if pyautogui.pixelMatchesColor(30, 15, (16, 110, 191, 255)):
            pyautogui.moveTo(450, 250)
            matches = True
        else:
            matches = False

def EIsMatching():
    matches = False
    while matches == False:
        if pyautogui.pixelMatchesColor(68, 15, (16, 110, 191, 255)):
            pyautogui.moveTo(450, 250)
            matches = True
        else:
            matches = False


i = int(0)
while i < 3:
    os.system("VerifyIntegrity.py")
    i += 1

print("everything is ok, starting the program")

with open('preferences', 'r') as file:
        preferences = file.read().splitlines()
        lang = preferences[0].split(':')[1]
        browser = preferences[1].split(':')[1]
        webBrowserIconColomn = int(preferences[2].split(':')[1])

PixelResult = 120 + (webBrowserIconColomn * 50)


pyautogui.click(PixelResult, 745)

#wait 1.5s
time.sleep(1.5)

if browser == 'firefox':
    #click on the search bar
    pyautogui.click(300, 65)

    #enter the word "bing" and press enter
    pyautogui.typewrite("bing")
    pyautogui.press("enter")

    #get the 20, 20 pixel color and if its rgba(16,110,191,255) then set the mouse to the pixel: 450, 250 and if not print the color with rgba and ait 0.5s and repeat
    FIsMatching()

    #enter random word with a-z A-Z 0-9 and with 10 characters
    random_word = ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(10))
    pyautogui.typewrite(random_word, interval=0.05)
    pyautogui.press("enter")

    #do a loop that repeat 30 times so the cursor move first to the pixel 400, 150 then press backspace 10 times then redo the same thing of the random word but wait 1s after each times

    for i in range(5):
        pyautogui.click(400, 150)
        pyautogui.keyDown('ctrl')
        pyautogui.press('backspace')
        pyautogui.keyUp('ctrl')
        random_word = ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(10))
        pyautogui.typewrite(random_word, interval=0.01)
        pyautogui.press("enter")

        FIsMatching()

