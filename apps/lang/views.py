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
