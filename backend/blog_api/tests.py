from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from blog.models import Post, Category
from django.contrib.auth.models import User


class PostTests(APITestCase):
    def test_view_post(self):
        """
        Ensure we can view all objects
        """
        url = reverse("blog_api:listcreate")
        response = self.client.get(url, format="json")
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def create_post(self):
        """
        Ensure we can create a new Post object and view objects
        """
        self.test_category = Category.objects.create(name="django")
        self.testuser1 = User.objects.create_user(
            username="test_user1", password="12345678"
        )

        self.client.login(username=self.testuser.username, password="12345678")

        data = {"title": "new", "author": 1, "excerpt": "new", "content": "new"}
        url = reverse("blog_api:listcreate")
        response = self.clent.post(url, data, format="json")
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_post_update(self):
        """
        Ensure that 
        1. posts can be edited by their author even if that user
        is not a superuser
        2. posts can not be edited by non-superusers who are not the author
        """
        client = APIClient()

        # there's probably a better way of doing this than to create new data
        # for every test
        self.test_category = Category.objects.create(name="django")
        self.testuser1 = User.objects.create_user(
            username="test_user1", password="123456789"
        )
        self.testuser2 = User.objects.create_user(
            username="test_user2", password="123456789"
        )
        test_post = Post.objects.create(
            category_id=1,
            title="Post Title",
            excerpt="Post Excerpt",
            content="Post Content",
            slug="post-title",
            author_id=1,
            status="published",
        )

        client.login(username=self.testuser1.username, password="123456789")

        # navigate to the right endpoint
        url = reverse(("blog_api:detailcreate"), kwargs={"pk": 1})

        # create a PUT request
        response = client.put(
            url,
            {
                # id not required because it's in the URL
                "title": "New",
                "author": 1,
                "excerpt": "New",
                "content": "New",
                "status": "published",
            },
            format="json",
        )

        # a good tool for debugging tests
        # print(response.data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        edited_post = Post.postobjects.get(id=1)
        self.assertEqual(edited_post.title, "New")

        # Log in again, this time as a user who is trying to edit a post that's
        # not theirs
        client.logout()
        client.login(username=self.testuser2.username, password="123456789")
        url=reverse(("blog_api:detailcreate"), kwargs={"pk": 1})
        response = client.put(
            url,
            {
                # id not required because it's in the URL
                "title": "New 2",
                "author": 1,
                "excerpt": "New 2",
                "content": "New 2",
                "status": "published",
            },
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        not_edited_post = Post.postobjects.get(id=1)
        self.assertEqual(not_edited_post.title, "New")

    # TODO a test where we try to make a post without being logged into an account

    # TODO a test that looks for the error that you get when submitting
    # incomplete data for editing

    # TODO a test that looks at what happens when you try to submit a post title
    # that's too long, either in Post Creation or in Post Editing

    # TODO confirm that a superuser can edit someone else's post (is this true)

    # TODO rewrite tests so we don't need to login a bunch of times
