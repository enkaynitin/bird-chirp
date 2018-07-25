from django.urls import path, re_path

from . import views

app_name = 'chirp'
urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'search/$', views.search, name='search'),
    re_path(r'follow/<int:user_id>', views.follow, name='follow')
]





# chirp/search/?search=R  (?P<search>[\w\-]+)/$


