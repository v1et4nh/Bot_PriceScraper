# -*- coding: utf-8 -*-

import requests
import pathlib
import os
import numpy as np
from datetime import datetime
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from twilio.rest import Client

bot_token = str(os.getenv('TELEGRAM_BOT_TOKEN'))    # Replace with your own bot_token
bot_chatID = str(os.getenv('TELEGRAM_BOT_CHATID'))  # Replace with your own bot_chatID


def whatsapp_bot_sendtext(bot_message):
    client = Client()
    from_number = 'whatsapp:' + str(os.getenv('TWILIO_PHONE_NUMBER'))  # Replace with your own twilio number
    to_number   = 'whatsapp:' + str(os.getenv('MY_PHONE_NUMBER'))      # Replace with your own phone number
    client.messages.create(body=bot_message,
                           from_=from_number,
                           to=to_number)


def telegram_bot_sendtext(bot_message):
    send_text  = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()


def telegram_bot_sendphoto(str_picpath):
    send_photo = 'https://api.telegram.org/bot' + bot_token + '/sendPhoto?chat_id=' + bot_chatID
    files = {'photo': open(str_picpath, 'rb')}
    img_stat = requests.post(send_photo, files=files)
    return img_stat


def getURL(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
        "Upgrade-Insecure-Requests": "1", "DNT": "1",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate"}
    req_url = requests.get(url=url, headers=headers)
    req_url.raise_for_status()

    return req_url


def get_savepath():
    current_path = pathlib.Path(__file__).parent.absolute()
    tmp = os.path.join(current_path, "screenshot")
    now = datetime.now()
    str_now = now.strftime("%Y%m%d_%H%M%S")
    filename = str_now + '.png'
    str_path = os.path.join(tmp, filename)
    return str_path


def get_latest_screenshot():
    list_dir = os.path.join(pathlib.Path(__file__).parent.absolute(), "screenshot")
    return list_dir[-1]


def get_pricetrigger(name):
    pricetrigger = 10000
    if name == 'Volvic':
        pricetrigger = 6
    elif name == 'Spezi':
        pricetrigger = 10
    elif name == 'FritzKola':
        pricetrigger = 18
    return pricetrigger


def get_flaschenpost_price(name, url):
    os.environ['MOZ_HEADLESS'] = '1'  # Run Firefox in the background
    service_log_path = os.path.join(pathlib.Path(__file__).parent.absolute(), "geckodriver.log")
    driver = webdriver.Firefox(service_log_path=service_log_path)
    driver.get(url)
    wait = WebDriverWait(driver, 10)
    zipcode_input = wait.until(EC.presence_of_element_located((By.ID, "validZipcode")))
    sleep(1)
    zipcode_input.send_keys('80807')
    sleep(1)
    driver.find_element_by_class_name("fp-button").click()
    sleep(1)

    try:
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "fp_article_price")))
        pricedict = driver.find_elements_by_class_name("fp_article_price")

        for price_idx in range(len(pricedict)):
            current_price = pricedict[price_idx].text
            current_price = current_price.replace('€', '').strip()
            current_price = current_price.replace(',', '.').strip()
            pricetrigger = get_pricetrigger(name)
            if float(current_price) <= pricetrigger:
                # Make screenshot
                str_fpath = get_savepath()
                driver.save_screenshot(str_fpath)
                str_message = name + ': ' + str(current_price) + '€\n' + url
                whatsapp_bot_sendtext(str_message)
                telegram_bot_sendtext(str_message)
                telegram_bot_sendphoto(str_fpath)
                break
    except:
        try:
            str_avail = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "fp_article_outOfStock")))
            # telegram_bot_sendtext(str_avail.text)
            # str_fpath = get_savepath()
            # driver.save_screenshot(str_fpath)
            # telegram_bot_sendphoto(str_fpath)
        except TimeoutException as e:
            telegram_bot_sendtext(e)

    driver.quit()


if __name__ == "__main__":
    # Web Scraping
    name_list = []
    url_list  = []
    name_list.append('Volvic')
    url_list.append('https://www.flaschenpost.de/volvic/volvic-naturelle')
    name_list.append('Spezi')
    url_list.append('https://www.flaschenpost.de/paulaner-spezi/paulaner-spezi')
    name_list.append('FritzKola')
    url_list.append('https://www.flaschenpost.de/fritz-kola/fritz-kola')

    fulllist = np.stack((name_list, url_list), axis=1)
    for name, url in fulllist:
        get_flaschenpost_price(name, url)

    print('Wieder mal gescraped xD')