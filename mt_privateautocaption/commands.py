#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (C) PR0FESSOR-99

import os

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery




@Client.on_message(filters.private & filters.command("start"))
async def start_meg(client, update):
    text = f"""<b> 👋Hello {update.from_user.mention}\n\nI am an AutoCaption bot\n\nAll you have to do is add me to your channel and I will show you my power\n\nFor more info check help Button\n\n</b>"""
    await update.reply_text(
        text=text
  )

