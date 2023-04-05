import telebot.types
from telebot import TeleBot
from bot.models import *
from django.core.management.base import BaseCommand
# from ...models import Post

TOKEN = '6270134745:AAG42IsYldbf8jdylxNFMqaR17T_B1RsQk4'
SOURSE_CHANEL_ID = '-1001687669379'
CHANEL_TO = '-1001854770516'
SELF_CHAT_ID = '671176962'
file_ids = []





class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        bot = TeleBot(TOKEN)

        def decor(func):
            def wraper(*args, **kwargs):
                func(*args, **kwargs)
                bot.send_message(SELF_CHAT_ID, 'text')
                return True
            return wraper

        # @bot.edited_channel_post_handler(content_types=['text', 'photo'], func=lambda message: message.chat.id == int(SOURSE_CHANEL_ID))
        # def edit(message):
        #     print(message)
            # bot.send_message(SELF_CHAT_ID, message)

        # @bot.channel_post_handler(content_types=['photo'], func=lambda message: message.chat.id == int(SOURSE_CHANEL_ID))
        # def upload_post(message):
        #     if message.photo:
        #         file_id = message.photo[-1].file_id
        #         post, flag = Post.objects.get_or_create(post=message.id)
        #         if post.images is None:
        #             post.images = file_id
        #             post.save()
        #         else:
        #             post.images = post.images + f",{file_id}"
        #             post.save()
            #     bot.send_message(SELF_CHAT_ID, message)
            #     print(message)

        @bot.channel_post_handler(content_types=['photo'], func=lambda message: message.chat.id == int(SOURSE_CHANEL_ID))
        def new_photo_post(message):
            if message.photo:
                file_id = message.photo[-1].file_id
                bot.send_photo(CHANEL_TO, photo=file_id, caption=message.caption)

        # @bot.channel_post_handler(content_types=['text'], func=lambda message: message.chat.id == int(SOURSE_CHANEL_ID))
        # def new_text_post(message):
        #     post, created = Post.objects.get_or_create(post_id=message.id)
        #     post.text = message.text
        #     info = bot.send_message(CHANEL_TO, message.text)
        #     post.chanel_to_id = info.id
        #     post.save()
        #
        # @bot.edited_channel_post_handler(content_types=['text'], func=lambda message: message.chat.id == int(SOURSE_CHANEL_ID))
        # def edit_text_post(message):
        #     post = Post.objects.get(post_id=message.id)
        #     post.text = message.text
        #     post.save()
        #
        #     bot.edit_message_text(chat_id=CHANEL_TO, message_id=post.chanel_to_id, text=post.text)


        @bot.message_handler(content_types=['document'])
        def docs(message):
            bot.send_message(SELF_CHAT_ID, message)
            print(message.document)

        @bot.channel_post_handler(content_types=['text'], func=lambda message: message.chat.id == int(SOURSE_CHANEL_ID))
        def new_text_post(message):
            post, created = Post.objects.get_or_create(post_id=message.id)
            post.text = message.text
            post.save()

            chanel_post = Chanel.objects.create(post_id=post.id, origin_post_id=post.post_id)
            info = bot.send_message(CHANEL_TO, message.text)
            chanel_post.self_post_id = info.id
            chanel_post.save()

        @bot.edited_channel_post_handler(content_types=['text'], func=lambda message: message.chat.id == int(SOURSE_CHANEL_ID))
        def edit_text_post(message):
            post = Post.objects.get(post_id=message.id)
            post.text = message.text
            post.save()

            chanel_post = Chanel.objects.get(post_id=post.id)

            bot.edit_message_text(chat_id=CHANEL_TO, message_id=chanel_post.self_post_id, text=post.text)





        # @bot.channel_post_handler(content_types=['text', 'photo'], func=lambda message: message.chat.id == int(SOURSE_CHANEL_ID))
        # def new_post(message):
        #     print(message.photo[-1].file_id)
        #     if message.photo:
        #         file_id = message.photo[-1].file_id
        #         file_ids.append(file_id)
        #
        #         bot.send_message(SELF_CHAT_ID, message.photo)
        #         bot.send_photo(CHANEL_TO, photo=file_id)
        #         bot.send_media_group(SELF_CHAT_ID, media=[telebot.types.InputMediaPhoto(ids[0])])
        #     else:
        #         bot.send_message(CHANEL_TO, message.text)
        #     bot.send_media_group(SELF_CHAT_ID, media=[telebot.types.InputMediaPhoto(file_ids[0]), telebot.types.InputMediaPhoto(file_ids[1])])


        bot.infinity_polling()