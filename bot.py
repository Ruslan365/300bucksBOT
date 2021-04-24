import config
import telebot
import requests
import json

bot = telebot.TeleBot(config.token)
keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('Узнать курс валют', 'Пересчитать свою валюту в другую')

responce = requests.get(config.url)
val = json.loads(responce.text)



@bot.message_handler(commands=["start"])
def get_text_messages(message):
    bot.send_message(message.from_user.id, "Доброго времени суток, выберете желаемую функцию.", reply_markup=keyboard1)





@bot.message_handler(content_types=['text'])
def Check_valute(message):
    if message.text == "Узнать курс валют":
        bot.send_message(message.chat.id, "Курс Евро: 1 EUR = " + str(round(1/(val["rates"]["EUR"]), 3)) + " рублей")
        bot.send_message(message.chat.id, "Курс Доллара: 1 USD = " + str(round(1/(val["rates"]["USD"]), 3)) + " рублей")

    else:
        bot.send_message(message.chat.id, "Введите значение в рублях: ")
        '''bot.send_message(message.chat.id, "Рубль - > ЕВРО: " + str(resEUR)) 
        bot.send_message(message.chat.id, "Рубль - > ДОЛЛАР: " + str(resUSD))
'''

'''def recount(message):     Функция пересчета валюты(не робит)
    EUR = float(1/(val["rates"]["EUR"]))
    USD = float(1/(val["rates"]["USD"]))
    RUB = float(message.text)
    resEUR = round((RUB * EUR), 3)
    resUSD = round((RUB * USD), 3)
    return resEUR, resUSD
'''


if __name__ == '__main__':
   bot.polling(none_stop=True, interval=0)

