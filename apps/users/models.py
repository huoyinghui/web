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

    def __unicode__(self):
        return "{}".format(self.get_username())
