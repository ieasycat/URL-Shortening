# Generated by Django 3.1.7 on 2021-04-01 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('link_shortening', '0002_auto_20210401_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='count',
            field=models.IntegerField(),
        ),
        migrations.DeleteModel(
            name='CountClick',
        ),
    ]
