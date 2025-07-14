from django.shortcuts import render

from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status
from .models import Movies, Comments
from .serializers import MoviesSerializer, CommentSerializer

@api_view(['GET'])
def movie_list(request):
    # 1) ?search=검색어 2) ?page=페이지번호
    # 1) 검색
    qs = Movies.objects.all()
    q = request.GET.get('search')
    if q:
        qs = qs.filter(title_kor__icontains=q)

    # 2) 페이징(한 페이지당 8개)
    paginator = Paginator(qs, 8)
    page_num = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_num)

    serializer = MoviesSerializer(page_obj, many=True)
    return Response({
        'movies' : serializer.data,
        'page' : page_obj.number,
        'totalPage' : paginator.num_pages,
    })


@api_view(['GET'])
def movie_detail(request, movie_id):
    #  영화 상세 + 관련 댓글 목록 조회
    movie = get_object_or_404(Movies, pk=movie_id)
    movie_ser = MoviesSerializer(movie)

    comments = movie.comments.order_by('-create_date')  # related_name='comments'
    comm_ser = CommentSerializer(comments, many=True)

    return Response({
        'movie' : movie_ser.data,
        'comments': comm_ser.data,
    })


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_comment(request, movie_id):
    #  로그인한 사용자만 댓글 작성.
    #  로그아웃 상태면 401 리턴 → 프론트에서 로그인 페이지로 리다이렉트
    movie = get_object_or_404(Movies, pk=movie_id)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user, movie=movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)