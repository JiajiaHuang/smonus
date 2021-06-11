from django.db import models

# Create your models here.
from django.utils import timezone

from core.fields import MultilingualCharField, MultilingualTextField, MultilingualRichTextField
from django.utils.translation import ugettext_lazy as _


class Channel(models.Model):
    """
    栏目表
    """
    parent_ID = models.CharField(verbose_name='ParentID', max_length=256, blank=False, null=False)
    fill_path = models.CharField(verbose_name='FillPath', max_length=256, blank=True, null=True)
    sequence_index = models.IntegerField(verbose_name='排序', blank=True, null=True)
    title = MultilingualCharField(_('title'), max_length=256, blank=True, null=True)
    description = models.CharField(verbose_name='Description', max_length=256, blank=True, null=True)
    state = models.IntegerField(verbose_name='栏目状态', blank=True, null=True)
    created = models.DateTimeField(verbose_name='创建时间', default=timezone.now)
    updated = models.DateTimeField(verbose_name='修改时间', auto_now=True)
    channel_folder = models.CharField(verbose_name='ChannelFolder', max_length=256, blank=True, null=True)
    title_image = models.ImageField(upload_to='photos/', default="photos/default.png")
    channel_name = MultilingualCharField(_('channel_name'), max_length=256, blank=True, null=True)
    full_url = MultilingualCharField(_('full_url'), max_length=256, blank=True, null=True)
    enum_state = models.CharField(verbose_name='栏目状态', max_length=256, blank=True, null=True)
    articles_count = models.IntegerField(verbose_name='统计该栏目下的文章数', blank=True, null=True)
    tags = models.CharField(verbose_name='Tags', max_length=256, blank=True, null=True)
    keyword = models.CharField(verbose_name='KeyWord', max_length=256, blank=True, null=True)
    description_key = models.CharField(verbose_name='DescriptionKey', max_length=256, blank=True, null=True)


class Article(models.Model):
    """
    文章表
    """
    title_id = models.CharField(verbose_name='标题编号', max_length=100, blank=True, null=True)
    title = MultilingualCharField(_('Title'), max_length=256, blank=True, null=True)
    owner_ID = models.CharField(verbose_name='OwnerID', max_length=100, blank=False, null=False)
    title_url = MultilingualCharField(_('TitleUrl'), max_length=256, blank=True, null=True)
    account_ID = models.CharField(verbose_name='AccountID', max_length=100, blank=False, null=False)
    author = models.CharField(verbose_name='Author', max_length=100, blank=False, null=False)
    content = MultilingualRichTextField(_('Content'))
    created = models.DateTimeField(verbose_name='创建时间', default=timezone.now)
    updated = models.DateTimeField(verbose_name='修改时间', auto_now=True)
    source = models.CharField(verbose_name='来源', max_length=256, blank=False, null=False)
    allow_comments = models.BooleanField(verbose_name='讨论', blank=False, null=False)
    is_image = models.BooleanField(verbose_name='是否有缩略图', )
    is_show = models.BooleanField(verbose_name='是否置顶')
    subtitle = MultilingualCharField(_('SubTitle'), max_length=256, blank=True, null=True)
    thumbnail_image = models.ImageField(upload_to='photos/', default="photos/default.png")
    is_deleted = models.BooleanField(verbose_name='是否删除')
    process_state = models.BooleanField(verbose_name='文章审核', blank=True, null=True)
    channel_ID = models.CharField(verbose_name='栏目ID', max_length=100, blank=False, null=False)
    channel_name = models.CharField(verbose_name='栏目名称', max_length=100, blank=False, null=False)
    channelFull_Url_ID = models.CharField(verbose_name='ChannelFullUrlID', max_length=100, blank=False, null=False)
    clicked = models.IntegerField(verbose_name='点击数', default=0, null=True)
    comment_count = models.IntegerField(verbose_name='评论数', default=0, null=True)
    tags = models.CharField(verbose_name='Tags', max_length=256, blank=True, null=True)
    keyword = MultilingualCharField(_('keyword'), max_length=256, blank=True, null=True)
    description_key = MultilingualCharField(_('description_key'), max_length=256, blank=True, null=True)
    privacy_level = models.BooleanField(verbose_name='是否公开')


class Attachment(models.Model):
    """文件表"""
    article_ID = models.CharField(verbose_name='ArticleID', max_length=100, blank=True, null=True)
    sequence_index = models.CharField(verbose_name='SequenceIndex', max_length=100, blank=True, null=True)
    file_type = models.CharField(verbose_name='FileType', max_length=100, blank=True, null=True)
    file_name = models.CharField(verbose_name='FileName', max_length=256, blank=True, null=True)
    file_size = models.IntegerField()
    file_path = models.CharField(verbose_name='FilePath', max_length=256, blank=True, null=True)
    description = models.CharField(verbose_name='Description', max_length=256, blank=True, null=True)
    upload_date = models.DateTimeField(verbose_name='上传时间')
    download_times = models.IntegerField()
    Created = models.DateTimeField(verbose_name='创建时间', default=timezone.now)
    Updated = models.DateTimeField(verbose_name='更新时间', auto_now=True)


class Comments(models.Model):
    """评论表 """
    article_ID = models.CharField(verbose_name='ArticleID', max_length=100, blank=True, null=True)
    author = models.CharField(verbose_name='评论作者', max_length=100, blank=True, null=True)
    content = models.TextField(verbose_name='评论内容', blank=True, null=True)
    created = models.DateTimeField(verbose_name='创建时间', default=timezone.now)
    updated = models.DateTimeField(verbose_name='更新时间', auto_now=True)
    sequenceIndex = models.CharField(verbose_name='评论索引', max_length=100, blank=True, null=True)
    state = models.BooleanField(verbose_name='评论状态', default=False,  blank=True, null=True)
    IP = models.CharField(verbose_name='ip地址', max_length=100, blank=True, null=True)
    website = models.CharField(verbose_name='用户website', max_length=100, blank=True, null=True)
    email = models.CharField(verbose_name='用户email', max_length=100, blank=True, null=True)



class TagsModels(models.Model):
    """Tags 标签"""
    tags_name = models.CharField(verbose_name='tags_name', max_length=100, blank=True, null=True)
    tags_numb = models.IntegerField()
    tags_index = models.CharField(verbose_name='tags索引', max_length=100, blank=True, null=True)
    tags_created = models.DateTimeField(verbose_name='创建时间', default=timezone.now)
    tags_updated = models.DateTimeField(verbose_name='更新时间', auto_now=True)
