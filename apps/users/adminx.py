import xadmin

from xadmin import views

# from .models import UserProfile
from .models import EmailVerifyRecord, Banner

# Register your models here.


# class UserProfileAdmin(object):
#     """
#
#     """
#
#     pass

# 使用默认的
# xadmin.site.unregister(UserProfile)
# xadmin.site.register(UserProfile, UserProfileAdmin)

class EmailVerifyRecordAdmin(object):
    pass

# class BaseSetting(object):
#     enable_thems = True
#     use_bootswatch = True
#

# 将Xadmin全局管理器与我们的view绑定注册。
# xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
