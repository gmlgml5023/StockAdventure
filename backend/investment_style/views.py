from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import InvestmentStyle

@api_view(['POST', 'PUT'])
@permission_classes([IsAuthenticated])
def investment_test(request):
    try:
        style_id = request.data.get('style_id')
        user = request.user
        
        # 투자 스타일 객체 가져오기
        investment_style = InvestmentStyle.objects.get(style_id=style_id)
        
        if request.method == 'POST':
            # 첫 검사: 투자성향이 없는 경우
            if not hasattr(user, 'investment_style'):
                user.investment_style = investment_style
                user.save()
                return Response({
                    'message': '투자성향이 성공적으로 저장되었습니다.',
                    'style_id': style_id
                })
            return Response(
                {'error': '이미 투자성향이 존재합니다. PUT 메서드를 사용하세요.'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
            
        elif request.method == 'PUT':
            # 재검사: 기존 투자성향 업데이트
            user.investment_style = investment_style
            user.save()
            return Response({
                'message': '투자성향이 성공적으로 업데이트되었습니다.',
                'style_id': style_id
            })
            
    except InvestmentStyle.DoesNotExist:
        return Response(
            {'error': '유효하지 않은 투자성향입니다'}, 
            status=status.HTTP_404_NOT_FOUND
        )

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def investment_result(request):
    try:
        user = request.user
        # Profile 모델을 통해 투자성향 정보 조회
        profile = Profile.objects.filter(user=user).first()
        
        if profile and profile.investment_style:
            return Response({
                'style_id': profile.investment_style.style_id,
                'style_name': profile.investment_style.style_name
            })
        return Response(
            {'message': '투자성향 정보가 없습니다'}, 
            status=status.HTTP_200_OK  # 404 대신 200 반환
        )
    except Exception as e:
        return Response(
            {'error': str(e)}, 
            status=status.HTTP_400_BAD_REQUEST
        )