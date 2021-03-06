# Generated by Django 3.1.7 on 2021-03-03 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20210226_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='nascimento',
            field=models.DateField(blank=True, help_text='Data de nascimento para saber os aniversariantes da semana', null=True),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='estado',
            field=models.CharField(blank=True, editable=False, max_length=20, null=True),
        ),
    ]
