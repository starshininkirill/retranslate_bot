import telebot.types
from telebot import TeleBot
from bot.models import *
from django.core.management.base import BaseCommand
from ...models import *
import time


TOKEN = '6270134745:AAG42IsYldbf8jdylxNFMqaR17T_B1RsQk4'
SOURSE_CHANEL_ID = '-1001687669379'
CHANEL_TO = '-1001854770516'
SELF_CHAT_ID = '671176962'
file_ids = []
bot = TeleBot(TOKEN)


class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        @bot.channel_post_handler(content_types=['text'], func=lambda message: message.chat.id == int(SOURSE_CHANEL_ID))
        def new_text_post(message):
            post, created = OriginPost.objects.get_or_create(post_id=message.id)
            post.text = message.text
            post.post_id = message.id
            post.save()

            chanels = Chanel.objects.filter(type='dependent')
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

        @bot.edited_channel_post_handler(content_types=['text'], func=lambda message: message.chat.id == int(SOURSE_CHANEL_ID))
        def edit_text_post(message):
            post = OriginPost.objects.get(post_id=message.id)
            post.text = message.text
            post.save()

            chanels = Chanel.objects.filter(type='dependent')
            for chanel in chanels:
                try:
                    chanel_post = ChanelPost.objects.get(origin_post_id=post.id, chanel=chanel.id)
                    bot.edit_message_text(chat_id=chanel.chanel_id, message_id=chanel_post.self_post_id, text=post.text)
                except ChanelPost.DoesNotExist:


        @bot.channel_post_handler(content_types=['photo'], func=lambda message: message.chat.id == int(SOURSE_CHANEL_ID))
        def new_post(message):
            if message.photo:
                post, create = OriginPost.objects.get_or_create(post_id=message.id)
                print(message.caption)
                if create:
                    post.image = message.photo[-1].file_id
                    if message.caption:
                        post.text = message.caption
                    post.save()

                    chanels = Chanel.objects.filter(type='dependent')
                    for chanel in chanels:
                        info = bot.send_photo(chanel.chanel_id, photo=post.image, caption=post.text)
                        chanel_post = ChanelPost(chanel=chanel, self_post_id=info.id, origin_post=post)
                        chanel_post.save()






        bot.infinity_polling()