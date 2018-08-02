from datetime import datetime
from django.db import models

from courses.models import Course
from users.models import UserProfile

# Create your models here.


class UserAsk(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'姓名')
    mobile = models.CharField(max_length=11, verbose_name=u'手机')
    course_name = models.CharField(max_length=50, verbose_name=u'课程名')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'用户咨询'
        verbose_name_plural = verbose_name

    def __str__(self):
        return 'user:{} mobile:{}'.format(self.name, self.mobile)


class CourseComments(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name=u'课程')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name=u'用户')
    comments = models.CharField(max_length=250, verbose_name=u"评论")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"评论时间")

    class Meta:
        verbose_name = u"课程评论"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '用户({0})对于《{1}》 评论 :'.format(self.user, self.course)


class UserFavorite(models.Model):
    TYPE_CHOICES = (
        (1, u'课程'),
        (2, u'课程机构'),
        (3, u'讲师'),
    )
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name=u"用户")
    fav_id = models.IntegerField(default=0)
    fav_type = models.IntegerField(
        choices=TYPE_CHOICES,
        default=1,
        verbose_name=u'收藏类型'
    )
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"评论时间")

    class Meta:
        verbose_name = u"用户收藏"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '用户({0})收藏了{1} '.format(self.user, self.fav_type)


class UserMessage(models.Model):
    user = models.IntegerField(default=0, verbose_name=u"接收用户")
    message = models.CharField(max_length=500, verbose_name=u"消息内容")

    # 是否已读: 布尔类型 BooleanField False未读,True表示已读
    has_read = models.BooleanField(default=False, verbose_name=u"是否已读")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户消息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '用户({0})接收了{1} '.format(self.user, self.message)


class UserCourse(models.Model):
    # 会涉及两个外键: 1. 用户， 2. 课程。import进来
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name=u"课程")
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name=u"用户")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户课程"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '用户({0})学习了{1} '.format(self.user, self.course)
