from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CommandHandler
import requests
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove

TOKEN = "852223716:AAGdVVMYgHTro5LM7yTfmprosTgE9cBTxOA"


def start(update, context):
    reply_keyboard = [["С русского на английский"], ["С английского на русский"]]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text("Вас приветствует бот переводчик. С помощью "
                              "меня вы можете все что угодно перевести с русского на английский и с"
                              " английского на русский. Выберите с какого языка на кокой вы хотите "
                              "что-либо перевести.", reply_markup=markup)


def rus_en(update, context):
    text = update.message.text
    api_key = "trnsl.1.1.20200509T104640Z.f4e0b25c97cc8759.d024296fd1e6e72bc0481dc7857fdbc142af1947"
    url_trans = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    trans_option = {'key': api_key, 'lang': 'en-ru', 'text': text}
    webRequest = requests.get(url_trans, params=trans_option)
    print(webRequest.text)


def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.regex("С русского на английский"), rus_en))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
