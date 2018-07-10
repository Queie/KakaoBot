from django.urls import re_path
from .views import index, keyboard, answer

app_name='kakao'
urlpatterns = [
    re_path(r'^$',         index,    name='index'),
    re_path(r'^keyboard/', keyboard),
    re_path(r'^message$',  answer),
]