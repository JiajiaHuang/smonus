from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


# Create your views here.
class UserProfile(AbstractUser):
    objects = UserManager()

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'

    # 重载为了打印自定义的字符串
    def __unicode__(self):
        return self.username

    def __str__(self):
        return "User Class"


class PersonalProfile(UserProfile):
    Clear_Password = models.CharField(max_length=16, null=False, default='123456')

    def __str__(self):
        return "Personal Profile"


class RootProfile(UserProfile):
    def __str__(self):
        return "RootProfile Profile"


class SmAdminAction(models.Model):
    """权限标识表"""
    action_id = models.IntegerField()
    parent_id = models.IntegerField()
    action_names = models.CharField(max_length=512, blank=True, null=True, verbose_name='权限标识的名字')
    action_code = models.CharField(max_length=512, blank=True, null=True, verbose_name='权限标识码')
    is_show = models.BooleanField(default=False, verbose_name='是否显示')
    is_status = models.BooleanField(default=True, verbose_name='是否启用')
    action_order = models.IntegerField(blank=True, null=True, default=99, verbose_name='排序')
    action_note = models.CharField(max_length=1024, blank=True, null=True, verbose_name='权限标识说明')

    def __str__(self):
        return self.action_names

    class Meta:
        verbose_name = '权限标识'
        verbose_name_plural = '权限标识'
        ordering = ['-action_names']


class SmAdminUser(UserProfile):
    """用户表"""
    user_status_choice = (
        (0, '禁用'),
        (1, '正常'),
        (2, '离职'),
    )
    user_true_name = models.CharField(verbose_name='姓名', max_length=64, blank=True, null=True)
    fenji = models.CharField(verbose_name='分机号', max_length=64, blank=True, null=True)
    bianhao = models.CharField(verbose_name='编号', max_length=64, blank=True, null=False)
    role_id = models.IntegerField(verbose_name='角色 与ck_role表的 role_id 关联', blank=True, null=False, default=0)
    group_id = models.IntegerField(verbose_name='部门  获取部门名称', blank=True, null=False, default=0)
    is_manage = models.BooleanField(verbose_name='是否部门主管 0不是  1 是', blank=True, null=True, default=False)
    purview_type = models.BooleanField(verbose_name='是定义权限', blank=True, null=True, default=False)
    user_plus = models.BooleanField(verbose_name='附加权限', blank=True, null=True, default=False)
    enty_time = models.DateTimeField(verbose_name='入职时间', null=True, auto_now_add=True)
    user_status = models.SmallIntegerField(verbose_name='用户状况 0禁用  1正常 2 离职', choices=user_status_choice, default=1)
    is_hs = models.IntegerField()
    one_two = models.IntegerField()
    is_update = models.IntegerField(verbose_name='更新用户信息', blank=True, null=True, default=1)
    logintype = models.CharField(verbose_name='', blank=True, null=True, max_length=64)
    pid = models.IntegerField()
    depth = models.CharField(verbose_name='', blank=True, null=True, max_length=64)
    sproupid = models.IntegerField()
    user_level = models.IntegerField()
    website_id = models.CharField(verbose_name='为空取部门  不为空取website_id', max_length=64, blank=True, null=True)


class SmGroupType(models.Model):
    """部门表"""
    group_name = models.CharField(verbose_name='部门名称', max_length=64, blank=True, null=True)
    top_id = models.IntegerField(verbose_name='顶级ID', blank=True, null=True, default=0)
    p_id = models.IntegerField(verbose_name='父级ID', blank=True, null=True, default=0)
    g_level = models.IntegerField(verbose_name='部门所在的层级', blank=True, null=True, default=0)
    g_list = models.IntegerField(verbose_name='', blank=True, null=True, default=0)
    is_manage = models.IntegerField(verbose_name='', blank=True, null=True, default=0)
    group_orderby = models.IntegerField(verbose_name='排序', blank=True, null=True, default=0)
    is_status = models.BooleanField(verbose_name='是否启用', blank=True, null=True, default=True)
    is_show = models.BooleanField(verbose_name='是否显示', blank=True, null=True, default=True)
    group_list = models.CharField(verbose_name='部门所拥有的网站权限', max_length=64, blank=True, null=True)
    group_list2 = models.CharField(verbose_name='部门所管辖的子部门，每个部门ID用[ ]进行分割', max_length=1024, blank=True, null=True)
    action_list = models.CharField(verbose_name='部门所拥有的权限标识字符串', max_length=64, blank=True, null=True)
    customer_site_list = models.CharField(verbose_name='客户来源，主要用于二线的网站控制', max_length=64, blank=True, null=True)
    max_order_zck = models.IntegerField(verbose_name='部门最大暂存订单数', blank=True, null=True, default=5)
    inter_userName = models.CharField(verbose_name='短信接口的名字，暂时用不上', max_length=64, blank=True, null=True)
    sms_id = models.IntegerField(verbose_name='短信接口的ID', blank=True, null=True)
    mail_user = models.CharField(verbose_name='邮箱的名字，用于邮箱的同步', max_length=64, blank=True, null=True)
    mail_psw = models.CharField(verbose_name='邮箱的密码，用于邮箱的同步程序', max_length=64, blank=True, null=True)
    company_id = models.CharField(verbose_name='部门管理的公司ID，只用到添加用户的时候，获取部门的这个值，具体管理公司的权限是在用户表', max_length=64,
                                  blank=True, null=True)
    work_company_id = models.IntegerField(verbose_name='部门所在的公司', blank=True, null=True)
    zhekou = models.FloatField(verbose_name='最低折扣', blank=True, null=True, default=0)
    max_customer = models.IntegerField(verbose_name='部门所能拥有的最大的客户数，用于二线的客户数量控制', blank=True, null=True, default=0)
    is_leaf = models.IntegerField(verbose_name='暂时没有', blank=True, null=True, default=0)


class SmRole(models.Model):
    """权限表"""
    parent_id = models.IntegerField(verbose_name='父级ID', blank=True, null=True)
    role_name = models.CharField(verbose_name='角色名字', max_length=64, blank=True, null=True)
    action_list = models.CharField(verbose_name='权限标识组成的字符串', max_length=64, blank=True, null=True)
    web_list = models.CharField(verbose_name='', max_length=64, blank=True, null=True)
    role_describe = models.CharField(verbose_name='角色描述', max_length=256, blank=True, null=True)
    role_orderby = models.IntegerField(verbose_name='排序', blank=True, null=True, default=0)
    action_code = models.CharField(verbose_name='角色标识码，ID是会变的，标识码更灵活一点', max_length=64, blank=True, null=True)


class SmMenu(models.Model):
    """Menu"""
    url = models.CharField(verbose_name='链接', max_length=64, blank=True, null=True)
    path = models.CharField(verbose_name='Path', max_length=64, blank=True, null=True)
    component = models.CharField(verbose_name='component', max_length=64, blank=True, null=True)
    name = models.CharField(verbose_name='名称', max_length=64, blank=True, null=True)
    iconCls = models.CharField(verbose_name='图标', max_length=64, blank=True, null=True)
    keepAlive = models.BooleanField(verbose_name='', blank=True, null=True, default=None)
    requireAuth = models.BooleanField(verbose_name='', blank=True, null=True, default=None)
    parentId = models.IntegerField(verbose_name='', blank=True, null=True)
    enabled = models.BooleanField(verbose_name='', blank=True, null=True, default=True)
