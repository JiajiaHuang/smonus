# Generated by Django 2.2.1 on 2020-02-21 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backstage', '0009_auto_20200220_2103'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='smadminmenu',
            name='action_code',
        ),
        migrations.AddField(
            model_name='smadminmenu',
            name='menu_mc',
            field=models.CharField(blank=True, max_length=64, verbose_name='中文名称'),
        ),
        migrations.AlterField(
            model_name='smadminmenu',
            name='is_show',
            field=models.BooleanField(blank=True, default=True, null=True, verbose_name='是否显示  1为显示  0不显示'),
        ),
        migrations.AlterField(
            model_name='smadminmenu',
            name='is_status',
            field=models.BooleanField(blank=True, default=True, null=True, verbose_name='是否显示  1为显示  0不显示'),
        ),
    ]