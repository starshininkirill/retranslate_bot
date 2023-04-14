from django.db import models

class Chanel(models.Model):
    TYPES = [('sourse', 'Исходный канал'), ('dependent', 'Зависимый')]
    ACTIVE = [(True, 'Активен'), (False, 'Не активен')]
    LANGUAGES = [('ru', 'ru'), ('en', 'en')]

    name = models.CharField(null=True, verbose_name='Название канала')
    chanel_id = models.CharField(max_length=100, verbose_name='id канала')
    start_time = models.TimeField(null=True, default='00:00:00', verbose_name='Начало работы канала')
    end_time = models.TimeField(null=True, default='00:00:00', verbose_name='Окончание работы канала')
    type = models.CharField(max_length=20, choices=TYPES, default='dependent', verbose_name='Тип канала')
    active = models.BooleanField(default=False, choices=ACTIVE, verbose_name='Статус канала')
    language = models.CharField(max_length=10, choices=LANGUAGES, default='en', verbose_name='Язык')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Канал'
        verbose_name_plural = 'Каналы'


class OriginPost(models.Model):
    images = models.TextField(null=True)
    text = models.TextField(null=True)
    post_id = models.IntegerField(null=True)
    chanel = models.ForeignKey(Chanel, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.post_id}'

    class Meta:
        verbose_name = 'Пост исходного канала'
        verbose_name_plural = 'Посты исходного канала'


class ChanelPost(models.Model):
    chanel = models.ForeignKey(Chanel, on_delete=models.CASCADE)
    self_post_id = models.IntegerField(null=True)
    origin_post = models.ForeignKey(OriginPost, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.chanel}, id post: {self.origin_post.post_id}'

    class Meta:
        verbose_name = 'Пост канала'
        verbose_name_plural = 'Посты канала'

