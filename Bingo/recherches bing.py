#import all the necessaries
import random
import time
from multiprocessing.connection import wait
import pyautogui
import os

colomnStart = 120

#load file 'preferences', check if 'webBrowserIconNum' is an INT. if the file doesn't exist create it with values: 'lang:en', 'browser:firefox', 'webBrowserIconColomn:0'
try:
    with open('preferences', 'r') as file:
        preferences = file.read().splitlines()
        lang = preferences[0].split(':')[1]
        browser = preferences[1].split(':')[1]
        webBrowserIconColomn = int(preferences[2].split(':')[1])
except:
    with open('preferences', 'w') as file:
        file.write('lang:en\nbrowser:firefox\nwebBrowserIconColomn:0')
    with open('preferences', 'r') as file:
        preferences = file.read().splitlines()
        lang = preferences[0].split(':')[1]
        browser = preferences[1].split(':')[1]
        webBrowserIconColomn = int(preferences[2].split(':')[1])

print(lang)
print(browser)
print(webBrowserIconColomn)

PixelResult = colomnStart + (webBrowserIconColomn * 50)
print(PixelResult)


pyautogui.click(PixelResult, 745)

# #then do a variable to store the location of the pixel: 300, 65
# FireSearchBar = pyautogui.pixel(300, 65)

# #wait 1.5s
# time.sleep(1.5)

# #click on it
# pyautogui.click(300, 65)

# #enter the word "google" and press enter
# pyautogui.typewrite("bing", interval=0.1)
# pyautogui.press("enter")

# #get the 20, 20 pixel color and if its rgba(16,110,191,255) then set the mouse to the pixel: 450, 250 and if not print the color with rgba and ait 0.5s and repeat
# matches = False
# while matches == False:
#     if pyautogui.pixelMatchesColor(20, 20, (16, 110, 191, 255)):
#         pyautogui.moveTo(450, 250)
#         matches = True
#     else:
#         matches = False
#         time.sleep(0.5)

# #enter random word with a-z A-Z 0-9 and with 10 characters
# random_word = ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(10))
# pyautogui.typewrite(random_word, interval=0.05)
# pyautogui.press("enter")

# #do a loop that repeat 20 times so the cursor move first to the pixel 400, 150 then press backspace 10 times then redo the same thing of the random word but wait 1s after each times
# for i in range(1):
#     pyautogui.click(400, 150)
#     for i in range(10):
#         pyautogui.press("backspace")
#     random_word = ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(10))
#     pyautogui.typewrite(random_word, interval=0.01)
#     pyautogui.press("enter")
#     time.sleep(0.75)
