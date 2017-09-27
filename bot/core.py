from datetime import datetime
import pymongo

import strings

# conn = pymongo.MongoClient()
# db = conn.get_default_database()
# collection = db.date

end_string = '7-12-2017'
end_datetime = datetime.strptime(end_string , '%d-%m-%Y')
end_string = end_datetime.strftime('%d-%m-%Y')

def start(bot, update):
    update.message.reply_text(strings.GREETING_TXT)
    update.message.reply_text(end_string)
    time_delta = end_datetime - datetime.today()
    results = str(time_delta).split(' ')
    update.message.reply_text(f"O semestre de 2017 da UFSC acaba em {results[0]} dias.")

def get_help(bot, update):
    pass

def set_date(bot, update):
    pass

