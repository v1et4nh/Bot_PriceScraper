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
      <a href="#What is the Project about and why?">What is the Project about and why?</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#Telegram Bot Configuration">Telegram Bot Configuration</a></li>
        <li><a href="#Virtual Environment">Virtual Environment</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## What is the Project about and why?
Because I am super lazy I use the service of beverage delivery directly to my door. 
There is only one company in my region: The german www.flaschenpost.de (No Affiliate-Link :P) 
Sometimes it's even cheaper to order on their website than buying in the supermarket. 
But as I already mentioned, I am super lazy and I also don't really want to look up for their super deals all the time..
That's why I started this little project to save my valuable time 
(and maybe to also improve my programming skills. Nice!).

Here is my idea:
* Get the price from www.flaschenpost.de with a webscraper
* If the price falls below a certain amount -> send me a message on telegram
* Message content: Beverage + Price + Url (+ Screenshot of the current page)

And here are my steps:
* Use Python because it's easy
* Use Selenium to navigate through the website and get the price
* Use Telegram API to send messages and images

<!-- GETTING STARTED -->
## Getting Started
So before we jump in, we first need to configure our Telegram Client or Bot...
1. Obviously you need a Telegram Account, so get the app and register
2. Once you've installed the app, search for `BotFather`: <br>
<img src="images/BotFather.png" alt="BotFather" width="383" height="323">

### Telegram Bot Configuration


### Virtual Environment
* Create a virtual environment
    ```sh
    $ virtualenv venv
    ```
* Activate the new created virtual environment `venv`
    ```sh
    # Windows (CMD.exe)
    $ venv\Scripts\activate.bat
    # Unix
    $ source venv//bin/activate
    ```
* If the virtual environment is activated correctly, your console should look like this:
    ```sh
    $ (venv)  
    ```
* Install the required dependencies for this project
    ```sh
    $ (venv) pip install -r requirements.txt
    ```
 

### Installation

1. tbd
2. Clone the repo
   ```sh
   git clone https://github.com/v1et4nh/PriceScraper-Telegram-Bot
   ```
3. tbd
   ```sh
   tbd
   ```
4. tbd `config.js`
   ```JS
   const API_KEY = 'ENTER YOUR API';
   ```

<!-- USAGE EXAMPLES -->
## Usage

tbd

<!-- CONTACT -->
## Contact

Viet Anh Le Cong - [@linkedin](https://linkedin.com/in/viet-anh-le-cong) - hello@v1et4nh.de

Project Link: [https://github.com/v1et4nh/PriceScraper-Telegram-Bot](https://github.com/v1et4nh/PriceScraper-Telegram-Bot)

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/viet-anh-le-cong
