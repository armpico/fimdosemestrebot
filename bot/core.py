from datetime import datetime, date
from telegram import InlineQueryResultArticle, InputTextMessageContent, ParseMode
from telegram.ext import InlineQueryHandler

import strings

today = date.today()
end_string = '07-12-2017'
end_datetime = datetime.strptime(end_string , '%d-%m-%Y')
end_string = end_datetime.strftime('%d-%m-%Y')

def result():
    time_delta = end_datetime - datetime.today()
    results = str(time_delta).split(' ')
    return results[0]

def start(bot, update):
    days_left = result()
    if int(days_left) >= 0:
        update.message.reply_text(f"O semestre de {today.year} da UFSC acaba em {result()} dias.")
    else:
        update.message.reply_text(strings.HORN + f"O semestre de {today.year} da UFSC acabou." + strings.PALM_TREE)

def inline(bot, update):
    days_left = result()
    query = update.inline_query.query

    username = update.inline_query.from_user.username
    if username is None:
        username = update.inline_query.from_user.first_name
    phrase = f'@{username}, faltam {days_left} dias para o fim do semestre da UFSC.'

    results = list()

    results.append(
        InlineQueryResultArticle(
            id=1,
            title=f'Fim do semestre em {days_left} dias',
            input_message_content=InputTextMessageContent(phrase)))

    update.inline_query.answer(results)

def get_help(bot, update):
    update.message.reply_text(strings.HELP_TXT)
