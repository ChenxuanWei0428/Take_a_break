# Generated by Django 4.0.1 on 2022-07-05 20:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('take_a_break_app', '0004_remove_user_web_websites_user_web_websites'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_web',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='fav_webs', to=settings.AUTH_USER_MODEL),
        ),
    ]
