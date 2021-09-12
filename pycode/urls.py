from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view()), # 파이썬 코딩 프로젝트 리스트
    path('<int:pk>/', views.python_code_page),  # 코딩에 관한 배경 설명 (문제/배경 , 풀이/code)
]