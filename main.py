try:
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from msedge.selenium_tools import Edge, EdgeOptions
    from selenium.webdriver.common.by import By
    import time, pyautogui as pya, keyboard, random
except Exception:
    import os
    os.system("pip install selenium")
    os.system("pip install pyautogui")
    os.system("pip install keyboard")
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from msedge.selenium_tools import Edge, EdgeOptions
    from selenium.webdriver.common.by import By
    import time, pyautogui as pya, keyboard, random
    
webdriver_location="MicrosoftWebDriver.exe"
options=EdgeOptions()
options.use_chromium=True
options.binary_location=r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
browser=Edge(options=options,executable_path=webdriver_location)
browser.get("https://www.nitrotype.com/race")
running=False

keybind=input("-Start typeing keybind, press on start of race: ")

while True:
    try:
        # Prevent it from running two times.
        if keyboard.is_pressed(keybind) == True and running == False:
            runningEFE=True
            newtype=""
            typestring=[]
            print('-Reading...')
            elements=browser.find_elements_by_class_name('dash-letter')
            # Remove invalid character at finish.
            elements.pop()
            print("-Typing...")
            for e in elements:
                # Get text of hidden and visible items.
                text=e.get_attribute("textContent")
                if "\xa0" in text:
                    text=str(text).replace("\xa0"," ")
                typestring.append(text)
            # Type characters found in search. [Make browser only]
            for c in typestring:
                newtype=newtype+str(c)
            time.sleep(0.75)
            pya.write(newtype, interval=0.05)
            # Allow it to run again.
            runningEFE=False
            print("-Ready!")
    except Exception:
        print("-Error occured...")

# Don't set words per minute up or you will be banned, I've gone through 5 accounts now.
