# Generated by Django 4.2 on 2023-04-05 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0011_chanel_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='chanel',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='chanel',
            name='chanel_id',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='chanel',
            name='type',
            field=models.CharField(choices=[('sourse', 'Исходный канал'), ('dependent', 'Зависимый')], default='dependent', max_length=20),
        ),
        migrations.AlterField(
            model_name='chanelpost',
            name='chanel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bot.chanel'),
        ),
        migrations.AlterField(
            model_name='chanelpost',
            name='origin_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bot.originpost'),
        ),
    ]