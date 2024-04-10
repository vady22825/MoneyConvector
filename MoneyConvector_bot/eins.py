import telebot
from config import keys, TOKEN
from extensions import ConvertionExeption, MoneyConvertion


bot=telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['help', 'start'])
def help_hp(message):
    bot.reply_to(message,'''Привет ! Для того чтобы перевести валюту,
отправьте сообщение в виде:
<имя валюты, цену которой он хочет узнать> 
<имя валюты, в которой надо узнать цену первой валюты> 
<количество первой валюты>.''')

@bot.message_handler(content_types=['document','audio'])
def handle_docs_audio(message):
    bot.reply_to(message,'Нет,введи мне лучше какую валюту ты хочешь перевести !')

@bot.message_handler(content_types=['photo', ])
def haha(message:telebot.types.Message):
    bot.reply_to(message, 'Nice meme XDD')

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text='Доступные волюты:'
    for key in keys.keys():
        text= '\n'.join((text, key))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) !=3:
            raise ConvertionExeption('Слишком много параметров.')

        quote, base, amount = values
        total_base= MoneyConvertion.convert(quote, base, amount)
    except ConvertionExeption as e:
        bot.reply_to(message, f'Ошибка пользователя.\n{e}')

    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:

        total_base = int(amount)*float(total_base)

        text= f'Цена {amount} {quote} в {base} - {total_base}'
        bot.send_message(message.chat.id, text)

bot.polling(none_stop=True)