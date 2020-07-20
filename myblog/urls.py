"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path, include, re_path
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings


# from django.http import HttpResponse
# #1.导入系统logging
# import logging
# #2.创建（获取）日志器
# logger = logging.getLogger('django')
# #3.使用日志器记录信息
# def log(request):
#     logger.info('info')
#     return HttpResponse('test')
#
# def log(request):
#     return HttpResponse('test')
from myblog import settings

from myblog.settings import MEDIA_ROOT

from django.views.static import serve
from . import settings

urlpatterns = [

    path('admin/', admin.site.urls),
    # include的第一个参数是设置一个元组urlconf_module,app_name
    # urlconf_module 子应用的路由
    # app_name 子应用的名字
    # namespace命名空间
    path('', include(('users.url', 'users'), namespace='users')),

    path('', include(('home.url', 'home'), namespace='home')),
    # url(r'^media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT}),
    re_path(r'ckeditor/', include('ckeditor_uploader.urls')),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns = [
#     path(r'media/(?P.*)', serve, {'document_root': settings.MEDIA_ROOT}),
# ]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)