from argparse import Namespace
from pydoc_data.topics import topics
from unicodedata import name
from xml.etree.ElementInclude import include
from django.urls import re_path as url

from learning_logs.models import Topic
from . import views

urlpatterns=[
    #设置主页
    url(r'^$',views.index,name='index'),
    #显示所有主题
    url(r'^topics/$',views.topics,name='topics'),
    #显示指定主题的详细页面
    url(r'topics/(?P<topic_id>\d+)/$',views.topic,name='topic'),
    #用于添加新主题的网页
    url(r'^new_topic/$',views.new_topic,name='new_topic'),
    #用于添加新条目的网页
    url(r'^new_entry/(?P<topic_id>\d+)/$',views.new_entry,name='new_entry'),
    url(r'^edit_entry/(?P<entry_id>\d+)/$',views.edit_entry,name='edit_entry'),
 ]