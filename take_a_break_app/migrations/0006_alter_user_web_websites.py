# Generated by Django 4.0.1 on 2022-07-06 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('take_a_break_app', '0005_alter_user_web_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_web',
            name='websites',
            field=models.ManyToManyField(blank=True, to='take_a_break_app.Websites'),
        ),
    ]
