# posts/views.py
from rest_framework import generics , permissions
from .models import Post
from .permissions import IsAuthorOrReadOnly # new
from .serializers import PostSerializer

class PostList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated) # new
    queryset = Post.objects.all() 
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView): 
    permission_classes = (IsAuthorOrReadOnly)  # new
    queryset = Post.objects.all()
    serializer_class = PostSerializer
