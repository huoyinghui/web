import xadmin

from .models import Course, Lesson, Video, CourseResource


class CourseAdmin(object):
    """
    默认模型显示模式:

    1.search_fields:    #搜索范围
    2.list_display:     #列表显示
    3.list_filter:      #列表过滤
    4.ordering:         #默认排序,'-':倒序,从大到小
    5.readonly_fields   # 直接编辑
    6.refresh_times     # 刷新秒数
    7.list_editable     # 直接编辑
    """
    list_display = [
        'id', 'name', 'desc', 'add_time',
        'detail', 'degree', 'learn_times', 'students',
        'fav_nums', 'you_need_know', 'teacher_tell',
        'image', 'click_nums', 'category', 'tag',
    ]
    search_fields = ['id', 'name', 'degree', 'desc']
    list_filter = ['id', 'name', 'degree', 'desc']
    ordering = ['-id']
    # readonly_fields = ['id', 'send_type', 'send_time']
    refresh_times = [3, 5]


class LessonAdmin(object):
    list_display = ['id', 'course', 'name', 'add_time']
    search_fields = ['id', 'course', 'name']
    list_filter = ['id', 'course', 'name']


class VideoAdmin(object):
    list_display = ['id', 'name', 'lesson', 'learn_times', 'url', 'add_time']
    search_fields = ['id', 'url', 'lesson']
    list_filter = ['id', 'lesson']


class CourseResourceAdmin(object):
    list_display = ['id', 'name', 'course', 'download', 'add_time']
    search_fields = ['id', 'name', 'course']
    list_filter = ['id', 'name', 'course', 'download']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)

