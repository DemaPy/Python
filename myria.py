from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import string
import time
import random

s = Service(executable_path='./chromedriver.exe')
options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_extension("MetaMask.crx")
driver = webdriver.Chrome(service=s, options=options)
sleep5s =  3

def generate_pass():
    letters_and_digits = string.ascii_letters + string.digits
    rand_string = ''.join(random.sample(letters_and_digits, 20))
    return rand_string



def metamask(sleep):
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(sleep)
    driver.find_element(By.CLASS_NAME, 'button.btn--rounded.btn-primary.first-time-flow__button').click()
    time.sleep(sleep)
    driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/button').click()
    time.sleep(sleep)
    driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div/div[5]/div[1]/footer/button[1]').click()
    time.sleep(sleep)
    driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/form/div[4]/div[1]/div/input').send_keys('lumber video bulb physical pencil boy tuna hood split online deer guard')
    time.sleep(sleep)
    randPass = generate_pass()
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(randPass)
    driver.find_element(By.XPATH, '//*[@id="confirm-password"]').send_keys(randPass)
    time.sleep(sleep)
    driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/form/div[7]/div').click()
    time.sleep(sleep)
    driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/form/button').click()
    time.sleep(sleep)
    driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/button').click()
    click_btn(sleep)



def click_btn(sleep):
        driver.get("https://myria.com/sigil/")
        time.sleep(sleep)
        driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div/button').click()
        time.sleep(sleep)
        driver.switch_to.window(driver.window_handles[2])
        time.sleep(sleep)
        driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div[2]/div[3]/div[2]/button[2]').click()
        time.sleep(sleep)
        driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div[2]/div[2]/div[2]/footer/button[2]').click()
        time.sleep(sleep)
        driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div[3]/button[2]').click()
        


def get_page(sleep):
    metamask(sleep)

get_page(sleep5s)
