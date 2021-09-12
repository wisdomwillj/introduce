from django.shortcuts import render
from .models import PostCode # post 모델 불러옴 위치는 project/model.py의 Post 클래스 선언
from django.views.generic import ListView, DetailView

# Create your views here.

class PostList(ListView): # portfolio 앱(웹페이지) 리스트 표현방식 정의
    model = PostCode # portfolio/model.py의 Post 클래스 객체생성
    ordering = 'pk' # Post 레코드 중 pk값에 따라 내림차순

class PostDetail(DetailView): # portfolio 앱(웹페이지) 상세보기 표현방식 정의
    model = PostCode # portfolio/model.py의 Post 클래스 객체생성

def python_code_page(request, pk):
    post = PostCode.objects.get(pk=pk)
    return render(
        request,
        'pycode/index.html', # index이름의 html 양식을 불러와서 post 객체 내용을 호출
        {
            'post' : post,
        }
    )
