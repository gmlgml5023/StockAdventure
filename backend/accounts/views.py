from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import UserProfile
from .serializers import ProfileSerializer

User = get_user_model()

# 마이페이지 조회
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_profile(request, username):
    try:
        user = get_object_or_404(User, username=username)
        profile = UserProfile.objects.get(user=user)
        data = {
            'username': user.username,
            'investment_style': profile.investment_style.get_style_id_display() if profile.investment_style else None,
            'description': profile.description,
            'nickname': profile.nickname,
            'image':  f'character_{profile.investment_style.style_id}.png' if profile.investment_style else 'default.png'
        }
    
        return Response(data, status=status.HTTP_200_OK)
    except UserProfile.DoesNotExist:
        return Response({'error': '프로필이 존재하지 않습니다.'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# 회원정보 수정
@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def update_profile(request, username):
    user = get_object_or_404(User, username=username)
    if request.user != user:
        return Response({'error': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
    
    if request.method == 'GET':
        serializer = ProfileSerializer(user)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ProfileSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 프로필 정보 조회 및 수정
# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def update_user(request, username):
#     Users = get_object_or_404(User, username=username)
#     if request.user == User:
#         serializer = ProfileSerializer(instance=Users, data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             serializer = ProfileSerializer(Users)
#             return Response(serializer.data)
        
# @api_view(['GET'])
# @permission_classes([IsAuthenticated]) # 인증된 사용자만 권한 허용
# def user_movie_list(request, user_pk):
#     Users = get_object_or_404(User, pk=user_pk)
#     serializer = UserMovieListSerializer(Users)
#     user_list = {
#         'id' : serializer.data.get('id'),
#         'user_rated_movie_count' : Users.user_rated_movie.count(),
#         'user_rated_movie' : serializer.data.get('user_rated_movie'),
#         'like_movies_count' : Users.like_movies.count(),
#         'like_movies' : serializer.data.get('like_movies'),
#         'wish_moives_count' : Users.wish_moives.count(),
#         'wish_moives' : serializer.data.get('wish_moives'),
#     }
    # return JsonResponse(user_list)        
# 