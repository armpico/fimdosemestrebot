from datetime import datetime
import pymongo

import strings

# conn = pymongo.MongoClient()
# db = conn.get_default_database()
# collection = db.date

end_string = '7-12-2017'
end_datetime = datetime.strptime(end_string , '%d-%m-%Y')
end_string = end_datetime.strftime('%d-%m-%Y')

def result():
    time_delta = end_datetime - datetime.today()
    results = str(time_delta).split(' ')
    return results[0]

def start(bot, update):
    update.message.reply_text(strings.GREETING_TXT)
    update.message.reply_text("O semestre de 2017 da UFSC acaba em {} dias.".format(result()))

def inline(bot, update):
    query = update.inline_query.query
    results = list()

    username = update.inline_query.from_user.username
    phrase = '@{username}, faltam {} dias para o fim do semestre da UFSC.'.format(result())

    results.append(InlineQueryResultArticle(id=1,
        title='Fim do semestre em {} dias'.format(result()),
        input_message_content=InputTextMessageContent(result(), parse_mode=ParseMode.MARKDOWN)))

def get_help(bot, update):
    update.message.reply_text(strings.HELP_TXT)

def set_date(bot, update):
    pass

