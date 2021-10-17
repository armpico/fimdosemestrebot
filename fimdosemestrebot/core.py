import re, pytz
import fimdosemestrebot.strings as strings
import fimdosemestrebot.config as config

from logging import info
from datetime import datetime, date
from telegram import InlineQueryResultArticle, InputTextMessageContent, ParseMode

tz = pytz.timezone('America/Sao_Paulo')


def start(bot, update):
    update.message.reply_text(check())
    update.message.reply_text(strings.INLINE)
    info(str(update))


def get_start_date():
    file = open('file.date', 'r')
    contents = file.readline().split()
    date = contents[0] + ' ' + contents[1]
    start_date = datetime.strptime(date, '%d-%m-%Y %H:%M')
    return tz.localize(start_date)


# Read file and return datetime object
def get_end_date():
    file = open('file.date', 'r')
    contents = file.readline().split()
    date = contents[2] + ' ' + contents[3]
    end_date = datetime.strptime(date, '%d-%m-%Y %H:%M')
    return tz.localize(end_date)


# Function called when bot is used inline
def inline(bot, update):
    phrase = check()

    results = []
    results.append(
        InlineQueryResultArticle(
            id=1,
            title=phrase,
            input_message_content=InputTextMessageContent(phrase),
            parse_mode=ParseMode.MARKDOWN,
        )
    )
    info(str(update))
    update.inline_query.answer(results)


# Returns a string according to n of days left
def check():
    string = strings.START_STRINGS
    date = get_start_date()
    if (today() - get_start_date()).total_seconds() > 0:
        string = strings.END_STRINGS
        date = get_end_date()

    days_left = date - today()

    date = date.strftime("%d/%m/%y")
    date_str = f"({date})"
    time_left = ''
    if days_left.days < 0:
        return f'{strings.PALM_TREE} O semestre {string[2]} da UFSC {string[0]}! {date_str} {strings.CONFETTI} {strings.HORN}'
    elif days_left.days == 0:
        hours_left = int(days_left.total_seconds() // 3600)
        if hours_left == 1:
            time_left = str(hours_left) + " hora"
        else:
            time_left = str(hours_left) + " horas"
    elif days_left.days == 1:
        time_left = str(days_left.days) + " dia"
    else:
        time_left = str(days_left.days) + " dias"
    return f'{strings.PALM_TREE} O semestre {string[2]} da UFSC {string[1]} em {time_left} {date_str}'


def today():
    return datetime.now(tz=tz)


# Used to change the target date
def set_date(bot, update, job_queue, chat_data):
    if str(update.message.chat.id) == config.MAINTAINER:
        contents = update.message.text.strip('/set ')
        split = contents.split()
        update.message.reply_text("Set start date as: " + split[0] + ' ' + split[1])
        update.message.reply_text("Set end date as: " + split[2] + ' ' + split[3])
        file = open('file.date', 'w')
        file.write(contents)
    else:
        update.message.reply_text(
            strings.DENIED + "\nYour id: " + str(update.message.chat.id)
        )


def get_help(bot, update):
    update.message.reply_text(strings.HELP_TXT)
