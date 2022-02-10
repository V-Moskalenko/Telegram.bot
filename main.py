import requests
import telebot
import datetime
from telebot import types
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

DATA = {
    "Брязу Наталья": "23.01",
    "Давыденко Екатерина": "27.01",
    "Хачатрян Анастасия": "4.02",
    "Москаленко Вадим": "7.02",
    "Матренинская Мария": "20.02",
    "Медведева Таня": "19.03",
    "Риттер Анна": "14.04",
    "Деникаева Рита": "17.04",
    "Московкина Нина": "4.05",
    "Новикова Наташа": "15.05",
    "Лавринова Марина": "16.05",
    "Миронова Наташа": "28.05",
    "Соколенко Любовь": "1.06",
    "Седова Галина": "25.06",
    "Костынюк Оля": "26.06",
    "Хутова Настя": "11.07",
    "Александрова Жанна": "24.07",
    "Вершняк Катя":"28.07",
    "Юрикова Рита":"31.07",
    "Кузьмичева Екатерина": "11.09",
    "Москаленко Елена": "5.10",
    "Романова Анастасия": "29.10",
    "Азаров Константин": "6.11",
    "Тороп Юлия": "11.11"}


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton("Какая погода в Тамани❓")
    btn2 = types.KeyboardButton("Какая погода в Москве❓")
    btn3 = types.KeyboardButton("Когда у всех дни рождения? 🎂")
    btn4 = types.KeyboardButton("У кого в этом месяце день рождения? 🍰")
    btn5 = types.KeyboardButton("У кого в следующем месяце день рождения? 🧁")
    markup.add(btn1, btn2, btn3, btn4, btn5)
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! Я твой помощник по Департаменту, пожалуйста выбери кнопку вопроса".format(
                         message.from_user), reply_markup=markup)
@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "Какая погода в Тамани❓"):
        bot.send_message(message.chat.id, f'В Тамани сейчас {what_weather("Тамань")}')
    elif (message.text == "Какая погода в Москве❓"):
        bot.send_message(message.chat.id, f'В Москве сейчас {what_weather("Москва")}')
    elif (message.text == "Когда у всех дни рождения? 🎂"):
        bot.send_message(message.chat.id, f'Дни рождения: \n {all_bd()}')
    elif (message.text == "У кого в этом месяце день рождения? 🍰"):
        bot.send_message(message.chat.id, f'Дни рождения: \n {bd_month()}')
    elif (message.text == "У кого в следующем месяце день рождения? 🧁"):
        bot.send_message(message.chat.id, f'Дни рождения: \n {bd_nextmonth()}')

def all_bd():
    itog = '\n'
    for key, value in DATA.items():
        k = value.split(".")
        if k[1] == "01":
            itog += str(key) + ' 🎂 ' + str(k[0]) +" января\n"
        elif k[1] == "02":
            itog += str(key) + ' 🎂 '+ str(k[0]) +" февраля\n"
        elif k[1] == "03":
            itog += str(key) + ' 🎂 '+ str(k[0]) +" марта\n"
        elif k[1] == "04":
            itog += str(key) + ' 🎂 '+ str(k[0]) +" апреля\n"
        elif k[1] == "05":
            itog += str(key) + ' 🎂 '+ str(k[0]) +" мая\n"
        elif k[1] == "06":
            itog += str(key) + ' 🎂 '+ str(k[0]) +" июня\n"
        elif k[1] == "07":
            itog += str(key) + ' 🎂 '+ str(k[0]) +" июля\n"
        elif k[1] == "08":
            itog += str(key) + ' 🎂 '+ str(k[0]) +" августа\n"
        elif k[1] == "09":
            itog += str(key) + ' 🎂 '+ str(k[0]) +" сентября\n"
        elif k[1] == "10":
            itog += str(key) + ' 🎂 '+ str(k[0]) +" октября\n"
        elif k[1] == "11":
            itog += str(key) + ' 🎂 '+ str(k[0]) +" ноября\n"
        elif k[1] == "12":
            itog += str(key) + ' '+ str(k[0]) +"декабря\n"
    return itog

def bd_month():
    dt_now = datetime.datetime.now()
    cr_dt_now = dt_now.strftime('%m')
    itog ='\n'
    for key, value in DATA.items():
        k = value.split(".")
        if k[1] == cr_dt_now:
            itog += str(key) + ' 🍰 ' + str(k[0]) + " числа\n"
    return itog

def bd_nextmonth():
    dt_now = datetime.datetime.now()
    cr_dt_now = ''
    if dt_now.strftime('%m')[0] == '0':
        cr_dt_now = '0' + str(int(dt_now.strftime('%m')) + 1)
    elif dt_now.strftime('%m')[0] != '0':
        cr_dt_now = str(int(dt_now.strftime('%m')) + 1)
    elif dt_now.strftime('%m') == '12':
        cr_dt_now = '01'
    itog ='\n'
    for key, value in DATA.items():
        k = value.split(".")
        if k[1] == cr_dt_now:
            itog += str(key) + ' 🧁 ' + str(k[0]) + " числа\n"
    return itog

def what_weather(city):
    url = f'http://wttr.in/{city}'
    weather_parameters = {
        'format': 2,
        'M': ''
    }
    try:
        response = requests.get(url, params=weather_parameters)
    except requests.ConnectionError:
        return '<сетевая ошибка>'
    if response.status_code == 200:
        return response.text.strip()
    else:
        return '<ошибка на сервере погоды>'


if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=False, interval=0, timeout=20)
        except:
            print('Error')
