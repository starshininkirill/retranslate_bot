# Generated by Django 4.2 on 2023-04-04 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0010_alter_chanel_end_time_alter_chanel_start_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='chanel',
            name='type',
            field=models.CharField(default='dependent', max_length=20),
        ),
    ]
