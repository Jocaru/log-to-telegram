#!/usr/bin/env python

import logging
import os
import time

from telegram.ext import Updater

TELEGRAM_API_KEY = os.getenv('TELEGRAM_API_KEY')
CHAT_ID = os.getenv('CHAT_ID')

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

def follow(thefile):
    thefile.seek(0, os.SEEK_END)

    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue

        yield line

if __name__ == '__main__':
    updater = Updater(TELEGRAM_API_KEY)

    logfile = open("/app/log/log.txt","r")
    loglines = follow(logfile)

    for line in loglines:
        updater.bot.send_message(chat_id=CHAT_ID, text=f"```\n{line}\n```", parse_mode='MarkdownV2')
        print(line)