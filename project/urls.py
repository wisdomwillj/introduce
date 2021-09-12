from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view()), # 리스트 페이지
    path('<int:pk>/', views.single_post_page),  # 상세페이지
]