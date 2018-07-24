from django.db import models

# Create your models here.


class UserMessage(models.Model):
    address = models.CharField(max_length=100, verbose_name=u'留言地址')
    email = models.EmailField(verbose_name=u'邮箱')
    name = models.CharField(max_length=20, verbose_name=u'用户名')
    text = models.CharField(max_length=100, verbose_name=u'留言信息', blank=True, default='')

    class Meta:
        verbose_name = u'用户留言信息'
        verbose_name_plural = verbose_name
        db_table = 'user_message'
