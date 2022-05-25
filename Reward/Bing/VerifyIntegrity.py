import os

#get if pyautogui is installed
try:
    import pyautogui
except:
    print("pyautogui isn't installed yet, downloading it")
    os.system("pip install pyautogui")
    print("pyautogui is now installed")

import pyautogui
Useless = 0

#verify if 'preferences' file exists and if not create it with default values (lang:en, browser:firefox, webBrowserIconColomn:0)
if os.path.exists('preferences'):
    with open('preferences', 'r') as file:
        preferences = file.read().splitlines()
        lang = preferences[0].split(':')[1]
        browser = preferences[1].split(':')[1]
        webBrowserIconColomn = preferences[2].split(':')[1]
        isPath = preferences[3].split(':')[1]
        browserPath = preferences[4].split(':')[1]

        if lang == 'en' or lang == 'fr':
            Useless = 0
        else:
            with open('preferences', 'w') as file:
                file.write('lang:en\nbrowser:'+browser +
                        '\nwebBrowserIconColomn:'+webBrowserIconColomn+'\nisPath:'+isPath+'\nbrowserPath:'+browserPath)
        if browser == 'chrome' or browser == 'firefox' or browser == 'edge' or browser == 'opera':
            Useless = 0
        else:
            with open('preferences', 'w') as file:
                file.write(
                    'lang:'+lang+'\nbrowser:firefox\nwebBrowserIconColomn:'+webBrowserIconColomn+'\nisPath:'+isPath+'\nbrowserPath:'+browserPath)
        if webBrowserIconColomn.isdigit():
            webBrowserIconColomn = int(webBrowserIconColomn)
            if webBrowserIconColomn >= 0 and webBrowserIconColomn <= 10:
                Useless = 0
            else:
                with open('preferences', 'w') as file:
                    file.write('lang:'+lang+'\nbrowser:' +
                            browser+'\nwebBrowserIconColomn:0'+'\nisPath:'+isPath+'\nbrowserPath:'+browserPath)
        else:
            with open('preferences', 'w') as file:
                file.write('lang:'+lang+'\nbrowser:' +
                        browser+'\nwebBrowserIconColomn:0'+'\nisPath:'+isPath+'\nbrowserPath:'+browserPath)
        if isPath == 'True' or isPath == 'False':
            Useless = 0
        else :
            with open('preferences', 'w') as file:
                file.write('lang:'+lang+'\nbrowser:' +
                        browser+'\nwebBrowserIconColomn:'+webBrowserIconColomn+'\nisPath:False'+'\nbrowserPath:'+browserPath)
        if browserPath.endswith('firefox.exe') or browserPath.endswith('chrome.exe') or browserPath.endswith('opera.exe') or browserPath.endswith('edge.exe'):
            Useless = 0
        else:
            with open('preferences', 'w') as file:
                file.write('lang:'+lang+'\nbrowser:' +
                        browser+'\nwebBrowserIconColomn:'+webBrowserIconColomn+'\nisPath:'+isPath+'\nbrowserPath:C:\\Program Files\\Mozilla Firefox\\firefox.exe')
else:
    with open('preferences', 'w') as file:
        file.write("lang:en\n")
        file.write("browser:firefox\n")
        file.write("webBrowserIconColomn:0\n")
        file.write("isPath:False\n")
        file.write("browserPath:C:\\Program Files\\Mozilla Firefox\\firefox.exe\n")
        file.close()


