import telebot.types
from telebot import TeleBot
from bot.models import *
from django.core.management.base import BaseCommand
from ...models import *
# import time
import datetime as dt
from .utils import check_time, translate, translate_dict

TOKEN = '6229389421:AAEgn0UhQ5ehVrYmoeuWvffBrPNnfCYRpzk'


try:
    sourse_chanels = Chanel.objects.filter(type='sourse')

    if len(sourse_chanels) == 0:
        while len(sourse_chanels) == 0:
            sourse_chanels = Chanel.objects.filter(type='sourse')
        sourse_chanel = Chanel.objects.filter(type='sourse')[0]
    else:
        sourse_chanel = Chanel.objects.filter(type='sourse')[0]
except:
    pass



bot = TeleBot(TOKEN)


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        try:
            @bot.channel_post_handler(content_types=['text', 'photo'], func=lambda message: message.chat.id == int(sourse_chanel.chanel_id))
            def new_text_post(message):
                chanels = Chanel.objects.filter(type='dependent', active=True)
                if message.photo:
                    post = OriginPost.objects.create(post_id=message.id, text=message.caption, images=message.photo[-1].file_id, chanel=sourse_chanel)
                    for chanel in chanels:
                        now = dt.datetime.now()
                        now = now.time()
                        start_time = chanel.start_time
                        end_time = chanel.end_time
                        if check_time(now, start_time, end_time) or start_time == end_time:
                            text = translate(post.text, sourse_chanel.language, chanel.language)
                            info = bot.send_photo(chanel.chanel_id, photo=post.images, caption=text)
                            chanel_post = ChanelPost(chanel=chanel, self_post_id=info.id, origin_post=post)
                            chanel_post.save()

                else:
                    post = OriginPost.objects.create(post_id=message.id, text=message.text, chanel=sourse_chanel)
                    for chanel in chanels:

                        now = dt.datetime.now()
                        now = now.time()
                        start_time = chanel.start_time
                        end_time = chanel.end_time
                        print(post.text)
                        if check_time(now, start_time, end_time) or start_time == end_time:
                            text = translate(post.text, sourse_chanel.language, chanel.language)
                            info = bot.send_message(chanel.chanel_id, text)
                            chanel_post = ChanelPost(chanel=chanel, self_post_id=info.id, origin_post=post)
                            chanel_post.save()

            @bot.edited_channel_post_handler(content_types=['text', 'photo'], func=lambda message: message.chat.id == int(sourse_chanel.chanel_id))
            def edit_text_post(message):
                chanels = Chanel.objects.filter(type='dependent')
                if message.photo:
                    post = OriginPost.objects.get(post_id=message.id, chanel=sourse_chanel)
                    if message.caption:
                        post.text = message.caption
                    else:
                        post.text = ''

                    post.images = message.photo[-1].file_id
                    post.save()

                    for chanel in chanels:
                        try:
                            chanel_post = ChanelPost.objects.get(origin_post_id=post.id, chanel=chanel.id)
                            text = translate(post.text, sourse_chanel.language, chanel.language)
                            bot.edit_message_media(chat_id=chanel.chanel_id, message_id=chanel_post.self_post_id, media=telebot.types.InputMediaPhoto(post.images, caption=text))
                        except ChanelPost.DoesNotExist:
                            pass
                else:
                    post = OriginPost.objects.get(post_id=message.id, chanel=sourse_chanel)
                    post.text = message.text
                    post.image = ''
                    post.save()

                    chanels = Chanel.objects.filter(type='dependent')
                    for chanel in chanels:
                        try:
                            chanel_post = ChanelPost.objects.get(origin_post_id=post.id, chanel=chanel.id)
                            text = translate(post.text, sourse_chanel.language, chanel.language)
                            bot.edit_message_text(chat_id=chanel.chanel_id, message_id=chanel_post.self_post_id, text=text)
                        except ChanelPost.DoesNotExist:
                            pass
        except:
            pass

        try:
            bot.infinity_polling()
        except:
            pass