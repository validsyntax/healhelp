import telebot
keyboard = telebot.types.ReplyKeyboardMarkup(True)
bot = telebot.TeleBot('5152525989:AAHwAD68j53syI4tX8jI48gYAkb_yYjhx9Q')

id =''

@bot.message_handler(commands=['start'])
def start(message):
    global id
    keyboard_menu = telebot.types.ReplyKeyboardMarkup(True, True)
    keyboard_menu.row('Позвать кресло','Выключить кресло')
    keyboard_menu.row('Выберите, куда ехать', 'Включить кресло')
    bot.send_message(message.chat.id, 'Здравствуйте!Спасибо, что пользуетесь нашим продуктом.', reply_markup=keyboard_menu)


@bot.message_handler(content_types=['text'])
def tex(message):
    global id
    if message.text == 'Выберите, куда ехать':
        kb_menu = telebot.types.ReplyKeyboardMarkup(True, True)
        kb_menu.row('Выберите первую комнату', 'Выберите вторую комнату')
        kb_menu.row('Выберите третью комнату', 'Выберите четвёртую комнату')
        kb_menu.row('Выберите пятую комнату')
        kb_menu.row('Назад в меню')
        bot.send_message(message.chat.id, 'Выбирайте комнату и куда ехать', reply_markup=kb_menu)
        if message.text == 'Выберите первую комнату':
            ka_menu = telebot.types.ReplyKeyboardMarkup(True, True)
            ka_menu.row('Ехать в спальную','Ехать в ванную')
            ka_menu.row('Ехать на кухню','Ехать в тренировочный зал')
            ka_menu.row('Ехать в зону отдыха')
            if message.text == 'Ехать в ванную':
                bot.send_message(message.chat.id, 'Едем в ванную')
            elif message.text == 'Ехать в тренировочный зал':
                bot.send_message(message.chat.id, 'Едем в тренировочный зал')
            elif message.text == 'Ехать на кухню':
                bot.send_message(message.chat.id, 'Едем на кухню')
            elif message.text == 'Ехать в комнату отдыха':
                bot.send_message(message.chat.id, 'Едем в комнату отдыха')
            elif message.text == 'Ехать в спальню':
                bot.send_message(message.chat.id, 'Едем в спальню')
            elif message.text == 'Назад в меню':
                tex(message)
        elif message.text == 'Выберите вторую комнату':
            ka_menu = telebot.types.ReplyKeyboardMarkup(True, True)
            ka_menu.row('Ехать в спальную','Ехать в ванную')
            ka_menu.row('Ехать на кухню','Ехать в тренировочный зал')
            ka_menu.row('Ехать в зону отдыха')
            if message.text == 'Ехать в ванную':
                bot.send_message(message.chat.id, 'Едем в ванную')
            elif message.text == 'Ехать в тренировочный зал':
                bot.send_message(message.chat.id, 'Едем в тренировочный зал')
            elif message.text == 'Ехать на кухню':
                bot.send_message(message.chat.id, 'Едем на кухню')
            elif message.text == 'Ехать в комнату отдыха':
                bot.send_message(message.chat.id, 'Едем в комнату отдыха')
            elif message.text == 'Ехать в спальню':
                bot.send_message(message.chat.id, 'Едем в спальню')
            elif message.text == 'Назад в меню':
                tex(message)
        elif message.text == 'Выберите третью комнату':
            ka_menu = telebot.types.ReplyKeyboardMarkup(True, True)
            ka_menu.row('Ехать в спальную','Ехать в ванную')
            ka_menu.row('Ехать на кухню','Ехать в тренировочный зал')
            ka_menu.row('Ехать в зону отдыха')
            if message.text == 'Ехать в ванную':
                bot.send_message(message.chat.id, 'Едем в ванную')
            elif message.text == 'Ехать в тренировочный зал':
                bot.send_message(message.chat.id, 'Едем в тренировочный зал')
            elif message.text == 'Ехать на кухню':
                bot.send_message(message.chat.id, 'Едем на кухню')
            elif message.text == 'Ехать в комнату отдыха':
                bot.send_message(message.chat.id, 'Едем в комнату отдыха')
            elif message.text == 'Ехать в спальню':
                bot.send_message(message.chat.id, 'Едем в спальню')
            elif message.text == 'Назад в меню':
                tex(message)
        elif message.text == 'Выберите четвёртую комнату':
            ka_menu = telebot.types.ReplyKeyboardMarkup(True, True)
            ka_menu.row('Ехать в спальную','Ехать в ванную')
            ka_menu.row('Ехать на кухню','Ехать в тренировочный зал')
            ka_menu.row('Ехать в зону отдыха')
            if message.text == 'Ехать в ванную':
                bot.send_message(message.chat.id, 'Едем в ванную')
            elif message.text == 'Ехать в тренировочный зал':
                bot.send_message(message.chat.id, 'Едем в тренировочный зал')
            elif message.text == 'Ехать на кухню':
                bot.send_message(message.chat.id, 'Едем на кухню')
            elif message.text == 'Ехать в комнату отдыха':
                bot.send_message(message.chat.id, 'Едем в комнату отдыха')
            elif message.text == 'Ехать в спальню':
                bot.send_message(message.chat.id, 'Едем в спальню')
            elif message.text == 'Назад в меню':
                tex(message)
        elif message.text == 'Выберите пятую комнату':
            ka_menu = telebot.types.ReplyKeyboardMarkup(True, True)
            ka_menu.row('Ехать в спальную','Ехать в ванную')
            ka_menu.row('Ехать на кухню','Ехать в тренировочный зал')
            ka_menu.row('Ехать в зону отдыха')
            if message.text == 'Ехать в ванную':
                bot.send_message(message.chat.id, 'Едем в ванную')
            elif message.text == 'Ехать в тренировочный зал':
                bot.send_message(message.chat.id, 'Едем в тренировочный зал')
            elif message.text == 'Ехать на кухню':
                bot.send_message(message.chat.id, 'Едем на кухню')
            elif message.text == 'Ехать в комнату отдыха':
                bot.send_message(message.chat.id, 'Едем в комнату отдыха')
            elif message.text == 'Ехать в спальню':
                bot.send_message(message.chat.id, 'Едем в спальню')
            elif message.text == 'Назад в меню':
                tex(message)





bot.polling(none_stop=True)