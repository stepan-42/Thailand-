import telebot
from telebot import types
from datetime import datetime, timezone, timedelta



bot = telebot.TeleBot('7762704477:AAE0TyUIws5hgJid7VlUwhnp5XH5Nv3HcR0')


@bot.message_handler(commands=['start'] )
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Русский 🇷🇺')
    btn2 = types.KeyboardButton('English 🇬🇧')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text='Choose your language / Выберите язык', reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in ['Русский 🇷🇺', 'English 🇬🇧'])
def handle_language(message):
    global language
    language = message.text
    if language == 'Русский 🇷🇺':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Пхукет')
        btn2 = types.KeyboardButton('Чангмай')
        btn3 = types.KeyboardButton('Банкок')
        btn4 = types.KeyboardButton('Вернутся в главное меню')

        markup.add(btn1, btn2, btn3, btn4)
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Phuket')
        btn2 = types.KeyboardButton('Chiang Mai')
        btn3 = types.KeyboardButton('Bangkok')
        btn4 = types.KeyboardButton('Back to main menu')

        markup.add(btn1, btn2, btn3, btn4)

    if language == 'Русский 🇷🇺':
        bot.send_message(message.chat.id, text='Где вы находитесь?', reply_markup=markup)

    elif message.text == 'Вернутся в главное меню' or message.text == 'Back to main menu':
        start_message(message)
    elif language == 'English 🇬🇧':
        bot.send_message(message.chat.id, text='Where are you located?', reply_markup=markup)




@bot.message_handler(func=lambda message: message.text in ['Phuket', 'Chiang Mai', 'Bangkok', 'Пхукет', 'Чангмай', 'Банкок'])
def handle_location(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    global place

    place = message.text
    if language == 'Русский 🇷🇺':
        btn1 = types.KeyboardButton('Пляж')
        btn2 = types.KeyboardButton('Кафе')
        btn3 = types.KeyboardButton('Отель')
        btn4 = types.KeyboardButton('Вернутся в главное меню')

        markup.add(btn1, btn2, btn3, btn4)
    elif language == 'English 🇬🇧':
        btn1 = types.KeyboardButton('Beach')
        btn2 = types.KeyboardButton('Cafes')
        btn3 = types.KeyboardButton('Hotel')
        btn4 = types.KeyboardButton('Back to main menu')
        markup.add(btn1, btn2, btn3, btn4)
    elif message.text == 'Вернутся в главное меню' or message.text == 'Back to main menu':
        start_message(message)


    if language == 'Русский 🇷🇺':
        bot.send_message(message.chat.id, text='Что вас интересует?', reply_markup=markup)
    elif language == 'English 🇬🇧':
        bot.send_message(message.chat.id, text='What are you interested in?', reply_markup=markup)




@bot.message_handler(func=lambda message: message.text in ['Пляж', 'Кафе', 'Отель', 'Beach', 'Cafes', 'Hotel', 'Back to main menu', 'Вернутся в главное меню', 'Назад', 'Back'])
def handle_interest(message):


        # ПЛЯЖ
        if message.text == 'Пляж' and place == "Пхукет":
            bot.send_message(message.chat.id, text='https://www.tripadvisor.ru/Attraction_Review-g1210687-d450974-Reviews-Kata_Beach-Kata_Beach_Karon_Phuket.html')
            now = datetime.now()
            Thailand = timezone(timedelta(hours=7), "Тайланд")
            a = datetime.now(Thailand)
            print(a.strftime("%H:%M:%S %Z"))
            bot.send_message(message.chat.id, a.strftime("%H:%M:%S %Z"))
        elif message.text == 'Пляж' and place == "Чангмай":
            Thailand = timezone(timedelta(hours=7), "Тайланд")
            a = datetime.now(Thailand)
            print(a.strftime("%H:%M:%S %Z"))
            bot.send_message(message.chat.id, a.strftime("%H:%M:%S %Z"))
            bot.send_message(message.chat.id, text='https://www.tripadvisor.ru/Hotel_Review-g293917-d17519162-Reviews-Riverside_Luxury_Pool_Villa_88_Place-Chiang_Mai.html')
        elif message.text == 'Пляж' and  place == "Банкок":
            Thailand = timezone(timedelta(hours=7), "Тайланд")
            a = datetime.now(Thailand)
            print(a.strftime("%H:%M:%S %Z"))
            bot.send_message(message.chat.id, a.strftime("%H:%M:%S %Z"))
            bot.send_message(message.chat.id, text='https://www.tripadvisor.ru/Hotel_Review-g297916-d2644429-Reviews-Tamarina_Resort-Chonburi_Chonburi_Province.html')
        elif message.text == 'Вернутся в главное меню':

            start_message(message)

        # КАФЕ
        elif message.text == 'Кафе' and place == "Пхукет":
            bot.send_message(message.chat.id, text="https://www.tripadvisor.ru/Restaurant_Review-g1215781-d25184563-Reviews-The_5th_Element_Phuket-Phuket_Town_Phuket.html", reply_markup=markup)
            Thailand = timezone(timedelta(hours=7), "Тайланд")
            a = datetime.now(Thailand)
            print(a.strftime("%H:%M:%S %Z"))
            bot.send_message(message.chat.id, a.strftime("%H:%M:%S %Z"))
        elif message.text == 'Кафе' and place == "Чангмай":
            bot.send_message(message.chat.id, text='https://www.tripadvisor.ru/Restaurant_Review-g293917-d25110134-Reviews-Bodhi_Terrace-Chiang_Mai.html')
            Thailand = timezone(timedelta(hours=7), "Тайланд")
            a = datetime.now(Thailand)
            print(a.strftime("%H:%M:%S %Z"))
            bot.send_message(message.chat.id, a.strftime("%H:%M:%S %Z"))
        elif message.text == 'Кафе' and  place == "Банкок":
            bot.send_message(message.chat.id, text='https://www.tripadvisor.ru/Restaurant_Review-g293916-d27039273-Reviews-Babyccino_Co-Bangkok.html')
            Thailand = timezone(timedelta(hours=7), "Тайланд")
            a = datetime.now(Thailand)
            print(a.strftime("%H:%M:%S %Z"))
            bot.send_message(message.chat.id, a.strftime("%H:%M:%S %Z"))
        elif message.text == 'Вернутся в главное меню':
            start_message(message)

        # ОТЕЛЬ
        elif message.text == 'Отель' and place == "Пхукет":
            bot.send_message(message.chat.id, text='https://www.tripadvisor.ru/Hotel_Review-g10804710-d535970-Reviews-Beyond_Karon-Karon_Beach_Karon_Phuket.html')
            Thailand = timezone(timedelta(hours=7), "Тайланд")
            a = datetime.now(Thailand)
            print(a.strftime("%H:%M:%S %Z"))
            bot.send_message(message.chat.id, a.strftime("%H:%M:%S %Z"))
        elif message.text == 'Отель' and place == "Чангмай":
            bot.send_message(message.chat.id, text='https://www.tripadvisor.ru/Hotel_Review-g293917-d7620257-Reviews-Akyra_Manor_Chiang_Mai-Chiang_Mai.html')
            Thailand = timezone(timedelta(hours=7), "Тайланд")
            a = datetime.now(Thailand)
            print(a.strftime("%H:%M:%S %Z"))
            bot.send_message(message.chat.id, a.strftime("%H:%M:%S %Z"))
        elif message.text == 'Отель' and  place == "Банкок":
            bot.send_message(message.chat.id, text='https://www.tripadvisor.ru/Hotel_Review-g293916-d13134217-Reviews-Akara_Hotel-Bangkok.html')
            Thailand = timezone(timedelta(hours=7), "Тайланд")
            a = datetime.now(Thailand)
            print(a.strftime("%H:%M:%S %Z"))
            bot.send_message(message.chat.id, a.strftime("%H:%M:%S %Z"))
        elif message.text == 'Вернутся в главное меню':
            start_message(message)

        # BEACH
        if message.text == 'Beach' and place == "Phuket":
            bot.send_message(message.chat.id, text='https://www.tripadvisor.ru/Attraction_Review-g1210687-d450974-Reviews-Kata_Beach-Kata_Beach_Karon_Phuket.html')
            Thailand = timezone(timedelta(hours=7), "Thailand")
            a = datetime.now(Thailand)
            print(a.strftime("%H:%M:%S %Z"))
            bot.send_message(message.chat.id, a.strftime("%H:%M:%S %Z"))
        elif message.text == 'Beach' and place == "Chiang Mai":
           bot.send_message(message.chat.id, text='https://www.tripadvisor.ru/Hotel_Review-g293917-d17519162-Reviews-Riverside_Luxury_Pool_Villa_88_Place-Chiang_Mai.html')
           Thailand = timezone(timedelta(hours=7), "Thailand")
           a = datetime.now(Thailand)
           print(a.strftime("%H:%M:%S %Z"))
           bot.send_message(message.chat.id, a.strftime("%H:%M:%S %Z"))
        elif message.text == 'Beach' and place == "Bangkok":
            bot.send_message(message.chat.id, text='https://www.tripadvisor.ru/Restaurant_Review-g293916-d27039273-Reviews-Babyccino_Co-Bangkok.html')
            Thailand = timezone(timedelta(hours=7), "Thailand")
            a = datetime.now(Thailand)
            print(a.strftime("%H:%M:%S %Z"))
            bot.send_message(message.chat.id, a.strftime("%H:%M:%S %Z"))
        elif message.text == 'Back to main menu':
            start_message(message)

        # CAFES
        elif message.text == 'Cafes' and place == "Phuket":
            bot.send_message(message.chat.id, text='https://www.tripadvisor.ru/Restaurant_Review-g1215781-d25184563-Reviews-The_5th_Element_Phuket-Phuket_Town_Phuket.html", reply_markup=markup')
            Thailand = timezone(timedelta(hours=7), "Thailand")
            a = datetime.now(Thailand)
            print(a.strftime("%H:%M:%S %Z"))
            bot.send_message(message.chat.id, a.strftime("%H:%M:%S %Z"))
        elif message.text == 'Cafes' and place == "Chiang Mai":
            bot.send_message(message.chat.id, text='https://www.tripadvisor.ru/Restaurant_Review-g293917-d25110134-Reviews-Bodhi_Terrace-Chiang_Mai.html')
            Thailand = timezone(timedelta(hours=7), "Thailand")
            a = datetime.now(Thailand)
            print(a.strftime("%H:%M:%S %Z"))
            bot.send_message(message.chat.id, a.strftime("%H:%M:%S %Z"))
        elif message.text == 'Cafes' and place == "Bangkok":
            bot.send_message(message.chat.id, text='https://www.tripadvisor.ru/Restaurant_Review-g293916-d27039273-Reviews-Babyccino_Co-Bangkok.html')
            Thailand = timezone(timedelta(hours=7), "Thailand")
            a = datetime.now(Thailand)
            print(a.strftime("%H:%M:%S %Z"))
            bot.send_message(message.chat.id, a.strftime("%H:%M:%S %Z"))
        elif message.text == 'Back to main menu':
            start_message(message)
        # HOTEL
        elif message.text == 'Hotel' and place == "Phuket":
                bot.send_message(message.chat.id, text='https://www.tripadvisor.ru/Hotel_Review-g10804710-d535970-Reviews-Beyond_Karon-Karon_Beach_Karon_Phuket.html')
                Thailand = timezone(timedelta(hours=7), "Thailand")
                a = datetime.now(Thailand)
                print(a.strftime("%H:%M:%S %Z"))
        elif message.text == 'Hotel' and place == "Chiang Mai":
            bot.send_message(message.chat.id, text='https://www.tripadvisor.ru/Hotel_Review-g293917-d7620257-Reviews-Akyra_Manor_Chiang_Mai-Chiang_Mai.html')
            Thailand = timezone(timedelta(hours=7), "Thailand")
            a = datetime.now(Thailand)
            print(a.strftime("%H:%M:%S %Z"))
            bot.send_message(message.chat.id, a.strftime("%H:%M:%S %Z"))
        elif message.text == 'Hotel' and place == "Bangkok":
            bot.send_message(message.chat.id, text='https://www.tripadvisor.ru/Hotel_Review-g293916-d13134217-Reviews-Akara_Hotel-Bangkok.html')
            Thailand = timezone(timedelta(hours=7), "Thailand")
            a = datetime.now(Thailand)
            print(a.strftime("%H:%M:%S %Z"))
            bot.send_message(message.chat.id, a.strftime("%H:%M:%S %Z"))





if __name__ == '__main__':
    bot.infinity_polling()