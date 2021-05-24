from main import Flaschenpost, bot
from time import sleep


# Single
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Hi and welcome to my channel :)')


@bot.message_handler(commands=['volvic'])
def run_flaschenpost(message):
    bot.send_message(message.chat.id, 'Flaschenpost Request started... Please wait..')
    list_beverage = [('Volvic', 'https://www.flaschenpost.de/volvic/volvic-naturelle', 99)]
    flaschenpost = Flaschenpost(list_beverage=list_beverage, run_background=True)
    flaschenpost.run_query(message.chat.id)
    print('Finished scraping')


# Channel
@bot.channel_post_handler(commands=['volvic'])
def run_flaschenpost(message):
    bot.send_message(message.chat.id, 'Flaschenpost Request started... Please wait..')
    list_beverage = [('Volvic', 'https://www.flaschenpost.de/volvic/volvic-naturelle', 99)]
    flaschenpost = Flaschenpost(list_beverage=list_beverage, run_background=True)
    flaschenpost.run_query(message.chat.id)
    print('Finished scraping')


@bot.message_handler(func=lambda message: True)
def unknown_command(message):
    bot.send_message(message.chat.id, 'Unknown Command...Please try again.')


# Start Bot
print('Bot Listener started..')
while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(e)
        sleep(5)
        print('Bot restart..')
