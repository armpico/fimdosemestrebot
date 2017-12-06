import re
import strings

from datetime import datetime, date
from telegram import InlineQueryResultArticle, InputTextMessageContent, ParseMode

TODAY = date.today()
END_STRING = '08-12-2017 23:59:59'
END_DATETIME = datetime.strptime(END_STRING, '%d-%m-%Y %H:%M:%S')

def result():
    time_delta = END_DATETIME - datetime.today()
    return time_delta

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
    if days_left.days < 0:
        ret = f'{strings.PALM_TREE} O semestre de {TODAY.year} da UFSC acabou! {strings.CONFETTI} {strings.HORN}'
    elif days_left.days == 0:
        ret = f'{strings.PALM_TREE} O semestre de {TODAY.year} da UFSC acaba em {int(days_left.total_seconds() // 3600)} horas'
    else:
        ret = f'{strings.PALM_TREE} O semestre de {TODAY.year} da UFSC acaba em {days_left.days} dias'
    return ret

def get_help(bot, update):
    update.message.reply_text(strings.HELP_TXT)
