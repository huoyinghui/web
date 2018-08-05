import xadmin

from .models import UserAsk, UserMessage, CourseComments, UserFavorite


class UserAskAdmin(object):
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
    list_display = ['id', 'name', 'mobile', 'course_name', 'add_time']
    search_fields = ['id', 'name', 'mobile', 'course_name']
    list_filter = ['id', 'name', 'mobile', 'course_name']
    ordering = ['-id']
    # readonly_fields = ['id', 'send_type', 'send_time']
    refresh_times = [3, 5]


class CourseCommentsAdmin(object):
    """

    """
    list_display = ['id', 'course', 'user', 'comments', 'add_time']
    search_fields = ['id', 'course', 'user', 'comments']
    list_filter = ['id', 'course', 'user', 'comments', 'add_time']


class UserMessagesAdmin(object):
    """

    """
    list_display = ['id', 'user', 'message', 'has_read', 'add_time']
    search_fields = ['id', 'user', 'message', 'has_read']
    list_filter = ['id', 'user', 'message', 'has_read', 'add_time']


class UserFavoriteAdmin(object):
    """

    """
    list_display = ['id', 'user', 'fav_id', 'fav_type', 'add_time']
    search_fields = ['id', 'user', 'fav_id', 'fav_type']
    list_filter = ['id', 'user', 'fav_id', 'fav_type', 'add_time']

xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(CourseComments, CourseCommentsAdmin)
xadmin.site.register(UserMessage, UserMessagesAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)

