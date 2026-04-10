from django.test import TestCase
from django.urls import reverse

from blog.models import Post
from django.contrib.auth import get_user_model

User = get_user_model()


class IndexTestCase(TestCase):
    def setUp(self):
        self.url = reverse("blog:index")
        self.user = User.objects.create_user(
            username="User1", password="Password1"
        )
        self.post = Post.objects.create(
            title="Title1", content="Body1", owner=self.user
        )
        self.post2 = Post.objects.create(
            title="Title2", content="Body2", owner=self.user
        )
        self.post3 = Post.objects.create(
            title="Title3", content="Body3", owner=self.user
        )

        for i in range(4, 11):
            Post.objects.create(
                title=f"Title{i}", content=f"Body{i}", owner=self.user
            )

    def test_view_returns_200(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_view_posts_ordered_by_created_time(self):
        response = self.client.get(self.url)
        self.assertEqual(
            list(response.context["posts"]),
            list(Post.objects.all().order_by("-created_time")),
        )

    def test_view_paginated_correctly(self):
        response = self.client.get(self.url)
        self.assertEqual(len(response.context["posts"]), 5)

    def test_view_pagination_page_2(self):
        response = self.client.get(self.url, {"page": 2})
        self.assertEqual(len(response.context["posts"]), 5)

        all_posts = list(Post.objects.all())
        ordered_posts = sorted(
            all_posts, key=lambda x: x.created_time, reverse=True
        )
        titles_on_second_page = [post.title for post in ordered_posts[5:10]]

        page_titles = [post.title for post in response.context["posts"]]
        self.assertEqual(page_titles, titles_on_second_page)
