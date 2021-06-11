# Generated by Django 2.2.1 on 2020-02-29 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backstage', '0013_contactinfo_contact_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactinfo',
            name='contact_info_en',
            field=models.CharField(blank=True, db_tablespace='', max_length=512, verbose_name='contact_info (English)'),
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='contact_info_es',
            field=models.CharField(blank=True, db_tablespace='', max_length=512, verbose_name='contact_info (España)'),
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='contact_info_fr',
            field=models.CharField(blank=True, db_tablespace='', max_length=512, verbose_name='contact_info (Le français)'),
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='contact_info_pt',
            field=models.CharField(blank=True, db_tablespace='', max_length=512, verbose_name='contact_info (Português)'),
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='contact_info_zh_hans',
            field=models.CharField(blank=True, db_tablespace='', max_length=512, verbose_name='contact_info (中文简体)'),
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='contact_info_zh_hant',
            field=models.CharField(blank=True, db_tablespace='', max_length=512, verbose_name='contact_info (中文繁体)'),
        ),
    ]