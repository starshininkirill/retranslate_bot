# Generated by Django 4.2 on 2023-04-04 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0003_rename_post_post_post_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='chanel_to_id',
            field=models.IntegerField(null=True),
        ),
    ]
