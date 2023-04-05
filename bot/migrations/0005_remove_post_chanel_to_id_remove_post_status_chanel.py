# Generated by Django 4.2 on 2023-04-04 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0004_post_chanel_to_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='chanel_to_id',
        ),
        migrations.RemoveField(
            model_name='post',
            name='status',
        ),
        migrations.CreateModel(
            name='Chanel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(null=True)),
                ('self_post_id', models.IntegerField(null=True)),
                ('origin_post_id', models.IntegerField(null=True)),
                ('status', models.CharField(choices=[('publushed', 'Опубликован'), ('chern', 'Не опубликован')], default='chern', max_length=30)),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bot.post')),
            ],
        ),
    ]