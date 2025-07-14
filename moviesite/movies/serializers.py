from rest_framework import serializers
from .models import Movies, Comments


class CommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    # 댓글 작성자 이름 노출
    class Meta:
        model = Comments
        fields = ['id', 'username', 'content', 'create_date']

class MoviesSerializer(serializers.ModelSerializer):
    Comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Movies
        fields = '__all__' # 메인리스트에서 댓글까지 안 보여줄거면 '_all_' 대신 원하는 필드만 명시