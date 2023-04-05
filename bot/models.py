from django.db import models


class OriginPost(models.Model):
    images = models.TextField(null=True)
    text = models.TextField(null=True)
    post_id = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.post_id}'


class Chanel(models.Model):
    TYPES = [('sourse', 'Исходный канал'), ('dependent', 'Зависимый')]
    ACTIVE = [(True, 'Активен'), (False, 'Не активен')]

    name = models.CharField(null=True)
    chanel_id = models.CharField(max_length=100)
    start_time = models.TimeField(null=True, default='00:00:00')
    end_time = models.TimeField(null=True, default='00:00:00')
    type = models.CharField(max_length=20, choices=TYPES, default='dependent')
    active = models.BooleanField(default=False, choices=ACTIVE)

    def __str__(self):
        return self.name


class ChanelPost(models.Model):
    chanel = models.ForeignKey(Chanel, on_delete=models.CASCADE)
    self_post_id = models.IntegerField(null=True)
    origin_post = models.ForeignKey(OriginPost, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.chanel}, post"{self.origin_post.post_id}"'



