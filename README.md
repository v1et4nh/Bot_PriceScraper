<!-- Template: https://github.com/othneildrew/Best-README-Template -->

[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/v1et4nh/PriceScraper-Telegram-Bot">
    <img src="images/bot-logo.png" alt="Bot-Logo" width="80" height="80">
  </a>

  <h3 align="center">PriceScraper-Telegram-Bot</h3>

  <p align="center">
    A pricescraper for <a href="https://www.flaschenpost.de">flaschenpost.de</a>
    <br />
    Price alert send via Telegram
    <br />
    <br />
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#what-is-the-project-about-and-why">What is the Project about and why?</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#telegram-bot-configuration">Telegram Bot Configuration</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#configuration-and-usage">Configuration and Usage</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#sources">Sources</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
# What is the Project about and why?
Because I am super lazy I use the service of beverage delivery directly to my door. 
There is only one company in my region: The german www.flaschenpost.de (No Affiliate-Link :P) 
Sometimes it's even cheaper to order on their website than buying in the supermarket. 
But as I already mentioned, I am super lazy and I also don't really want to look up for their super deals all over again..
That's why I started this little project to save my valuable time 
(and maybe also to improve my programming skills. Nice!).

Here is my idea:
* Get the price from www.flaschenpost.de with a webscraper
* If the price falls below a certain amount -> send me a message on telegram
* Message content: Beverage + Price + Url (+ Screenshot of the current page)

And here are my steps:
* Use Python because it's easy
* Use Selenium to navigate through the website and get the price
* Use Telegram API to send messages and images

<!-- GETTING STARTED -->
# Getting Started
So before we jump in, we first need to configure our Telegram Client or Bot...

## Telegram Bot Configuration
* Obviously you need a Telegram Account, so get the app and create a new account
* Once you've installed the app and logged in, you need to create your own bot. For that search for `@BotFather`: <br>
<p align="center"><img src="images/BotFather.png" alt="BotFather" width="383" height="323"></p>

### Create new Bot and get `bot_token`
* Send him a "/start" message or press the Start Button and create a new bot by sending "/newbot"
* Follow the instructions to define a username (which will be displayed in your app) and a unique botname
* Be sure to save the API Token ("Use this token to access the HTTP API"), which will be needed later, that's your `bot_token`

### Get `bot_chatID`
* Now search for your bot (the username you just created) in your telegram app
* Send "/start" or press the Start Button
* Open a new tab and enter `https://api.telegram.org/bot<yourtoken>/getUpdates`
* Replace `yourtoken` with the `bot_token`
* Assume the `bot_token` = 123abc456, then the address would be: <br>`https://api.telegram.org/bot123abc456/getUpdates`
* You will see a json-like format. Look for `"id"`. Thats your `bot_chatID` <br>
Note: You will only see the ID once you send your bot the "/start" message <br> <br>
That's it for now. Keep both your `bot_token` and `bot_chatID` ready for later :)

## Installation
### Clone the repo
   ```shell script
   git clone https://github.com/v1et4nh/PriceScraper-Telegram-Bot
   ```
### Virtual Environment
This chapter is optional but I highly recommend to use it in order to keep your projects tidy.
* Create a new virtual environment
    ```shell script
    $ virtualenv venv
    ```
* Activate the new created virtual environment `venv`
    ```shell script
    # Windows
    $ venv\Scripts\activate.bat
    # Unix
    $ source venv//bin/activate
    ```
* If the virtual environment is activated correctly, your console should look like this:
    ```shell script
    $ (venv)  
    ```

### Dependencies
Install the required dependencies for this project
```shell script
# Virtual environment
$ (venv) pip install -r requirements.txt
  
# Without virtual environment
$ pip install -r requirements.txt
```
 
# Configuration and Usage
* I highly recommend to create a `.env`-file to store your `bot_token` and `bot_chatID` in there:
    ```.env
    TELEGRAM_BOT_TOKEN  = <yourtoken>
    TELEGRAM_BOT_CHATID = <yourchatID>
    ```
    In this way, sensitive information like your token and ID can be hidden, 
    so no one has access to it if you intend to share your project on github. <br>
    Just add the `.env`-file to your `.gitignore` and it won't be considered by git. <br>
    Otherwise, if you only use this locally, you can also just insert your `bot_token` and `bot_chatID` directly in the `main.py`-sourcecode:
    ```python
    16 # Load environment variables
    17 load_dotenv()
    18 bot_token  = <yourtoken>    # Replace with your own bot_token
    19 bot_chatID = <yourchatID>   # Replace with your own bot_chatID
    ```

* Adjust the zipcode in `get_flaschenpost_price`-function:
    ```python
    zipcode_input.send_keys('48151')  # 48151 is an example
    ```
  or add it to your `.env`-file:
    ```.env
    TELEGRAM_BOT_TOKEN  = <yourtoken>
    TELEGRAM_BOT_CHATID = <yourchatID>
    ZIPCODE             = 48151
    ```
  and use this line of code instead:
    ```python
    zipcode_input.send_keys(os.getenv('ZIPCODE'))
    ```

* For testing & debug purpose unhide your browser while running by changing the parameter `background` to False:
    ```python
    for name, url in full_list:
        get_flaschenpost_price(name, url, background=False)
    ```

* Adjust the links and the names in `if __name__ == "__main__"` to your personal preferences:
    ```python
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
    ```

* Adjust the price trigger depending on the type of beverages:
    ```python
    def get_pricetrigger(name):
      pricetrigger = 10000
      if name == 'Volvic':
          pricetrigger = 5
      elif name == 'Spezi':
          pricetrigger = 10
      elif name == 'FritzKola':
          pricetrigger = 18
      return pricetrigger
    ```
  If the price falls below that pricetrigger, it will send a message to your telegram account. <br>
  For testing purpose, set your pricetrigger to a high value to receive an alert.

Once everything is set up, you can just run the script and see what happens. <br>


<!-- CONTACT -->
# Contact
[![LinkedIn][linkedin-shield]][linkedin-url]

Please share your thoughts and connect with me on [linkedin](https://linkedin.com/in/viet-anh-le-cong) 

Viet Anh Le Cong - [@linkedin](https://linkedin.com/in/viet-anh-le-cong) - hello@v1et4nh.de

Project Link: [https://github.com/v1et4nh/PriceScraper-Telegram-Bot](https://github.com/v1et4nh/PriceScraper-Telegram-Bot)

# Sources
* [Medium: Man Hay Hong](https://medium.com/@ManHay_Hong/how-to-create-a-telegram-bot-and-send-messages-with-python-4cf314d9fa3e)
* [Official Telegram Bot Homepage](https://core.telegram.org/bots)

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/viet-anh-le-cong
