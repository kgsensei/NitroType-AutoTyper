from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time,keyboard,random
import pyautogui as pya
from fake_useragent import UserAgent

def GetUA():
    ua=UserAgent()
    userAgent=ua.random
    return userAgent

webdriver_location="hacked_chromedriver.exe"
options=webdriver.ChromeOptions()
options.use_chromium=True
options.binary_location=r'C:\Program Files\Google\Chrome\Application\chrome.exe'
options.add_argument("--user-agent="+GetUA())
options.add_argument('--disable-extensions')
options.add_argument("--start-maximized")
options.add_argument("--disable-plugins-discovery")
options.add_argument('--profile-directory=Default')
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_experimental_option('useAutomationExtension',False)
options.add_experimental_option("excludeSwitches",["enable-automation"])
options.add_experimental_option('excludeSwitches',['enable-logging'])
browser=webdriver.Chrome(options=options,executable_path=webdriver_location)
browser.delete_all_cookies()
browser.get("https://www.nitrotype.com/race")
browser.execute_script("Object.defineProperty(navigator,'webdriver',{get:()=>undefined})")
runningEFE=False

keybind=input("-Start typing keybind, press on start of race: ")
autotof=int(input("-Automatically play through games [1/0]: "))

def exists(classname:str):
    try:
        if browser.find_element_by_css_selector(classname):
            return True
    except (Exception,NoSuchElementException):
        return False

if autotof==0:
    while True:
        try:
            browser.execute_script("let items=document.getElementsByClassName('ad');for(let i=0;i<items.length;i++){items[i].remove()}")
            if keyboard.is_pressed(keybind)==True and runningEFE==False and browser.current_url=="https://www.nitrotype.com/race":
                runningEFE=True
                newtype=""
                typestring=[]
                print('-Waiting...')
                if exists('.dash-letter')==False:
                    wait=WebDriverWait(browser,20)
                    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'.dash-letter')))
                elements=browser.find_elements_by_class_name('dash-letter')
                elements.pop()
                print('-Reading...')
                for e in elements:
                    text=e.get_attribute("textContent")
                    if "\xa0" in text:
                        text=str(text).replace("\xa0"," ")
                    typestring.append(text)
                for c in typestring:
                    newtype=newtype+str(c)
                if exists('.is-retracting'):
                    wait=WebDriverWait(browser,10)
                    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'.is-retracting')))
                    time.sleep(3)
                print("-Working...")
                pya.write(newtype,interval=0.0441)
                print("-Finished...")
                runningEFE=False
        except Exception as e:
            print("-Error: "+str(e))
else:
    while True:
        try:
            browser.execute_script("let items=document.getElementsByClassName('ad');for(let i=0;i<items.length;i++){items[i].remove()}")
            newtype=""
            typestring=[]
            print('-Waiting...')
            if exists('.dash-letter')==False:
                wait=WebDriverWait(browser,20)
                wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'.dash-letter')))
            elements=browser.find_elements_by_class_name('dash-letter')
            elements.pop()
            print('-Reading...')
            for e in elements:
                text=e.get_attribute("textContent")
                if "\xa0" in text:
                    text=str(text).replace("\xa0"," ")
                typestring.append(text)
            for c in typestring:
                newtype=newtype+str(c)
            if exists('.is-retracting'):
                wait=WebDriverWait(browser,10)
                wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'.is-retracting')))
                time.sleep(3)
            print("-Working...")
            pya.write(newtype,interval=0.0441)
            print("-Finished...")
            time.sleep(5)
            browser.execute_script("window.location.reload()")
            time.sleep(5)
        except Exception as e:
            print("-Error: "+str(e))
