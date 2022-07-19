from django.core.paginator import Paginator
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from blog.serializer import PostSerializer
from blog.models import Post


@api_view(['GET'])
def index(request):
    routes = [
        {'url': '/posts', 'method': 'GET', 'name': 'get_posts'},
        {'url': '/posts/<int:id>', 'method': 'GET', 'name': 'get_post'},
    ]
    return Response(routes)


@api_view(['GET'])
def get_posts(request):
    posts = Paginator(Post.objects.all(), request.GET.get('limit', 10))
    serializer = PostSerializer(posts.page(request.GET.get('page', 1)), many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_post(request, id):
    post = Post.objects.get(id=id)
    serializer = PostSerializer(post)
    return Response(serializer.data)


@api_view(['POST'])
def create_post(request):
    if request.method == 'POST':
        Post.objects.create(**request.data)
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_400_BAD_REQUEST)
