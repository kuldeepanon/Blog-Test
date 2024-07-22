from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Comment

# Create your tests here.

class PostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.post = Post.objects.create(title='Test Post', content='Test Content', author=self.user)

    def test_post_creation(self):
        self.assertEqual(self.post.title, 'Test Post')

class CommentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.post = Post.objects.create(title='Test Post', content='Test Content', author=self.user)
        self.comment = Comment.objects.create(post=self.post, author=self.user, text='Test Comment')

    def test_comment_creation(self):
        self.assertEqual(self.comment.text, 'Test Comment')
