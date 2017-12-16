import re
import strings
import config

from datetime import datetime, date
from telegram import InlineQueryResultArticle, InputTextMessageContent, ParseMode

TODAY = datetime.today()

def start(bot, update):
    update.message.reply_text(check(get_end_date() - TODAY))

# Read file and return datetime object
def get_end_date():
    file = open('file.date', 'r')
    end_date = datetime.strptime(file.readline(), '%d-%m-%Y %H:%M') # Update end_date
    return end_date

# Function called when bot is used inline
def inline(bot, update):
    phrase = check(get_end_date() - TODAY)

    results = []
    results.append(
        InlineQueryResultArticle(
            id=1,
            title=phrase,
            input_message_content=InputTextMessageContent(phrase),
            parse_mode=ParseMode.MARKDOWN)
    )
    update.inline_query.answer(results)

# Returns a string according to n of days left
def check(days_left):
    adaptive_string = strings.START_STRINGS
    if (get_end_date().month >= 6 and get_end_date().month < 8) or get_end_date().month >= 11:
        adaptive_string = strings.END_STRINGS

    if days_left.days < 0:
        ret = f'{strings.PALM_TREE} O semestre de {get_end_date().year} da UFSC {adaptive_string[0]}! {strings.CONFETTI} {strings.HORN}'
    elif days_left.days == 0:
        ret = f'{strings.PALM_TREE} O semestre de {get_end_date().year} da UFSC {adaptive_string[1]} em {int(days_left.total_seconds() // 3600)} horas'
    else:
        ret = f'{strings.PALM_TREE} O semestre de {get_end_date().year} da UFSC {adaptive_string[1]} em {days_left.days} dias'
    return ret

# Used to change the target date
def set_date(bot, update, job_queue, chat_data):
    if update.message.chat.id == config.MAINTAINER: # replace with environment
        contents = update.message.text.strip('/set ')
        update.message.reply_text("Set date as: " + contents)
        file = open('file.date', 'w')
        file.write(contents)
    else :
        update.message.reply_text(strings.DENIED)

def get_help(bot, update):
    update.message.reply_text(strings.HELP_TXT)
