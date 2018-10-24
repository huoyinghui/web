import xadmin

from xadmin import views

from .models import Blog, Tag

# Register your models here.
# 使用默认的
# xadmin.site.unregister(UserProfile)
# xadmin.site.register(UserProfile, UserProfileAdmin)


class BlogAdmin(object):
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
    list_display = ['id', 'caption', 'tags', 'content']
    search_fields = ['id', 'caption', 'tags']
    list_filter = ['id', 'caption', 'tags']
    ordering = ['-id']
    refresh_times = [3, 5]


class TagAdmin(object):
    """

    """
    list_display = ['id', 'tag_name']
    search_fields = ['id', 'tag_name']
    list_filter = ['id', 'tag_name']
    ordering = ['-id']
    refresh_times = [3, 5]

xadmin.site.register(Blog, BlogAdmin)
xadmin.site.register(Tag, TagAdmin)
