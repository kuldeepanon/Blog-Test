from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Post, User

class PostTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.post = Post.objects.create(title='Test Post', content='Content', author=self.user)

    def test_like_post(self):
        url = reverse('like-post', args=[self.post.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(self.user, self.post.likes.all())

        # Unliking the post
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertNotIn(self.user, self.post.likes.all())

    def test_post_pagination(self):
        for i in range(10):
            Post.objects.create(title=f'Test Post {i}', content='Content', author=self.user)

        response = self.client.get(reverse('post-list') + '?page=1&page_size=5')
        self.assertEqual(len(response.data), 5)