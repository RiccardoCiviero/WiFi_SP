import os
import time
import subprocess
import requests
# import re
from splinter import Browser
# import mechanize

sleepTime = 10
longSleepTime = 60 # 1 min

path = os.getenv("APPDATA") +  "\\CoreTech\\options.opt"
user = ""
passwd = ""

exeScript = True
while exeScript == True:
    # Check if connected to SanPaoloWiFi
    connected = False
    while connected == False:
        netsh = subprocess.check_output('netsh wlan show interfaces').decode('utf-8')
        if 'San Paolo WiFi' in netsh:
            print("Connected to SanPaoloWiFi")
            connected = True
        time.sleep(sleepTime)

    # Read config files
    with open(path, "r") as opt_file:
        opt_read = opt_file.readlines()
        user = opt_read[0]
        passwd = opt_read[1]
    print("Keys loaded")

    # Login automation [Firefox]
    browser = Browser()
    browser.visit('https://6.6.6.6')
    browser.fill('username', user)
    browser.fill('pwd', passwd)
    button = browser.find_by_name('Login')
    button.click()

    # Login automation [Mechanize]
    # browser = mechanize.Browser()
    # browser.set_handle_equiv(False)
    # browser.set_handle_robots(False)
    # browser.set
    # browser.open("https://6.6.6.6")
    # browser.select_form("username")
    # mechanize.HTMLForm.set_value(user)
    # browser.select_form("pwd")
    # mechanize.HTMLForm.set_value(passwd)
    # browser.select_form("Login")
    # browser.click()

    # Check if the script has to be relaunched
    # If the connection is active doesn't need to realunch
    relaunch = False
    while relaunch == False:
        url = "https://www.google.com"
        try:
            requests.get(url, timeout=5)
            time.sleep(longSleepTime)
        except(requests.ConnectionError, requests.Timeout) as exception:
            relaunch = True
    


