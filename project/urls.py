from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view()), # blog 첫페이지는 project/views.py 내 PostList 클래스로 처리
    path('<int:pk>/', views.single_post_page), # 상세페이지는 project/views.py 내 single_post_page 클래스로 처리
]