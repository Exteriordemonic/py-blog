from django.test import TestCase
from blog.models import Post


class PostTestCase(TestCase):
    def setUp(self):
        self.post = Post.objects.create(title="Title1", content="Body1")

    def test_post_str(self):
        self.assertEqual(self.post.__str__, "Title1")
