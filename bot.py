import config
import telebot
import requests
import json

bot = telebot.TeleBot(config.token)
keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('Узнать курс валют', 'Пересчитать свою валюту в другую')

responce = requests.get(config.url)
val = json.loads(responce.text)


def is_number(message):
    try:
        float(message.text)
        return True
    except ValueError:
        return False







@bot.message_handler(commands=["start"])
def get_text_messages(message):
    bot.send_message(message.from_user.id, "Доброго времени суток, выберете желаемую функцию.", reply_markup=keyboard1)


def reccount(message):
    if is_number(message):
        bot.send_message(message.chat.id, "work1")
    else:
        bot.send_message(message.chat.id, "work")
        #она не должна запускаться пока прользватель не введет сообщение


@bot.message_handler(content_types=['text'])
def Check_valute(message):
    if message.text == "Узнать курс валют":
        bot.send_message(message.chat.id, "Курс Евро: 1 EUR = " + str(round(1/(val["rates"]["EUR"]), 3)) + " рублей")
        bot.send_message(message.chat.id, "Курс Доллара: 1 USD = " + str(round(1/(val["rates"]["USD"]), 3)) + " рублей")
    else:
        bot.send_message(message.chat.id, "Введите значение в рублях: ")
        #вот тут функция reccount вызывается




if __name__ == '__main__':
   bot.polling(none_stop=True, interval=0)

