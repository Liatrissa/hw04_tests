# Generated by Django 2.2.9 on 2022-10-25 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20221025_1237'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-pub_date']},
        ),
    ]
