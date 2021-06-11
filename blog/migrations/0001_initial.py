# Generated by Django 2.2.1 on 2020-09-29 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_ID', models.CharField(max_length=100, verbose_name='OwnerID')),
                ('account_ID', models.CharField(max_length=100, verbose_name='AccountID')),
                ('author', models.CharField(max_length=100, verbose_name='Author')),
                ('created', models.DateTimeField(verbose_name='创建时间')),
                ('updated', models.DateTimeField(verbose_name='修改时间')),
                ('source', models.CharField(max_length=256, verbose_name='来源')),
                ('allow_comments', models.BooleanField(verbose_name='讨论')),
                ('is_image', models.BooleanField(verbose_name='是否有缩略图')),
                ('is_show', models.BooleanField(verbose_name='是否置顶')),
                ('thumbnail_image', models.ImageField(default='photos/default.png', upload_to='photos/')),
                ('is_deleted', models.BooleanField(verbose_name='是否删除')),
                ('process_state', models.IntegerField(blank=True, null=True, verbose_name='文章审核')),
                ('channel_ID', models.CharField(max_length=100, verbose_name='栏目ID')),
                ('channel_name', models.CharField(max_length=100, verbose_name='栏目名称')),
                ('channelFull_Url_ID', models.CharField(max_length=100, verbose_name='ChannelFullUrlID')),
                ('clicked', models.IntegerField(blank=True, null=True, verbose_name='点击数')),
                ('comment_count', models.IntegerField(blank=True, null=True, verbose_name='评论数')),
                ('tags', models.CharField(blank=True, max_length=256, null=True, verbose_name='Tags')),
                ('keyword', models.CharField(blank=True, max_length=256, null=True, verbose_name='KeyWord')),
                ('description_key', models.CharField(blank=True, max_length=256, null=True, verbose_name='DescriptionKey')),
                ('privacy_level', models.BooleanField(verbose_name='是否公开')),
                ('title_zh_hans', models.CharField(blank=True, db_tablespace='', max_length=256, verbose_name='Title (中文简体)')),
                ('title_en', models.CharField(blank=True, db_tablespace='', max_length=256, verbose_name='Title (English)')),
                ('title_zh_hant', models.CharField(blank=True, db_tablespace='', max_length=256, verbose_name='Title (中文繁体)')),
                ('title_fr', models.CharField(blank=True, db_tablespace='', max_length=256, verbose_name='Title (Le français)')),
                ('title_es', models.CharField(blank=True, db_tablespace='', max_length=256, verbose_name='Title (España)')),
                ('title_pt', models.CharField(blank=True, db_tablespace='', max_length=256, verbose_name='Title (Português)')),
                ('title_url_zh_hans', models.CharField(blank=True, db_tablespace='', max_length=256, verbose_name='TitleUrl (中文简体)')),
                ('title_url_en', models.CharField(blank=True, db_tablespace='', max_length=256, verbose_name='TitleUrl (English)')),
                ('title_url_zh_hant', models.CharField(blank=True, db_tablespace='', max_length=256, verbose_name='TitleUrl (中文繁体)')),
                ('title_url_fr', models.CharField(blank=True, db_tablespace='', max_length=256, verbose_name='TitleUrl (Le français)')),
                ('title_url_es', models.CharField(blank=True, db_tablespace='', max_length=256, verbose_name='TitleUrl (España)')),
                ('title_url_pt', models.CharField(blank=True, db_tablespace='', max_length=256, verbose_name='TitleUrl (Português)')),
                ('content_zh_hans', models.TextField(blank=True, db_tablespace='', verbose_name='Content (中文简体)')),
                ('content_en', models.TextField(db_tablespace='', verbose_name='Content (English)')),
                ('content_zh_hant', models.TextField(blank=True, db_tablespace='', verbose_name='Content (中文繁体)')),
                ('content_fr', models.TextField(blank=True, db_tablespace='', verbose_name='Content (Le français)')),
                ('content_es', models.TextField(blank=True, db_tablespace='', verbose_name='Content (España)')),
                ('content_pt', models.TextField(blank=True, db_tablespace='', verbose_name='Content (Português)')),
                ('subtitle_zh_hans', models.CharField(blank=True, db_tablespace='', max_length=256, verbose_name='SubTitle (中文简体)')),
                ('subtitle_en', models.CharField(blank=True, db_tablespace='', max_length=256, verbose_name='SubTitle (English)')),
                ('subtitle_zh_hant', models.CharField(blank=True, db_tablespace='', max_length=256, verbose_name='SubTitle (中文繁体)')),
                ('subtitle_fr', models.CharField(blank=True, db_tablespace='', max_length=256, verbose_name='SubTitle (Le français)')),
                ('subtitle_es', models.CharField(blank=True, db_tablespace='', max_length=256, verbose_name='SubTitle (España)')),
                ('subtitle_pt', models.CharField(blank=True, db_tablespace='', max_length=256, verbose_name='SubTitle (Português)')),
            ],
        ),
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_ID', models.CharField(blank=True, max_length=100, null=True, verbose_name='ArticleID')),
                ('sequence_index', models.CharField(blank=True, max_length=100, null=True, verbose_name='SequenceIndex')),
                ('file_type', models.CharField(blank=True, max_length=100, null=True, verbose_name='FileType')),
                ('file_name', models.CharField(blank=True, max_length=256, null=True, verbose_name='FileName')),
                ('file_size', models.IntegerField()),
                ('file_path', models.CharField(blank=True, max_length=256, null=True, verbose_name='FilePath')),
                ('description', models.CharField(blank=True, max_length=256, null=True, verbose_name='Description')),
                ('upload_date', models.DateTimeField(verbose_name='上传时间')),
                ('download_times', models.IntegerField()),
                ('Created', models.DateTimeField(verbose_name='创建时间')),
                ('Updated', models.DateTimeField(verbose_name='更新时间')),
            ],
        ),
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_ID', models.CharField(max_length=256, verbose_name='ParentID')),
                ('fill_path', models.CharField(blank=True, max_length=256, null=True, verbose_name='FillPath')),
                ('sequence_index', models.IntegerField(blank=True, null=True, verbose_name='排序')),
                ('description', models.CharField(blank=True, max_length=256, null=True, verbose_name='Description')),
                ('state', models.IntegerField(blank=True, null=True, verbose_name='栏目状态')),
                ('created', models.DateTimeField()),
                ('channel_folder', models.CharField(blank=True, max_length=256, null=True, verbose_name='ChannelFolder')),
                ('title_image', models.ImageField(default='photos/default.png', upload_to='photos/')),
                ('enum_state', models.CharField(blank=True, max_length=256, null=True, verbose_name='栏目状态')),
                ('articles_count', models.IntegerField(blank=True, null=True, verbose_name='统计该栏目下的文章数')),
                ('tags', models.CharField(blank=True, max_length=256, null=True, verbose_name='Tags')),
                ('keyword', models.CharField(blank=True, max_length=256, null=True, verbose_name='KeyWord')),
                ('description_key', models.CharField(blank=True, max_length=256, null=True, verbose_name='DescriptionKey')),
                ('title_zh_hans', models.CharField(blank=True, db_tablespace='', max_length=256, verbose_name='title (中文简体)')),
                ('title_en', models.CharField(blank=True, db_tablespace='', max_length=256, verbose_name='title (English)')),
                ('title_zh_hant', models.CharField(blank=True, db_tablespace='', max_length=256, verbose_name='title (中文繁体)')),
                ('title_fr', models.CharField(blank=True, db_tablespace='', max_length=256, verbose_name='title (Le français)')),
                ('title_es', models.CharField(blank=True, db_tablespace='', max_length=256, verbose_name='title (España)')),
                ('title_pt', models.CharField(blank=True, db_tablespace='', max_length=256, verbose_name='title (Português)')),
                ('channel_name_zh_hans', models.CharField(blank=True, db_tablespace='', max_length=256, verbose_name='channel_name (中文简体)')),
                ('channel_name_en', models.CharField(blank=True, db_tablespace='', max_length=256, verbose_name='channel_name (English)')),
                ('channel_name_zh_hant', models.CharField(blank=True, db_tablespace='', max_length=256, verbose_name='channel_name (中文繁体)')),
                ('channel_name_fr', models.CharField(blank=True, db_tablespace='', max_length=256, verbose_name='channel_name (Le français)')),
                ('channel_name_es', models.CharField(blank=True, db_tablespace='', max_length=256, verbose_name='channel_name (España)')),
                ('channel_name_pt', models.CharField(blank=True, db_tablespace='', max_length=256, verbose_name='channel_name (Português)')),
                ('full_url_zh_hans', models.CharField(blank=True, db_tablespace='', max_length=256, verbose_name='full_url (中文简体)')),
                ('full_url_en', models.CharField(blank=True, db_tablespace='', max_length=256, verbose_name='full_url (English)')),
                ('full_url_zh_hant', models.CharField(blank=True, db_tablespace='', max_length=256, verbose_name='full_url (中文繁体)')),
                ('full_url_fr', models.CharField(blank=True, db_tablespace='', max_length=256, verbose_name='full_url (Le français)')),
                ('full_url_es', models.CharField(blank=True, db_tablespace='', max_length=256, verbose_name='full_url (España)')),
                ('full_url_pt', models.CharField(blank=True, db_tablespace='', max_length=256, verbose_name='full_url (Português)')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_ID', models.CharField(blank=True, max_length=100, null=True, verbose_name='ArticleID')),
                ('author', models.CharField(blank=True, max_length=100, null=True, verbose_name='评论作者')),
                ('content', models.TextField(blank=True, null=True, verbose_name='评论内容')),
                ('created', models.DateTimeField(verbose_name='创建时间')),
                ('updated', models.DateTimeField(verbose_name='更新时间')),
                ('sequenceIndex', models.CharField(blank=True, max_length=100, null=True, verbose_name='评论索引')),
                ('state', models.CharField(blank=True, max_length=100, null=True, verbose_name='评论状态')),
                ('IP', models.CharField(blank=True, max_length=100, null=True, verbose_name='ip地址')),
                ('account_ID', models.CharField(blank=True, max_length=100, null=True, verbose_name='用户ID')),
            ],
        ),
        migrations.CreateModel(
            name='TagsModels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tags_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='tags_name')),
                ('tags_numb', models.IntegerField()),
                ('tags_index', models.CharField(blank=True, max_length=100, null=True, verbose_name='tags索引')),
                ('tags_created', models.DateTimeField(verbose_name='创建时间')),
                ('tags_updated', models.DateTimeField(verbose_name='更新时间')),
            ],
        ),
    ]
