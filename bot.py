import telebot
from telebot import types
import parser

TOKEN = '6803198156:AAH-vbWrtvN9PJZqKISnqw2MUKnJvjdQBOc'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def handle_start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Афиша")
    markup.add(btn1)
    bot.send_message(message.chat.id,
                     'Привет! Я бот. Чтобы получить информацию о двух ближайших мероприятиях нажмите на кнопку "Афиша"',
                     reply_markup=markup)


@bot.message_handler(content_types=['text'])
def handle_text(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Афиша")
    btn2 = types.KeyboardButton("Первое мероприятие")
    btn3 = types.KeyboardButton("Второе мероприятие")
    if message.text == "Афиша":
        markup.add(btn2, btn3)
        parser.poster()
        photo_path = 'choice.png'
        photo = open(photo_path, 'rb')
        bot.send_photo(message.chat.id, photo)
        photo.close()
        bot.send_message(message.chat.id,
                         'Чтобы посмотреть свободные места на мероприятии выберите мероприятие',
                         reply_markup=markup)
    elif message.text == "Первое мероприятие":
        parser.first_event()
        photo_path = 'first.png'
        photo = open(photo_path, 'rb')
        bot.send_photo(message.chat.id, photo)
        photo.close()
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, "Для получения информации о свободных местах или афише нажмите на кнопку",
                         reply_markup=markup)
    elif message.text == "Второе мероприятие":
        parser.second_event()
        photo_path = 'second.png'
        photo = open(photo_path, 'rb')
        bot.send_photo(message.chat.id, photo)
        photo.close()
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, "Для получения информации о свободных местах или афише нажмите на кнопку",
                         reply_markup=markup)
    else:
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, "Для получения информации о свободных местах или афише нажмите на кнопку",
                         reply_markup=markup)


bot.polling(none_stop=True, interval=0)
