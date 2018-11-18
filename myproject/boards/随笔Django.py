# 所有模型都是django.db.models.Model的子类。每个类将被转换为数据库表。
# 每个字段由django.db.models.Field子类（内置在Djangocore）的实例表示，它们并将转换为数据库的例

# 字段CharField，DateTimeField等等，都是django.db.models.Field的子类，包含在Django的核心里面，随时可以使用

# 在这里，我们仅仅使用CharField，DateTimeField，TextField和ForeignKey字段来定义我们的模型，当然在Django提供了更广泛的选择来代表不同类型的数据

# 在Board模型定义中，更具体地说，在name字段中，我们设置了参数unique=True ，顾名思义，它将强调数据库级别字段的唯一性

# 在Post模型中，creat_at字段有一个可选参数auto_now_add：告诉Django创建Post对象时间为当前日期和时间

# 模型之间的关系使用ForeignKey字段。它将在模型之间创建一个连接，并在数据库级别创建适当的关系（译注：外键关联）。该ForeighKey字段需要一个related_name：用于它关联的模型（created_by是外键字段，关联的User模型，表明这个帖子是谁创建的，related_name=posts表示User那边可以使用user.posts来查看这个用户创建了哪些帖子）
# #
from django.db import models
from django.contrib.auth.models import User

class Board(models.Model):
	name = models.CharField(max_length = 30,unique = True)
	description = models.CharField(max_length = 100)
    def __str__(self):
    	return self.name

class Topic(models.Model):
	subject = models.CharField(max_length = 225)
	last_updated = models.DateTimeField(auto_now_add = True)
	board = models.ForeighKey(Board,related_name = 'topics')
	starter = models.Foreighkey(User,related_name = 'topics')

class Post(models.Model):
	message = models.TextField(max_length = 400)
	topic = models.ForeighKey(Topic,related_name = 'posts')

	created_at = models.DateTime (auto_now_add =True)
	updated_at = models.DateTime(null = True)

	created_by = models.Foreighkey(User,related_name = 'posts')
	updated_by = models.Foreighkey(User,null = True,related_name = '+')

#URL调度器和URLconf（url configuration）是Django应用中的基础部分。
#一个项目中可以有很多url.PY分布在多个应用（app）中。Django需要一个url.py作为
# 入口，这个特殊的url.py叫做根路由配置（root URLconf）。
# 它被定义在setting.PY中。
# myproject/setting.py
# ROOT_URLCONF = 'myproject.urls' 已经自动配置好了，不需要做任何改变
# 当Django 接受一个请求（request），它就会在项目的URLconf中寻找匹配项。
# 它将从urlpatterns变量的第一条开始，然后在每个url中去匹配请求的URL。
# 如果Django找到了一个匹配路径，它就会把请求发给url的第二个参数 视图函数(view function)

# 当URL的一部分被当作某些资源的标识的时候就去创建一个dongtai页面，比如说这个标识可以是一个整数的
# ID或者是一个字符串。
# 开始的时候，我们使用Board ID去创建Topics列表的动态页面
PK OR ID pk表示主键，（primaryKEY）这是访问模型的主键（ID）的简写方法，所有Django模型都有这个属性，更多时候
使用pk属性和使用ID是一样的，这是因为如果我们没有给model定义主键时，Django将自动创建一个AutoField类型的字段，
名字叫做ID，它就是主键。如果你给model定义了一个不同的键，例如，假设email是你主键，你就可以这样访问：obj.email或者
obj.pk，二者是等价的



		
