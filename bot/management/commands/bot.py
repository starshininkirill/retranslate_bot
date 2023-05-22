import telebot.types
from telebot import TeleBot
from bot.models import *
from django.core.management.base import BaseCommand
from ...models import *
import time

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
                
                print(sourse_chanels[0].chanel_id)
                if message.photo:
                    post = OriginPost.objects.create(post_id=message.id, text=message.caption, images=message.photo[-1].file_id)

                    for chanel in chanels:
                        now = time.strftime("%H:%M:%S", time.localtime())
                        start_time = str(chanel.start_time)
                        end_time = str(chanel.end_time)
                        if start_time <= now <= end_time or start_time == end_time:
                            info = bot.send_photo(chanel.chanel_id, photo=post.images, caption=post.text)
                            chanel_post = ChanelPost(chanel=chanel, self_post_id=info.id, origin_post=post)
                            chanel_post.save()

                else:
                    post = OriginPost.objects.create(post_id=message.id, text=message.text)

                    for chanel in chanels:
                        now = time.strftime("%H:%M:%S", time.localtime())
                        start_time = str(chanel.start_time)
                        end_time = str(chanel.end_time)
                        if start_time <= now <= end_time or start_time == end_time:
                            info = bot.send_message(chanel.chanel_id, post.text)
                            chanel_post = ChanelPost(chanel=chanel, self_post_id=info.id, origin_post=post)
                            chanel_post.save()

            @bot.edited_channel_post_handler(content_types=['text', 'photo'], func=lambda message: message.chat.id == int(sourse_chanel.chanel_id))
            def edit_text_post(message):
                chanels = Chanel.objects.filter(type='dependent')
                if message.photo:
                    post = OriginPost.objects.get(post_id=message.id)
                    if message.caption:
                        post.text = message.caption
                    else:
                        post.text = ''

                    post.images = message.photo[-1].file_id
                    post.save()

                    for chanel in chanels:
                        try:
                            chanel_post = ChanelPost.objects.get(origin_post_id=post.id, chanel=chanel.id)
                            bot.edit_message_media(chat_id=chanel.chanel_id, message_id=chanel_post.self_post_id, media=telebot.types.InputMediaPhoto(post.images, caption=post.text))
                        except ChanelPost.DoesNotExist:
                            pass
                else:
                    post = OriginPost.objects.get(post_id=message.id)
                    post.text = message.text
                    post.image = ''
                    post.save()

                    chanels = Chanel.objects.filter(type='dependent')
                    for chanel in chanels:
                        try:
                            chanel_post = ChanelPost.objects.get(origin_post_id=post.id, chanel=chanel.id)
                            bot.edit_message_text(chat_id=chanel.chanel_id, message_id=chanel_post.self_post_id, text=post.text)
                        except ChanelPost.DoesNotExist:
                            pass
        except:
            pass

        try:
            bot.infinity_polling()
        except:
            pass
