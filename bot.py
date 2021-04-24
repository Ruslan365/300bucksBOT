import config
import telebot
import requests
import json

bot = telebot.TeleBot(config.token)
keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('Узнать курс валют', 'Пересчитать свою валюту в другую')

responce = requests.get(config.url)

val = json.loads(responce.text)
print(val["rates"]["EUR"])





@bot.message_handler(commands=["start"])
def get_text_messages(message):
    bot.send_message(message.from_user.id, "Доброго времени суток, выберете желаемую функцию.", reply_markup=keyboard1)





@bot.message_handler(content_types=['text'])
def Check_valute(message):
    check=int(0)
    if message.text == "Узнать курс валют":
        bot.send_message(message.chat.id, responce.text)
        check=1
    else:
        bot.send_message(message.chat.id, "Работает")
        check=0

    return check








if __name__ == '__main__':
   bot.polling(none_stop=True, interval=0)

