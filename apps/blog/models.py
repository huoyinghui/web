from django.db import models


# Create your models here.
# 标签模型
class Tag(models.Model):
    tag_name = models.CharField(max_length=20, verbose_name=u'标签')

    class Meta:
        verbose_name = u'标签'
        verbose_name_plural = verbose_name
        db_table = 'blog_tag'

    def __str__(self):
        return '{}'.format(self.tag_name)


# 博客模型
class Blog(models.Model):
    caption = models.CharField(max_length=50, verbose_name=u'标题', blank=True, null=True)
    content = models.TextField(max_length=1000, verbose_name=u'内容', default='')
    tags = models.ManyToManyField(Tag, blank=True, verbose_name=u'标签')

    class Meta:
        verbose_name = u'博客'
        verbose_name_plural = verbose_name
        db_table = 'blog_blog'

    def __str__(self):
        return '{}'.format(self.caption)
