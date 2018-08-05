import xadmin

from .models import UserMessage


class UserMessageAdmin(object):
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
    list_display = ['id', 'name', 'address', 'email', 'text']
    search_fields = ['id', 'name', 'address', 'email', 'text']
    list_filter = ['id', 'name', 'email']
    ordering = ['-id']


xadmin.site.register(UserMessage, UserMessageAdmin)
