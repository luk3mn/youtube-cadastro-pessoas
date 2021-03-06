# Generated by Django 4.0.5 on 2022-07-17 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0003_pessoa_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='email',
            field=models.EmailField(max_length=256),
        ),
        migrations.AlterField(
            model_name='contato',
            name='nome',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='nome_completo',
            field=models.CharField(max_length=256),
        ),
    ]
