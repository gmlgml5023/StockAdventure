from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import UserProfile
from .serializers import ProfileSerializer
from journals.serializers import JournalListSerializer
from journals.models import Journal

User = get_user_model()

# 마이페이지 조회
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_profile(request, username):
    try:
        user = get_object_or_404(User, username=username)
        profile, created = UserProfile.objects.get_or_create(user=user)
        data = {
            'username': profile.nickname or user.username,  # 닉네임이 있으면 닉네임을, 없으면 username을 표시
            'investment_style': profile.investment_style.get_style_id_display() if profile.investment_style else None,
            'resolution': profile.resolution,
            'nickname': profile.nickname,
            'image': request.build_absolute_uri(f'/media/images/character_{profile.investment_style.style_id}.png') if profile.investment_style else request.build_absolute_uri('/media/images/default_character.png')        }
    
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
    profile = get_object_or_404(UserProfile, user=user)
    
    if request.user.username != username:
        return Response({'error': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
    
    if request.method == 'GET':
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        
@api_view(['GET'])
@permission_classes([IsAuthenticated]) # 인증된 사용자만 권한 허용
def user_journal_list(request, username):
    user = get_object_or_404(User, username=username)
    journals = Journal.objects.filter(user=user)
    serializer = JournalListSerializer(journals, many=True)
    return Response(serializer.data)   
