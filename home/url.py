from django.urls import path
from home.views import IndexView, DatailView
from users.views import WriteBlogView

urlpatterns = [
    #首页路由
    path('', IndexView.as_view(), name='index'),
    #写博客路由
    path('write/', WriteBlogView.as_view(), name='write'),
    #详情页面路由
    path('detail/', DatailView.as_view(), name='detail'),
]