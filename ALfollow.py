from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
chrome_driver_binary = r'C:\Users\satya\Downloads\chromedriver_win32 (1)\chromedriver.exe'
driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)

driver.get("https://anilist.co/login")
time.sleep(60)
for i in range(100000):
    driver.get('https://anilist.co/user/' + str(i+1))
    time.sleep(2)
    if driver.current_url == ('https://anilist.co/404'):
        print("User " + str(i) + " does not exist")
        continue
    followbutton = driver.find_element_by_class_name('nav-btn')
    followbutton.click() #does the epic
    print("Following user number " + str(i+1))
    time.sleep(2)