from django.db import models
from django.utils.translation import ugettext_lazy as _

# Receive the pre_delete signal and delete the file associated with the model instance.
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

from core.fields import (
    MultilingualCharField,
    MultilingualTextField
)


# Create your models here.

class SmAdminMenu(models.Model):
    """菜单栏表 """
    parent_id = models.IntegerField(verbose_name='判断码', blank=True, null=False)
    nenu_names = MultilingualCharField(_('nenu_names'), max_length=64, blank=True, null=False)
    menu_mc = models.CharField(verbose_name='中文名称', max_length=64, blank=True, null=False)
    url = models.CharField(verbose_name='菜单的跳转页面', max_length=64, blank=True, null=False)
    is_show = models.BooleanField(verbose_name='是否显示  1为显示  0不显示', blank=True, null=True, default=True)
    is_status = models.BooleanField(verbose_name='是否显示  1为显示  0不显示', blank=True, null=True, default=True)
    menu_order = models.IntegerField(verbose_name='排序', blank=True, null=True)


class SmWebsite(models.Model):
    """"""
    site_name = MultilingualCharField(_('site_name'), max_length=64, blank=True, null=True)
    site_url = models.CharField(verbose_name='网站的url,暂时没用上', max_length=64, blank=True, null=True)


class IndexInfo(models.Model):
    """URL文本信息"""
    page_info = models.CharField(verbose_name='信息名字', max_length=256, blank=True, null=True)
    page_where = models.CharField(verbose_name='信息位置', max_length=256, blank=True, null=True)
    page_name = MultilingualCharField(_('page_name'), max_length=256, blank=True, null=True)
    page_url = models.CharField(verbose_name='信息链接', max_length=256, blank=True, null=True)


class IndexUrl(models.Model):
    """单文本信息"""
    page_info = MultilingualCharField(_('page_info'), max_length=256, blank=True, null=True)
    page_where = models.CharField(verbose_name='信息位置', max_length=256, blank=True, null=True)


class MediaUrl(models.Model):
    """设置媒体信息"""
    page_info = MultilingualCharField(_('page_info'), max_length=256, blank=True, null=True)
    page_url = models.CharField(verbose_name='媒体信息链接', max_length=256, blank=True, null=True)
    page_img = models.CharField(verbose_name='媒体信息链接', max_length=256, blank=True, null=True)
    page_order = models.IntegerField(verbose_name='排序', blank=True, null=True)


class NewsInfo(models.Model):
    """index news"""
    news_name = models.CharField(verbose_name='新闻名称', max_length=256, blank=True, null=True)
    news_url = models.CharField(verbose_name='新闻编号', max_length=256, blank=True, null=True)
    news_info = MultilingualCharField(_('news_info'), max_length=256, blank=True, null=True)


class CarouselDisplay(models.Model):
    """Carousel Display"""
    carousel_nub = models.CharField(verbose_name='轮播编号', max_length=256, blank=True, null=True)
    carousel_img = models.ImageField(upload_to='photos/', default="photos/default.png")
    carousel_url = models.CharField(verbose_name='轮播链接', max_length=256, blank=True, null=True)
    carousel_info = MultilingualCharField(_('carousel_info'), max_length=256, blank=True, null=True)


@receiver(pre_delete, sender=CarouselDisplay)
def ColumnListsInfo_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.carousel_img.delete(False)


class ProductRecommendation(models.Model):
    """ProductRecommendation"""
    product_nub = models.CharField(verbose_name='产品编号', max_length=256, blank=True, null=True)
    product_info = MultilingualCharField(_('product_info'), max_length=256, blank=True, null=True)
    product_time = models.CharField(verbose_name='推荐时间', max_length=256, blank=True, null=True)


class CategoryRecommendation(models.Model):
    category_nub = models.CharField(verbose_name='产品编号', max_length=256, blank=True, null=True)
    category_info = MultilingualCharField(_('category_info'), max_length=256, blank=True, null=True)
    category_url = models.CharField(verbose_name='推荐信息', max_length=256, blank=True, null=True)
    category_img = models.ImageField(upload_to='photos/', default="photos/default.png")
    category_time = models.CharField(verbose_name='推荐时间', max_length=256, blank=True, null=True)


class FlowerImgUrl(models.Model):
    flower_nub = models.CharField(verbose_name='flower编号', max_length=256, blank=True, null=True)
    flower_url = models.CharField(verbose_name='flower链接', max_length=256, blank=True, null=True)
    flower_text = MultilingualCharField(_('flower_text'), max_length=256, blank=True, null=True)
    flower_info = MultilingualCharField(_('flower_info'), max_length=256, blank=True, null=True)
    flower_img = models.ImageField(upload_to='photos/', default="photos/default.png")


class ContactInfo(models.Model):
    contact_nub = models.CharField(verbose_name='contact编号', max_length=256, blank=True, null=True)
    contact_name = models.CharField(verbose_name='contact名称', max_length=256, blank=True, null=True)
    contact_url = models.CharField(verbose_name='contact链接', max_length=256, blank=True, null=True)
    contact_info = MultilingualCharField(_('contact_info'), max_length=512, blank=True, null=True)


class FooterListInfo(models.Model):
    footer_list_nub = models.CharField(verbose_name='footer_list编号', max_length=256, blank=True, null=True)
    footer_list_sort = models.CharField(verbose_name='footer_list排序', max_length=256, blank=True, null=True)
    footer_list_url = models.CharField(verbose_name='footer_list链接', max_length=256, blank=True, null=True)
    footer_list_info = MultilingualCharField(_('footer_list_info'), max_length=256, blank=True, null=True)


class ColumnListsInfo(models.Model):
    column_lists_nub = models.CharField(verbose_name='column_lists_nub', max_length=256, blank=True, null=True)
    column_url = models.CharField(verbose_name='column_lists_nub', max_length=256, blank=True, null=True)
    column_lists_img = models.ImageField(upload_to='photos/', default="photos/default.png")
    column_lists_title = MultilingualCharField(_('column_lists_title'), max_length=256, blank=True, null=True)
    column_lists_subtitle = MultilingualCharField(_('column_lists_subtitle'), max_length=256, blank=True, null=True)
    column_lists_alt = MultilingualCharField(_('column_lists_alt'), max_length=256, blank=True, null=True)


@receiver(pre_delete, sender=ColumnListsInfo)
def ColumnListsInfo_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.column_lists_img.delete(False)


class InstaContentInfo(models.Model):
    insta_content_nub = models.CharField(verbose_name='insta_content_nub', max_length=256, blank=True, null=True)
    insta_content_img = models.ImageField(upload_to='photos/', default="photos/default.png")
    insta_content_url = models.CharField(verbose_name='insta_content_url', max_length=256, blank=True, null=True)
    insta_content_alt = MultilingualCharField(_('insta_content_alt'), max_length=256, blank=True, null=True)
