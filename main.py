from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from msedge.selenium_tools import Edge, EdgeOptions
import time
import pyautogui as pya
import keyboard
webdriver_location = "MicrosoftWebDriver.exe"
options = EdgeOptions()
options.use_chromium = True
options.binary_location=r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
browser = Edge(options=options, executable_path=webdriver_location)
browser.get("https://www.nitrotype.com/race")
running = False
pya.moveTo(565, 25)
pya.dragTo(565, 0, 0.3, button='left')
while True:
    if keyboard.is_pressed('/') == True and running == False:
        runningEFE = True
        typestring = []
        print('reading...')
        elements = browser.find_elements_by_class_name('dash-letter')
        elements.pop()
        for e in elements:
            typestring.append(e.text)
        print(typestring)
        for c in typestring:
            pya.write(c)
        runningEFE = False
        print("Ready!")
