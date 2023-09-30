from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Post


# Create your tests here.
class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username="testuser",
            password="testpassword",
        )

        cls.post = Post.objects.create(
            title="Test Post",
            slug="test-post",
            author=cls.user,
            body="This is a test post.",
            publish="2023-09-30 12:00:00",
            status=Post.Status.PUBLISHED,
        )

    def test_post_creation(self):
        self.assertEqual(self.post.title, "Test Post")
        self.assertEqual(self.post.slug, "test-post")
        self.assertEqual(self.post.author, self.user)
        self.assertEqual(self.post.body, "This is a test post.")
        self.assertEqual(self.post.status, Post.Status.PUBLISHED)

    def test_post_list_view(self):
        response = self.client.get(reverse("blog:post_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Post")
        self.assertTemplateUsed(response, "post/list.html")

    def test_post_detail_view(self):
        response = self.client.get(reverse("blog:post_detail", args=[self.post.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Post")
        self.assertContains(response, "This is a test post.")
        self.assertTemplateUsed(response, "post/detail.html")
