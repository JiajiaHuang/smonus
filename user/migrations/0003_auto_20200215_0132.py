# Generated by Django 2.2.1 on 2020-02-14 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_smmenu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smadminuser',
            name='is_update',
            field=models.IntegerField(blank=True, default=1, null=True, verbose_name='更新用户信息'),
        ),
    ]