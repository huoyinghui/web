import xadmin

from .models import CourseOrg, Teacher, CityDict


class CityDictAdmin(object):
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
    list_display = ['id', 'name', 'parent', 'desc', 'add_time']
    search_fields = ['id', 'name', 'parent', 'desc']
    list_filter = ['id', 'name', 'parent', 'desc']
    ordering = ['-id']
    # readonly_fields = ['id', 'send_type', 'send_time']
    refresh_times = [3, 5]
    list_editable = ['name', 'parent', 'desc']


class TeacherAdmin(object):
    list_display = ['id', 'org', 'name', 'age', 'points',
                    'click_nums', 'fav_nums',
                    'work_years', 'work_company', 'work_position',
                    'image', 'add_time'
                    ]
    search_fields = ['id', 'name', 'org']
    list_filter = ['id', 'org', 'org', 'click_nums']


class CourseOrgAdmin(object):
    list_display = ['id', 'name', 'desc', 'category', 'tag',
                    'click_nums', 'fav_nums', 'address',
                    'city', 'students', 'course_nums'
                    ]
    search_fields = ['id', 'name', 'category']
    list_filter = ['id', 'name', 'city', 'category']


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
