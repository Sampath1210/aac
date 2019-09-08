# Generated by Django 2.0 on 2019-09-08 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190906_2027'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='content',
            new_name='body',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='timestamp',
            new_name='created',
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commnets', to='blog.Post'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.CharField(max_length=250),
        ),
    ]
