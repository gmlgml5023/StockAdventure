from django.shortcuts import get_object_or_404, render, redirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.http import HttpResponseRedirect
from .models import StyleQuestion, StyleChoice, InvestmentStyle
from accounts.models import UserProfile

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def calculate_investment_style(request):
    if request.method == 'POST':
        total_score = 0
        print("Received data:", request.data) # 디버깅용 로그
        
        for key, value in request.data.items():
            if key.startswith('question_'):
                try:
                    choice = StyleChoice.objects.get(pk=int(value))
                    total_score += choice.style_points
                    print(f"Question {key}: Choice {value}, Points {choice.style_points}")  # 디버깅용 로그
                except (ValueError, StyleChoice.DoesNotExist):
                    print(f"Invalid choice for {key}: {value}")  # 디버깅용 로그

                    pass # 잘못된 선택은 무시
        
        print(f"Total score calculated: {total_score}")  # 디버깅용 로그

            
        # 총 점수에 따라 투자 성향 결정
        try:        
            if total_score <= 13:
                investment_style = InvestmentStyle.objects.get(style_id=1)
            elif 14 <= total_score <= 21:
                investment_style = InvestmentStyle.objects.get(style_id=2)
            else:  # total_score > 37
                investment_style = InvestmentStyle.objects.get(style_id=3)
        
            # UserProfile 객체 가져오기 (없으면 생성)
            profile, created = UserProfile.objects.get_or_create(user=request.user)
            
            # 투자 스타일 저장
            profile.investment_style = investment_style
            profile.save()    
            
            print(f"Investment style: {investment_style.get_style_id_display()}")
            
        except InvestmentStyle.DoesNotExist:
            print("Investment style not found")
            
            return Response({'error': 'Investment style not found'}, status=status.HTTP_404_NOT_FOUND)
        
        except InvestmentStyle.DoesNotExist:
            # 적절한 오류 처리 또는 기본값 설정
            return Response({'error': 'Investment style not found'}, status=status.HTTP_404_NOT_FOUND)
        
        # 결과를 세션에 저장
        # request.session['total_score'] = total_score
        # request.session['investment_style_id'] = investment_style.style_id            
        
        # return redirect('investment_style:investment_result')
        return Response({
            'total_score': total_score,
            'investment_style_id': investment_style.style_id,
            'investment_style_name': investment_style.get_style_id_display()
        }, status=status.HTTP_200_OK)
    
    else:
        questions = StyleQuestion.objects.all()
        return Response([{
            'id': q.id,
            'question_text': q.question_text,
            'choices': [{
                'id': c.id,
                'choice_text': c.choice_text
            } for c in q.choices.all()]
        } for q in questions], status=status.HTTP_200_OK)

@api_view(['GET'])
def investment_test_result(request):
    total_score = request.session.get('total_score', 0)
    investment_style_id = request.session.get('investment_style_id')
    
    if investment_style_id is not None:
        investment_style = InvestmentStyle.objects.get(style_id=investment_style_id)
        return Response({
            'total_score': total_score,
            'investment_style_id': investment_style.style_id,
            'investment_style_name': investment_style.get_style_id_display()
        }, status=status.HTTP_200_OK)
    else:
        return Response({
            'error': '투자 스타일 테스트 결과가 없습니다.'
        }, status=status.HTTP_404_NOT_FOUND)