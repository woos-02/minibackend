# from django.shortcuts import render

# # Create your views here.
# # accounts/views.py

# from django.contrib.auth import authenticate, get_user_model
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.decorators import (api_view, authentication_classes, permission_classes)
# from rest_framework.permissions import AllowAny, IsAuthenticated
# from rest_framework_simplejwt.authentication import JWTAuthentication
# from rest_framework_simplejwt.tokens import RefreshToken

# from .serializers import CustomRegisterSerializer, CustomUserDetailSerializer

# User = get_user_model()


# @api_view(['POST'])
# @authentication_classes([]) # 회원가입은 비인증 상태에서도 허용
# @permission_classes([AllowAny])
# def signup(request):
#     """
#     POST /api/accounts/signup/
#     {
#       "username": "...",
#       "password1": "...",
#       "password2": "...",
#       "nickname": "..."
#     }
#     """
#     serializer = CustomRegisterSerializer(data=request.data)
#     if serializer.is_valid():
#         user = serializer.save(request)
#         detail_user = CustomUserDetailSerializer(user)
#         return Response(detail_user.data, status=status.HTTP_201_CREATED)

#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['POST'])
# @authentication_classes([])                # 로그인도 비인증에서 시작
# @permission_classes([AllowAny])
# def login_view(request):
#     """
#     POST /api/accounts/login/
#     {
#       "username": "...",
#       "password": "..."
#     }
#     → access / refresh 토큰 반환
#     """
#     username = request.data.get('username')
#     password = request.data.get('password')
#     user = authenticate(request, username=username, password=password)
#     if user is None:
#         return Response(
#             {"detail": "아이디 또는 비밀번호가 잘못되었습니다."},
#             status=status.HTTP_401_UNAUTHORIZED
#         )

#     refresh = RefreshToken.for_user(user)
#     return Response({
#         'access': str(refresh.access_token),
#         'refresh': str(refresh),
#     }, status=status.HTTP_200_OK)


# @api_view(['POST'])
# @authentication_classes([JWTAuthentication])  # 발급된 토큰으로 인증
# @permission_classes([IsAuthenticated])
# def logout_view(request):
#     """
#     POST /api/accounts/logout/
#     {
#       "refresh": "<refresh-token>"
#     }
#     → 블랙리스트에 등록하여 로그아웃 처리
#     """
#     refresh_token = request.data.get('refresh')
#     if not refresh_token:
#         return Response(
#             {"detail": "refresh 토큰을 함께 보내주세요."},
#             status=status.HTTP_400_BAD_REQUEST
#         )
#     try:
#         token = RefreshToken(refresh_token)
#         token.blacklist()  # simplejwt의 blacklist 앱이 활성화되어 있어야 합니다.
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     except Exception:
#         return Response(
#             {"detail": "유효하지 않은 토큰입니다."},
#             status=status.HTTP_400_BAD_REQUEST
#         )
