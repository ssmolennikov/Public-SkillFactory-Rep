import telebot
from config import TOKEN, currencies
from extensions import APIException, Converter

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message: telebot.types.Message):
    text = 'Привет!' \
           '\n\nЯ — валютный бот, могу помочь перевести тебе валюты, например, из рубля в доллар.' \
           '\n\nДанные обновляются регулярно, поэтому итоговая сумма каждый раз может быть разной.' \
           '\nТекущий курс я беру отсюда: https://clck.ru/Gbrwu' \
           '\n\nВ будущем, я буду становиться умнее и смогу переводить больше валют, если так решит мой создатель.' \
           '\n\nЧтобы узнать как мной пользоваться напиши или нажми: /help' \
           '\nЧтобы узнать доступные валюты напиши или нажми: /value'
    bot.reply_to(message, text)


@bot.message_handler(commands=['help'])
def help(message: telebot.types.Message):
    text = 'Для начала работы необходимо ввести команды в формате: ' \
           '\n<Имя валюты, которую будем переводить>; ' \
           '\n<Имя валюты в которую будем переводить>; ' \
           '\n<Количество переводимой валюты>' \
           '\nПример: доллар рубль 100.' \
           '\n\nВвод суммы перевода с десятичными осуществляется при помощи знаков "," или ".".' \
           '\nПример: доллар рубль 101.1 или рубль евро 10,8.' \
           '\n\nДля большего удобства, итоговая сумма сокращена до двух знаков после запятой, то есть до сотых.' \
           '\n\nУвидеть список всех доступных валют: /value'
    bot.reply_to(message, text)


@bot.message_handler(commands=['value'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in currencies.keys():
        text = '\n'.join((text, key))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise APIException('Некорретные данные.\nЧитайте /help.')

        quote, base, amount = values
        total_base = Converter.get_price(quote, base, amount)
    except APIException as e:
        bot.reply_to(message, f'Пользовательская ошибка.\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'Цена {amount} {quote} в {base} - {total_base} {base}'
        bot.send_message(message.chat.id, text)


bot.polling()
