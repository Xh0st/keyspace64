#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.

def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('😁 Hi')


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('🆘 Help!')

def price_command(update, context):
    response = requests.get("https://api.pancakeswap.info/api/tokens/0x8076C74C5e3F5852037F31Ff0093Eeb8c8ADd8D3")
    val = float(response.json()['data']['price'])
    update.message.reply_text('💲 Price: ' + '{:.9f}'.format(val))

def contract(update, context):
    """Send a message when the command /contract is issued."""
    update.message.reply_text('📃 Contract: 0x00000000000000000000000dead')

def site(update, context):
    """Send a message when the command /site is issued."""
    update.message.reply_text('🌐 Website: https://jadeite.site')

def chart(update, context):
    """Send a message when the command /chart  is issued."""
    update.message.reply_text('📈 Chart:' + "\n" + '💩 [PooCoin](https://poocoin.app/tokens/0xB09FE1613fE03E7361319d2a43eDc17422f36B09)' + "\n" +  '📊 [Bogged](https://charts.bogged.finance/?token0xB09FE1613fE03E7361319d2a43eDc17422f36B09)' , parse_mode='MarkdownV2')

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("1860742283:AAGAi1drvCsovYEqMwHhwGEc9UJxBFTb7FQ", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

# on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("contract", contract))
    dp.add_handler(CommandHandler("site", site))
    dp.add_handler(CommandHandler("chart", chart))
    dp.add_handler(CommandHandler("price", price_command))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

# Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if name == '__main__':
    main()