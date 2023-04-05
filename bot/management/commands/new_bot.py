import telebot.types
from telebot import TeleBot
from bot.models import *
from django.core.management.base import BaseCommand
from ...models import *
import time


TOKEN = '6270134745:AAG42IsYldbf8jdylxNFMqaR17T_B1RsQk4'

sourse_chanel = Chanel.objects.get(type='sourse')
SOURSE_CHANEL_ID = '-1001687669379'
CHANEL_TO = '-1001854770516'
SELF_CHAT_ID = '671176962'
bot = TeleBot(TOKEN)


class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        @bot.channel_post_handler(content_types=['text', 'photo'], func=lambda message: message.chat.id == int(sourse_chanel.chanel_id))
        def new_text_post(message):
            chanels = Chanel.objects.filter(type='dependent', active=True)
            if message.photo:
                post = OriginPost.objects.create(post_id=message.id, text=message.caption, images=message.photo[-1].file_id)
                # post, created = OriginPost.objects.get_or_create(post_id=message.id)
                # post.text = message.caption
                # post.image = message.photo[-1].file_id
                # post.post_id = message.id
                # post.save()

                for chanel in chanels:
                    now = time.strftime("%H:%M:%S", time.localtime())
                    start_time = str(chanel.start_time)
                    end_time = str(chanel.end_time)
                    if start_time <= now <= end_time or start_time == end_time:
                        info = bot.send_photo(chanel.chanel_id, photo=post.images, caption=post.text)
                        chanel_post = ChanelPost(chanel=chanel, self_post_id=info.id, origin_post=post)
                        chanel_post.save()
                    else:
                        print(f'Канал {chanel.name} сейчас не активен')
            else:
                post = OriginPost.objects.create(post_id=message.id, text=message.text)
                # post, created = OriginPost.objects.get_or_create(post_id=message.id)
                # post.text = message.text
                # post.post_id = message.id
                # post.save()

                for chanel in chanels:
                    now = time.strftime("%H:%M:%S", time.localtime())
                    start_time = str(chanel.start_time)
                    end_time = str(chanel.end_time)
                    if start_time <= now <= end_time or start_time == end_time:
                        info = bot.send_message(chanel.chanel_id, post.text)
                        chanel_post = ChanelPost(chanel=chanel, self_post_id=info.id, origin_post=post)
                        chanel_post.save()
                    else:
                        print(f'Канал {chanel.name} сейчас не активен')

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


        bot.infinity_polling()