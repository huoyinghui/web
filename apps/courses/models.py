from datetime import datetime
from django.db import models

# Create your models here.


class Course(models.Model):
    DEGREE_CHOICES = (
        ('primary', u'初级'),
        ('mediate', u'中级'),
        ('senior', u'高级'),
    )
    name = models.CharField(max_length=50, verbose_name=u'课程名称')
    desc = models.CharField(max_length=300, verbose_name=u'课程描述')
    detail = models.TextField(verbose_name=u'课程详情')
    degree = models.CharField(
        choices=DEGREE_CHOICES,
        max_length=10,
        verbose_name=u'难度',
    )
    learn_times = models.IntegerField(default=0, verbose_name=u'学习时长')
    students = models.IntegerField(default=0, verbose_name=u'学习人数')
    fav_nums = models.IntegerField(default=0, verbose_name=u'收藏人数')
    you_need_know = models.CharField(max_length=300, default=u"一颗勤学的心是本课程必要前提", verbose_name=u"课程须知")
    teacher_tell = models.CharField(max_length=300, default=u"什么都可以学到,按时交作业,不然叫家长", verbose_name=u"老师告诉你")
    image = models.ImageField(
        upload_to="courses/%Y/%m",
        verbose_name=u"封面图",
        max_length=100)
    # 保存点击量，点进页面就算
    click_nums = models.IntegerField(default=0, verbose_name=u"点击数")
    category = models.CharField(max_length=20, verbose_name=u"课程类别", default=u"后端开发")
    tag = models.CharField(max_length=15, verbose_name=u"课程标签", default=u"")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"课程"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{}'.format(self.name)


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name=u'课程')
    name = models.CharField(max_length=100, verbose_name=u"章节名")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"章节"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '《{0}》课程的章节 >> {1}'.format(self.course, self.name)


class Video(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name=u'章节')
    url = models.CharField(max_length=200, default="http://blog.mtianyan.cn/", verbose_name=u"访问地址")
    name = models.CharField(max_length=100, verbose_name=u"视频名")
    # 使用分钟做后台记录(存储最小单位)前台转换
    learn_times = models.IntegerField(default=0, verbose_name=u"学习时长(分钟数)")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"视频"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}章节的视频 >> {1}'.format(self.lesson, self.name)


class CourseResource(models.Model):
    # 因为一个课程对应很多资源。所以在课程资源表中将课程设置为外键。
    # 作为一个字段来让我们可以知道这个资源对应那个课程
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name=u"课程")
    name = models.CharField(max_length=100, verbose_name=u"名称")
    # 这里定义成文件类型的field，后台管理系统中会直接有上传的按钮。
    # FileField也是一个字符串类型，要指定最大长度。
    download = models.FileField(
        upload_to="course/resource/%Y/%m",
        verbose_name=u"资源文件",
        max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"课程资源"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '《{0}》课程的资源: {1}'.format(self.course, self.name)
