# DjangoBlog
# Django开发的一个可评论的博客系统
# 项目名称：DJangoBlog
# 项目简介：用 Django 开发一个支持评论的博客系统，代码上传到 GitHub，系统部署到 Heroku
# 项目启动时间：2020-07-18
# 项目完成时间：2020-07-21
# 参考文档：
https://docs.djangoproject.com/en/2.2/intro/ 
https://devcenter.heroku.com/articles/deploying-python
# 开发模式：前后端不分离
# 后端框架：Django+Django模板引擎
# python版本：python3.6
# django版本：django3.0.8
# pycharm版本：pycharm2020.1
# 需求分析：
	1.页面及页面上的业务逻辑
	2.归纳业务逻辑并划分模块
	3.共有7个页面：
		(1).注册页面：注册功能
		(2).登录页面：注册功能，状态保持功能，cookie，session
		(3).忘记密码页面：和注册页面类似
		(4).用户中心页面：用户信息/头像上传（更新数据）
		(5).博客发布页面：博客发布功能（数据入库）
		(6).博客首页：博客分页展示（数据分页）
		(7).博客详情页面：博客详情数据，评论，推荐博客展示
# mysql 8.0.19
	数据库根账户密码：772312
	数据库用户名：bloguser
	数据库库名：my_blog

# redis 5.0.9 
把session由数据库存储改为redis存储
redis数据库服务启动命令（需要切换到redis安装目录下）：redis-server.exe redis.windows.conf
启动redis服务后 才可以启动redis客户端：redis-cli

虚拟环境中创建子应用：python manage.py startapp user
数据库生成迁移文件：python manage.py makemigrations
数据库迁移：python manage.py migrate

# 管理员：
	手机号:40077774000
	用户名:40077774000
	emial:40077774000@163.com
	密码:40077774000

# 难题
1.all() 方法那里是怎么回事？ 一直报错all() takes exactly one argument (5 given)
  （已解决,原因是里面应该是一个列表或可迭代对象，我直接往()里面添加元素了，导致报错)

2.发布文章时总是提示：没有该分类，也就是说无法通过写文章时选择的栏目id去反向索引数据库，还也许是无法获取到文章栏目的Id
   (已解决，原因是tags，也就是栏目没有传入数据库。。)

3.数据库保存的图片无法渲染的前端模板上，即文章的图片是保存到media文件夹中的（确认保存成功了，数据库也有保存），但是前端无法接收，报错404
  （已解决，原因是session配置中的meida配置路径错了，而且应该将media放入static中，或者把media删除，让系统自动生成存储文件，还有前端的调用路径应该为:例子：/static/{{ item.img }}）

# 蠕虫语句添加Mysql测试数据：
	insert into tb_comment(content, created, article_id, user_id) select content, created, article_id, user_id from tb_comment;

# 依赖文件：
在项目根目录中，打开终端执行以下命令
# 生成 requirements.txt 文件
pip3 freeze > requirements.txt

# 安装依赖文件
pip3 install -r /var/www/project/requriements.txt 
