# Generated by Django 3.1.7 on 2021-02-26 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210226_1205'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pessoa',
            options={'ordering': ('nome', 'cidade')},
        ),
    ]
