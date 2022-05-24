import os

Useless = 0

with open('preferences', 'r') as file:
    preferences = file.read().splitlines()
    lang = preferences[0].split(':')[1]
    browser = preferences[1].split(':')[1]
    webBrowserIconColomn = preferences[2].split(':')[1]
    
    if lang == 'en' or lang == 'fr':
        Useless = 0
    else:
        with open('preferences', 'w') as file:
            file.write('lang:en\nbrowser:'+browser+'\nwebBrowserIconColomn:'+webBrowserIconColomn)
    if browser == 'chrome' or browser == 'firefox' or browser == 'edge' or browser == 'opera':
        Useless = 0
    else:
        with open('preferences', 'w') as file:
            file.write('lang:'+lang+'\nbrowser:firefox\nwebBrowserIconColomn:'+webBrowserIconColomn)
    if webBrowserIconColomn.isdigit():
        webBrowserIconColomn = int(webBrowserIconColomn)
        if webBrowserIconColomn >= 0 and webBrowserIconColomn <= 10:
            Useless = 0
        else:
            with open('preferences', 'w') as file:
                file.write('lang:'+lang+'\nbrowser:' + browser+'\nwebBrowserIconColomn:0')
    else:
        with open('preferences', 'w') as file:
            file.write('lang:'+lang+'\nbrowser:'+browser+'\nwebBrowserIconColomn:0')