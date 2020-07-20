from django.db import models
from django.utils import timezone

# Create your models here.
class ArticleCategory(models.Model):
    """
    文章分类
    """
    title = models.CharField(max_length=100, blank=True)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'tb_category'
        verbose_name = '类别'
        verbose_name_plural = verbose_name

from users.models import User
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
class Article(models.Model):
    """
    文章
    """
    #参数on_delete=models.CASCADE 就是当user表中的数据删除时，文章信息也同步删除
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='media/article/%Y%m%d', blank=True, default='/static/avator/title.png')
    title = models.CharField(max_length=30, blank=True)
    category = models.ForeignKey(ArticleCategory, null=True, on_delete=models.CASCADE, related_name='article')
    tags = models.CharField(max_length=20, blank=True)
    sumary = models.CharField(max_length=200, null=False, blank=False)
    content = RichTextField()
    total_views = models.PositiveIntegerField(default=0)
    comments_count = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(default=timezone.now)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'tb_article'
        ordering = ('-created',)
        verbose_name = '文章管理'
        verbose_name_plural = verbose_name

class Comment(models.Model):
    """
    评论
    """
    content = RichTextField()
    article = models.ForeignKey(Article, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.article.title

    class Meta:
        db_table = 'tb_comment'
        verbose_name = '评论管理'
        verbose_name_plural = verbose_name