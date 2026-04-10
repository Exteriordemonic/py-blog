from django.test import TestCase
from django.contrib.auth import get_user_model
from django.shortcuts import reverse


from blog.models import Post
from blog.models import Commentary


class PostAdminTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_superuser(
            username="admin", password="adminpass", email="admin@example.com"
        )
        self.author = get_user_model().objects.create_user(
            username="Author1", password="password1"
        )
        self.client.force_login(self.user)
        self.post = Post.objects.create(
            title="Title1", content="Body1", owner=self.author
        )

    def test_admin_changelist_view(self):
        url = reverse("admin:blog_post_changelist")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Title1")
        self.assertContains(response, "Author1")

    def test_admin_add_view(self):
        url = reverse("admin:blog_post_add")

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class CommentaryAdminTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_superuser(
            username="admin", password="adminpass", email="admin@example.com"
        )
        self.author = get_user_model().objects.create_user(
            username="Author1", password="password1"
        )
        self.post = Post.objects.create(
            title="Title1", content="Body1", owner=self.author
        )
        self.client.force_login(self.user)
        self.commentary = Commentary.objects.create(
            content="BodyCommentary1", user=self.author, post=self.post
        )

    def test_admin_changelist_view(self):
        url = reverse("admin:blog_commentary_changelist")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "BodyCommentary1")
        self.assertContains(response, "Author1")

    def test_admin_add_view(self):
        url = reverse("admin:blog_commentary_add")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_admin_plural_name_displayed(self):
        url = reverse("admin:blog_commentary_changelist")
        response = self.client.get(url)
        self.assertContains(response, "Commentaries")
