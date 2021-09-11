from .models import Post_aboutme
from django.views.generic import ListView

# Create your views here.

class PostList(ListView): # project 앱(웹페이지) 리스트 표현방식 정의
    model = Post_aboutme # project/model.py의 Post 클래스 객체생성

