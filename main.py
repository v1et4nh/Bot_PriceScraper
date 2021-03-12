import requests
import pathlib
import os
from datetime import datetime
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup

bot_token = '1698488378:AAF7ljXq4ikA-nUBNvP7ogATeS9txUw0gYc'
bot_chatID = '383615621'


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


def get_flaschenpost_price(url):
    os.environ['MOZ_HEADLESS'] = '1'  # Run Firefox in the background
    driver = webdriver.Firefox(service_log_path="C:\\Users\\Viet Anh\\PycharmProjects\\TelegramBot\\geckodriver.log")
    driver.get(url)
    wait = WebDriverWait(driver, 10)
    zipcode_input = wait.until(EC.presence_of_element_located((By.ID, "validZipcode")))
    sleep(1)
    zipcode_input.send_keys('80807')
    driver.find_element_by_class_name("fp-button").click()
    try:
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "fp_article_price")))
        pricedict = driver.find_elements_by_class_name("fp_article_price")

        for price_idx in range(len(pricedict)):
            current_price = pricedict[price_idx].text
            current_price.replace('€', '').strip()
            current_price.replace(',', '.').strip()
            # if float(current_price) < 5:
            if True:
                # Make screenshot
                str_fpath = get_savepath()
                driver.save_screenshot(str_fpath)
                telegram_bot_sendtext('Neuer Preis')
                telegram_bot_sendphoto(str_fpath)
                break
    except Exception:
        try:
            str_avail = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "fp_article_outOfStock")))
            telegram_bot_sendtext(str_avail.text)
            str_fpath = get_savepath()
            driver.save_screenshot(str_fpath)
            telegram_bot_sendphoto(str_fpath)
        except TimeoutException as e:
            telegram_bot_sendtext(e)

    driver.quit()


if __name__ == "__main__":
    # Web Scraping
    url = 'https://www.flaschenpost.de/volvic/volvic-naturelle'
    # url = 'https://www.flaschenpost.de/aera/aerastill'
    get_flaschenpost_price(url)
    print("xD")
