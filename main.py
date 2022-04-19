import telebot
keyboard = telebot.types.ReplyKeyboardMarkup(True)
bot = telebot.TeleBot('5152525989:AAHwAD68j53syI4tX8jI48gYAkb_yYjhx9Q')

id =''
keyboard.row('Ехать в ванную')
keyboard.row('Ехать в тренировочный зал')
keyboard.row('Ехать на кухню')
keyboard.row('Ехать в комнату отдыха')
keyboard.row('Ехать в спальню')
keyboard.row('Позвать кресло')
keyboard.row('Отправить кресло на зарядную станцию')
keyboard.row('Выключить кресло')
@bot.message_handler(commands=['start'])
def start(message):
    global id
    id = message.chat.id
    bot.send_message(message.chat.id, 'Привет! Спасибо, что пользуетесь нашим продуктом.', reply_markup=keyboard)
@bot.message_handler(content_types=['text'])
def tex(message):
    global id
    if message.text == 'Позвать кресло':
        bot.send_message(message.chat.id,'Кресло едет к вам')
    elif message.text == 'Отправить кресло на зарядную станцию':
        bot.send_message(message.chat.id,'Кресло направляется на зарядную станцию')
    elif message.text == 'Выключить кресло':
        bot.send_message(message.chat.id,'Кресло выключается')
    elif message.text == 'Ехать в ванную':
        bot.send_message(message.chat.id, 'Едем в ванную')
    elif message.text == 'Ехать в тренировочный зал':
        bot.send_message(message.chat.id, 'Едем в тренировочный зал')
    elif message.text == 'Ехать на кухню':
        bot.send_message(message.chat.id, 'Едем на кухню')
    elif message.text == 'Ехать в комнату отдыха':
        bot.send_message(message.chat.id, 'Едем в комнату отдыха')
    elif message.text == 'Ехать в спальню':
        bot.send_message(message.chat.id, 'Едем в спальню')

    @bot.message_handler(commands=['info'])
    def info(message):
        global id
        id = message.chat.id
        inline = telebot.types.InlineKeyboardMarkup()
        item1 = telebot.types.InlineKeyboardButton(text='Позвать кресло', callback_data='Кресло успешно позвано')
        item2 = telebot.types.InlineKeyboardButton(text='Отослать кресло обратно',
                                                   callback_data='Кресло успешно вернулось обратно')
        inline.add(item1, item2)
        bot.send_message(message.chat.id, 'Ваш id сохранен', reply_markup=inline)

    # @bot.message_handler(commands=['start'])
    # def start(message):
    #     global id
    #     id = message.chat.id
    #     inline = telebot.types.InlineKeyboardMarkup()
    #     item1 = telebot.types.InlineKeyboardButton(text='INF1', callback_data='info1')
    #     item2 = telebot.types.InlineKeyboardButton(text='INF z     b2', callback_data='info2')
    #     inline.add(item1, item2)
    #     bot.send_message(message.chat.id, 'Что вы хотите про меня узнать?', reply_markup=inline)

    @bot.callback_query_handler(func=lambda call: True)
    def answer(call):
        if call.data == 'info1':
            bot.send_message(call.message.chat.id, 'info1')
        elif call.data == 'info2':
            bot.send_message(call.message.chat.id, 'info2')
@bot.message_handler(content_types=['text'])
def text(message):
    global id
    if message.text == 'Ехать в ванную':
        bot.send_message(message.chat.id, 'Едем  в ванную')
    elif message.text == 'Ехать в тренировочный зал':
        bot.send_message(message.chat.id,'Едем в тренировочный зал')
    elif message.text == 'Ехать на кухню':
        bot.send_message(message.chat.id,'Едем на кухню')
    elif message.text == 'Ехать в комнату отдыха':
        bot.send_message(message.chat.id, 'Едем в комнату отдыха')
    elif message.text == 'Ехать в спальню':
        bot.send_message(message.chat.id, 'Едем в спальню')

@bot.message_handler(commands=['info'])
def info(message):
    global id
    id = message.chat.id
    inline = telebot.types.InlineKeyboardMarkup()
    item1 = telebot.types.InlineKeyboardButton(text='Позвать кресло', callback_data='Кресло успешно позвано')

# @bot.message_handler(commands=['start'])
# def start(message):
#     global id
#     id = message.chat.id
#     inline = telebot.types.InlineKeyboardMarkup()
#     item1 = telebot.types.InlineKeyboardButton(text='INF1', callback_data='info1')
#     item2 = telebot.types.InlineKeyboardButton(text='INF z     b2', callback_data='info2')
#     inline.add(item1, item2)
#     bot.send_message(message.chat.id, 'Что вы хотите про меня узнать?', reply_markup=inline)

@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    if call.data == 'info1':
        bot.send_message(call.message.chat.id, 'info1')
    elif call.data == 'info2':
        bot.send_message(call.message.chat.id, 'info2')
bot.polling(none_stop=True)