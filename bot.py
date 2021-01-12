import time

import telebot

from gnews import get_msg, get_news
from read_token import read_token_from_config_file
from stats import get_country_stat, get_state_list, get_state_stat

config = "config.cfg"
TOKEN = read_token_from_config_file(config)
bot = telebot.TeleBot(TOKEN, threaded=False)


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(
        message.chat.id,
        'Hello  @'+str(message.from_user.username) +
        "\nGreetings! I can show you Trending and Reliable news about Covid-19. \n" +
        'For more details press /help or type help.'
    )
    help_command(message)


@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(
        message.chat.id,
        'To Receieve the trending news about Covid-19 press <b>/news</b> or type news.\n' +
        'To see the details of developer and credits press <b>/credits</b> or type credits.\n' +
        'To get statistics press <b>/stats</b> or type stats.\n',
        parse_mode='HTML'
    )


@bot.message_handler(commands=['credits'])
def credit_command(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(
        telebot.types.InlineKeyboardButton(
            'Message the developer', url="t.me/bishal2020"
        )
    )
    bot.send_message(
        message.chat.id,
        'Powered By - Goggle News API.\n\n' +
        'Covid Statistics data Source: api.covid19india.org.\n\n' +
        'Hosted on  - Heroku\n\n' +
        'If you have any Query Click the Button below to contact the develover',
        reply_markup=keyboard
    )


@bot.message_handler(commands=['news'])
def news_command(message):
    bot.send_message(message.chat.id, "Wait! Fetching news!")
    news_data = get_news()
    # show the bot "typing" (max. 5 secs)
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(3)
    if len(news_data) > 0:
        msg = get_msg(news_data)
        bot.send_message(message.chat.id, msg, parse_mode='HTML')
    else:
        msg = "Sorry! Problem Fetching the News!"
        bot.send_message(message.chat.id, msg)


@bot.message_handler(commands=['stats'])
def stats_command(message):
    bot.send_message(message.chat.id, "Wait! Fetching Data!")
    country_stat = get_country_stat()
    # show the bot "typing" (max. 5 secs)
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(3)
    bot.send_message(message.chat.id, country_stat, parse_mode='HTML')


help_command_list = ['help', 'help me', 'please help',
                     'what can you do', 'can you help me', 'tell me what can you do']


@bot.message_handler(func=lambda message: message.text.lower() in help_command_list)
def help_default(message):
    help_command(message)


news_command_list = ['news', 'news now',
                     'give me updates', 'news update', 'get the news']


@bot.message_handler(func=lambda message: message.text.lower() in news_command_list)
def news_default(message):
    news_command(message)


credit_command_list = ['who made you', 'who created you',
                       'developer of you', 'what are the sources of data', 'credits']


@bot.message_handler(func=lambda message: message.text.lower() in credit_command_list)
def credit_default(message):
    credit_command(message)


start_command_list = ['hi', 'hello', 'hey',
                      'start', 'covind', 'start bot', 'on', 'covind']


@bot.message_handler(func=lambda message: message.text.lower() in start_command_list)
def start_default(message):
    start_command(message)


stats_command_list = ['stats', 'statistics', 'deaths',
                      'affected', 'recovered', 'india statistics']


@bot.message_handler(func=lambda message: message.text.lower() in stats_command_list)
def start_default(message):
    stats_command(message)


@bot.message_handler(func=lambda message: True)
def command_default(message):
    bot.send_message(message.chat.id, "I don't understand \"" +
                     message.text + "\"\nMaybe try the help page at /help")


bot.polling()
