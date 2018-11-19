# encoding: utf-8
import django

from .views import BlogView, BlogDetailView

from django.conf.urls import url
from django.urls import path, re_path

app_name = "blog"
urlpatterns = [
    path('', BlogView.as_view(), name="blog_all"),
    re_path('^(?P<question_id>[0-9]+)/$', BlogDetailView.as_view(), name="blog_detail"),
    url(r"^(?P<question_id>[0-9]+)/tag/$", BlogDetailView.as_view(), name='blog_detail'),
]
