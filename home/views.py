from django.shortcuts import render
from django.views import View
from home.models import ArticleCategory, Article
from django.http.response import HttpResponseNotFound
from django.shortcuts import render,redirect
from django.urls import reverse
# Create your views here.
class IndexView(View):
    def get(self, request):
        """
        1.获取所有分类信息
        2.接收用户点击的分类信息
        3.根据分类id进行查询
        4.数据传递给模板进行渲染
        :param request:
        :return:
        """
        categories = ArticleCategory.objects.all()
        articles = Article.objects.all()
        cat_id = request.GET.get('cat_id', 1)
        try:
            category = ArticleCategory.objects.get(id=cat_id)
        except ArticleCategory.DoesNotExist:
            return HttpResponseNotFound('没有此分类')
        context = {
            'categories':categories,
            'category':category,
            'articles':articles
        }

        return render(request, 'index.html', context=context)

article = []
from home.models import Comment
class DatailView(View):
    def get(self, request):
        global article
        #接收文章id
        id = request.GET.get('art_id')
        #根据文章id进行文章数据的查询
        try:
            article = Article.objects.get(id=id)
        except Article.DoesNotExist:
            HttpResponseNotFound('该文章不存在了')
        else:

            article.total_views += 1
            article.save()

        #查询分类数据
        categories = ArticleCategory.objects.all()
        #查询浏览量前十的文章数据
        hot_articles = Article.objects.order_by('-total_views')[:9]
        #获取分页请求参数
        page_size = request.GET.get('page_size', 10)
        page_num = request.GET.get('page_num', 1)
        #根据当前文章查询评论数据

        comments = Comment.objects.filter(article=article).order_by('-created')

        #获取评论总数
        total_count = comments.count()
        #创建分页器
        from django.core.paginator import Paginator, EmptyPage
        paginator = Paginator(comments, page_size)
        #分页处理
        try:
            page_comments = paginator.page(page_num)
        except EmptyPage:
            return HttpResponseNotFound('Empty Page')
        #获取总页数
        total_page = paginator.num_pages

        context = {
            'categories':categories,
            'category': article.category,
            'article':article,
            'hot_articles':hot_articles,
            'total_count':total_count,
            'comments':page_comments,
            'page_size':page_size,
            'total_page':total_page,
            'page_num':page_num
        }

        return render(request, 'detail.html', context=context)



    def post(self, request):
        """
        1.先接收用户信息
        2.判断用户是否登录
        3.登录用户则可以接收form数值
            3.1接收评论数据
            3.2验证文章是否存在
            3.3保存评论数据
            3.4修改文章评论数量
        4.未登录用户跳转到登录界面
        :return:
        """
        user = request.user
        if user and user.is_authenticated:
            id = request.POST.get('id')
            content = request.POST.get('content')

            try:
                article = Article.objects.get(id=id)
            except Article.DoesNotExist:
                return HttpResponseNotFound('该文章已不存在')

            Comment.objects.create(
                content = content,
                article = article,
                user = user
            )

            article.comments_count += 1
            article.save()

            # 刷新当前页面,使用页面重定向
            path = reverse('home:detail') + '?id={}'.format(article.id)
            return redirect(path)

        else:
            return redirect(reverse('user:login'))
