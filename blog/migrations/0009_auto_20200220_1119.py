# Generated by Django 3.0.3 on 2020-02-20 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_remove_comment_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]