# Generated by Django 3.2.3 on 2021-05-22 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mpost', '0003_alter_blog_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='user_name',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]
