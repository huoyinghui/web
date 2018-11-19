# Create your views here.
import time
from django.http import HttpResponse
from django.utils.translation import gettext as _
from django.views.generic.base import View


class LangView(View):
    """

    """
    def get(self, request):
        words = ['Welcome', 'to', 'my', 'site.']
        output = _(' '.join(words))
        return HttpResponse(output)
        # 获得系统本地时间，返回的格式是 UTC 中的 struct_time 数据
        # t = time.localtime()
        # 第 6 个元素是 tm_wday , 范围为 [0,6], 星期一 is 0
        # n = t[6]
        # 星期一到星期日字符串
        # weekdays = [_('Monday'), _('Tuesday'), _('Wednesday'), _('Thursday'), _('Friday'), _('Saturday'), _('Sunday')]
        # return HttpResponse(weekdays[n])
