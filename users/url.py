# 进行uesrs子应用的视图路由
from django.urls import path
from users.views import RegisterView, LoginView, ForgetPasswordView, UserCenterView, LogoutView, WriteBlogView

urlpatterns = [
    # path第一个参数是路由，第二个参数是视图函数名
    #注册路由
    path('register/', RegisterView.as_view(), name='register'),

    #登录路由
    path('login/', LoginView.as_view(), name='login'),

    #忘记密码
    path('forget/', ForgetPasswordView.as_view(), name='forget'),

    #退出登录
    path('logout/', LogoutView.as_view(), name='logout'),

    #个人信息
    path('center/', UserCenterView.as_view(), name='center'),

    # #写博客
    # path('write/', WriteBlogView.as_view(), name='write')
]