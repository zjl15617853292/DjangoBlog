from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponse
from django.http.response import HttpResponseBadRequest
import re
from users.models import User
from django.db import DatabaseError

from home.models import ArticleCategory, Article
from django.http.response import HttpResponseNotFound

# Create your views here.
#注册视图
from django.views import View

class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        #1.接收数据
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if not all([mobile, password, password2]):
            return HttpResponseBadRequest('请完整输入必要信息')

        if not re.match(r'^1[3-9]\d{9}$', mobile):
            return HttpResponseBadRequest("手机号不符合格式规定")

        if not re.match(r'^[0-9A-Za-z]{8,20}$', password):
            return HttpResponseBadRequest('请输入8~20位密码，只能是数字和字母的组合')

        if password != password2:
            return HttpResponseBadRequest('两次密码输入不一致')

        try:
            user = User.objects.create_user(
                username=mobile,
                mobile=mobile,
                password=password
            )
        except DatabaseError as e:
            import logging
            logger = logging.getLogger('django')
            logger.error(e)
            return HttpResponseBadRequest('注册失败,该用户已存在')

        from django.contrib.auth import login
        login(request, user)

        # 注册成功，重定向
        # reverse : 是可以通过namespace:name来获取到视图对应的路由
        response = redirect(reverse('home:index'))

        #设置cookie信息，方便首页用户信息展示的判断
        response.set_cookie('is_login', True)
        response.set_cookie('username', user.username, max_age=7*24*3600)

        return response

class LoginView(View):

    def get(self, request):
        return render(request, 'login.html')

    """
    1.接收参数
    2.参数验证
        2.1 手机号是否符合规则
        2.2 密码是否符合规则
    3.用户认证登录
    4.状态保持
    5.根据用户选择是否记住登录状态来进行判断
    6.为了首页显示需要设置一些cookie信息
    7.返回响应
    :param request: 
    :return: 
    """
    def post(self, request):

        mobile = request.POST.get('mobile')
        password = request.POST.get('password')
        remember = request.POST.get('remember')

        if not re.match(r'^1[3-9]\d{9}$', mobile):
            return HttpResponseBadRequest("手机号/账号不符合规则")

        if not re.match(r'^[0-9A-Za-z]{8,20}$', password):
            return HttpResponseBadRequest('请输入8~20位密码，只能是数字和字母的组合')

        from django.contrib.auth import authenticate
        #修改认证字段 到User模型中修改
        user = authenticate(mobile=mobile, password=password)

        from django.contrib import auth
        from django.http import JsonResponse
        if user is None:
            return HttpResponseBadRequest('用户名或密码错误')


        #根据next参数来进行页面跳转
        next_page = request.GET.get('next')
        if next_page:
            response = redirect(next_page)
        else:
            response = redirect(reverse('home:index'))
        #选择记住用户是否

        if remember != 'on':
            request.session["user"] = user.username
            auth.login(request, user)  # 将用户信息添加到session中
            response = redirect(reverse('home:index'))
            response.set_cookie('is_login', False)
        else:
            request.session["user"] = user.username
            auth.login(request, user)  # 将用户信息添加到session中
            response = redirect(reverse('home:index'))
            response.set_cookie('is_login', True)
        #返回响应
        return response

class LogoutView(View):
    def get(self, request):
        from django.contrib import auth
        auth.logout(request)

        response = redirect(reverse('home:index'))
        response.set_cookie('is_login', False)
        return response

class ForgetPasswordView(View):

    def get(self, request):
        return render(request, 'forget.html')

# LoginRequiredMixin判断用户是否登录
from django.contrib.auth.mixins import LoginRequiredMixin
class UserCenterView(LoginRequiredMixin,View):

    def get(self, request):
        user = request.user
        context = {
            'username':user.username,
            'mobile':user.mobile,
            'avatar':user.avatar.url if user.avatar else None,
            'user_desc':user.user_desc
        }
        return render(request, 'center.html', context=context)

from home.models import ArticleCategory
class WriteBlogView(LoginRequiredMixin, View):

    def get(self, request):
        from django.http.response import HttpResponseNotFound
        categories = ArticleCategory.objects.all()
        cat_id = request.GET.get('cat_id', 1)
        try:
            category = ArticleCategory.objects.get(id=cat_id)
        except ArticleCategory.DoesNotExist:
            return HttpResponseNotFound('没有此分类')
        context = {
            'categories': categories,
            'category': category,
        }
        return render(request, 'write_blog.html', context=context)

    def post(self, requset):
        avatar = requset.FILES.get('avatar')
        title = requset.POST.get('title')
        category_id = requset.POST.get('category')
        tags = requset.POST.get('tags')
        sumary = requset.POST.get('sumary')
        content = requset.POST.get('content')
        user = requset.user
        print(avatar)
        print('-----------------')
        print(title)
        print('-----------------')
        print(category_id)
        print('-----------------')
        print(sumary)
        print('-----------------')
        print(content)
        print('-----------------')
        print(user)
        # 验证获取的数据
        if not all([avatar, title, category_id, sumary, content]):
            return HttpResponseBadRequest('发布失败！请输入必要的内容')

        try:
            category = ArticleCategory.objects.get(id=category_id)
        #如果查询不到该分类
        except ArticleCategory.DoesNotExist:
            return HttpResponseBadRequest("没有此分类")

        try:
            from home.models import Article
            article = Article.objects.create(
                author = user,
                avatar = avatar,
                category = category,
                title = title,
                tags = tags,
                sumary = sumary,
                content = content
            )
        except Exception as e:
            print('-----------------')
            print(e)
            import logging
            logger = logging.getLogger('django')
            logger.error(e)
            return HttpResponseBadRequest("发布失败！请稍后再试")

        return redirect(reverse('home:index'))

# class DetailView(View):
#     def get(self, request):
#         #1.获取前端art_id,默认为5
#         art_id = request.GET.get('art_id', 5)
#         #2.获取art_id对应的Article数据表内容
#         #3.判断数据是否存在
#         try:
#             artdetail = Article.objects.get(id=art_id)
#         except Article.DoesNotExist:
#             return HttpResponseNotFound("该文章已不存在")
#         #4.将获取到的数据详情context返回给前端
#         context = {
#             'artdetail':artdetail
#         }
#         return render(request, 'detail.html', context=context)


