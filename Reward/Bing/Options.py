
from ast import While
import time

from numpy import printoptions


#get the option 'lang' from the preferences file and if 'en' then get all the lines in 'lang\en' to a list and if 'fr' then get all the lines in 'lang\fr' to a list
with open('preferences', 'r') as file:
    preferences = file.read().splitlines()
    lang = preferences[0].split(':')[1]

if lang == 'en':
    with open('lang\\en', 'r') as file:
        lines = file.read().splitlines()
elif lang == 'fr':
    with open('lang\\fr', 'r') as file:
        lines = file.read().splitlines()

PreferencesNotFound = lines[0].split(';')[1]
ErrorForPreferences = lines[1].split(';')[1]
PrintHelp = lines[2].split(';')[1]
PrintOptions = lines[3].split(';')[1]
PrintExit = lines[4].split(';')[1]
OptionsHelp = lines[5].split(';')[1]
ExitProg = lines[6].split(';')[1]
OptionsLangChanged = lines[7].split(';')[1]
OptionsBrowserChanged = lines[8].split(';')[1]
OptionsWebBrowserIconColomnChanged = lines[9].split(';')[1]
UnknownCommand = lines[10].split(';')[1]
Input = lines[11].split(';')[1]
IsNew = lines[12].split(';')[1]


print(IsNew+"\n")
UserInput = input(Input)
UserInput = UserInput.lower()




while True:
    #if the user enters 'help' print "Help: print this help menu", on a new line, "Options: print the options menu or modify the options in Preferences file", on a new line, "Exit: Close the program"
    if UserInput== "help":
        print("\n"+PrintHelp+"\n")
        print(PrintOptions+"\n")
        print(PrintExit+"\n")
    elif UserInput== "options":
        print("\n"+OptionsHelp+"\n")
    elif UserInput== "exit":
        print("\n"+ExitProg)
        time.sleep(1)
        exit()
    
    #if the user enter 'options lang:fr' then print "You have changed the language to French" and change the language in file 'preferences' to 'fr'
    elif UserInput.startswith("options lang:fr") or UserInput.startswith("options lang:en"):
        #get all the options in the file 'preferences' to rewrite it with the new language
        with open('preferences', 'r') as file:
            preferences = file.read().splitlines()
            lang = preferences[0].split(':')[1]
            browser = preferences[1].split(':')[1]
            webBrowserIconColomn = preferences[2].split(':')[1]
        #rewrite the file 'preferences' with the new language
        with open('preferences', 'w') as file:
            file.write('lang:'+UserInput.split(':')[1]+'\nbrowser:'+browser+'\nwebBrowserIconColomn:'+webBrowserIconColomn)
        print(OptionsLangChanged+UserInput.split(':')[1])


        #do the same for the browser but only if browser is firefox, chrome or opera
    elif UserInput.startswith("options browser:firefox") or UserInput.startswith("options browser:chrome") or UserInput.startswith("options browser:opera") or UserInput.startswith("options browser:edge"):
        #get all the options in the file 'preferences' to rewrite it with the new language
        with open('preferences', 'r') as file:
            preferences = file.read().splitlines()
            lang = preferences[0].split(':')[1]
            browser = preferences[1].split(':')[1]
            webBrowserIconColomn = preferences[2].split(':')[1]
        #rewrite the file 'preferences' with the new language
        with open('preferences', 'w') as file:
            file.write('lang:'+lang+'\nbrowser:'+UserInput.split(':')[1]+'\nwebBrowserIconColomn:'+webBrowserIconColomn)
        print(OptionsBrowserChanged+UserInput.split(':')[1])
    
    # do the same with the webBrowserIconColomn but only if it's a number
    elif UserInput.startswith("options icon:"):
        #get all the options in the file 'preferences' to rewrite it with the new language
        with open('preferences', 'r') as file:
            preferences = file.read().splitlines()
            lang = preferences[0].split(':')[1]
            browser = preferences[1].split(':')[1]
            webBrowserIconColomn = preferences[2].split(':')[1]
        #rewrite the file 'preferences' with the new language
        with open('preferences', 'w') as file:
            file.write('lang:'+lang+'\nbrowser:'+browser+'\nwebBrowserIconColomn:'+UserInput.split(':')[1])
        print(OptionsWebBrowserIconColomnChanged+UserInput.split(':')[1])

    
    else:
        print(UnknownCommand+"\n")

    UserInput = input(Input)
    UserInput = UserInput.lower()