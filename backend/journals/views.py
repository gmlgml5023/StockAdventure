from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import JournalListSerializer, JournalSerializer
from .models import Journal

# permission Decorators
from rest_framework.permissions import IsAuthenticated



# 매매일지 목록 관련 (조회, 작성)
# @api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
# def journal_list(request): 
#     if request.method == 'GET':
#         journals = get_list_or_404(Journal)
#         serializer = JournalListSerializer(journals, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = JournalSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)


# # 매매일지 상세 관련 (조회, 수정, 삭제)
# @api_view(['GET', 'DELETE', 'PUT'])
# def journal_detail(request, journal_pk):
#     journal = get_object_or_404(Journal, pk=journal_pk)

#     if request.method == 'GET':
#         serializer = JournalSerializer(journal)
#         return Response(serializer.data)

#     elif request.method == 'DELETE':
#         journal.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#     elif request.method == 'PUT':
#         serializer = JournalSerializer(
#             journal, data=request.data, partial=True
#         )
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def journal_list(request): 
    if request.method == 'GET':
        journals = Journal.objects.filter(user=request.user)
        serializer = JournalListSerializer(journals, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = JournalSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)  # 현재 사용자를 저장
            return Response(serializer.data, status=status.HTTP_201_CREATED)

# 매매일지 상세 관련 (조회, 수정, 삭제)
@api_view(['GET', 'DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
def journal_detail(request, journal_pk):
    journal = get_object_or_404(Journal, pk=journal_pk, user=request.user)

    if request.method == 'GET':
        serializer = JournalSerializer(journal)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        journal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = JournalSerializer(journal, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)