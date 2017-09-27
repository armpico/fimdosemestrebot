import logging
from telegram.ext import Updater, CommandHandler, MessageHandler
from telegram.ext import Filters, Job

import core
import config

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG)
logger = logging.getLogger(__name__)

def error_callback(bot, update, error):
    logging.error(error)

updater = Updater(token=config.FDS_TOKEN)
dp = updater.dispatcher
job = updater.job_queue

dp.add_error_handler(error_callback)
dp.add_handler(CommandHandler('start', core.start))
dp.add_handler(CommandHandler('set', core.set_date))
dp.add_handler(CommandHandler('help', core.get_help))

updater.start_polling()
updater.idle()
