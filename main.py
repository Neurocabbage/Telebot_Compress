import telebot
from config import TOKEN
import random
bot = telebot.TeleBot(TOKEN)


"""Команда СТАРТ"""


@bot.message_handler(commands=['start'])
def welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

    item1 = telebot.types.KeyboardButton('Рандомное число')
    item2 = telebot.types.KeyboardButton('Кинуть кость')
    item3 = telebot.types.KeyboardButton('Сжать строку')

    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id, 'Добро пожаловать! Выберите нужный вам пункт меню: ', reply_markup=markup)


def random_number(message):
    bot.send_message(message.chat.id, str(random.randint(1, 10)))

def compress(message):
    str = convert(message.text)
    bot.send_message(message.chat.id, str)


def convert(string):
    # check = lambda string: not all('A'<=x<='Z' for x in string.upper())
    # try:
    #     if check != True:
    #         print('строка должна состоять из букв A-Z:')
    #     else:
            result = []
            last_sym = string[0]
            count = 0
            for sym in (list(string)):
                if last_sym and sym != last_sym:
                    if count == 1:
                        result.append(last_sym)
                    else:
                        result.append(last_sym + str(count))
                    count = 1
                    last_sym = sym
                else:
                    count += 1
            return ''.join(result)
    # except:
    #     print('Какая-то ошибка')




@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'привет':
        bot.send_message(message.chat.id, 'Привет, как дела?')
    elif message.text == 'Рандомное число':
        random_number(message)
    elif message.text == 'Кинуть кость':
        bot.send_message(message.chat.id, f'Вам выпало {(random.randint(1, 6))}')
    elif message.text == 'Сжать строку':
        msg = bot.send_message(message.chat.id, 'Введи строку для сжатия.')
        bot.register_next_step_handler(msg, compress)
    else:
        bot.send_message(message.chat.id, 'Данный функционал находится в разработке')


bot.polling(none_stop=True)
