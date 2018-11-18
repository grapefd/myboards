from django.test import TestCase
from django.core.urlresolvers import reverse
from django.urls import resolve
from .views import home,board_topics
from .models import Board

class HomeTests(TestCase):
	def test_home_view_status_code(self):
		url = reverse('home')
		response = self.client.get(url)
		self.assertEquals(response.status_code,200)

	def test_home_url_resolves_home_view(self):
		view = resolve('/')
		self.assertEquals(view.func,home)
# Create your tests here.
class BoardTopicTests(TestCase):

	def setUp(self):
		Board.objects.create(name = 'Django',description ='Django board.')
		#使用setup方法 创建B我爱人的实例来用于测试，
		#因为Django的测试机制不会针对当前的数据库来运行你的测试
		#运行Djiango测试会即时创建一个新的数据库，应用所有的模型迁移，
		#运行测试完成后会销毁这个测试的数据库	
	def test_board_topics_view_not_found_status_code(self):

		url = reverse('board_topics',kwargs ={'pk': 99})
		response = self.client.get(url)
		self.assertEquals(response.status_code,404)
		# 404 写成了400

		#测试 Django 是否使用了正确的视图函数去渲染 topics。
	def test_board_topics_url_resolves_board_topics_view(self):
		view = resolve('/boards/1/')
		#error resolve 写错了
		self.assertEquals(view.func,board_topics)


	def test_board_topics_view_success_status_code(self):
		url = reverse('board_topics', kwargs={'pk': 1})
		response = self.client.get(url)
		self.assertEquals(response.status_code, 200)


class HomeTests(TestCase):

    def setUp(self):
        self.board = Board.objects.create(name='Django', description='Django board.')
        url = reverse('home')
        self.response = self.client.get(url)

    def test_home_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)

    def test_home_view_contains_link_to_topics_page(self):
        board_topics_url = reverse('board_topics', kwargs={'pk': self.board.pk})
        self.assertContains(self.response, 'href="{0}"'.format(board_topics_url))
		#我们使用 assertContains 方法来测试 response 主体部分是否包含给定的文本。
		#我们在测试中使用的文本是 a 标签的 href 部分。所以基本上我们是在测试 response 主体是否包含文本 href="/boards/1/"。