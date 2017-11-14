import re
import strings

from datetime import datetime, date
from telegram import InlineQueryResultArticle, InputTextMessageContent, ParseMode

TODAY = date.today()
END_STRING = '07-12-2017'
END_DATETIME = datetime.strptime(END_STRING, '%d-%m-%Y')
END_STRING = END_DATETIME.strftime('%d-%m-%Y')

def result():
    time_delta = END_DATETIME - datetime.today()
    results = str(time_delta).split(' ')
    return results[0]

def start(bot, update):
    days_left = result()
    update.message.reply_text(check(days_left))

def inline(bot, update):
    days_left = result()

    username = update.inline_query.from_user.username
    if username is None:
        username = update.inline_query.from_user.first_name
    phrase = check(days_left)

    results = []
    results.append(
        InlineQueryResultArticle(
            id=1,
            title=check(days_left),
            input_message_content=InputTextMessageContent(phrase),
            parse_mode=ParseMode.MARKDOWN)
    )

    update.inline_query.answer(results)

def check(days_left):
    if int(days_left) >= 0:
        return f'O semestre de {TODAY.year} da UFSC acaba em {days_left} dias.'
    return strings.HORN + f'O semestre de {TODAY.year} da UFSC acabou' + strings.PALM_TREE

def get_help(bot, update):
    update.message.reply_text(strings.HELP_TXT)
