import telebot.types
from telebot import TeleBot
from bot.models import *
from django.core.management.base import BaseCommand
from ...models import *
from time import sleep
from .bot import bot, CHANEL_TO


while True:
    sleep(2)
    chanel_posts = ChanelPost.objects.all()
    for post in chanel_posts:
        if post.published == False:
            info = bot.send_message(CHANEL_TO, post.origin_post.text)
            post.self_post_id = info.id
            post.published = True
            post.save()
        if post.edited:
            bot.edit_message_text(chat_id=CHANEL_TO, message_id=post.self_post_id, text=post.origin_post.text)
            post.edited = False
            post.save()