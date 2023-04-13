import telebot

token = '6219748190:AAGNRV7_VUZfMGcoC5utb3bf0zw2vBQxnuA'

bot = telebot.TeleBot(token)


@bot.message_handler(content_types=["text"])
def echo(message):
    bot.send_message(message.chat.id, message.text)


bot.polling(none_stop=True)
