from django.db import models


# Create your models here.


class SmOrderGoods(models.Model):
    """订购商品表"""
    order_id = models.IntegerField(verbose_name='订单编号  开发用', blank=True, null=True)
    goods_id = models.IntegerField(verbose_name='商品编号', blank=True, null=True, default=0)
    goods_name = models.CharField(verbose_name='商品', max_length=64, blank=True, null=True)
    goods_sn = models.CharField(verbose_name='货号', max_length=64, blank=True, null=True)
    goods_number = models.IntegerField(verbose_name='数量', blank=True, null=True, default=1)
    market_price = models.FloatField(verbose_name='市价', blank=True, null=True)
    goods_price = models.FloatField(verbose_name='商品价', blank=True, null=True)
    goods_old_price = models.FloatField(verbose_name='临时变量，保存因为折扣用的价格在里面，没怎么用', blank=True, null=True)
    goods_attr = models.CharField(verbose_name='商品口属性', max_length=1024, blank=True, null=True)
    send_number = models.IntegerField(verbose_name='', blank=True, null=True, default=0)
    is_real = models.IntegerField(verbose_name='', blank=True, null=True, default=1)
    parent_id = models.IntegerField(verbose_name='优惠券', blank=True, null=True)
    is_gift = models.BooleanField(verbose_name='是否赠品', blank=True, null=True, default=False)
    add_time = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(verbose_name='是否显示', blank=True, null=True, default=True)
    goods_type = models.IntegerField(verbose_name='商品类型，用于打折', blank=True, null=True)
    admin_id = models.IntegerField(verbose_name='操作人', blank=True, null=True)
    shop_price = models.FloatField(verbose_name='商品实际单价，等于折扣后的价格*数量', blank=True, null=True)
    bramd_id = models.IntegerField(verbose_name='品牌ID', blank=True, null=True)
    bramd_name = models.CharField(verbose_name='品牌', max_length=64, blank=True, null=True)
    comment_status = models.BooleanField(verbose_name='是否评论', blank=True, null=True, default=True)


class SmBrand(models.Model):
    """品牌表"""
    bramd_id = models.IntegerField(verbose_name='品牌ID', blank=True, null=True)
    bramd_name = models.CharField(verbose_name='品牌', max_length=64, blank=True, null=True)
    brand_order = models.IntegerField(verbose_name='排序', blank=True, null=True)
    is_status = models.BooleanField(verbose_name='是否启用', blank=True, null=True, default=True)
    hide_value = models.IntegerField(verbose_name='隐藏的字数', blank=True, null=True, default=0)


class SmGoods(models.Model):
    cat_id = models.IntegerField(verbose_name='', blank=True, null=True)
    goods_sn = models.CharField(verbose_name='商品货号', max_length=64, blank=True, null=True)
    goods_name = models.CharField(verbose_name='商品名字', max_length=256, blank=True, null=True)
    goods_name_style = models.CharField(verbose_name='商品类型', max_length=256, blank=True, null=True)
    click_count = models.IntegerField(verbose_name='点击数量', blank=True, null=True, default=0)
    brand_id = models.IntegerField(verbose_name='品牌ID', blank=True, null=True)
    provider_name = models.CharField(verbose_name='', max_length=64, blank=True, null=True)
    goods_number = models.IntegerField(verbose_name='品牌ID', blank=True, null=True)
    goods_weight = models.FloatField(verbose_name='', blank=True, null=True)
    market_price = models.FloatField(verbose_name='市场价', blank=True, null=True)
    shop_price = models.FloatField(verbose_name='销售价', blank=True, null=True)
    promote_price = models.FloatField(verbose_name='促销价', blank=True, null=True)
    promote_start_date = models.DateField(verbose_name='促销开始日期', blank=True, null=True)
    promote_end_date = models.DateField(verbose_name='促销开始日期', blank=True, null=True)
    warn_number = models.IntegerField(verbose_name='', blank=True, null=True)
    keywords = models.CharField(verbose_name='关键词', max_length=256, blank=True, null=True)
    goods_brief = models.CharField(verbose_name='货物简介', max_length=1024, blank=True, null=True)
    goods_desc = models.TextField(verbose_name='货物详细', blank=True, null=True)
    goods_thumb = models.CharField(verbose_name='', max_length=64, blank=True, null=True)
    goods_img = models.CharField(verbose_name='', max_length=64, blank=True, null=True)
    original_img = models.CharField(verbose_name='', max_length=64, blank=True, null=True)
    is_real = models.BooleanField(verbose_name='是否审核', blank=True, null=True, default=True)
    extension_code = models.CharField(verbose_name='', max_length=64, blank=True, null=True)
    integral = models.IntegerField(verbose_name='', blank=True, null=True)
    add_time = models.DateTimeField(verbose_name='添加时间', blank=True, null=True)
    sort_order = models.IntegerField(verbose_name='排序', blank=True, null=True)
    is_delete = models.BooleanField(verbose_name='是否删除', blank=True, null=True, default=False)
    is_best = models.BooleanField(verbose_name='是否最好', blank=True, null=True, default=True)
    is_new = models.BooleanField(verbose_name='是否最新', blank=True, null=True, default=True)
    is_hot = models.BooleanField(verbose_name='是否最热', blank=True, null=True, default=False)
    is_promote = models.BooleanField(verbose_name='是否公开', blank=True, null=True, default=True)
    bonus_type_id = models.IntegerField(verbose_name='利润类型', blank=True, null=True)
    last_update = models.DateTimeField(verbose_name='更新时间', blank=True, null=True)
    goods_type = models.IntegerField(verbose_name='商品类型，促销有用', blank=True, null=True)
    goods_info = models.CharField(verbose_name='商品属性', max_length=10000, blank=True, null=True)
    seller_note = models.CharField(verbose_name='票据信息', max_length=64, blank=True, null=True)
    give_integral = models.IntegerField(verbose_name='积分', blank=True, null=True, default=0)
    comment_status = models.BooleanField(verbose_name='是否评论', blank=True, null=True, default=True)
    warehouse_id = models.IntegerField(verbose_name='仓库ID', blank=True, null=True)
    goods_status = models.IntegerField(verbose_name='商品上下架，-1是回收站，0是缺货，1是下架', blank=True, null=True, default=0)
    is_taozhuang = models.BooleanField(verbose_name='是否套餐', blank=True, null=True, default=False)
    gift_id = models.IntegerField(verbose_name='赠品ID', blank=True, null=True)
    series_id = models.IntegerField(verbose_name='系列ID', blank=True, null=True)
    reserved_field = models.CharField(verbose_name='保留字段', max_length=64, blank=True, null=True)


class SmCatGoods(models.Model):
    cat_id = models.IntegerField(verbose_name='目录ID（goods_category表）', blank=True, null=True)
    goods_id = models.IntegerField(verbose_name='商品ID', blank=True, null=True)
    goods_price = models.FloatField(verbose_name='商品价格', blank=True, null=True)
    expand_name = models.CharField(verbose_name='商品扩展名', max_length=64, blank=True, null=True)
    is_status = models.BooleanField(verbose_name='是否启用', blank=True, null=True, default=True)
    add_time = models.DateTimeField(verbose_name='添加时间', blank=True, null=True)
    note = models.CharField(verbose_name='备注', max_length=1024, blank=True, null=True)


class SmCatGoodsBackup(models.Model):
    """备份"""
    cat_id = models.IntegerField(verbose_name='目录ID（goods_category表）', blank=True, null=True)
    goods_id = models.IntegerField(verbose_name='商品ID', blank=True, null=True)
    goods_price = models.FloatField(verbose_name='商品价格', blank=True, null=True)
    expand_name = models.CharField(verbose_name='商品扩展名', max_length=64, blank=True, null=True)
    is_status = models.BooleanField(verbose_name='是否启用', blank=True, null=True, default=True)
    add_time = models.DateTimeField(verbose_name='添加时间', blank=True, null=True)
    note = models.CharField(verbose_name='备注', max_length=1024, blank=True, null=True)


class SmCoupon(models.Model):
    """优惠券"""
    coupon_id_type = models.IntegerField(verbose_name='分类ID', blank=True, null=True)
    coupon_sn = models.CharField(verbose_name='优惠券号', max_length=256, blank=True, null=True)
    user_id = models.IntegerField(verbose_name='使用会员ID', blank=True, null=True)
    used_time = models.DateTimeField(verbose_name='使用时间', blank=True, null=True)
    order_sn = models.CharField(verbose_name='使用订单号', max_length=256, blank=True, null=True)
    soruce_order_sn = models.CharField(verbose_name='由该订单产生的优惠券', max_length=256, blank=True, null=True)
    emailed = models.CharField(verbose_name='邮箱地址', max_length=64, blank=True, null=True)
    send_type = models.BooleanField(verbose_name='是否启用', blank=True, null=True, default=False)
    send_phone = models.CharField(verbose_name='发送的手机号码', max_length=64, blank=True, null=True)
    send_time = models.DateTimeField(verbose_name='发送时间', blank=True, null=True)


class SmCouponType(models.Model):
    """优惠券类型"""
    type_money = models.IntegerField(verbose_name='类别金额', blank=True, null=True)
    type_name = models.CharField(verbose_name='类别名称', max_length=256, blank=True, null=True)
    send_type = models.IntegerField(verbose_name='发送类型', blank=True, null=True)
    min_amount = models.IntegerField(verbose_name='最小使用金额', blank=True, null=True)
    max_amount = models.IntegerField(verbose_name='最大使用金额', blank=True, null=True)
    send_start_date = models.DateTimeField(verbose_name='发送开始时间', blank=True, null=True)
    send_end_date = models.DateTimeField(verbose_name='发送最后时间', blank=True, null=True)
    use_start_date = models.DateTimeField(verbose_name='使用开始时间', blank=True, null=True)
    use_end_date = models.DateTimeField(verbose_name='最后使用时间', blank=True, null=True)
    min_goods_amount = models.IntegerField(verbose_name='最小使用商品金额', blank=True, null=True)
    add_time = models.DateTimeField(verbose_name='添加时间', blank=True, null=True)


class SmGoodsCategory(models.Model):
    """商品种型"""
    cat_name = models.CharField(verbose_name='目录名称', max_length=256, blank=True, null=True)
    keywords = models.CharField(verbose_name='关键字', max_length=256, blank=True, null=True)
    cat_desc = models.CharField(verbose_name='目录描述', max_length=256, blank=True, null=True)
    parent_id = models.IntegerField(verbose_name='父ID', blank=True, null=True)
    g_level = models.IntegerField(verbose_name='层级', blank=True, null=True)
    sort_order = models.IntegerField(verbose_name='排序', blank=True, null=True)
    template_file = models.CharField(verbose_name='', max_length=256, blank=True, null=True)
    measure_unit = models.CharField(verbose_name='', max_length=256, blank=True, null=True)
    show_in_nav = models.IntegerField(verbose_name='', blank=True, null=True)
    style = models.CharField(verbose_name='', max_length=256, blank=True, null=True)
    is_show = models.BooleanField(verbose_name='是否显示', blank=True, null=True, default=True)
    grade = models.IntegerField(verbose_name='', blank=True, null=True)
    filter_attr = models.IntegerField(verbose_name='', blank=True, null=True)
    site_id = models.IntegerField(verbose_name='', blank=True, null=True, default=0)


