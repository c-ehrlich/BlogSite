from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from blog.models import Post, Category
from django.contrib.auth.models import User


class PostTests(APITestCase):
    def test_view_post(self):
        """view a post"""
        url = reverse("blog_api:listcreate")
        response = self.client.get(url, format="json")
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def create_post(self):
        """create a post"""
        self.test_category = Category.objects.create(name="django")
        self.testuser1 = User.objects.create_user(
            username="test_user1", password="12345678"
        )
        data = {"title": "new", "author": 1, "excerpt": "new", "content": "new"}
        url = reverse("blog_api:listcreate")
        response = self.clent.post(url, data, format='json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
