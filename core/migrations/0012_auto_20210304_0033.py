# Generated by Django 3.1.7 on 2021-03-04 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20210304_0031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='app',
            field=models.CharField(blank=True, choices=[('Whatsapp', 'Whatsapp'), ('Telegram', 'Telegram'), ('Signal', 'Signal')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='cidade',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='grupo',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
