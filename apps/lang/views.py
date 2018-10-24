# Create your views here.
import time
from django.http import HttpResponse
from django.utils.translation import ugettext as _
from django.views.generic.base import View



class LangView(View):
    """

    """
    def get(self, request):
        # 获得系统本地时间，返回的格式是 UTC 中的 struct_time 数据
        t = time.localtime()
        # 第 6 个元素是 tm_wday , 范围为 [0,6], 星期一 is 0
        n = t[6]
        # 星期一到星期日字符串
        weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        weekdays = [_(i) for i in weekdays]
        return HttpResponse(weekdays[n])
