import telebot
from MyToken import token
from telebot import types 
import json

def get_list():
    with open('carskg.json', 'rt') as my_file:
        dictionary = json.load(my_file)
        my_file.close()
        data_json = [dict(i) for i in dictionary]
        
    return data_json

bot = telebot.TeleBot(token)

# кнопки для выбора обьявлений
income_keyboard = types.InlineKeyboardMarkup()
data_json = get_list()


income_keyboard = types.InlineKeyboardMarkup()

@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    index = 1
    for title in data_json:
        new_title = title['title']
        button = types.InlineKeyboardButton(f'{index}. {new_title}', callback_data=f'{index}')
        index = index + 1
        income_keyboard.add(button)
    bot.send_message(chat_id, 'Интересны сегодняшние обьявления авто? \n Свежие объявления 👇', reply_markup=income_keyboard)

panel = types.InlineKeyboardMarkup()
button1 = types.InlineKeyboardButton('Вернуться к списку', callback_data='back')
button2 = types.InlineKeyboardButton('Выйти', callback_data='exit')
panel.add(button1, button2)

@bot.callback_query_handler(func=lambda c: True)
def inline(c): #c - message.data
    if c.data == 'back':
        bot.send_message(c.message.chat.id, 'Вы вернулись к списку', reply_markup=income_keyboard)
    elif c.data == 'exit':
        bot.edit_message_text('До свидания!!!', c.message.chat.id, c.message.message_id, reply_markup=None)
    else:
        list_ = get_list()
        list_elem = list(list_[int(c.data) - 1].values())
        bot.send_message(c.message.chat.id, f'Машина: {list_elem[0]} \n Фото: {list_elem[1]} \n Описание: {list_elem[2]} \n Цена: {list_elem[3]}',
                        reply_markup=panel)

    
bot.polling()

