# Generated by Django 2.0.6 on 2018-06-18 13:13

from django.conf import settings
from django.db import migrations, models
import posts.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20180618_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(default=1, on_delete=models.SET(posts.models.get_sentinel_user), related_name='posts', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
