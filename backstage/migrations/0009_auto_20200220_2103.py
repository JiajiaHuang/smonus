# Generated by Django 2.2.1 on 2020-02-20 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backstage', '0008_auto_20200217_2259'),
    ]

    operations = [
        migrations.CreateModel(
            name='MediaUrl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_url', models.CharField(blank=True, max_length=256, null=True, verbose_name='媒体信息链接')),
                ('page_img', models.CharField(blank=True, max_length=256, null=True, verbose_name='媒体信息链接')),
                ('page_order', models.IntegerField(blank=True, null=True, verbose_name='排序')),
                ('page_info_zh_hans', models.CharField(blank=True, db_tablespace='', max_length=256, verbose_name='page_info (中文简体)')),
                ('page_info_en_us', models.CharField(blank=True, db_tablespace='', max_length=256, verbose_name='page_info (英语)')),
                ('page_info_zh_hant', models.CharField(blank=True, db_tablespace='', max_length=256, verbose_name='page_info (中文繁体)')),
                ('page_info_fr', models.CharField(blank=True, db_tablespace='', max_length=256, verbose_name='page_info (Le français)')),
                ('page_info_es', models.CharField(blank=True, db_tablespace='', max_length=256, verbose_name='page_info (España)')),
                ('page_info_pt', models.CharField(blank=True, db_tablespace='', max_length=256, verbose_name='page_info (Português)')),
            ],
        ),
        migrations.RemoveField(
            model_name='indexurl',
            name='page_where_en_us',
        ),
        migrations.RemoveField(
            model_name='indexurl',
            name='page_where_es',
        ),
        migrations.RemoveField(
            model_name='indexurl',
            name='page_where_fr',
        ),
        migrations.RemoveField(
            model_name='indexurl',
            name='page_where_pt',
        ),
        migrations.RemoveField(
            model_name='indexurl',
            name='page_where_zh_hans',
        ),
        migrations.RemoveField(
            model_name='indexurl',
            name='page_where_zh_hant',
        ),
        migrations.AddField(
            model_name='indexurl',
            name='page_where',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='信息位置'),
        ),
        migrations.AlterField(
            model_name='smadminmenu',
            name='menu_order',
            field=models.IntegerField(blank=True, null=True, verbose_name='排序'),
        ),
        migrations.AlterField(
            model_name='smadminmenu',
            name='parent_id',
            field=models.IntegerField(blank=True, verbose_name='判断码'),
        ),
    ]
