from .models import Post, Comment
from rest_framework import serializers
from django.contrib.auth.models import User

class PostSerializer(serializers.ModelSerializer):
    total_likes = serializers.IntegerField(read_only=True)

    class Meta:
        model = Post
        fields = ["id","title","content","total_likes"]

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id","text"]
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user