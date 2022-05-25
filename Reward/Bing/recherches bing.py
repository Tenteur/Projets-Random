#import all the necessaries
import os
import random
import time
from multiprocessing.connection import wait

i = int(0)
while i < 3:
    os.system("VerifyIntegrity.py")
    i += 1

#ask the user what number of searches he wants to do nad id not an integer re ask
while True:
    try:
        numberOfSearches = int(input("How many searches do you want to do? "))
        break
    except ValueError:
        print("Please enter a number")
print("everything is ok, starting the program")

import pyautogui

pyautogui.FAILSAFE = False

def FIsMatching():
    matches = False
    while matches == False:
        if pyautogui.pixelMatchesColor(20, 20, (16, 110, 191, 255)):
            pyautogui.moveTo(450, 250)
            matches = True
        else:
            matches = False

def GIsMatching():
    pxielx = 29
    pxiely = 18
    matches = False
    while matches == False:
        if pyautogui.pixelMatchesColor(pxielx, pxiely, (17, 123, 214)):
            pyautogui.moveTo(450, 250)
            matches = True
        else:
            matches = False
            #print the current color of the pixel
            print(pyautogui.pixel(pxielx, pxiely))
            #do a point where the pixel is
            pyautogui.moveTo(pxielx, pxiely)

def EIsMatching():
    matches = False
    while matches == False:
        if pyautogui.pixelMatchesColor(68, 15, (16, 110, 191, 255)):
            pyautogui.moveTo(450, 250)
            matches = True
        else:
            matches = False

with open('preferences', 'r') as file:
        preferences = file.read().splitlines()
        lang = preferences[0].split(':')[1]
        browser = preferences[1].split(':')[1]
        webBrowserIconColomn = int(preferences[2].split(':')[1])
        isPath = preferences[3].split(':')[1]
        browserPath = preferences[4].split(':')[1]

PixelResult = 120 + (webBrowserIconColomn * 50)

pyautogui.click(PixelResult, 745)

time.sleep(1.5)

def RandomWord():
    random_word = ''.join(random.choice(
        'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(10))
    pyautogui.typewrite(random_word, interval=0.05)
    pyautogui.press("enter")

def EnterBing():
    pyautogui.typewrite("bing.com")
    pyautogui.press("enter")

def TypeEnterSpam():
    pyautogui.keyDown('ctrl')
    pyautogui.press('backspace')
    pyautogui.keyUp('ctrl')
    random_word = ''.join(random.choice(
            'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(10))
    pyautogui.typewrite(random_word, interval=0.01)
    pyautogui.press("enter")


if browser == 'firefox':
    #click on the search bar
    pyautogui.click(300, 65)
    #enter the word "bing" and press enter
    EnterBing()
    FIsMatching()
    RandomWord()
    #do a loop that repeat 30 times so the cursor move first to the pixel 400, 150 then press backspace 10 times then redo the same thing of the random word but wait 1s after each times
    for i in range(numberOfSearches):
        pyautogui.click(400, 150)
        TypeEnterSpam()
        FIsMatching()

elif browser == 'chrome':
    #click on the search bar
    pyautogui.click(330, 50)
    #enter the word "bing" and press enter
    EnterBing()
    #get the 20, 20 pixel color and if its rgba(16,110,191,255) then set the mouse to the pixel: 450, 250 and if not print the color with rgba and ait 0.5s and repeat
    GIsMatching()
    #enter random word with a-z A-Z 0-9 and with 10 characters
    RandomWord()
    #do a loop that repeat 30 times so the cursor move first to the pixel 400, 150 then press backspace 10 times then redo the same thing of the random word but wait 1s after each times
    for i in range(numberOfSearches):
        pyautogui.click(350, 110)
        TypeEnterSpam()

        GIsMatching()