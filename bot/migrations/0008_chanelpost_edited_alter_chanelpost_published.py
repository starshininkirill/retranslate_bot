# Generated by Django 4.2 on 2023-04-04 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0007_remove_chanel_origin_post_id_remove_chanel_post_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='chanelpost',
            name='edited',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='chanelpost',
            name='published',
            field=models.BooleanField(default=False, null=True),
        ),
    ]