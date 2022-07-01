# -*- coding: utf-8 -*-
from telnetlib import EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import time, random, traceback
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from twocaptcha import TwoCaptcha




def move_to_element(element, driver):
    driver.execute_script("return arguments[0].scrollIntoView(true);", element)


def clickble(selector, driver, timeout=1):
    try:
        if WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.XPATH, selector))):
            return True
        else:
            return False
    except:
        pass


def click(selector, driver, timeout=10, find=True):
    if find:
        WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.XPATH, selector)))
        accept = driver.find_element(By.XPATH, selector)
        actions = ActionChains(driver)
        actions.move_to_element(accept).perform()
        html = driver.find_element(By.TAG_NAME, 'html')
        for i in range(2):
            try:
                WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.XPATH, selector))).click()
                break
            except:
                html.send_keys(Keys.DOWN)
                time.sleep(0.2)
            time.sleep(random.randrange(1, 3))
    else:
        WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(selector))
        accept = selector
        actions = ActionChains(driver)
        actions.move_to_element(accept).perform()
        html = driver.find_element(By.TAG_NAME, 'html')
        for i in range(2):
            try:
                WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.XPATH, selector))).click()
                break
            except:
                html.send_keys(Keys.DOWN)
                time.sleep(0.2)
            time.sleep(random.randrange(1, 3))
        WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(selector)).click()
        time.sleep(random.randrange(1, 3))


def send_keys(selector, send_keys, driver, timeout=20, find=True):
    if find:
        accept = driver.find_element(By.XPATH, selector)
        actions = ActionChains(driver)
        actions.move_to_element(accept).perform()
        WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.XPATH, selector))).send_keys(send_keys)
        time.sleep(random.randrange(1, 2))
    else:
        accept = selector
        actions = ActionChains(driver)
        actions.move_to_element(accept).perform()
        WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(selector)).send_keys(send_keys)
        time.sleep(random.randrange(1, 2))


def xpath_exists(xpath, driver):
    try:
        driver.find_element(By.XPATH, xpath)
        exist = True
    except NoSuchElementException:
        exist = False
    return exist


def mail_ru(email, password, driver):
    try:
        handler = driver.window_handles

        driver.execute_script('''window.open("https://account.mail.ru/login","_blank");''')
        time.sleep(3)
        handler2 = driver.window_handles
        cur_url_first = list(set(handler2) - set(handler))
        if len(handler2) != len(handler):
            time.sleep(2)
            driver.switch_to.window(cur_url_first[0])
        WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.XPATH, '//input[@name="username"]')))
        send_keys('//input[@name="username"]', email, driver)
        time.sleep(1)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//button[@data-test-id="next-button"]')))
        driver.find_element(By.XPATH, '//button[@data-test-id="next-button"]').click()  # Log
        time.sleep(1)

        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//input[@name="password"]')))
        send_keys('//input[@name="password"]', password, driver)
        time.sleep(1)

        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@data-test-id="submit-button"]')))
        click('//button[@data-test-id="submit-button"]', driver)
        time.sleep(6)
        if xpath_exists('//div[@class="b-panel__content__desc"]', driver):   # Иногда вылазит капча, мол а это ваш акк?!?!?!
            time.sleep(10)
            captcha = driver.find_element(By.XPATH, '//img[@class="js-captcha-img b-captcha__captcha"]')
            captcha.screenshot("captcha.png")
            api_key_norm = "2captha.token"
            solver_norm = TwoCaptcha(api_key_norm)
            result_norm = solver_norm.normal('captcha.png')
            result = result_norm['code']
            send_keys('//input[@class="b-input b-input_captcha b-input_responsive js-captcha"]', result, driver)
            click('//button[@class="btn btn_main btn_stylish btn_responsive js-submit"]', driver)
        WebDriverWait(driver, 50).until(EC.presence_of_element_located(
            (By.XPATH, '//span[contains(text(), "MemeBank")]/../..//span[@class="ll-sj__normal"]')))
        code = driver.find_element(By.XPATH,
                                   '//span[contains(text(), "MemeBank")]/../..//span[@class="ll-sj__normal"]').text
        split_code = code.split(': ')[-1]
        driver.switch_to.window(driver.window_handles[0])
        send_keys('//input[@placeholder="verification code"]', split_code, driver)

    except Exception as e:
        traceback.print_exc()



if __name__ == '__main__':
    mail_ru()