import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserProfile(AbstractUser):
    GENDER_CHOICE = [
        ('male', u'男'),
        ('female', u'女'),
    ]
    nick_name = models.CharField(max_length=50, verbose_name=u'昵称', default='')
    birthday = models.DateField(verbose_name=u'生日', null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICE, default="female")
    address = models.CharField(max_length=100, default=u'')
    moblile = models.CharField(max_length=11, null=True, blank=True)
    image = models.ImageField(upload_to="image/%Y/%m", default=u"image/default.png", max_length=100)

    class Meta:
        verbose_name = u"用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{}".format(self.get_username())


class EmailVerifyRecord(models.Model):
    SEND_CHOICES = (
        ('regisgter', u"注册"),
        ('forget', u"找回密码"),
        ('update_email', u"修改邮箱"),
    )

    code = models.CharField(max_length=20, verbose_name=u'验证码')
    email = models.EmailField(max_length=50, verbose_name=u'邮箱')
    send_type = models.CharField(choices=SEND_CHOICES, max_length=20, verbose_name=u'验证码类型')
    send_time = models.DateTimeField(default=datetime.datetime.now, verbose_name=u'发送时间')

    def __str__(self):
        return "{code}({email})".format(code=self.code, email=self.email)


class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name=u'标题')
    image = models.ImageField(
        upload_to='banner/%Y/%m',
        verbose_name=u'轮播图',
        max_length=100,
    )
    url = models.URLField(max_length=200, verbose_name=u'访问地址')
    index = models.IntegerField(default=100, verbose_name=u'顺序')
    add_time = models.DateTimeField(default=datetime.datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'轮播图'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{title}({index})'.format(title=self.title, index=self.index)
