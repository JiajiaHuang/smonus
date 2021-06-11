# Generated by Django 2.2.1 on 2020-10-03 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_article_title_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='description_key',
        ),
        migrations.RemoveField(
            model_name='article',
            name='keyword',
        ),
        migrations.AddField(
            model_name='article',
            name='description_key_en',
            field=models.CharField(blank=True, db_tablespace='', max_length=256, verbose_name='description_key (English)'),
        ),
        migrations.AddField(
            model_name='article',
            name='description_key_es',
            field=models.CharField(blank=True, db_tablespace='', max_length=256, verbose_name='description_key (España)'),
        ),
        migrations.AddField(
            model_name='article',
            name='description_key_fr',
            field=models.CharField(blank=True, db_tablespace='', max_length=256, verbose_name='description_key (Le français)'),
        ),
        migrations.AddField(
            model_name='article',
            name='description_key_pt',
            field=models.CharField(blank=True, db_tablespace='', max_length=256, verbose_name='description_key (Português)'),
        ),
        migrations.AddField(
            model_name='article',
            name='description_key_zh_hans',
            field=models.CharField(blank=True, db_tablespace='', max_length=256, verbose_name='description_key (中文简体)'),
        ),
        migrations.AddField(
            model_name='article',
            name='description_key_zh_hant',
            field=models.CharField(blank=True, db_tablespace='', max_length=256, verbose_name='description_key (中文繁体)'),
        ),
        migrations.AddField(
            model_name='article',
            name='keyword_en',
            field=models.CharField(blank=True, db_tablespace='', max_length=256, verbose_name='keyword (English)'),
        ),
        migrations.AddField(
            model_name='article',
            name='keyword_es',
            field=models.CharField(blank=True, db_tablespace='', max_length=256, verbose_name='keyword (España)'),
        ),
        migrations.AddField(
            model_name='article',
            name='keyword_fr',
            field=models.CharField(blank=True, db_tablespace='', max_length=256, verbose_name='keyword (Le français)'),
        ),
        migrations.AddField(
            model_name='article',
            name='keyword_pt',
            field=models.CharField(blank=True, db_tablespace='', max_length=256, verbose_name='keyword (Português)'),
        ),
        migrations.AddField(
            model_name='article',
            name='keyword_zh_hans',
            field=models.CharField(blank=True, db_tablespace='', max_length=256, verbose_name='keyword (中文简体)'),
        ),
        migrations.AddField(
            model_name='article',
            name='keyword_zh_hant',
            field=models.CharField(blank=True, db_tablespace='', max_length=256, verbose_name='keyword (中文繁体)'),
        ),
    ]