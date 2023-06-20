import time
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

username = 'test'
email='test@rt-ed.co.il'
tel='0505000000'

# name_locator: str='//input[@id="form-field-name"]'
name_locator: str='#form-field-name'
email_locator: str='//input[@id="form-field-myEmail"]'
tel_locator: str='//input[@id="form-field-number"]'
login_locator: str='//body/div[1]/section[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[2]/div[1]/div[4]/div[1]/form[1]/div[1]/div[5]/button[1]'



web_element = webdriver.Chrome()
web_element.maximize_window()
wait=WebDriverWait(web_element,15)
web_element.get('https://rt-ed.tech/%D7%A7%D7%95%D7%A8%D7%A1-%D7%91%D7%93%D7%99%D7%A7%D7%95%D7%AA-%D7%AA%D7%95%D7%9B%D7%A0%D7%94-qa_lp/')
time.sleep(2)


def find_element_By(key):
    locating= {'xpath':By.XPATH,'css':By.CSS_SELECTOR,'name':By.NAME}
    return locating[key]


def if_presence(key: object, locator: object)-> WebElement:
   return wait.until(EC.presence_of_element_located((key,locator)))



def click_element(key,locator)->WebElement:
      return wait.until(EC.element_to_be_clickable((key,locator))).click()


def screen_shot(name):
    timestr = time.strftime('%Y-%m-%d-%H.%M.%S')

    time.sleep(2)
    web_element.save_screenshot(f".{name, timestr}.png")



if_presence(find_element_By('css'),name_locator).send_keys(username)
time.sleep(2)

if_presence(find_element_By('xpath'),tel_locator).send_keys(tel)
time.sleep(2)

if_presence(find_element_By('xpath'),email_locator).send_keys(email)
time.sleep(2)



click_element(find_element_By('xpath'),login_locator)
time.sleep(10)

screen_shot("The form has been sent successfully.")










