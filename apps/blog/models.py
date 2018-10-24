from django.db import models


# Create your models here.
# 标签模型
class Tag(models.Model):
    tag_name = models.CharField(max_length=20, verbose_name=u'标签')


# 博客模型
class Blog(models.Model):
    caption = models.CharField(max_length=50, verbose_name=u'标题')
    tags = models.ManyToManyField(Tag, blank=True, verbose_name=u'标签')
