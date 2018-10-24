# encoding: utf-8
import django


from lang.views import LangView
from django.urls import path

app_name = "lang"
urlpatterns = [
    # 语言信息
    path('', LangView.as_view(), name="lang_en"),
]
