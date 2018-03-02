from django.shortcuts import render
from consultapp.models import Post
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse

from consultapp.serializers import PostSerializer

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.all().filter(user=self.request.user)

    

