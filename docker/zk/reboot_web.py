from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import datetime

chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--remote-debugging-port=9222")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-infobars")

browser = webdriver.Chrome(chrome_options=chrome_options)
login_user, pass_user = '1', '0608'


def login():
    username = browser.find_element(By.NAME, "username")
    password = browser.find_element(By.NAME, "userpwd")
    username.send_keys(login_user)
    password.send_keys(pass_user)
    b = '//input[@value="Login"]'
    browser.find_element(By.XPATH, b).send_keys(Keys.ENTER)
    time.sleep(2)


def reboot(ip):
    browser.get(ip)
    time.sleep(1)


def selenium_open(ip):
    login_url = "http://" + ip + "/csl/login"
    reboot_url = "http://" + ip + "/form/Device"
    browser.implicitly_wait(10)
    browser.get(login_url)
    login(), login()
    reboot(reboot_url)


# def debug():
#     try:
#         with open("C:\Python27\log.txt", "a") as it:
#             ctime = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
#             it.write(ctime + " " + ip + " successfully rebooted\n")
#
#     except NoSuchElementException:
#         pass